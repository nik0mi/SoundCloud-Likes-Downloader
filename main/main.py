import os
import sys
import glob
import yt_dlp

USERNAME = ""
COOKIES_DIR = "cookies/cookies.txt"
OUTPUT_DIR = "../songs"

def download_soundcloud_likes(start_index=None, end_index=None):
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

    if start_index is not None:
        range_str = str(start_index)
        if end_index is not None:
            range_str += f"-{end_index}"
        ydl_opts['playlist_items'] = range_str

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
        print("You must enter your SoundCloud username (EX: 'python main.py username [start] [end]')")
        sys.exit(1)
    
    USERNAME = sys.argv[1]
    start = None
    end = None

    if len(sys.argv) >= 3:
        try:
            start = int(sys.argv[2])
            if len(sys.argv) >= 4:
                end = int(sys.argv[3])
        except ValueError:
            print("Invalid range")
            start = None
            end = None

    range_info = "all tracks" 
    if start is not None:
        range_info = f"tracks {start}"
        if end is not None:
            range_info += f" to {end}"
        else:
            range_info += " onward"
    
    print(f"Starting download of {USERNAME}'s liked tracks ({range_info})")
    download_soundcloud_likes(start, end)
    print("\nDownload completed!")
