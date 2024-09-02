from tkinter import *
from tkinter import ttk,messagebox
import YT_Downloader
from PIL import Image,ImageTk
from urllib.request import urlopen
from pathlib import Path
import os



text_names = ["Enter Url:","Check","Download Video","Download Audio","Download","Language","Change"]


def Window(text):
    #variables
    res_list = []
    text_names = text
    def translate():
        global text_names
        if lang_combobox.get() == "TR":
            text_names = ["Video linki:","Getir","Video indir","Ses indir","Indir","Dil","Degistir"]
        else:
            text_names = ["Enter Url:","Check","Download Video","Download Audio","Download","Language","Change"]
        window.destroy()
        Window(text_names)
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
        res_combobox.place(x=15,y=255)

    def radiocheck_selected():
        if radio_check_state.get() == 2:
            res_combobox.place_forget()
        return radio_check_state.get()

    def paste():
        clipboard = window.clipboard_get() # Get the copied item from system clipboard
        link_entry.insert('end',clipboard) # Insert the item into the entry widget


    #Main windows
    window = Tk()
    window.minsize()
    window.title("Youtube Downloader \ ByTuran")

    #Logo
    ico = Image.open(resource_path("logo.png")).resize((256,144), Image.LANCZOS)
    photo = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(False, photo)
    logo_label = Label(image=photo)
    logo_label.image= photo
    logo_label.place(x=250,y=35)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 550
    window_height = 450
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    #Enter url and chech link
    link_label = Label(text=text_names[0])
    link_label.place(x=0,y=10)

    link_entry = Entry(width=60)
    link_entry.place(x=60,y=10)


    link_button = Button(text=text_names[1],command=lambda:[YT_Downloader.youtube_object_creater(link_entry.get()),get_thumbnail_gui()])
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
    thumbnail_label.place(x=15,y=45)

    title_lable = Label()
    title_lable.place(x=15,y=195)



    #Download type selection
    radio_check_state = IntVar()
    emty_radiobutton = Radiobutton(text="bos",value=0,variable= radio_check_state,command=video_download_menu)
    video_radiobutton = Radiobutton(text=text_names[2],value=1,variable= radio_check_state,command=video_download_menu)
    video_radiobutton.place(x=10,y=230)

    audio_radiobutton = Radiobutton(text=text_names[3],value=2,variable= radio_check_state,command=radiocheck_selected)
    audio_radiobutton.place(x=130,y=230)

    #Download Button
    download_button = Button(text=text_names[4],command=download)
    download_button.place(x=300,y=250)

    #Resolution list
    res_combobox = ttk.Combobox()
    #Language
    lang_combobox = ttk.Combobox(values=["TR","ENG"])
    lang_combobox.place(x=300,y=320)

    lang_label = Label(text=text_names[5])
    lang_label.place(x=300,y=295)

    lang_button = Button(text=text_names[6],command=translate)
    lang_button.place(x=450,y=320)
    window.mainloop()

Window(text_names)