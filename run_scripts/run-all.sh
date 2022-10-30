cd ..
redis-server &
SLEEP_TIME=5
sleep $SLEEP_TIME

INIFILES='template_inifiles'
EEGSYNTH_MODULE='eegsynth/module'

# Execute buffer module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 1st step)
python $EEGSYNTH_MODULE/buffer/buffer.py -i $INIFILES/buffer.ini &
sleep $SLEEP_TIME

# Execute openbci module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial3.md)
$EEGSYNTH_MODULE/openbci2ft/openbci2ft.sh -i $INIFILES/openbci2ft.ini &
sleep $SLEEP_TIME

# Execute plotter module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 3rd step)
python $EEGSYNTH_MODULE/plotsignal/plotsignal.py -i $INIFILES/plotsignal.ini &
sleep $SLEEP_TIME

# Execute preprocessing module
python $EEGSYNTH_MODULE/preprocessing/preprocessing.py -i $INIFILES/preprocessing.ini &
sleep $SLEEP_TIME

# Execute nightlight neurofeedback
PYTHONPATH=$PYTHONPATH:eegsynth/lib MNE_USE_NUMBA=false python ./src/test.py
sleep $SLEEP_TIME

# Wait for processes to finish
wait
