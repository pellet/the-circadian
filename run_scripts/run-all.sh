cd ..
redis-server &
SLEEP_TIME=5
sleep $SLEEP_TIME

INIFILES='../../template_inifiles'
cd eegsynth/module

# Execute buffer module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 1st step)
python buffer/buffer.py -i $INIFILES/buffer.ini &
sleep $SLEEP_TIME

# Execute openbci module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial3.md)
./openbci2ft/openbci2ft.sh -i $INIFILES/openbci2ft.ini &
sleep $SLEEP_TIME

# Execute plotter module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 3rd step)
python plotsignal/plotsignal.py -i $INIFILES/plotsignal.ini &
sleep $SLEEP_TIME

# Execute preprocessing module
python preprocessing/preprocessing.py -i $INIFILES/preprocessing.ini &
sleep $SLEEP_TIME

# Execute nightlight neurofeedback
cd ../../src
PYTHONPATH=$PYTHONPATH:../eegsynth/lib MNE_USE_NUMBA=false python ./test.py
sleep $SLEEP_TIME

# Wait for processes to finish
wait
