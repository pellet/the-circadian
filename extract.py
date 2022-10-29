import mne
import numpy as np
from scipy import signal
from scipy.integrate import simps


def get_power_relative(signal_data,
                       target_bands=None):
    """
    Reads and parses an edf file, takes a 1-second segment,
    """
    # How large should the chunk of EEG be?
    window_seconds = 1
    target_bands = [("theta", 4, 8),
                    ("alpha", 8, 12),
                    ("beta", 12, 30),
                    ("gamma", 30, 100)] if target_bands is None else target_bands
    arr, sfreq, ch_names = signal_data
    arr = arr[:, 0:int(sfreq*window_seconds)]
    return get_powers(arr, ch_names, sfreq, target_bands)


def get_array_mne(fname):
    """
    Loads an edf file, filters it and returns raw data as numpy array, sample frequency and channel names
    """
    # TODO: select channels
    raw = mne.io.read_raw_edf(fname, preload=True)
    raw.notch_filter(50, notch_widths=3)
    raw.filter(1, 60)
    sfreq = raw.info["sfreq"]
    ch_names = raw.ch_names
    arr = raw.get_data(ch_names)
    return arr, sfreq, ch_names


def get_powers(data, channels, sf, target_bands):
    """
    Computes absolute and relative band powers for each channel
    """
    # dict for results
    powers = {}

    # iterate through channels
    for channel in range(data.shape[0]):
        powers[channels[channel]] = {}
        # print("Channel: " + channels[channel])
        selected_channel = data[channel, ...]
        freqs, psd = signal.welch(selected_channel, sf)

        # Get absolute and relative band power for each frequency band
        for name, low, high in target_bands:
            powers[channels[channel]][name] = {}
            # Find intersecting values in frequency vector
            idx_delta = np.logical_and(freqs >= low, freqs <= high)

            # Frequency resolution
            freq_res = freqs[1] - freqs[0]  # = 1 / 4 = 0.25

            # Compute the absolute power by approximating the area under the curve
            delta_power = simps(psd[idx_delta], dx=freq_res)

            # Relative delta power (expressed as a percentage of total power)
            total_power = simps(psd, dx=freq_res)
            delta_rel_power = delta_power / total_power
            # print('relative band power ' + str(name) + ' power: %.3f' % delta_rel_power)

            # Save results to dict
            powers[channels[channel]][name]["absolute"] = delta_power
            powers[channels[channel]][name]["relative"] = delta_rel_power

    return powers
