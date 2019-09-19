# -*- coding: utf-8 -*-
import threading
import functools
import time
import json
import MySQLdb


def synchronized(wrapped):
    lock = threading.Lock()
    print(lock, id(lock))

    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            print("Calling '%s' with Lock %s from thread %s [%s]"
                  % (wrapped.__name__, id(lock),
                     threading.current_thread().name, time.time()))
            result = wrapped(*args, **kwargs)
            print("Done '%s' with Lock %s from thread %s [%s]\n"
                  % (wrapped.__name__, id(lock),
                     threading.current_thread().name, time.time()))
            return result

    return _wrap


class DBMain(object):
    def __init__(self):
        self.db = MySQLdb.connect("127.0.0.1", "user", "1234", "student", charset='utf8')
        self.cursor = self.db.cursor()

    def get_student_account(self, account):
        sql = "SELECT * FROM essential_english_words_1.unit WHERE unit_id = (SELECT" + \
              " current_course FROM student.course_progress WHERE sid = \"{}\");".format(account)
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.cursor.execute(sql)
        results = self.cursor.fetchone()

        if len(results) == 0:
            return 'no account'
        else:
            stu_data = {'unit_id': results[0], 'unit': results[1], 'title': results[2]}
            return json.dumps(stu_data)

    def get_word(self, unit):
        sql = "SELECT word FROM essential_english_words_1.words WHERE unit = " \
              "(SELECT unit FROM essential_english_words_1.unit WHERE" + \
              " unit_id = {});".format(str(unit))
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.cursor.execute(sql)

        words = {'words': []}
        results = self.cursor.fetchall()
        for res in results:
            words['words'].append(res[0])

        return json.dumps(words)

    def get_reading_content(self, sid):
        sql = "select unit, content from essential_english_words_1.reading_content where rid = (select " \
              "current_course FROM student.course_progress where sid = '{}');".format(str(sid))
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)
        results = self.cursor.fetchone()
        reading_len = len(results[1].split(' '))
        return int(results[0]), reading_len, results[1]

    def record_reading(self, sid, unit, content, speed, wer, confidence):

        datetime = 'NOW()'
        sql = "INSERT INTO `student`.`stu_reading_wer`(sid, unit, stu_reading_content, stu_reading_speed, " \
              "stu_reading_wer, avg_confidence, datetime) VALUE ('{}', {}, \"{}\", {}, {}, {},{});". \
            format(sid, unit, content, speed, wer, confidence, datetime)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except NameError, MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)
            self.db.commit()
            return False

        return True

    def get_quiz(self, unit):

        sql = "SELECT q.`order`, q.answer, q.quiz, a.content FROM essential_english_words_1.unit_quiz AS q," \
              "essential_english_words_1.unit_answer AS a WHERE	q.unit = {} AND a.unit = {}	AND " \
              "a.`q_order` = q.`order`  AND q.answer = a.answer;".format(str(unit), str(unit))

        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)

        order = []
        answer = []
        quizzes = []
        content = []

        quiz = {'order': [], 'answer': [], 'quiz': [], 'content': []}
        results = self.cursor.fetchall()

        for res in results:
            order.append(res[0])
            answer.append(res[1])
            quizzes.append(res[2])
            content.append(res[3])

        quiz['order'] = order
        quiz['answer'] = answer
        quiz['quiz'] = quizzes
        quiz['content'] = content

        return json.dumps(quiz)

    def record_quiz_answer(self, student_reading_log):
        datetime = 'NOW()'
        reading_log = json.loads(student_reading_log)
        sql_sentence = ''
        sid = str(reading_log['sid'])
        unit = str(reading_log['unit'])

        for i in range(len(reading_log['order'])):
            stu_r_ans = reading_log['stu_read_ans'][i].replace("'", r"\'")
            stu_ans = reading_log['stu_answer'][i]
            order = reading_log['order'][i]
            wer = reading_log['wer'][i]
            speed = reading_log['reading_speed'][i]
            sql_sentence += "('{}', '{}', '{}', '{}', '{}', '{}', {}, {})," \
                .format(sid, unit, order, stu_ans, stu_r_ans, wer, speed, datetime)

        sql_sentence = "INSERT INTO `student`.`stu_reading_answer` (`sid`, `unit`, `order`, `stu_answer`, " \
                       "`stu_read_ans`, `wer`, `reading_speed`, `reading_time`) VALUES {};".format(sql_sentence[:-1])

        try:
            self.cursor.execute(sql_sentence)
            self.db.commit()
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql_sentence)
            self.db.commit()

        return sid, unit

    def update_progress(self, data):
        stu_data = json.loads(data)
        print stu_data

        sql = "UPDATE student.course_progress SET current_course = {} WHERE sid = \"{}\";"\
            .format(stu_data['course'], stu_data['student'])

        print sql

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)
            self.db.commit()

    def operation_error(self):
        self.db = MySQLdb.connect("127.0.0.1", "user", "1234", "student", charset='utf8')
        self.cursor = self.db.cursor()
        print('reconnect database')
