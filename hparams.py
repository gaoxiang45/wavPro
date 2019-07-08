import tensorflow as tf

hparams=tf.contrib.training.HParams(
    use_lws=False,
    silence_threshold=2,

    n_fft=4096,
    hop_size=600,
    win_size=2400,
    sample_rate=48000,
    frame_shift_ms=None,
    preemphasis=0.97,

    num_mels=160,  # Number of mel-spectrogram channels and local conditioning dimensionality
    num_freq=2049,  # (= n_fft / 2 + 1) only used when adding linear spectrograms post processing network
    rescale=True,  # Whether to rescale audio prior to preprocessing
    rescaling_max=0.999,  # Rescaling value
    trim_silence=True,  # Whether to clip silence in Audio (at beginning and end of audio only, not the middle)
    clip_mels_length=True,  # For cases of OOM (Not really recommended, working on a workaround)
    max_mel_frames=900,  # Only relevant when clip_mels_length = True

    trim_fft_size=512,
    trim_hop_size=128,
    trim_top_db=60,

    signal_normalization=True,
    allow_clipping_in_normalization=False,  # Only relevant if mel_normalization = True
    symmetric_mels=True,  # Whether to scale the data to be symmetric around 0
    max_abs_value=4.,  # max absolute value of data. If symmetric, data will be [-max, max] else [0, max]

    min_level_db=-120,
    ref_level_db=20,
    fmin=125,
    # Set this to 75 if your speaker is male! if female, 125 should help taking off noise. (To test depending on dataset)
    fmax=7600,
)