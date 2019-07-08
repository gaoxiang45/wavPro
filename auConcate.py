
#  通过pydub+ffmpeg来进行音频处理


from pydub import AudioSegment
import os
import glob
import time

base_path = "/home/gaoxiang/eval"
target_path=glob.glob(os.path.join(base_path,"*.wav"))
target_path.sort()  # 得到语音数据并进行排序

list_wav = [AudioSegment.from_wav(wav_file)for wav_file in target_path]  # wav文件的列表
first_audio = list_wav.pop(0)  # 得到第一个音频文件
if len(first_audio) > 24000:  # 如果文件的时长大于24 则进行压缩
    begin_of_song = first_audio[:-9*1000].fade_in(2000).fade_out(500)  # 截去后面的九秒
else:
    begin_of_song = first_audio[:-500].fade_in(2000).fade_out(500)  # 否则截取0.5秒

begin_of_song_db = begin_of_song.dBFS
playlist = begin_of_song


for audio in list_wav:
    print(len(audio))
    audio_db = audio.dBFS
    if audio_db > begin_of_song_db:
        audio -= audio_db-begin_of_song_db
    else:
        audio += begin_of_song_db-audio_db  # 调整分贝数，使其与第一段音频分贝大小一致
    if len(audio) > 24000:
        wav = audio[0:-9*1000].fade_in(2000).fade_out(500)  # fadein fadeout 淡入淡出
    else:
        wav = audio[0:-500].fade_in(2000).fade_out(500)  # 淡入淡出调整音频衔接段的效果
    wav.remove_dc_offset()  # 消除直流偏移
    wav.invert_phase()  # 产生反向信号的副本，消除反向位波或者降低噪音
    playlist = playlist.append(wav)


playlist_length = len(playlist)/(1000*60)  # 时间长度

out=open("/home/gaoxiang/eval/syn/output_%s.wav" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "wb")
playlist.export(out, format="wav")


