import librosa as lib

wav1,sr1=lib.core.load("/home/gaoxiang/000001.wav")

print(sr1)

stretch_wav=lib.effects.time_stretch(wav1,2.0)

lib.output.write_wav("/home/gaoxiang/out.wav",stretch_wav,sr=sr1)

wav2,sr2=lib.core.load("/home/gaoxiang/out.wav")

pitch_wav=lib.effects.pitch_shift(wav1,sr1,1)

lib.output.write_wav("/home/gaoxiang/out1.wav",pitch_wav,sr=sr2)



