import glob,os
import numpy as np
from scipy import signal


def preprocess(message_path):

    outputdir="/home/gaoxiang/outputdir"
    os.makedirs(outputdir,exist_ok=True)
    files=glob.glob(os.path.join(message_path,"*.txt"))
    index=0
    for file in files:
        binary=np.load(file)
        print(binary.shape)
        # wav_data=np.fromstring(str_data,dtype=np.int8)
        # f1,t1,Zsample=signal.stft(wav_data,fs=16000)
        # mel_filename=os.path.join(outputdir,'mel-{}.npy'.format(index))
        # np.save(mel_filename,Zsample,allow_pickle=False)
        # _,melrec=signal.istft(Zsample,fs=16000)
        # print(melrec.tostring())
        # index+=1


def postprocess(message_path):
    mel_data=np.load(message_path)
    mel_data=mel_data.reshape(900,160)
    wav_data=signal.istft(mel_data,16000)

def main():
    path="/home/gaoxiang/eval/text"
    preprocess(path)
    path1="/home/gaoxiang/outputdir/m_test.npy"

if __name__ == '__main__':
    main()
