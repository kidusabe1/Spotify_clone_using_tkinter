import pygame
import tkinter

home=tkinter.Tk()
home.config(bg="#191414")
home.geometry("200x200")
home.resizable(False,False)
pygame.mixer.init()
pygame.mixer.music.load("mp1.mp3")

icons=tkinter.StringVar()
text=tkinter.StringVar()
i=0

def pause():
    global i
    global icons
    global text

    if i==0:
        pygame.mixer.music.play()
        i+=1
        icons.set("⏸")
        text.set("Playing I'm yours")
    elif i==1:
        pygame.mixer.music.pause()
        i+=1
        icons.set("►")
        text.set("Paused")
    else:
        pygame.mixer.music.unpause()
        i-=1
        icons.set("⏸")
        text.set("Playing I'm yours")

def stop():
    global i
    global icons
    global text
    pygame.mixer.music.stop()
    i=0
    icons.set("►")
    text.set("I'm yours stopped")

header=tkinter.Label(home,textvariable=text,bg="black",fg='white',width=20,height=0,anchor="center",font=("Gotham", 12, "bold"))
header.grid(padx=0,pady=20,column=0,row=0,columnspan=13,sticky="NEWS")

bplay=tkinter.Button(home,textvariable=icons,width = 3, height = 0,
    padx=0, pady=0, borderwidth=0,
    bg = "#1DB954", fg = "white", 
    font = ("Gotham", 20, "bold"),
    relief=tkinter.GROOVE, command=pause)

icons.set("►")
text.set("Press ► to Play")
bplay.grid(padx=25, pady=0, column=0, row=1, sticky="NEWS")

bstop=tkinter.Button(home, text="⏸",width = 3, height = 0,
    padx=0, pady=0, borderwidth=0,
    bg = "red", fg = "white",
    font = ("Gotham", 20, "bold"),
    relief=tkinter.GROOVE, command=stop)

bstop.grid(padx=25, pady=0, column=1, row=1, sticky="NEWS")

home.mainloop()