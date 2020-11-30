from os import walk
from playsound import playsound
from random import randrange
import tkinter as tk
from PIL import Image, ImageTk

clear = input("Would you like to clear played files? [y/N] ")
if clear.lower() == "y":
    with open("played", "w") as f:
        f.write("")

DIRECTORY = "recordings"
_, _, files = next(walk(DIRECTORY))

lastindex = None

def play():
    global lastindex
    if len(files):
        index = randrange(len(files))
        with open("played") as f:
            played = list(map(lambda x: x.strip(), f.readlines()))
            while files[index] in played:
                index = randrange(len(files))
        playsound(f"{DIRECTORY}/{files[index]}")
        lastindex = index
    else:
        print("All files played.")

def getcolor(event):
    if not lastindex is None:
        value = img.getpixel((event.x, event.y))
        with open("played", "a") as f:
            f.write(files[lastindex]+"\n")
        files.pop(lastindex)
        print(value)
    play()

root = tk.Tk()
img = Image.open("colorspace.png").resize((640,640))
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img_tk)
label.pack()
root.resizable(False, False)
root.bind("<Button 1>", getcolor)

root.mainloop()