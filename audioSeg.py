from pydub import AudioSegment
import os

base_path="/home/gaoxiang"
# 创建没有声音的音频片段
ten_second_silence = AudioSegment.silent(duration=10000)  # duration持续时间（毫秒） frame_rate 默认为11.025khz

# 将两个单声道合并为一个多声道
left_channel = AudioSegment.from_wav(os.path.join(base_path, "00001.wav"))
right_channel = AudioSegment.from_wav(os.path.join(base_path,"00002.wav"))
stereo_sound = AudioSegment.from_mono_audiosegments(left_channel,right_channel)

# 声道音量分贝
left_channel_db = left_channel.dBFS
right_channel_db = right_channel.dBFS

# 声道数目
left_channel_count = left_channel.channels
right_channel_count = right_channel.channels

# 采样宽度
left_channel_sample = left_channel.sample_width
right_channel_sample = right_channel.sample_width

# 总帧数=samp_width*channels
left_channel_frame = left_channel.frame_width
right_channel_frame = right_channel.frame_width

# 音频音量大小
left_channel_rms = left_channel.rms
right_channel_rms = right_channel.rms