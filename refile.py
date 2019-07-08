#  批量读取文件名

import os
import glob
import wave
#  得到路径下的某后缀文件列表
# file_path="/home"
# wav_file=glob.glob(os.path.join(file_path,"gaoxiang","*.wav"))
#
# #  打印文件
# for wav in wav_file:
#     print(wav)


file_path="/home/gaoxiang/eval/output/0.wav"
file=wave.open(file_path)
params=file.getparams()
n_channels, samp_width, frame_rate, n_frames = params[:4]
print(n_channels)
print(frame_rate)