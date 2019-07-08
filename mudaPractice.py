import muda
import jams
import wave

jam=jams.JAMS()

j_orig = muda.load_jam_audio(jam, '01-Make_It.wav')

# f=wave.open('01-Make_It.wav','rb')
# params=f.getparams()
# n_channels,samp_width,frame_rate,n_frames=params[:4]
#
# print(samp_width)

pitch=muda.deformers.PitchShift(n_semitones=2)

stretch=muda.deformers.TimeStretch(rate=0.8)

pipline=muda.Pipeline(steps=[('pitch_shift',pitch),
                             ('time_stretch',stretch)])

output_jams=list(pipline.transform(j_orig))
