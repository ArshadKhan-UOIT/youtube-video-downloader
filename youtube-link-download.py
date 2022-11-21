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

    # video = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    # print(video.mime_type)
    # extension = video.mime_type
    # print(extension.split("/"))
    # print(extension.split("/")[0])
    # print(extension.split("/")[1])
    # print(yt.streams.filter(progressive=True).all())
    # print()
    # print(yt.streams.filter(progressive=True).order_by('resolution').desc().all())
    # print()
    # print(yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first())
    # print(yt.streams.filter(adaptive=True,file_extension='mp4').order_by('resolution').desc().first())
    # print(yt.streams.get_highest_resolution())
    # print(yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first())


    try:
        video = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        video = yt.streams.get_highest_resolution() # this is the same as the above
        video.download()
        # yt.streams.filter(
        #     progressive=True,
        #     file_extension='mp4'
        #     ).order_by('resolution').desc().first().download()
        # yt.streams.filter(adaptive=True,file_extension='mp4').order_by('resolution').desc().first().download() # bug video only, no audio
        # could potentially download video and audio seperately and combine with ffmpeg
    except:
        print("[-] Download failed")
        exit()
    extension = video.mime_type
    print("[+] Youtube video '{}.{}' downloaded!".format(video.title,extension.split("/")[1]))
    print("\tVideo saved in directory path: '{}/{}.{}'".format(pathlib.Path(__file__).parent.resolve(),video.title,extension.split("/")[1]))
else:
    print("[-] Usage: python3 <python_file_name> <youtube video link>")
    exit()
