import os
import sys
import glob
import yt_dlp

USERNAME = ""
COOKIES_DIR = "cookies/cookies.txt"
OUTPUT_DIR = "../songs"

def download_soundcloud_likes():
    url = f"https://soundcloud.com/{USERNAME}/likes"
    
    ydl_opts = {
        'cookiefile': COOKIES_DIR,
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'writethumbnail': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },

            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },

            {
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': True,
            }
        ],
        'retries': 10,
        'sleep_interval': 1,
        'max_sleep_interval': 3,
        'ignoreerrors': True,
        'concurrent_fragment_downloads': 5,
        'windowsfilenames': True,
        'verbose': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        cleanup_thumbnails()

def cleanup_thumbnails():
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp']
    for ext in image_extensions:
        for file_path in glob.glob(os.path.join(OUTPUT_DIR, ext)):
                os.remove(file_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.error("You must enter your SoundCloud username (EX: 'python main.py username')")
    else:
        USERNAME = sys.argv[1]
        
        print(f"Starting download of {USERNAME}'s liked tracks")
        download_soundcloud_likes()
        print("\nDownload completed!")
