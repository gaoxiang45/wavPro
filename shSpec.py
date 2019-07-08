#语谱图

import wave
import matplotlib.pyplot as plt
import numpy as np
import os

file_path="/home/gaoxiang/test.wav"
f=wave.open(file_path,'rb')
params=f.getparams()
n_channels,samp_width,frame_rate,n_frames=params[:4]
str_data=f.readframes(n_frames)
wave_data=np.fromstring(str_data,dtype=np.int16)
wave_data=wave_data*1.0/(max(abs(wave_data)))
wave_data=np.reshape(wave_data,[n_frames,n_channels]).T
f.close()

plt.specgram(wave_data[0],Fs=frame_rate,scale_by_freq=True,sides='default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()
