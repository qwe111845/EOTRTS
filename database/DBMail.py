# -*- coding: utf-8 -*-
import MySQLdb


class DBMail(object):
    def __init__(self):
        self.db = MySQLdb.connect("127.0.0.1", "user", "1234", "student", charset='utf8')
        self.cursor = self.db.cursor()

    def operation_error(self):
        self.db = MySQLdb.connect("127.0.0.1", "user", "1234", "student", charset='utf8')
        self.cursor = self.db.cursor()

    def get_mail(self, sid):
        sql = "SELECT email FROM student.student_data WHERE student_id = '{}' ;".format(sid)
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)

        results = self.cursor.fetchone()

        return str(results[0])

    def get_record_data(self, sid, unit):
        sql = "SELECT stu_reading_content, stu_reading_speed, stu_reading_wer, avg_confidence " \
              "FROM student.stu_reading_wer WHERE sid = '{}' and unit = {};".format(sid, unit)
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)

        results = self.cursor.fetchall()

        return \
            str(results[len(results) - 1][0]), \
            str(results[len(results) - 1][1]), \
            str(results[len(results) - 1][2]), \
            str(results[len(results) - 1][3])

    def get_answer_data(self, sid, unit):
        sql = "SELECT `order`, `stu_answer`, `stu_read_ans`, `wer`, `reading_speed` " \
              "FROM student.stu_reading_answer WHERE sid = '{}' and unit = {};".format(sid, unit)
        try:
            self.cursor.execute(sql)
        except MySQLdb.OperationalError:
            self.operation_error()
            self.cursor.execute(sql)

        results = self.cursor.fetchall()
        order = []
        stu_answer = []
        stu_read_ans = []
        wer = []
        reading_speed = []
        for res in results:
            order.append(res[0])
            stu_answer.append(res[1])
            stu_read_ans.append(res[2])
            wer.append(res[3])
            reading_speed.append(res[4])

        return \
            order[-4:], \
            stu_answer[-4:], \
            stu_read_ans[-4:], \
            wer[-4:], \
            reading_speed[-4:]
