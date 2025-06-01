# SoundCloud Likes Downloader

Not the fastest downloader of liked songs.

*There are probably better ways to download all the songs without using cookies, so I do <ins>NOT</ins> recommend this script.*

# Usage

Put cookies in the cookies folder `(to get cookies you can use the cookie.txt browser extension)`

Make sure dependencies are installed
Go to the main folder open the console and run 
```bash
python main.py <soundcloud_user_name_here>
```

The songs will be saved in the songs folder

# Get Username `(if script not work)`

Go to your soundcloud profile and copy this part of the url `(this is your username)`

![image](https://github.com/user-attachments/assets/53cf9367-9f46-462d-9d10-af8302aae86c)


# Cookies

You need soundcloud cookies for the script to work. 

You can get them with the help of browser extension cookies.txt

After installing the extension, go to soundcloud and click on current site in the extension.

Place the saved cookies in the cookies folder of script.

# Installation

**FOR LINUX**

1) Click 'Code' button at `https://github.com/nik0mi/SoundCloud-Likes-Downloader` and download the ZIP onto your Desktop.

2) Extract the zip on desktop.

3) Open up Terminal.

4) In terminal type `cd ~/Desktop/SoundCloud-Likes-Downloader-main`.

5) In terminal type `pip install virtualenv`.

6) In the prompt type `virtualenv venv2`.

7) In the prompt type `source venv2/bin/activate (source venv2/bin/activate.fish # if using fish shell)`.

8) In the prompt type `pip install -r requirements.txt`

9) Run the script by typing `python main.py <soundcloud_user_name_here>`

10*) Run `sudo pacman -S ffmpeg` if ffmpeg not installed 

**FOR WINDOWS**

none

because I'm too lazy
`the installation process is unlikely to be much different`
