import csv
from os.path import exists
import filelist.filelist as filelist
import time

# check if the csv files exists otherwise create it
def is_wishlist():
    if not exists("wishlist.csv"):
        with open("wishlist.csv", "w") as file:
            torrent_writer = csv.writer(file)

# function adds a non empty string to a list of strings in a csv
def wishlist(torrent):
    is_wishlist()
    torrent_wishlist = []
    index = 0

    # if the input is empty ignore it
    if torrent == "": return

    #  open the csv file
    with open("wishlist.csv") as file:
        torrent_reader = csv.reader(file)

        # write every string in the csv into our list
        torrent_wishlist = list(torrent_reader)

    # ignore torrent if already in wishlist
    while index < len(torrent_wishlist):
        # remove all non torrent data from csv
        # could not find a good way to write clean data to csv
        torrent_string = str(torrent_wishlist[index]).replace(",", "").replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
        if torrent == torrent_string: return
        index += 1

    # insert our torrent at the end of the list
    torrent_wishlist.append(torrent)

    # update the csv file with our list
    with open("wishlist.csv", "w") as file:
        torrent_writer = csv.writer(file)
        torrent_writer.writerows(torrent_wishlist)

# function removes a non empty string from a list of string in a csv
def remove(torrent):
    is_wishlist()
    torrent_wishlist = []
    update_torrent_wishlist = []
    index = 0

    # if the input is empty ignore it
    if torrent == "": return

    #  open the csv file
    with open("wishlist.csv") as file:
        torrent_reader = csv.reader(file)

        # write every string in the csv into our list
        torrent_wishlist = list(torrent_reader)

    # remove torrent from wishlist by ignoring it in the reading
    while index < len(torrent_wishlist):
        # remove all non torrent data from csv
        # could not find a good way to write clean data to csv
        torrent_string = str(torrent_wishlist[index]).replace(",", "").replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
        if torrent != torrent_string: update_torrent_wishlist.append(torrent_wishlist[index])
        index += 1

    # update the csv file with our list
    with open("wishlist.csv", "w") as file:
        torrent_writer = csv.writer(file)
        torrent_writer.writerows(update_torrent_wishlist)

# function shows to user all the items in the wishlist
def show():
    is_wishlist()
    torrent_wishlist = []

    #  open the csv file
    with open("wishlist.csv") as file:
        torrent_reader = csv.reader(file)

        # write every string in the csv into our list
        torrent_wishlist = list(torrent_reader)
    
    # return our csv list cleanly
    torrent_string = str(torrent_wishlist).replace(",", "").replace(" ", "").replace("[", "").replace("]", "\n").replace("'", "")
    return torrent_string

def is_last_torrent_file():
    # allways start by creating a file that retains our last torrent value
    # this way it allows us to see the repeated torrent when we start the program but not whilst it is runing 
    if not exists("last_torrent.txt"):
        with open("last_torrent.txt", "w") as file:
            file.write("empty")

async def run(message):
    torrent = filelist.run() 
    i = 0

    # check if the last torrent retainer exists
    is_last_torrent_file()

    # retain the last torrent we found
    with open("last_torrent.txt") as file:
        temp = file.read()

    #  open the csv file
    with open("wishlist.csv") as file:
        torrent_reader = csv.reader(file)
        # get the length of our wishlist
        list_len = len(list(torrent_reader))
    
    # store the wishlist
    wishlist = show().split("\n")

    # if the torrent is not in the wishlist simply display the torrent name, no tag
    if torrent != temp: 
        # check if the torrent is in our wishlist
        # if so tag everyone and return
        while i < list_len:
            if wishlist[i] in torrent.lower():
                await message.channel.send("Found: " + torrent + "@everyone")
                # store the previous torrent so we do not display the same  torrent a second time
                temp = torrent

                with open("last_torrent.txt", "w") as file:
                    file.write(temp)
                return
            i += 1

        await message.channel.send("Found: " + torrent)
    
    # check to see if vars are the same
    print(temp, "\n")

    # store the previous torrent so we do not display the same  torrent a second time
    temp = torrent

    with open("last_torrent.txt", "w") as file:
        file.write(temp)