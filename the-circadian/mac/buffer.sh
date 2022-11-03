#!/bin/bash

MODULE=`basename $0 .sh`

EEGSYNTH=../../eegsynth
INIDIR=..
WORKINGDIR=`pwd`

./terminal.scpt $WORKINGDIR/$EEGSYNTH/module/$MODULE/$MODULE.sh -i $WORKINGDIR/$INIDIR/$MODULE.ini
