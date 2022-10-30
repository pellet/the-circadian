import FieldTrip
import mne

import extract
import nightlight

import numpy as np
from time import sleep


ch_names = ["Fp1", "Fp2", "C3", "C4", "P3", "P4", "O1", "O2"]
sfreq = 250

values = []

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

c_o = FieldTrip.Client()
c_o.connect(hostname='127.0.0.1', port=1974)

while True:
    h = c.getHeader()

    length = sfreq * 3
    n_channels = h.nChannels
    n_samples = h.nSamples

    raw_array = c.getData([
        n_samples - length, 
        n_samples - 1
    ]).T[1:9] # For OpenBCI only

    # raw = get_raw_signal(raw_array, sfreq, ch_names)
    signal_data = raw_array, sfreq, ch_names

    power_spectrum = extract.get_power_relative(signal_data)

    values.append(power_spectrum['C3']['alpha']['relative'])
    values.append(power_spectrum['C4']['alpha']['relative'])
    values.append(power_spectrum['P3']['alpha']['relative'])
    values.append(power_spectrum['P4']['alpha']['relative'])
    values.append(power_spectrum['O1']['alpha']['relative'])
    values.append(power_spectrum['O2']['alpha']['relative'])
    values = values[-10:]
    mean_value = np.mean(values)
    mean_value = (mean_value - 0.06) / (0.12 - 0.06)

    print("Changing to: ", 1 - mean_value)

    nightlight.set_night_light_value(mean_value)

    sleep(1)