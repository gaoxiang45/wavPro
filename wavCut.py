import os,glob
import wave
import numpy as np
from pydub import AudioSegment

file_path = "/home/gaoxiang/noise"
wav_file=glob.glob(os.path.join(file_path,"*.wav"))
wav_file.sort()
for wav in wav_file:
    print(wav)
    index=0
    f=wave.open(wav,'rb')
    params=f.getparams()
    n_channels, samp_width, frame_rate, n_frames = params[:4]
    wav_seg=AudioSegment.from_wav(wav)
    for i in range(30):
        begin=i*int(len(wav_seg)/30)
        end=begin+int(len(wav_seg)/30)
        audio=wav_seg[begin:end]
        out=open("/home/gaoxiang/eval/noise/%s#%d.wav" % (wav[21:-4],index), "wb")
        audio.export(out,format="wav")
        index+=1
