from tkinter import *
from tkinter import font
from pytube import YouTube
# 
root = Tk()
root.geometry('533x333')
root.maxsize(544,444)
root.minsize(400,300)
root.title("YouTube Video Downloader")
# 
frontText = Label(root, text="YouTube Video Downloader", font ='comicsansms 18 bold').pack()
linkBox = StringVar()
textVar2 = Label(root, text="Enter Youtube Video link here ", font='comicsansms 10 bold').place(x=155, y=45)
linkEntry = Entry(root,textvariable=linkBox, width=78).place(x=30, y= 90)
# DonwloaderFunction()
def YTVideoDownload():
    ytURL = YouTube(str(linkBox.get()))
    ytVideo = ytURL.streams.first()
    ytVideo.download('H:\\MCHX CODE FIELD (2021-22)\\YEAR 2022\\PYTHON TKINTER GUI 2022\\02 TK PROJECT(01)\\01 TK')
    textVar3 = Label(root, text="Downloaded", bg='green', foreground='white',font = 'comicsansms 12 bold').place(x=208, y= 185)
# 
button1 = Button(root, text="Download", font="comicsansms 12 bold",bg='blue', foreground='white', command=YTVideoDownload).place(x=210,y=145)
# 
root.mainloop()
# Arup Mondal (@MondalCodeHub-2022)