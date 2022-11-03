#!/bin/bash

# Execute buffer module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 1st step)
./buffer.sh

# Make sure Redis server is started
./redis.sh

# Stream EEG data over network via LSL from the OpenBCI GUI, 
# NOTE: not using openbci2ft due to experiencing issues.
./lsl2ft.sh

# Execute playback
# ./playbacksignal.sh

echo Waiting for a few seconds ...
sleep 10

./preprocessing.sh

echo Waiting for a few seconds ...
sleep 5

# Execute plotter module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 3rd step)
./plotsignal.sh

# Execute recording to edf file
# ./recordsignal.sh

# Execute nightlight neurofeedback
./the-circadian.sh
