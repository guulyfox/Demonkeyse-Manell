#!/usr/bin/python3
import random
import time

songs=['brave song','Hello,world!','butter-fly','crow song','brave shine','wild fire','the world is mine']
singers=['cali','tangqingyu','xlb','caoy','hubiwu']

def menu():
    print("===================The Lucky Days===================")
    print("1, show all singers or query all singers messages")
    print("2, add a singer or drop a singer")
    print("3, show all songs or query all songs messages")
    print("4, add a song or drop a song")
    print("5, select a singer to sing a song")
    print("6, exit")
    print("=======================Menu=========================")
    print("\n")
    option=input("please select :")
    print("\n")
    if option.isdigit():
        return(int(option))
    else:
        print("you must choose a defined choice!")

def show_singer():
    print(*singers, sep='\n')
    add_singer=input("Do you want to added a singer, who?:")

    if len(add_singer) == 0:
        pass

    else:

        if add_singer in singers:
            print("sorry, I konw your loverest singers, but they already in the list.")

        else:
            singers.append(add_singer)
            print("the new singer %s now is added in singer's group"%(add_singer))

    drop_singer=input("Do you want to drop a singer, who?:")

    if drop_singer in singers:
        singers.remove(drop_singer)
        print("a singer who is %s was drop by your order!"%(drop_singer))

    else:
        pass
    
    sequ = input("Do you want to use sequence to drop a singer? which:")
    
    if sequ.isdigit():
        if len(sequ)>0 and int(sequ) < len(singers):
            sequ = int (sequ)
            sequ = sequ - 1
            print("the %s singer was droped!"%(singers.pop(sequ)))

        else:
            print("not such choice!")

    else:
        print("please input a number!")    

def show_song():

    print(*songs, sep='\n')

    add_song=input("Do you want to add a song, which?:")

    if len(add_song) == 0:
        pass

    else:

        if add_song in songs:
            print("sorry, I konw you so love for this song, but we already added it in the list!")

        else:
            songs.append(add_song)
            print("the new song %s now is added in song's group"%(add_song))

    drop_song=input("DO you want to drop a song, which?:")

    if drop_song in songs:
        songs.remove(drop_song)
        print("a song %s in your orders was droped!"%(drop_song))

    else:
        pass

    sequ = input("Do you want to delete s song by sequence? which:")    

    if sequ.isdigit():
        if len(sequ) > 0 and int(sequ) < len(songs):
            sequ = int(sequ)
            sequ = sequ - 1
            print("the %s song was droped!"%(songs.pop(sequ)))

        else:
            print("Not such chioce!")

    else:
        print("please input a number!")

def Select():

    c_singers = len(singers)
    c_singers = c_singers - 1
    ran_singer = random.randint(0, c_singers)
    c_songs = len(songs)
    c_songs = c_songs - 1
    ran_song = random.randint(0, c_songs)
    print("\n")
    print("please let <%s> sing a song named <%s> for us!"%(singers[ran_singer], songs[ran_song]))
    print("\n")
    
def main():

    die = []
    print("\n")
    flag = 3
    record = menu()

    while flag:

        if record == 6: 
            flag = 0

        elif record == 5:
            Select()
            flag = 0
            main()

        elif record == 4:
            show_song()
            flag = 0
            main()

        elif record == 3:
            print("=================================================")
            print("there're have %d songs in the list"%(len(songs)))
            print(*songs, sep='\n')
            print("================================================")
            print("\n")
            s_song = input("search a song? who:")
            if s_song in songs:
                print("%s song is in the list."%(s_song))
            else:
                print("Nothing left but our chickens!") 
            flag = 0
            main()

        elif record == 2:
            show_singer()
            flag = 0
            main()

        elif record == 1:
            print("================================================")
            print("there're have %d singers in the list"%(len(singers)))
            print(*singers, sep='\n')
            print("================================================")
            print("\n")
            s_singer = input("search a singer? who:")
            if s_singer in singers:
                print("%s singer is in the list."%(s_singer))
            else:
                print("Nothing left but our chickens!")
            flag = 0
            main()

        else:
            print("RBQ, RBQ, RBQ!")
            time.sleep(1)
            flag = flag - 1
            
    else:
        die.append('Bye')

    print(*die)

main()
