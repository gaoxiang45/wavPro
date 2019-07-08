import os
import numpy as np
import wave
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import audio
from hparams import hparams

# base_path="/home/gaoxiang/eval/syn"
#
file_path="/home/gaoxiang/eval/A2_0.wav"

f1=wave.open(file_path)
params1 = f1.getparams()
n_channels1, samp_width1, frame_rate1, n_frames1 = params1[:4]
str_data1=f1.readframes(n_frames1)
wave_data1=np.fromstring(str_data1,dtype=np.int16)

f1,t1,Zsample1=signal.stft(wave_data1,fs=16000)
mel_filename='mel-{}.npy'.format(1)
np.save(mel_filename,Zsample1,allow_pickle=False)
_,Zsample1rec=signal.istft(Zsample1)
wavfile.write('1.wav',frame_rate1,np.asarray(Zsample1rec,dtype=np.int16))
# f1_sr,f1=wavfile.read(file_path)
# f2_sr,f2=wavfile.read(file_path1)
#
# maxlength=max(len(f1),len(f2))
#
# f1=np.pad(f1,(0,maxlength-len(f1)),'constant',constant_values=(0))
# f2=np.pad(f2,(0,maxlength-len(f2)),'constant',constant_values=(0))
#
#
# mel1=audio.melspectrogram(f1,hparams)
# mel2=audio.melspectrogram(f2,hparams)
#
#
# np.save("mel1.npy",mel1)
# np.save("mel2.npy",mel2)

# f1=np.load(file_path)
# f2=np.load(file_path1)
# print(f1.shape)
# print(f2.shape)
# f1_rec=signal.istft(f1,48000)
# f2_rec=signal.istft(f2,48000)
#
# wavfile.write(base_path + '/recovered1.wav', 48000, np.asarray(f1_rec, dtype=np.int16))
# wavfile.write(base_path + '/recovered2.wav', 48000, np.asarray(f2_rec, dtype=np.int16))
