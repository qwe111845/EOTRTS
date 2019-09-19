# -*- coding: utf-8 -*-

import socket
import threading
import time

from database.DBMain import DBMain
from cloud import upload_cloud
from file_processing import receive_file
from word_error_rate import wer_improve


class Server(object):
    def __init__(self, host, port):

        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.db = DBMain()
        self.course = ''
        self.results = ''
        self.robot_port = 5400

    def listen(self):

        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            client.settimeout(300)
            threading.Thread(args=(client, address), target=self.listen_to_client).start()

    def listen_to_client(self, client, address):

        print('connect by: ', address)

        size = 2048
        link = True  # type: bool
        while link:
            try:
                data = client.recv(size)
                if data:
                    print(data.decode('utf-8'))

                    if data == 'student account':
                        client.send('account')
                        student_account = client.recv(1024)
                        stu_data = self.db.get_student_account(student_account)
                        print(stu_data)
                        if stu_data == 'no account':
                            client.send('no account')
                        else:
                            client.send(stu_data)
                        link = False

                    elif data == 'word':
                        client.send('Which unit do you want to choose?')
                        word_unit = client.recv(size)
                        word_data = self.db.get_word(word_unit)
                        time.sleep(0.5)
                        client.sendall(word_data)
                        link = False

                    elif data == 'file':
                        sid, path = receive_file.save_file(client)
                        upload_cloud.upload_and_record(self.db, sid, path)
                        link = False

                    elif data == 'merge':
                        receive_file.merge_file(client)
                        link = False

                    elif data == 'quiz':
                        client.send('Which unit do you want to choose?')
                        quiz_unit = client.recv(size)
                        quiz_data = self.db.get_quiz(quiz_unit)
                        time.sleep(0.5)
                        client.sendall(quiz_data)
                        link = False

                    elif data == 'quiz_log':
                        from mail_transfer import MailTransfer
                        client.send('log')
                        student_reading_log = client.recv(2048)
                        sid, unit = self.db.record_quiz_answer(student_reading_log)
                        MailTransfer.send_mail(sid, unit)

                        link = False

                    elif data == 'wer':
                        client.send('ok')
                        student_say = client.recv(1024).split(';;')
                        wer = str(int((1 - wer_improve.wer(student_say[0], student_say[1])) * 100))
                        client.send(wer)

                    elif data == 'update progress':
                        client.send('ok')
                        student_data = client.recv(1024)
                        self.db.update_progress(student_data)
                        link = False
                    else:
                        print(type(data), '傳送', data.decode('utf-8'))
                        client.sendall(data.decode('utf-8'))

                else:
                    time.sleep(1)
            except TypeError:
                client.close()
                return False

        client.close()


Server('140.134.26.200', 5007).listen()
