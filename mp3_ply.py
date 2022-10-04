from pygame import mixer
mixer.init()
print("WELCOME TO OUR PREMIUM MP3 PLAYER ")
print("*"*50)
print("0)Create Playlist: ")
print("1)Load Music: ")
print("2)Play Music: ")
print("3)Pause Music: ")
print("4)Unpause Music: ")
print("5)Set Volume: ")
print("6)Skip Music In Seconds: ")
b=0
while(b==0):
    
    a=int(input("ENTER YOUR OPTION: "))
    if(a==0):
        print("Instructions To Create A Playlist: ")
        print("Copy Paste The Songs In The Folder Where Your MP3 Player Is Stored")
        print("Enter The Songs Name You Want To Add To The Playlist (case sensitive)")
        c=int(input("Enter Number Of Songs You want to Add: "))
        d=[]
        for i in range(0,c):
            e=input("Enter Name Of Song: ")
            d.append(e)
        print("*"*50)
    if(a==1):#load
        print("1)Play Playlist: ")
        print("2)Load A particular Music: ")
        f=int(input("Enter The Option: "))
        if(f==1):
            for i in range(0,len(d)):
                mixer.music.load(d[0]+".mp3")
                mixer.music.play()
        if(f==2):
            z=str(input("Enter the music name: "))
            mixer.music.load(z+".mp3")
        print("*"*50)    
    if(a==2):#plAY    
        mixer.music.play()
        print("*"*50)
    if(a==3):#pause
        mixer.music.pause()
        print("*"*50)
    if(a==4):#unpause
        mixer.music.unpause()
        print("*"*50)
    if(a==5):#set volume
        print("Current Volume Of The Song",mixer.music.get_volume())
        c=float(input("To Set The Volume Of Music Enter Value B/w 0.0 and 1.0:  "))
        mixer.music.set_volume(c)
        print("*"*50)
    if(a==6):
        a=int(input("Skip Music To How Many Seconds From The Beginning: "))
        mixer.music.rewind()
        mixer.music.set_pos(a)
        print("*"*50)

