import qrcode
from tkinter import *
from tkinter import messagebox

data="https://www.youtube.com/watch?v=pdy3nh1tn6I&t=3230s"
img=qrcode.make(data)
img.save("qrcode.png")
