# -*- coding: utf-8 -*-
import Tkinter as tk
import json
import tkMessageBox as tm
import tkFileDialog
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class SpeechGUI(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.var = tk.StringVar()
        self.link = tk.StringVar()
        self.root.title("雲端上傳")
        self.root.geometry("640x480")
        self.root.minsize(320, 240)

        self.init_gui()

    def init_gui(self):

        self.pack(fill='both', expand=1)

        self.file_button = tk.Button(self, text="選擇檔案")
        self.file_button.place(relx=0.85, rely=0.13, relheight=0.05, relwidth=0.15)
        self.file_button['command'] = self.set_data

        self.cloud_button = tk.Button(self, text="上傳雲端")
        self.cloud_button.place(relx=0.85, rely=0.18, relheight=0.05, relwidth=0.15)
        self.cloud_button['command'] = self.upload_cloud

        self.unit_label = tk.Label(self, text="unit:")
        self.unit_label.place(relx=0.80, relheight=0.05, relwidth=0.05)

        self.unit_text = tk.Text(self)
        self.unit_text.place(relx=0.85, relheight=0.05, relwidth=0.15)

        self.ans1_label = tk.Label(self, text="Q1:")
        self.ans1_label.place(relx=0.45, relheight=0.05, relwidth=0.05)

        self.ans1 = tk.Text(self)
        self.ans1.place(relx=0.5, relheight=0.05, relwidth=0.15)

        self.ans1_button = tk.Button(self, text="選擇檔案")
        self.ans1_button.place(relx=0.65, relheight=0.05, relwidth=0.15)
        self.ans1_button['command'] = self.set_data_ans1

        self.ans2_label = tk.Label(self, text="Q2:")
        self.ans2_label.place(relx=0.45, rely=0.05, relheight=0.05, relwidth=0.05)

        self.ans2 = tk.Text(self)
        self.ans2.place(relx=0.5, rely=0.05, relheight=0.05, relwidth=0.15)

        self.ans2_button = tk.Button(self, text="選擇檔案")
        self.ans2_button.place(relx=0.65, rely=0.05, relheight=0.05, relwidth=0.15)
        self.ans2_button['command'] = self.set_data_ans2

        self.ans3_label = tk.Label(self, text="Q3:")
        self.ans3_label.place(relx=0.45, rely=0.1, relheight=0.05, relwidth=0.05)

        self.ans3 = tk.Text(self)
        self.ans3.place(relx=0.5, rely=0.1, relheight=0.05, relwidth=0.15)

        self.ans3_button = tk.Button(self, text="選擇檔案")
        self.ans3_button.place(relx=0.65, rely=0.10, relheight=0.05, relwidth=0.15)
        self.ans3_button['command'] = self.set_data_ans3

        self.ans4_label = tk.Label(self, text="Q4:")
        self.ans4_label.place(relx=0.45, rely=0.15, relheight=0.05, relwidth=0.05)

        self.ans4 = tk.Text(self)
        self.ans4.place(relx=0.5, rely=0.15, relheight=0.05, relwidth=0.15)

        self.ans4_button = tk.Button(self, text="選擇檔案")
        self.ans4_button.place(relx=0.65, rely=0.15, relheight=0.05, relwidth=0.15)
        self.ans4_button['command'] = self.set_data_ans4

        self.sid_label = tk.Label(self, text="sid:")
        self.sid_label.place(relx=0.80, rely=0.08, relheight=0.05, relwidth=0.05)

        self.sid_text = tk.Text(self)
        self.sid_text.place(relx=0.85, rely=0.08, relheight=0.05, relwidth=0.15)

    def set_data(self):
        default_dir = r"C:/Users"
        self.save_file = tkFileDialog.askopenfilename(title="選擇檔案",
                                                      initialdir=(os.path.expanduser(default_dir)))

        self.save_file = self.save_file.replace('/', r'/')
        print(self.save_file)
        if len(self.save_file) <= 0:
            tm.showinfo(title='wrong', message='請選擇儲存的檔案')
            pass
        else:
            tm.showinfo(title='完成', message='選擇完成')

    def set_data_ans1(self):
        default_dir = r"C:/Users"
        self.ans1_file = tkFileDialog.askopenfilename(title="選擇檔案",
                                                      initialdir=(os.path.expanduser(default_dir)))

        self.ans1_file = self.ans1_file.replace('/', r'/')
        print(self.ans1_file)
        if len(self.ans1_file) <= 0:
            tm.showinfo(title='wrong', message='請選擇儲存的檔案')
            pass
        else:
            self.ans1_label['text'] += "ok"
            tm.showinfo(title='完成', message='選擇完成')

    def set_data_ans2(self):
        default_dir = r"C:/Users"
        self.ans2_file = tkFileDialog.askopenfilename(title="選擇檔案",
                                                      initialdir=(os.path.expanduser(default_dir)))

        self.ans2_file = self.ans2_file.replace('/', r'/')
        print(self.ans2_file)
        if len(self.ans2_file) <= 0:
            tm.showinfo(title='wrong', message='請選擇儲存的檔案')
            pass
        else:
            self.ans2_label['text'] += "ok"
            tm.showinfo(title='完成', message='選擇完成')

    def set_data_ans3(self):
        default_dir = r"C:/Users"
        self.ans3_file = tkFileDialog.askopenfilename(title="選擇檔案",
                                                      initialdir=(os.path.expanduser(default_dir)))

        self.ans3_file = self.ans3_file.replace('/', r'/')
        print(self.ans3_file)
        if len(self.ans3_file) <= 0:
            tm.showinfo(title='wrong', message='請選擇儲存的檔案')
            pass
        else:
            self.ans3_label['text'] += "ok"
            tm.showinfo(title='完成', message='選擇完成')

    def set_data_ans4(self):
        default_dir = r"C:/Users"
        self.ans4_file = tkFileDialog.askopenfilename(title="選擇檔案",
                                                      initialdir=(os.path.expanduser(default_dir)))

        self.ans4_file = self.ans4_file.replace('/', r'/')
        print(self.ans4_file)
        if len(self.ans4_file) <= 0:
            tm.showinfo(title='wrong', message='請選擇儲存的檔案')
            pass
        else:
            self.ans4_label['text'] += "ok"
            tm.showinfo(title='完成', message='選擇完成')

    def upload_cloud(self):
        """Uploads a file to the bucket."""
        from wav_read import WavInfo
        from cloud import cloud_speech
        from word_error_rate.wer_improve import wer
        from database import DB_GUI as DB
        from mail_transfer import MailTransfer
        db = DB.DBGUI()

        destination_blob_name = 'unit ' + self.unit_text.get("1.0", "end-1c") + '/' + \
                                self.sid_text.get("1.0", "end-1c") + '.wav'

        print(self.save_file, type(self.save_file.encode('utf-8')))
        print(destination_blob_name, type(destination_blob_name.encode('utf-8')))
        cloud_speech.upload_blob("speech_to_text_class", self.save_file,
                                 destination_blob_name)
        reading_len, content = db.get_reading_content_unit(self.unit_text.get("1.0", "end-1c"))
        number_of_channels, frame_rate = WavInfo.get_wav_frame(self.save_file.encode('utf-8'))

        gcs_url = "gs://speech_to_text_class/" + destination_blob_name.encode('utf-8')
        transcript, transcript_len, confidence = cloud_speech.transcribe_gcs(gcs_url, number_of_channels, frame_rate)

        print('finish transcribe')

        reading_time = WavInfo.get_wav_time(self.save_file.encode('utf-8'))
        reading_speed = int(transcript_len / (reading_time / 60.0))
        word_error_rate = (1 - wer(content.encode('utf-8'), str(transcript))) * 100
        word_error_rate = float('%.4f' % word_error_rate)

        db.record_reading(self.sid_text.get("1.0", "end-1c"), self.unit_text.get("1.0", "end-1c"),
                          transcript, reading_speed, word_error_rate, confidence)

        data = db.get_quiz(self.unit_text.get("1.0", "end-1c"))
        quiz_data = json.loads(data)
        print(quiz_data)
        quiz_time = []
        quiz_len = []
        stu_reading_log = {'sid': self.sid_text.get("1.0", "end-1c"),
                           'unit': self.unit_text.get("1.0", "end-1c"),
                           'order': [1, 2, 3, 4],
                           'stu_answer': [self.ans1.get("1.0", "end-1c"),
                                          self.ans2.get("1.0", "end-1c"),
                                          self.ans3.get("1.0", "end-1c"),
                                          self.ans4.get("1.0", "end-1c")],
                           'stu_read_ans': [],
                           'wer': [],
                           'reading_speed': []}

        transcript1, transcript_len1 = cloud_speech.transcribe_file_local(self.ans1_file)
        stu_reading_log['stu_read_ans'].append(transcript1)
        quiz_len.append(transcript_len1)
        quiz_time.append(WavInfo.get_wav_time(self.ans1_file))
        transcript2, transcript_len2 = cloud_speech.transcribe_file_local(self.ans1_file)
        stu_reading_log['stu_read_ans'].append(transcript2)
        quiz_len.append(transcript_len2)
        quiz_time.append(WavInfo.get_wav_time(self.ans2_file))
        transcript3, transcript_len3 = cloud_speech.transcribe_file_local(self.ans1_file)
        stu_reading_log['stu_read_ans'].append(transcript3)
        quiz_len.append(transcript_len3)
        quiz_time.append(WavInfo.get_wav_time(self.ans3_file))
        transcript4, transcript_len4 = cloud_speech.transcribe_file_local(self.ans1_file)
        stu_reading_log['stu_read_ans'].append(transcript4)
        quiz_len.append(transcript_len4)
        quiz_time.append(WavInfo.get_wav_time(self.ans4_file))

        for i in range(4):
            print(quiz_data['content'][i], stu_reading_log['stu_read_ans'][i])
            print (wer(quiz_data['content'][i].encode('utf-8'),
                       str(stu_reading_log['stu_read_ans'][i])))
            wer_reading = (1.0 - (wer(quiz_data['content'][i].encode('utf-8'),
                           str(stu_reading_log['stu_read_ans'][i])))) * 100  # type: float
            wer_reading = float('%.4f' % wer_reading)
            speed = int((quiz_len[i] / (1.0 * quiz_time[i])) * 60.0)
            stu_reading_log['wer'].append(wer_reading)
            stu_reading_log['reading_speed'].append(speed)
        print stu_reading_log

        db.record_quiz_answer_gui(json.dumps(stu_reading_log))

        MailTransfer.send_mail(self.sid_text.get("1.0", "end-1c"), self.unit_text.get("1.0", "end-1c"))
        print('send mail')

        self.ans1_label['text'] = "Q1:"
        self.ans2_label['text'] = "Q2:"
        self.ans3_label['text'] = "Q3:"
        self.ans4_label['text'] = "Q4:"


if __name__ == '__main__':
    root = tk.Tk()
    app = SpeechGUI(master=root)
    root.mainloop()
