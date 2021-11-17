import csv
from os.path import exists
import filelist.filelist as filelist
import time

temporal_torrent = "torrent"

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

async def run(message, temp):
    torrent = filelist.run() 

    if torrent != temp: 
        await message.channel.send("Found: " + torrent)
    
    temp = torrent

    time.sleep(10)

    await run(message, temp)