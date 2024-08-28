from pytubefix import YouTube
import moviepy.editor as mpe
from pathlib import Path
import os

yt=""

def youtube_object_creater(url=""):
    global yt
    yt = YouTube(url)

def get_resolutions():
    stream_query = yt.streams.filter(file_extension="mp4",type="video").order_by("resolution")
    resolutions = []
    for res in stream_query:
        if (res.resolution not in resolutions):
            resolutions.append(res.resolution)
    return resolutions

def downloader(res,downloads_path,download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    video = yt.streams.filter(res=res).first()
    if video.is_progressive == True:
        video.download(filename=f"{download_folder}\\{yt.title}_{res}.mp4")
    else:
        video.download(filename=f"{download_folder}\\video1.mp4")
        yt.streams.filter(type="audio").order_by("abr").desc().first().download(filename=f"{download_folder}\\audio1.mp3")
        video_combiner(res,downloads_path,download_folder)

def get_thumbnail():
    thumbnail = yt.thumbnail_url
    return thumbnail

def get_title():
    title = yt.title
    return title

def audio_download(downloads_path,download_folder):
    yt.streams.filter(type="audio").order_by("abr").desc().first().download(filename=f"{download_folder}\\{yt.title}.mp3")

def video_combiner(res,downloads_path,download_folder):

    my_clip = mpe.VideoFileClip(f"{download_folder}\\video1.mp4")
    audio_background = mpe.AudioFileClip(f"{download_folder}\\audio1.mp3")
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(f"{download_folder}\\{yt.title}_{res}.mp4", codec="libx264")
    os.remove(f"{download_folder}\\video1.mp4")
    os.remove(f"{download_folder}\\audio1.mp3")
    print("Download Completed!")
 