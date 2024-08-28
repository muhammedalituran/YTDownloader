from tkinter import *
from tkinter import ttk,messagebox
import YT_Downloader
from PIL import Image,ImageTk
from urllib.request import urlopen
from pathlib import Path
import os


#variables
res_list = []

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def get_thumbnail_gui():
    
    th_url = YT_Downloader.get_thumbnail()
    img = Image.open(urlopen(th_url)).resize((256,144), Image.LANCZOS)
    ph = ImageTk.PhotoImage(img)
    thumbnail_label.config(image=ph)
    thumbnail_label.image = ph
    video_title = YT_Downloader.get_title()
    title_lable.config(text=video_title)

def download():
    downloads_path = str(Path.home() / "Downloads")
    download_folder = downloads_path + "\YoutubeDownloads_byTuran"
    if radio_check_state.get() == 1:
        YT_Downloader.downloader(res_combobox.get(),downloads_path,download_folder)
        messagebox.showinfo("Download Info","Download Completed!")

    if radio_check_state.get() == 2:
        res_combobox.place_forget()
        YT_Downloader.audio_download(downloads_path,download_folder)
        messagebox.showinfo("Download Info","Download Completed!")

def video_download_menu():
    res_list = YT_Downloader.get_resolutions()
    res_combobox.config(values=res_list)
    res_combobox.set("Pick a resolution")
    res_combobox.place(x=10,y=80)

def radiocheck_selected():
    if radio_check_state.get() == 2:
        res_combobox.place_forget()
    return radio_check_state.get()

def paste():
    clipboard = window.clipboard_get() # Get the copied item from system clipboard
    link_entry.insert('end',clipboard) # Insert the item into the entry widget


#Main windows
window = Tk()
window.minsize(width=800,height=450)
window.title("Youtube Downloader \ ByTuran")
"""
#Logo
ico = Image.open(resource_path("logo.png")).resize((256,144), Image.LANCZOS)
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
logo_label = Label(image=photo)
logo_label.image= photo
logo_label.place(x=540,y=300)
"""
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 800
window_height = 450
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#Enter url and chech link
link_label = Label(text="Enter URL:")
link_label.place(x=0,y=10)

link_entry = Entry(width=60)
link_entry.place(x=60,y=10)


link_button = Button(text="Check",command=lambda:[YT_Downloader.youtube_object_creater(link_entry.get()),get_thumbnail_gui()])
link_button.place(x=430,y=7)


m = Menu(window, tearoff = 0)
m.add_command(label ="Paste",command=paste) 

  
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
link_entry.bind("<Button-3>", do_popup) 

#Get video thumbnail and title
thumbnail_label = Label(image="")
thumbnail_label.place(x=500,y=25)

title_lable = Label()
title_lable.place(x=500,y=180)



#Download type selection
radio_check_state = IntVar()
emty_radiobutton = Radiobutton(text="bos",value=0,variable= radio_check_state,command=video_download_menu)
video_radiobutton = Radiobutton(text="Download Video",value=1,variable= radio_check_state,command=video_download_menu)
video_radiobutton.place(x=10,y=50)

audio_radiobutton = Radiobutton(text="Download Audio",value=2,variable= radio_check_state,command=radiocheck_selected)
audio_radiobutton.place(x=130,y=50)

#Download Button
download_button = Button(text="Download",command=download)
download_button.place(x=300,y=100)

#Resolution list
res_combobox = ttk.Combobox()


window.mainloop()