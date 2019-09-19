# -*- coding: utf-8 -*-
import threading
import json
import functools
import time

import MySQLdb

import DBMain


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


class DBGui(DBMain.MysqlClass):
    def __init__(self):
        self.db = MySQLdb.connect("127.0.0.1", "user", "1234", "student", charset='utf8')
        self.cursor = self.db.cursor()

    def record_quiz_answer_gui(self, student_reading_log):
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
            return False
        return True

    def get_reading_content_unit(self, unit):
        sql = "select content from essential_english_words_1.reading_content where unit = {}".format(str(unit))
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)
        results = self.cursor.fetchone()
        reading_len = len(results[0].split(' '))
        return reading_len, results[0]

