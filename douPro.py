
from pydub import AudioSegment
import glob
import os
base_path="/home/gaoxiang"

all_wav_path=glob.glob(os.path.join(base_path,"*.wav"))
input_music_1=AudioSegment.from_wav(all_wav_path[0])
input_music_2=AudioSegment.from_wav(all_wav_path[1])  # 前两个wav文件
# 音频文件的分贝
input_music_1_db = input_music_1.dBFS
input_music_2_db = input_music_2.dBFS
# 音频文件的时间长度
input_music_1_time = len(input_music_1)
input_music_2_time = len(input_music_2)

# 使音频文件的分贝大小一致
db = input_music_1_db-input_music_2_db
if db > 0:
    input_music_1 += abs(db)
elif db<0:
    input_music_2 += abs(db)

# 取第一个文件的前十秒和后一个文件的后五秒进行连接，并改变分贝大小
ten_seconds = 10*1000
first_10_seconds = input_music_1[:ten_seconds]
last_5_seconds = input_music_2[:5000]
begining = first_10_seconds+6
end = last_5_seconds-3
output_music = begining+end
output_music.export("/home/gaoxiang/out.wav",format="wav",bitrate="192K")
print(len(output_music),output_music.channels)