from tkinter import *
from tkinter import ttk,messagebox
import YT_Downloader
from PIL import Image,ImageTk
from urllib.request import urlopen
from pathlib import Path
import os
import moviepy.editor as mpe


#variables
res_list = []



window = Tk()
window.minsize(width=850,height=450)
window.title("Youtube Downloader \ ByTuran")


#Enter url and chech link
link_label = Label(text="Enter URL:")
link_label.place(x=0,y=10)

link_entry = Entry(width=60)
link_entry.place(x=60,y=10)

link_button = Button(text="Check",command=lambda:[YT_Downloader.youtube_object_creater(link_entry.get()),get_thumbnail_gui()])
link_button.place(x=430,y=7)


#Get video thumbnail and title
thumbnail_label = Label(image="")
thumbnail_label.place(x=480,y=25)

title_lable = Label()
title_lable.place(x=480,y=170)

#Select download video or audio

def radiocheck_selected():
    return radio_check_state.get()


res_combobox = ttk.Combobox()

def video_download_menu():
    res_list = YT_Downloader.get_resolutions()
    res_combobox.config(values=res_list)
    res_combobox.set("Pick a resolution")
    res_combobox.place(x=10,y=80)
    





radio_check_state = IntVar()
emty_radiobutton = Radiobutton(text="bos",value=0,variable= radio_check_state,command=video_download_menu)
video_radiobutton = Radiobutton(text="Download Video",value=1,variable= radio_check_state,command=video_download_menu)
video_radiobutton.place(x=10,y=50)

audio_radiobutton = Radiobutton(text="Download Audio",value=2,variable= radio_check_state,command=radiocheck_selected)
audio_radiobutton.place(x=130,y=50)


def download():
    downloads_path = str(Path.home() / "Downloads")
    download_folder = downloads_path + "\YoutubeDownloads_byTuran"
    YT_Downloader.downloader(res_combobox.get(),downloads_path,download_folder)
    messagebox.showinfo("Download Info","Download Complited")



download_button = Button(text="Download",command=download)
download_button.place(x=300,y=100)


def get_thumbnail_gui():
    
    th_url = YT_Downloader.get_thumbnail()
    img = Image.open(urlopen(th_url)).resize((256,144), Image.LANCZOS)
    ph = ImageTk.PhotoImage(img)
    thumbnail_label.config(image=ph)
    thumbnail_label.image = ph
    video_title = YT_Downloader.get_title()
    title_lable.config(text=video_title)
    

window.mainloop()