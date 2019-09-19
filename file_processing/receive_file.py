# -*- coding: utf-8 -*-
import os
import threading

from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip


def check_exist(sid, file_path):
    path = 'record/'
    path_list = os.listdir(path)
    have_dir = False
    for item in path_list:
        if item == sid:
            have_dir = True
        else:
            pass
    if not have_dir:
        os.mkdir(path + sid, 0755)
        print('Dir not found! make new dir ' + sid)
    with open(file_path, 'wb'):
        pass


def receive_file(client, file_path):
    import socket
    while True:
        try:
            data = client.recv(8192)

            if not data:
                client.close()
                break
            else:
                with open(file_path, 'ab') as f:
                    f.write(data)
        except socket.error as error:
            print error
            client.close()
            break

    print('data received')


def save_file(client):
    client.send('Welcome from server!')
    print("receiving, please wait for a second ...")

    id_filename = client.recv(1024).split(';')
    sid = id_filename[0]
    filename = id_filename[1]
    path = 'record/' + sid + '/' + filename
    client.send('id get!')

    print('Begin to save ' + filename + ' ...')

    check_exist(sid, path)
    t = threading.Thread(target=receive_file, args=(client, path))
    t.setDaemon(True)
    t.start()
    t.join()
    print('Finished saving ' + filename + ' ...')

    return sid, path


def merge_file(client):
    try:
        client.send('Welcome from server!')

        print("receiving, please wait for a second ...")

        id_filename = client.recv(1024).split(';')
        sid = id_filename[0]
        filename = id_filename[1]
        recording_time = id_filename[2]
        path = 'record/' + sid + '/' + filename
        client.send('id get!')

        print('merge file ' + filename)

        clip1 = AudioFileClip('record/' + sid + '/' + sid + recording_time + '-record.wav')
        clip2 = VideoFileClip('record/' + sid + '/' + sid + recording_time + '-video.avi')

        new_video = clip2.set_audio(clip1)
        new_video.write_videofile(path)

        client.send('merge success')

        print('merge success!')

    except Exception as e:
        client.send('merge error')
        print(e)
