#!/usr/bin/python

import sys
from pytube import YouTube 
import pathlib

if (len(sys.argv) == 2):
    link = str(sys.argv[1])
    try:
        yt = YouTube(link)
    except:
        print("[-] Link connection error\n")
        exit()
    print("[+] Link connection success!")

# print(yt.streams.filter(progressive=True).all())
# print()
# print(yt.streams.filter(progressive=True).order_by('resolution').desc().all())
# print()
# print(yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first())
# print(yt.streams.filter(adaptive=True,file_extension='mp4').order_by('resolution').desc().first())

    try:
        yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            ).order_by('resolution').desc().first().download()
        # yt.streams.filter(adaptive=True,file_extension='mp4').order_by('resolution').desc().first().download() # bug video only, no audio
        # could potentially download video and audio seperately and combine with ffmpeg
    except:
        print("[-] Download failed")
        exit()
    print("[+] Youtube video '{}' downloaded!".format(yt.title))
    print("\tVideo saved in directory path: '{}/{}'".format(pathlib.Path(__file__).parent.resolve(),yt.title))
else:
    print("[-] Usage: python3 <python_file_name> <youtube video link>")
    exit()
