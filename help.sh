#!/bin/bash

##If "sox" is not installed:
#--------------------------
#brew install sox

##With command "play" we can play any file format supported by sox:
#-----------------------------------------------------------------
#play nameOftheFile.wav(.mp3)

##Convert into wav format with specific characteristics:
#------------------------------------------------------
#Example:
###
# ffmpeg -i sa1.m4a    -ar 16000 -ac 1 -acodec pcm_s16le sa1.wav


##Trim silence from both end in one fell swoop:
#---------------------------------------------
#sox q1.wav q1_test.wav silence 1 0.1 1% reverse silence 1 0.1 1% reverse

##Get the (Samples read) and (Length in seconds):
#-----------------------------------------------
WAVS=$(ls | grep .wav)
for i in $WAVS
do
#    name=$(echo "$i" | sed 's/.wav//');
#    echo "$name";
#    echo "Name of the file" > "$name".out;
#    echo ;
#    echo "$i";
#    tmp=$(sox "$i" -n stat);
    echo $(sox "$i" -n stat);
done



#for i in ./*.m4a;
#do 
	#echo "$i" ;
#	ffmpeg -i "$i" -ar 16000 -ac 1 -acodec pcm_s16le "$i.wav"
	#mv "$i" "~/Desktop/VUT\ FIT/2.year/ISS/SpeechRecognition/sentences/" ;
#done

