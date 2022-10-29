import FieldTrip
import mne


ch_names = ["Fp1", "Fp2", "C3", "C4", "P3", "P4", "O1", "O2"]


def get_raw_signal(signal_df, sampling_freq, ch_names):
    ch_types = ["eeg"] * len(ch_names)

    signal_info = mne.create_info(
        ch_names, 
        ch_types=ch_types, 
        sfreq=float(sampling_freq)
    )
    signal_info.set_montage('standard_1020')
    
    data = signal_df.T

    raw = mne.io.RawArray(data, signal_info)

    return raw


c = FieldTrip.Client()
c.connect(hostname='127.0.0.1', port=1973)

while True:
    h = c.getHeader()

    length = 250 * 10
    n_channels = h.nChannels
    n_samples = h.nSamples

    print(n_channels)

    raw_array = c.getData([
        n_samples - length, 
        n_samples - 1
    ])

    raw = get_raw_signal(raw_array, 250, ch_names)

    print(raw)