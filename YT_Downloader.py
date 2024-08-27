# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:53:07 2024

@author: m_ali_s85f
"""
from pytubefix import YouTube
import moviepy.editor as mpe
from pathlib import Path
import os



downloads_path = str(Path.home() / "Downloads")
download_folder = downloads_path + "\YoutubeDownloads_byTuran"


yt=""

def youtube_object_creater(url=""):
    global yt
    yt = YouTube(url)

def get_resolutions(stream_query):
    resolutions = []
    for res in stream_query:
        if (res.resolution not in resolutions):
            resolutions.append(res.resolution)
    return resolutions

def downloader(res):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    video = yt.streams.filter(res=res).first()
    if video.is_progressive == True:
        video.download()
    else:
        video.download(filename=f"{download_folder}\\video1.mp4")
        yt.streams.filter(type="audio").order_by("abr").desc().first().download(filename=f"{download_folder}\\audio1.mp3")
        video_combiner(res)
def get_thumbnail():
    thumbnail = yt.thumbnail_url
    return thumbnail

        
def audio_download():
    yt.streams.filter(type="audio").order_by("abr").desc().first().download(filename=f"{download_folder}\\{yt.title}.mp3")

    
    
def video_combiner(res):

    my_clip = mpe.VideoFileClip(f"{download_folder}\\video1.mp4")
    audio_background = mpe.AudioFileClip(f"{download_folder}\\audio1.mp3")
    final_clip = my_clip.set_audio(audio_background)
    video_name = input("Please Enter A Video Title After Saving:")
    final_clip.write_videofile(f"{download_folder}\\{video_name}.mp4", codec="libx264")
    os.remove(f"{download_folder}\\video1.mp4")
    os.remove(f"{download_folder}\\audio1.mp3")
    print("Download Completed!")
 
"""
while True:
    if cevap == 2:
        resolutions = list(enumerate(get_resolutions(yt.streams.filter(file_extension="mp4",type="video").order_by("resolution"))))
        for order,res in resolutions:
            print(f"{order}-{res}")
        down_res = int(input("İndirmek istediğiniz çözünürlüğü giriniz:"))
        downloader(resolutions[down_res][1])
    if cevap == 3:
        audio_download()
    if cevap == 0:
        break"""