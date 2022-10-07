from distutils.cmd import Command
import tkinter
import pickle
from turtle import home
from PIL import ImageTk,Image

list_row_counter=1
search_result=[]
justice_album=[
    "2 much.mp3",
    "anyone.mp3",
    "ghost.mp3",
    "lifetime.mp3",
    "MLK.mp3"
]
coldplay_album=[
    "A sky full of stars.mp3",
    "Clocks.mp3",
    "Fix you.mp3",
    "Flags",
    "Higher Power.mp3",
    "Hymn for The weekend.mp3",
    "My universe.mp3",
    "paradise.mp3",
    "The Scientist.mp3",
    "Yellow.mp3"
]

the_smiths_album=[
    "Charming.mp3",
    "Girl Afraid.mp3",
    "Heaven Knows.mp3",
    "How soon.mp3",
    "The Smiths.mp3"
]
the_beatles_album=[
    "Come together.mp3",
    "Don't let me.mp3",
    "Here comes the sun.mp3",
    "Hey jude.mp3",
    "In my life.mp3",
    "Let it be.mp3",
    "Penny Lane.mp3",
    "Saw her Standing.mp3",
    "Strawberry.mp3"
]

All_songs={
    "A sky full of stars.mp3":0,
    "Clocks.mp3":0,
    "Fix you.mp3":0,
    "Flags":0,
    "Higher Power.mp3":0,
    "Hymn for The weekend.mp3":0,
    "My universe.mp3":0,
    "paradise.mp3":0,
    "The Scientist.mp3":0,
    "Yellow.mp3":0,
    "2 much.mp3":0,
    "anyone.mp3":0,
    "ghost.mp3":0,
    "lifetime.mp3":0,
    "MLK.mp3":0,
    "Charming.mp3":0,
    "Girl Afraid.mp3":0,
    "Heaven Knows.mp3":0,
    "How soon.mp3":0,
    "The Smiths.mp3":0,
    "Come together.mp3":0,
    "Don't let me.mp3":0,
    "Here comes the sun.mp3":0,
    "Hey jude.mp3":0,
    "In my life.mp3":0,
    "Let it be.mp3":0,
    "Penny Lane.mp3":0,
    "Saw her Standing.mp3":0,
    "Strawberry.mp3":0}
def playy():
    pass


# Starting with the Search Page
def open_search_page():
    search_page=tkinter.Toplevel(home_page)
    search_page.configure(bg="#191414")
    search_page.geometry("375x700")
    search_page.resizable(False,False)
    search_page.iconbitmap("spotify.ico")
    search_page.title("Spotify")
    search_entry=tkinter.Entry(search_page,width=30)
    search_entry.grid(row=0,column=1,padx=(0,5),ipadx=6,ipady=6,pady=5)

#####################
# Next Task is to figure out a way to display search result
#####################

    def button_print():
        pass
    def display_songs(res):
        global list_row_counter
        i=0
        while(i<len(res)):
            list_button=tkinter.Button(search_page,text=res[list_row_counter-1])
            list_button.configure(command=button_print)
            list_button.grid(row=list_row_counter,column=0,padx=0,pady=0,ipadx=0,ipady=0,sticky="NEWS")
            list_row_counter+=1
    
#########################
# Next Task is to figure out a way to display search result
#########################
    def final_search():
        to_be_searched=search_entry.get()
        for i in All_songs.keys():
            if to_be_searched in i.lower():
                search_result.append(i)
        if len(search_result)>0:
            display_songs(search_result)

    back_button=tkinter.Button(search_page,text="⬅️",
        bg="#191414",fg="white",
        font=("Helvetica",18,"bold"),
        activebackground="#191414",activeforeground="white",
        command=lambda:[search_page.destroy(),home_page.deiconify()])
    back_button.grid(row=0,column=0,pady=5,padx=8)
    execute_search=tkinter.Button(search_page,text="Search",
        bg="#1DB954",fg="white",border=0, font=("Helvetica",12,"bold"),
        activeforeground="white",activebackground="#1DB954",command=final_search)
    execute_search.grid(row=0,column=2,ipadx=6,ipady=6,padx=(5,3),pady=5)
    


    """
    command= lambda:[root.withdraw(),add_new_task()]
    command=lambda:[new_win.destroy(),root.deiconify()]
    """










































home_page=tkinter.Tk()
home_page.config(bg="#191414")
home_page.geometry("375x700")
home_page.resizable(False,False)
home_page.iconbitmap("spotify.ico")
home_page.title("Spotify")


welcome=tkinter.Label(home_page,text="Good Evening you!",
    bg="#191414",fg="white",
    font=("Helvetica",15,"bold"))
welcome.grid(row=0,column=0,pady=(20,0),padx=0,sticky="NEWS")

search_button=tkinter.Button(home_page,text="🔍", border=0,
    fg="white",bg="#191414",
    font=("Helvetica",17,"bold"),
    activebackground="#191414",
    activeforeground="white",
    command=lambda:[home_page.withdraw(),open_search_page()])
search_button.grid(row=0,column=1,ipadx=0,ipady=0,sticky="NES",pady=(20,0),padx=(0,10))
"""
# Search button
image=Image.open("more.png")
image.resize((10,10))
search_button_image= tkinter.PhotoImage(image)
search_button=tkinter.Label(image=search_button_image)
search_button.grid(row=0,column=1)
"""

top_hits_button=tkinter.Button(home_page,text="Today's Top Hits",
    fg="white",bg="#313131",border=0,
    font=("Helvetica",11,"bold"),
    activebackground="#191414",
    activeforeground="white")
top_hits_button.grid(row=1,column=0,padx=(40,20),pady=(20,10),ipadx=5,ipady=2.5)

Recently_played_button=tkinter.Button(home_page,text="Recently Played",
    fg="white",bg="#313131",border=0,
    font=("Helvetica",11,"bold"),
    activebackground="#191414",
    activeforeground="white")
Recently_played_button.grid(row=1,column=1,pady=(20,10),ipadx=5,ipady=2.5)

Most_popular_button=tkinter.Button(home_page,text="Most Popular",
    fg="white",bg="#313131",border=0,
    font=("Helvetica",11,"bold"),
    activebackground="#191414",
    activeforeground="white")
Most_popular_button.grid(row=2,column=0,padx=(40,20),pady=(5,10),ipadx=5,ipady=2.5,sticky="NEWS")

Favorite_songs_button=tkinter.Button(home_page,text="Favorite Songs",
    fg="white",bg="#313131",border=0,
    font=("Helvetica",11,"bold"),
    activebackground="#191414",
    activeforeground="white")
Favorite_songs_button.grid(row=2,column=1,pady=(5,10),ipadx=5,ipady=2.5,padx=(25,1),sticky="NWS")


practice_frame=tkinter.LabelFrame(home_page,border=0,bg="#191414")
practice_frame.grid(row=3,column=0,sticky="NEWS",padx=7,pady=0)
album_label=tkinter.Label(practice_frame,text="Albums", width=0,
    bg="#191414",fg="white",
    font=("Helvetica",11,"bold"))
album_label.grid(row=0,column=0,padx=0,ipadx=0,sticky="NEWS")

"""I = Image.open("ethiopia.png")
IR=I.resize((150,100),Image.ANTIALIAS)
P = ImageTk.PhotoImage(IR)
LI=Label(w, image=P, bg="#E3E6F0")
"""


justin_frame=tkinter.Frame(home_page,border=0,bg="#191414")
justin_frame.grid(row=4,column=0,sticky="NEWS")

justice_thumbnail=Image.open("justice.png")
thumbnail=justice_thumbnail.resize((150,150))
final=ImageTk.PhotoImage(thumbnail)
justice_thumbnail_button=tkinter.Button(justin_frame,image=final,
    height=150,width=150,
    border=0,bg="#191414",
    activebackground="#191414")
justice_thumbnail_button.grid(row=0,column=0,
    sticky="NEWS",
    padx=15,pady=(10,0),
    ipadx=0,ipady=0)

album_name_justice=tkinter.Label(justin_frame,text="Justice",
    fg="white",bg="#191414",
    font=("Helvetica",11,"bold"))
album_name_justice.grid(row=1,column=0,ipadx=0,padx=15,sticky="W")

artist_name_justin=tkinter.Label(justin_frame,text="Album Justin Bieber",
    fg="white",bg="#191414",
    font=("Helvetica",9,"bold"))
artist_name_justin.grid(row=2,column=0,ipadx=0,padx=15,sticky="W")



coldplay_frame=tkinter.Frame(home_page,border=0,bg="#191414")
coldplay_frame.grid(row=4,column=1,sticky="NEWS",padx=0,pady=0)

coldplay_thumbnail=Image.open("coldplay.png")
coldlpay_thumbnail_2=coldplay_thumbnail.resize((150,150))
coldplay_final=ImageTk.PhotoImage(coldlpay_thumbnail_2)
coldplay_thumbnail_button=tkinter.Button(coldplay_frame,image=coldplay_final,
    height=150,width=150,
    border=0,bg="#191414",
    activebackground="#191414")
coldplay_thumbnail_button.grid(row=0,column=0,
    sticky="NEWS",
    padx=15,pady=(10,0),
    ipadx=0,ipady=0)

album_name_coldplay=tkinter.Label(coldplay_frame,text="Cold Play",
    fg="white",bg="#191414",
    font=("Helvetica",11,"bold"))
album_name_coldplay.grid(row=1,column=0,ipadx=0,padx=15,sticky="W")

artist_name_coldplay=tkinter.Label(coldplay_frame,text="Album Cold PLay",
    fg="white",bg="#191414",
    font=("Helvetica",9,"bold"))
artist_name_coldplay.grid(row=2,column=0,ipadx=0,padx=15,sticky="W")



playlists_frame=tkinter.LabelFrame(home_page,border=0,bg="#191414")
playlists_frame.grid(row=5,column=0,columnspan=2,sticky="NEWS",padx=7,pady=0)
playlists_label=tkinter.Label(playlists_frame,text="Playlists", width=0,
    bg="#191414",fg="white",
    font=("Helvetica",11,"bold"))
playlists_label.grid(row=0,column=0,padx=0,pady=(10,0),ipadx=0,sticky="NEWS")

The_Beatles_frame=tkinter.Frame(home_page,border=0,bg="#191414")
The_Beatles_frame.grid(row=6,column=0,sticky="NEWS",padx=0,pady=0)
The_Beatles_thumbnail=Image.open("the_beatles.png")
The_Beatles_thumbnail_2=The_Beatles_thumbnail.resize((150,150))
The_Beatles_final=ImageTk.PhotoImage(The_Beatles_thumbnail_2)
The_Beatles_thumbnail_button=tkinter.Button(The_Beatles_frame,image=The_Beatles_final,
    height=150,width=150,
    border=0,bg="#191414",
    activebackground="#191414")
The_Beatles_thumbnail_button.grid(row=0,column=0,
    sticky="NEWS",
    padx=15,pady=(10,0),
    ipadx=0,ipady=0)

album_name_The_Beatles=tkinter.Label(The_Beatles_frame,text="The Beatles",
    fg="white",bg="#191414",
    font=("Helvetica",11,"bold"))
album_name_The_Beatles.grid(row=1,column=0,ipadx=0,padx=15,sticky="W")

artist_name_The_Beatles=tkinter.Label(The_Beatles_frame,text="Album The Beatles",
    fg="white",bg="#191414",
    font=("Helvetica",9,"bold"))
artist_name_The_Beatles.grid(row=2,column=0,ipadx=0,padx=15,sticky="W")



Smiths_frame=tkinter.Frame(home_page,border=0,bg="#191414")
Smiths_frame.grid(row=6,column=1,sticky="NEWS",padx=0,pady=0)
Smiths_thumbnail=Image.open("smiths.png")
Smiths_thumbnail_2=Smiths_thumbnail.resize((150,150))
Smiths_final=ImageTk.PhotoImage(Smiths_thumbnail_2)
Smiths_thumbnail_button=tkinter.Button(Smiths_frame,image=Smiths_final,
    height=150,width=150,
    border=0,bg="#191414",
    activebackground="#191414")
Smiths_thumbnail_button.grid(row=0,column=0,
    sticky="NEWS",
    padx=15,pady=(10,0),
    ipadx=0,ipady=0)

album_name_Smiths=tkinter.Label(Smiths_frame,text="Smiths",
    fg="white",bg="#191414",
    font=("Helvetica",11,"bold"))
album_name_Smiths.grid(row=1,column=0,ipadx=0,padx=15,sticky="W")

artist_name_Smiths=tkinter.Label(Smiths_frame,text="Album Smiths",
    fg="white",bg="#191414",
    font=("Helvetica",9,"bold"))
artist_name_Smiths.grid(row=2,column=0,ipadx=0,padx=15,sticky="W")







home_page.mainloop()