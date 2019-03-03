# eYTd

A CLI python based program that allows you to download either video or sound files from Youtube but also from other sources

## Requirements
By now, you will need to execute this program:

* [Python 3.x](https://www.python.org/)
* [FFMpeg](https://www.ffmpeg.org/), to convert both audio and video
* [Youtube-DL](https://rg3.github.io/youtube-dl/) to fetch videos from multiples sources... and also from Youtube, was created for that ¯\_(ツ)_/¯
* For Linux&Mac users, you should give executions permissions to the **moving_script.sh** 

### Installing Python
It's possible that you already have Python installed in your system, but In case you don't have Python installed, just follow the next instuctions:
```
Debian --> sudo apt install python3 ffmpeg
Fedora --> sudo yum install python3 ffmpeg
Suse   --> sudo zypper install python3 ffmpeg
Arch   --> sudo pacman -S python3 ffmpeg
```
### Installing core packages
To install the packages listed in requirements.txt, you just simply type into a terminal the following command:
```
sudo pip3 install -r requirements.txt
```
Make sure that requirements.txt it's in the eYTd's folder

## Usage
The program mainly has 4 options to chose:

* **Download Audio file from a URL (opt_1) -->** Search the video in the given URL and downloads the audio source from it.
* **Download Video with his audio source (opt_2) -->** Same as opt_1 but downloads the video source too.
* **Download Video source (opt_3) -->** Search the video in the given URl and downloads the audio source from it.
* **Search in Youtube by a given term (url_generator, name_generator) -->** Simply searchs from youtube and parse the url and name. It's limited to display only 5 video.

Before you enter the URL, you'll be prompt with and warning telling if you want to enable ***Playlist Mode***, means that by enabling this you can download an entire playlist whitout needing to enter every single URL.

## Examples
Download a video with his audio source converted to .flac format
![ejemplo1](https://user-images.githubusercontent.com/46658066/53695893-68ef3380-3dc1-11e9-9724-bb9ae389be92.gif)
Download an audio source from a playlist and converting it into .flac format
![ejemplo2](https://user-images.githubusercontent.com/46658066/53699286-cba6f600-3de6-11e9-9077-6a4e0718a1f9.gif)

