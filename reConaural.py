
#  读取wav文件
import wave
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

#  得到路径下某后缀文件列表
file_path="/home"
wav_file=glob.glob(os.path.join(file_path,"gaoxiang","*.wav"))

#  打开文件，读取文件属性，声道数，量化位数，采样频率，采样点数，单通道：
for wav in wav_file:
    f=wave.open(wav,'rb')
    params=f.getparams()
    n_channels,samp_width,frame_rate,n_frames=params[:4]
    str_data=f.readframes(n_frames)#读取音频，字符串格式
    wave_data=np.fromstring(str_data,dtype=np.int16)#将字符串转化为int
    wave_data=wave_data*1.0/(max(abs(wave_data)))#wave幅值归一化
    # wave_data=np.reshape(wave_data,[n_frames,n_channels])
    f.close()

    # plot the wave
    time = np.arange(0, n_frames) * (1.0 / frame_rate)
    plt.figure()
    plt.subplot(5, 1, 1)
    plt.plot(time, wave_data[:, 0])
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Ch-1 wavedata")
    plt.grid('on')  # 标尺，on：有，off:无。
    plt.subplot(5, 1, 3)
    plt.plot(time, wave_data[:, 1])
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Ch-2 wavedata")
    plt.grid('on')  # 标尺，on：有，off:无。
    plt.subplot(5, 1, 5)
    plt.plot(time, wave_data[:, 2])
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Ch-3 wavedata")
    plt.grid('on')  # 标尺，on：有，off:无。
    plt.show()
