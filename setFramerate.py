import glob,os
from pydub import AudioSegment
import wave

wave="/home/gaoxiang/eval/text"
output="/home/gaoxiang/eval/output"
speech_list=glob.glob(os.path.join(wave,"*.wav"))
index=0
for speech in speech_list:
    speech_seg=AudioSegment.from_wav(speech)
    set=speech_seg.set_frame_rate(44100)
    print(set.frame_rate)
    out=open("%s/%d.wav"%(output,index),"wb")
    set.export(out,"wav")
    index+=1