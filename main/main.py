#! /main/venv2/bin/python3
import os
import argparse
import yt_dlp

USERNAME = ""
COOKIES_DIR = "cookies/cookies.txt"
OUTPUT_DIR = "songs"

def download_soundcloud_likes():
    url = f"https://soundcloud.com/{USERNAME}/likes"
    
    ydl_opts = {
        'cookiefile': COOKIES_DIR,
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'retries': 10,
        'sleep_interval': 5,
        'max_sleep_interval': 15,
        'ignoreerrors': True,
        'concurrent_fragment_downloads': 5,
        'windowsfilenames': True,
        'verbose': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

USERNAME = input("Enter soundcloud username: ")
print(f"Starting download of {USERNAME}'s liked tracks")
download_soundcloud_likes()
print("\nDownload completed!")
