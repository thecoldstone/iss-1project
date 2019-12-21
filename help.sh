#!/bin/bash

#BRIEF INFORMATION REGARDING THIS BASH SCRIPT
#--------------------------------------------
##That's a simple bash script which help you to minimize your work with:
### 1. Install sox if it is not installed
### 2. Play the audio (Firstly you need to install sox)
### 3. Convert audio to wav format.
### 4. Trim silence.
### 5. Get the data of converted wav files such as Samples read, length in seconds etc.
##How to use?
### Just uncomment the needed line.
#----------------------------------

##If "sox" is not installed:
#--------------------------
#brew install sox
#----------------

##With command "play" we can play any file format supported by sox:
#-----------------------------------------------------------------
#play nameOftheFile.wav(.mp3)
#----------------------------

##Convert into wav format with specific characteristics:
#------------------------------------------------------
#Example:
###
# ffmpeg -i sa1.m4a    -ar 16000 -ac 1 -acodec pcm_s16le sa1.wav
#---------------------------------------------------------------

#Convert all files to wav format
#SENTENCES=$(cd original && ls | grep .m4a)
#PATH_TO_ORIGINAL=$(cd original && pwd)
#
#if [ ! -d wav ]
#then
#    mkdir wav
#else
    #https://stackoverflow.com/questions/226703/how-do-i-prompt-for-yes-no-cancel-input-in-a-linux-shell-script
#    while true; do
#        read -p "The folder with this name already exist. Do you really want to rewrite data? [y/n]" yn
#        case $yn in
#            [Yy]* ) break;;
#            [Nn]* ) echo "Nothing has been changed" && exit;;
#        esac
#    done
#fi
#
#PATH_TO_WAV=$(cd wav && pwd)
#
#for i in $SENTENCES;
#do
#    name=$(echo "$i" | sed s/.m4a/.wav/)
#	ffmpeg -i "$PATH_TO_ORIGINAL"/"$i" -ar 16000 -ac 1 -acodec pcm_s16le "$name"
#	mv "$name" "$PATH_TO_WAV"
#done

#---------------------------------------------

##Trim silence from both end in one fell swoop:
#---------------------------------------------
#sox q1.wav q1_test.wav silence 1 0.1 1% reverse silence 1 0.1 1% reverse

##Get the (Samples read) and (Length in seconds):
#-----------------------------------------------
#WAVS=$(ls | grep .wav)
#for i in $WAVS
#do
#    echo $(sox "$i" -n stat);
#done
