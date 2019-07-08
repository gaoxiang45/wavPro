import os,glob
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
import pickle
import librosa
from scipy.io import wavfile
from scipy import signal
from math import ceil
from pydub import AudioSegment

os.environ["CUDA_VISIBLE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"
gpu_options=tf.GPUOptions(allow_growth=True)
config=tf.ConfigProto(gpu_options=gpu_options)
config.gpu_options.per_process_gpu_memory_fraction=0.34

n_file=1200
max_length=500
sr=16000


def loadfile(path):
    list_tr=[]
    list_stft=[]
    list_stft_abs=[]
    list_length=[]

    wav_file=glob.glob(os.path.join(path,"*.wav"))

    for i,wav_path in enumerate(wav_file):
        wav,wav_sr=librosa.load(wav_path)
        list_tr.append(wav)
        stft=librosa.stft(wav,n_fft=1024,hop_length=512)
        stft_len=stft.shape[1]
        list_stft.append(stft)
        stft_abs=np.abs(stft)
        stft_abs=np.pad(stft_abs,((0,0),(0,max_length-stft_len)),'constant')
        list_stft_abs.append(stft_abs)
        list_length.append(stft_len)

    return list_tr,list_stft,list_stft_abs,list_length


def mixtape(speech_path,noise_path):

    speech_list=glob.glob(os.path.join(speech_path,"*.wav"))
    speech_list.sort()
    print(speech_list)
    noise_list=glob.glob(os.path.join(noise_path,"*.wav"))
    noise_list.sort()
    print(noise_list)
    assert len(speech_list)==len(noise_list)
    index=0
    for i in range(len(speech_list)):
        sr_speech,speech=wavfile.read(speech_list[i])
        sr_noise,noise=wavfile.read(noise_list[i])

        max_len=max(len(speech),len(noise))
        speech=np.pad(speech,(0,max_len-len(speech)),'constant',constant_values=(0))
        noise=np.pad(noise,(0,max_len-len(noise)),'constant',constant_values=(0))
        mixed_series=speech+noise
        extrapadding = (ceil(len(mixed_series) / sr_speech) * sr_speech) - len(mixed_series)  # 向上取整
        mixed_series = np.pad(mixed_series, (0, extrapadding), 'constant', constant_values=(0))
        wavfile.write("/home/gaoxiang/eval/mixwav"+"/mix_series%d.wav"%index,sr_speech,np.asarray(mixed_series,dtype=np.int16))
        index+=1


def IBM(S,N):

    M=[]

    for i in range(len(S)):
        m_ibm=1*(S[i]>N[i])
        M.append(m_ibm)

    return M


def main():

    speech_path="/home/gaoxiang/eval/speech"
    noise_path="/home/gaoxiang/eval/noise"
    mix_path="/home/gaoxiang/eval/mixwav"
    # mixtape(speech_path,noise_path)
    noise,noise_stft,noise_abs,noise_len=loadfile(noise_path)
    speech,speech_stft,speech_abs,speech_len=loadfile(speech_path)
    sig,sig_stft,sig_abs,sig_len=loadfile(mix_path)
    M=IBM(speech_abs,noise_abs)
    batch_size=10
    keep_pr=tf.placeholder(tf.float32,())
    frame_size=513
    num_hidden=256
    seq_len=tf.placeholder(tf.int32,None)

    q2_x=tf.placeholder(tf.float32,[None,max_length,frame_size])
    q2_y=tf.placeholder(tf.float32,[None,max_length,frame_size])
    output,state=tf.nn.dynamic_rnn(tf.nn.rnn_cell.DropoutWrapper(tf.contrib.rnn.LSTMCell(num_hidden,initializer=tf.contrib.layers.xavier_initializer()),output_keep_prob=keep_pr),q2_x,dtype=tf.float32,sequence_length=seq_len)
    rnn_out=tf.layers.dense(output,513,kernel_initializer=tf.contrib.layers.xavier_initializer())
    dim=seq_len[0]
    fin_out=tf.sigmoid(rnn_out)

    lr=0.001

    cost=tf.reduce_mean(tf.losses.mean_squared_error(fin_out[:,:dim,:],q2_y[:,:dim,:]))
    optimizer=tf.train.AdamOptimizer(learning_rate=lr).minimize(cost)

    sess=tf.Session(config=config)
    saver=tf.train.Saver()
    sess.run(tf.global_variables_initializer())

    epochs=100
    error=np.zeros(epochs)

    for epoch in range(epochs):
        random=np.arange(0,1200,10)
        np.random.shuffle(random)
        for i in range(len(random)):
            start=int(random[i])
            end=int(start+batch_size)
            epoch_y=np.array(M[start:end]).swapaxes(1,2)
            epoch_x=np.array(noise_abs[start:end]).swapaxes(1,2)
            seqlen=np.array(noise_len[start:end])
            l, _ = sess.run([cost,optimizer],feed_dict={q2_x: epoch_x, q2_y: epoch_y, seq_len: seqlen, keep_pr: 1})
            error[epoch] += l

        print('Epoch',epoch+1,'complete out of',epochs,'; loss: ',error[epoch])


if __name__=="__main__":
    main()