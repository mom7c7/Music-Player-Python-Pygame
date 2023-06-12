# Modules
import os
import pygame
import tkinter as tt
from tkinter.filedialog import askdirectory

# Tkinter
mainmp = tt.Tk()
mainmp.geometry('386x386')
mainmp.title('MUSIC PLAYER')
mainmp.resizable(False,False)
# Tkinter - Askdirectory
mydir = askdirectory()

# Os for access 
os.chdir(mydir)
musiclist = os.listdir()

# Listbox

playlist = tt.Listbox(mainmp,selectmode=tt.SINGLE,bg='#3399FF')
playlist.pack(side='bottom',expand='yes',fill='x')

# *********************

for music in musiclist:
    pos = 0
    playlist.insert(pos,music)
    pos += 1

# Pygame
pygame.init()
pygame.mixer.init()

# Var

myvar = tt.StringVar()

# Function

def play():
    pygame.mixer.music.load(playlist.get(tt.ACTIVE))
    myvar.set(playlist.get(tt.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# Label

titles = tt.Label(mainmp,textvariable=myvar)
titles.pack()

# Button

btnplay = tt.Button(mainmp,height=2,width=4,text='PLAY',command=play,bg='#FF3333')
btnplay.pack(fill='x')
btnstop = tt.Button(mainmp,height=2,width=4,text='STOP',command=stop,bg='#999900')
btnstop.pack(fill='x')
btnpause = tt.Button(mainmp,height=2,width=4,text='PAUSE0',command=pause,bg='#006666')
btnpause.pack(fill='x')
btnunpause = tt.Button(mainmp,height=2,width=4,text='UNPAUSE',command=unpause,bg='#990099')
btnunpause.pack(fill='x')

mainmp.mainloop()