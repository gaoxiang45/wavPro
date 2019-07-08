#  单通道wav写入

import wave
import os
import glob
import struct
import numpy as np
import matplotlib as plt
#  添加路径
file_path="/home/gaoxiang/eval/linshi"
wav_file=glob.glob(os.path.join(file_path,"*.wav"))
index=1

for wav in wav_file:
    f=wave.open(wav,"rb")
    params=f.getparams()
    n_channels,samp_width,frame_rate,n_frames=params[:4]
    str_data=f.readframes(n_frames)
    # print(str_data)
    wave_data=np.fromstring(str_data,dtype=np.int16)
    # print(wave_data)
    wave_data=wave_data*1.0/(max(abs(wave_data)))
    f.close()
    out_data=wave_data#待写入数据
    out_file="%s/tacotron/out%d.wav"%(file_path,index)
    outwav=wave.open(out_file,"wb")
    n_channels=1
    samp_width=2
    fs=48000
    data_size=len(out_data)
    frame_rate=int(fs)
    n_frames=data_size
    comptype="NONE"
    compname="not compressed"
    outwav.setparams((n_channels,samp_width,frame_rate,n_frames,comptype,compname))
    for v in out_data:
        outwav.writeframes(struct.pack('h',int(v*64000/2)))
    outwav.close()