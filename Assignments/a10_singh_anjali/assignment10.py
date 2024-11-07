# Anjali Singh, anjalisi@usc.edu
#ITP 115, Spring 2022
#Section: 32096
# Assignment 10
# Description:
#A program that manages a user's music library
import MusicLibraryHelper
import random

#Parameter: None
#Return Value:None
#Description: Displays the menu to the user of the options they have
def displayMenu():
    print("Manage your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")
#Parameter:a dictionary representing the music library
#Return Value: none
#Description: Prints out the entire music library so the user can see the artists and their albums
def displayLibrary(dictionary):
    for key in dictionary:
        print("Artist:", key)
        print("\tAlbums:")
        for album in dictionary[key]:
            print("\t\t",album)
#Parameter: a dictionary representing the music library
#Return Value:none
#Description: displays all of the artists in the music library
def displayArtists(dictionary):
    print("Artists: ")
    for key in dictionary:
        print("\t",key)
#Parameter:a dictionary representing the music library
#Return Value: None
#Description: Gets input from the user for the name of the artist and the name of the album they waant to add to the music library
def addAlbum(dictionary):
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    #capitalize the users input
    artist = artist.title()
    album = album.title()
    #if the artist is in the dictionary but the album is not in library of that artist, add the album
    if artist in dictionary:
        if album not in dictionary[artist]:
            dictionary[artist].append(album)
    #if the artist is not in the dictionary, adds a new key(aritst) to the dictionary along iwth a new value(album)
    else:
        dictionary[artist] = []
        dictionary[artist].append(album)

#Parameter:a dictionary representing the music library
#Return Value: a boolean value that indicates if the album was successfully deleted or not
#Description: Gets input from the user for the name of the artist and the name of the album, and deletes the album from the music library
def deleteAlbum(dictionary):
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    #capitalizes the users input
    artist = artist.title()
    album = album.title()
    if artist in dictionary:
        #if the artist and album are in the dictionary, remove the album and change the boolean to true
        if album in dictionary[artist]:
            dictionary[artist].remove(album)
            outcome = True
    else:
        outcome = False
    return outcome

#Parameter:a dictionary representing the music library
#Return Value:a boolean value that indicates if the artist was successfully deleted or not
#Description: Gets input from the user for the name of the artist and deletes it from the music library(if it exists)
def deleteArtist(dictionary):
    artist = input("Enter arist to delete: ")
    artist = artist.title()
    #if the artist is in the dictionary, remove the artist and change the boolean value to true
    if artist in dictionary:
        del dictionary[artist]
        outcome = True
    else:
        outcome = False
    return outcome
#Parameter: a dictionary representing the music library
#Return Value:None
#Description: Generates a random playlist by randomly selecting artists and their songs from the music library
def generateRandomPlaylist(dictionary):
    print("Here is your random playlist:")
    #for every artist in the dictionary, choose a random song and print it out
    for artist in dictionary:
        randomAlbum = random.choice(dictionary[artist])
        print(randomAlbum,"by",artist)

def main():
    #creates a dictionary by loading the library from the music library helper
    dictionary = MusicLibraryHelper.loadLibrary("music_library.dat")
    #loop that keeps running until the user quits
    keepRunning = True
    while keepRunning:
        #displays menu and calls functions based on users input
        displayMenu()
        choice = input("Choice: ")
        if choice.lower() == "a":
            displayLibrary(dictionary)
        elif choice.lower() == "b":
            displayArtists(dictionary)
        elif choice.lower() == "c":
            addAlbum(dictionary)
        elif choice.lower() == "d":
            album = deleteAlbum(dictionary)
            #if album was deleted successfully, print out this statement
            if album == True:
                print("Delete album success")
            # if album was not deleted successfully, print out this statement
            else:
                print("Delete album failed")
        elif choice.lower() == "e":
            artist = deleteArtist(dictionary)
            # if artist was deleted successfully, print out this statement
            if artist == True:
                print("Delete artist success")
            # if artist was not deleted successfully, print out this statement
            else:
                print("Delete artist failed")
        elif choice.lower() == "f":
            generateRandomPlaylist(dictionary)
        elif choice.lower() == "g":
            keepRunning = False
        else:
            print("Invalid Entry")
    #Once the user quits, ask the user for a file name for the music library and save it using the helper function
    musicLibrary = input("Enter music library filename: ")
    MusicLibraryHelper.saveLibrary(musicLibrary,dictionary)
    print("Saved music library to",musicLibrary)

main()