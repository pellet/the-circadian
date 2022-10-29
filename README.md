- Clone this repo
- Use the create-env.sh or update-env.sh for setting up the conda/python environment.
- Clone eegsynth: https://github.com/eegsynth/eegsynth
- Execute install.sh in bin directory
- Install redis-server
- Execute buffer module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 1st step)
- Execute openbci module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial3.md)
- Execute plotter module (https://github.com/eegsynth/eegsynth/blob/master/doc/tutorial1.md, 3rd step)

 
Note: depending on version of qt you may have to edit depricatedvalues in plotsignal.py, ie. GraphicsWindow is now GraphicsLayoutWidget,  import QtWidgets for QtApplications.
