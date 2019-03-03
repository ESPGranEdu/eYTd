# eYTd

A CLI python based program that allows you to download either video or sound files from Youtube but also from other sources

## Requirements
By now, you will need to execute this program:

* [Python 3.x](https://www.python.org/)
* [FFMpeg](https://www.ffmpeg.org/), to convert both audio and video
* [Youtube-DL](https://rg3.github.io/youtube-dl/) to fetch videos from multiples sources... and also from Youtube, was created for that ¯\_(ツ)_/¯

### Installing Python
It's possible that you already have Python installed in your system, but In case you don't have Python installed, just follow the next instuctions:
```
sudo apt install python3 ffmpeg
```
* For Fedora based systems:
```
sudo yum install python3 ffmpeg
```
* For Suse based systems:
```
sudo zypper install python3 ffmpeg
```
* For Arch based systems:
```
sudo pacman -S python3 ffmpeg
```
### Installing core packages
If you don't have pip installed, run this command before the below one:
```
sudo apt install python3-pip
```
* For Fedora based systems:
```
sudo dnf install python3-pip
```
* For Suse based systems:
```
sudo zypper install python3-pip
```
* For Arch based systems:
```
sudo pacman -S python-pip
```
To install the packages listed in requirements.txt, you just simply type into a terminal the following command:
```
sudo pip3 install -r requirements.txt
```
Make sure that requirements.txt it's in the eYTd's folder

## Installing in Windows
Soon will be added the cross-platform usage of the program (if I can do that, more o less...)
