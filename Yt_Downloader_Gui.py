from tkinter import *
import YT_Downloader
from PIL import Image,ImageTk
from urllib.request import urlopen




#variables




window = Tk()
window.minsize(width=600,height=450)
window.title("Youtube Downloader \ ByTuran")



link_label = Label(text="Enter URL:")
link_label.grid(row=0,column=0)

link_entry = Entry()
link_entry.grid(row=0,column=1)

link_button = Button(text="Check",command=lambda:[YT_Downloader.youtube_object_creater(link_entry.get()),get_thumbnail_gui()])
link_button.grid(row=0,column=3)

thumbnail_label = Label(image="")
thumbnail_label.grid(row=1,column=4)

def get_thumbnail_gui():
    
    th_url = YT_Downloader.get_thumbnail()
    img = Image.open(urlopen(th_url)).resize((200,200), Image.LANCZOS)
    ph = ImageTk.PhotoImage(img)
    thumbnail_label.config(image=ph)
    thumbnail_label.image = ph
    

window.mainloop()