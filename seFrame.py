# 信号分帧
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import wave
import struct
import os

def enframes(signal,nw,inc,winfunc):
    """
    将音频信号转化为帧。
    参数含义：
    signal:原始音频型号
    nw:每一帧的长度（这里指采样点的长度，即采样频率×时间间隔）
    inc:相邻帧的间隔（同上定义）
    """
    signal_length=len(signal)#信号总长度
    if signal_length<nw:#若信号长度小于一个帧的长度，则帧数定义为1
        nf=1
    else:#否则，计算帧的总长度
        nf=int(np.ceil((1.0*signal_length-nw+inc)/inc))
    pad_length=int((nf-1)*inc+nw)#所有帧加起来的铺平后的长度
    zeros=np.zeros((pad_length-signal_length,))#不够的长度使用0填补，类似于FFT中的扩充数组操作
    pad_signal=np.concatenate((signal,zeros))#填补后的信号记为pad_signal
    indices=np.tile(np.arange(0,nw),(nf,1))+np.tile(np.arange(0,nf*inc,inc),(nw,1)).T#相当于对所有帧的时间点进行抽取，得到nf*nw长度的矩阵
    indices=np.array(indices,dtype=np.int32)#将indices转化为矩阵
    frames=pad_signal[indices]#得到帧信号
    win=np.tile(winfunc,(nf,1))#window窗函数，默认取1
    return frames*win#返回帧信号矩阵

def waveread(filename):
    f=wave.open(filename,'rb')
    params=f.getparams()
    n_channels,samp_width,frame_rate,n_frames=params[:4]
    str_data=f.readframes(n_frames)
    wave_data=np.fromstring(str_data,dtype=np.int16)
    f.close()
    wave_data=wave_data*1.0/(max(abs(wave_data)))
    wave_data=np.reshape(wave_data,[n_frames,n_channels]).T
    return wave_data

file_path="/home/gaoxiang/test.wav"
out_path="/home/gaoxiang/tacotron/out.wav"
data=waveread(file_path)
nw=512
inc=128
winfunc=signal.hamming(nw)#汉明窗
Frame=enframes(data[0],nw,inc,winfunc)