#!/bin/bash

#A script that complements eYTd to move the files to the home folder of the user

USER_FOLDER=$HOME
DOWNLOADS_FOLDER="$HOME/eYTd"
AUDIO="$DOWNLOADS_FOLDER/Audio"
VIDEO="$DOWNLOADS_FOLDER/Video"

if [ -d "$HOME/$DOWNLOADS_FOLDER" ]; then
    echo "Moving Files..."
else
    mkdir $DOWNLOADS_FOLDER
    echo "Moving Files..."
fi


if [ -d "$AUDIO" ]; then
      mv -v ./*.{mp3,flac,m4a,opus,vorbis,wav} $AUDIO 2>/dev/null
else
    mkdir $AUDIO
    mv -v ./*.{mp3,flac,m4a,opus,vorbis,wav} --target=$AUDIO 2>/dev/null
fi


if [ -d "$VIDEO" ]; then
    mv -v ./*.{mkv,mp4,avi,webm,flv,ogg} --target=$VIDEO 2>/dev/null
else
    mkdir $VIDEO
    mv -v ./*.{mkv,mp4,avi,webm,flv,ogg} --target=$VIDEO 2>/dev/null
fi

echo -e "\nAll files moved succesfully"
