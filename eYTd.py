from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import youtube_dl
import requests
import os
import time
#########################################################FUNCIONES#####################################################

def moving_script():
    """ A very simple UNIX Script that moves all the downloaded files into the user's home folder.
    If the folder doesn't exist, creates the folder"""
    os.system("bash $HOME/Documentos/Programasion/PROJECTOe/moving_script.sh")

def url_generator(term):

    """Returns a list of links given a term by the user"""

    url = term
    webpage_url = "http://www.youtube.com/results?search_query=" + url.replace(" ", "+")
    webpage_url = urllib.parse.quote(webpage_url, safe='/:?+=', encoding="utf-8", errors="strict")
    webpage_request = urllib.request.urlopen(webpage_url)
    status_code = webpage_request.getcode()

    if status_code == 200:
        list_of_videos = []
        html = BeautifulSoup(webpage_request, "html.parser")
        videos = html.find_all('div', {'class': 'yt-lockup-content'})
        for i, video in enumerate(videos):
            if len(list_of_videos) < 5:
                link = video.find('a')['href']
                formatted_text = "https://www.youtube.com{0}".format(link)
                list_of_videos.append(formatted_text)

    return list_of_videos

def name_generator(term):

    """ Like url_generator, returns a list of names given a term by the user. This complements with url_generator"""

    url = term
    webpage_url = "http://www.youtube.com/results?search_query=" + url.replace(" ", "+")
    webpage_url = urllib.parse.quote(webpage_url, safe='/:?+=', encoding="utf-8", errors="strict")
    webpage_request = urllib.request.urlopen(webpage_url)
    status_code = webpage_request.getcode()

    if status_code == 200:
        list_of_names = []
        html = BeautifulSoup(webpage_request, "html.parser")
        videos = html.find_all('div', {'class': 'yt-lockup-content'})
        for i, video in enumerate(videos):
            if len(list_of_names) < 5:
                name = video.find('a')['title']
                watch = video.find('a')['href']
                watch_formatted = watch.replace("/watch?v=","")
                formatted_text = "{0}-{1}".format(name, watch_formatted)
                list_of_names.append(formatted_text)

    return list_of_names


def opt_1(term, aud_format, playlist_mode=True):

    """ Using Youtube_DL and FFmpeg, it downloads the video and extracts the audio
        and finally, it converts the output to a desire audio format
    """
    ydl_opts={
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': '{}'.format(playlist_mode),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': '{}'.format(aud_format),
            'preferredquality': '320'
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(term)])
    


def opt_2 (url, aud_format, playlist_mode=True):

    """ Same as opt_1, but keeps the video """

    ydl_opts={
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s-audio',
        'noplaylist': '{}'.format(playlist_mode),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': '{}'.format(aud_format),
            'preferredquality': '320'
        }]
    }

    ydl2_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': '{}'.format(playlist_mode),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(url)])
    with youtube_dl.YoutubeDL(ydl2_opts) as ydl:
        ydl.download(['{}'.format(url)])
    
def opt_3(term, playlist_mode=True):

    """Same as opt_1, but only downloads the video"""

    ydl_opts={
        'noplaylist': '{}'.format(playlist_mode),
        'outtmpl': '%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["{}".format(term)])
    


#########################################################FUNCIONES###################################################
print("\t Welcome to eYTd\n")
user_selection = int(input("Select an option:\n1.Audio from YT URL\n2.Audio and Video from YT URL\n3.Video from YT URL\n4.Search by term on Youtube\n5.Exit\n---> "))
playlist_mode = True

if user_selection == 1:
    user = input("Enable Playlist mode?[Y/n]: ")
    if user == "sSYy":
        playlist_mode = False
    url = input("Input the video here: ")
    aud_format = input("Select a format [default --> mp3]: ")
    if aud_format == "":
        aud_format = "mp3"
    opt_1(url, aud_format, playlist_mode)
    moving_script()

elif user_selection == 2:
    user = input("Enable Playlist mode?[Y/n]: ")
    if user == "sSYy":
        playlist_mode = False
    url = input("Input the video here: ")
    aud_format = input("Select a format [default --> mp3]: ")
    print(aud_format)
    if aud_format == "":
        aud_format = "mp3"
    opt_2(url, aud_format, playlist_mode)
    moving_script()

elif user_selection == 3:
    user = input("Enable Playlist mode?[Y/n]: ")
    if user == "sSYy":
        playlist_mode = False
    url = input("Input the video here: ")
    opt_3(url, playlist_mode)
    moving_script()

elif user_selection == 4:
    user = input("Input a Search Term here: ")
    print("Searching...")
    url_list = url_generator(user)
    name_list = name_generator(user)
    for index in range(5):
        formatted_index = index+1
        print("{} ---> {}".format(formatted_index, name_list[index]))
    selection = int(input("Select the video: "))-1
    link = url_list[selection]
    opt_choice = input("Do you want to keep the video, the sound or both?[default -->  sound]: ").lower()
    if opt_choice == "":
        opt_choice = "sound"
        sound_format = input("Select a format[default --> mp3]")
        if sound_format == "":
            sound_format = "mp3"
        opt_1(url_list[selection], sound_format)
        moving_script()
    elif opt_choice == "video":
        opt_3(url_list[selection])
        moving_script()
    else:
        sound_format = input("Select a format the sound file [default --> mp3]")
        if sound_format == "":
            sound_format = "mp3"
        opt_2(url_list[selection], sound_format)
        moving_script()
elif user_selection == 5:
    os.system("clear")
    print("Thanks for using the program")
    time.sleep(2)
    os.system("clear")
