# -*- coding: utf-8 -*-
import wave


def get_wav_time(path):
    f = wave.open(path, 'rb')
    params = f.getparams()
    frame_rate, number_of_frames = params[2:4]
    time = number_of_frames / (1.0 * frame_rate)
    f.close()

    return time


def get_wav_frame(path):
    f = wave.open(path, 'rb')
    params = f.getparams()
    number_of_channels = params[0]
    frame_rate = params[2]

    return number_of_channels, frame_rate


def get_wav_info(path):
    f = wave.open(path, 'rb')
    params = f.getparams()
    number_of_channels, sampling_width, frame_rate, number_of_frames = params[:4]
    print(params)
    print(number_of_channels, sampling_width, frame_rate, number_of_frames)
