import urllib.request
import requests
import json
from apiFetcher import apiFetcher as af

def language_check(command):
    list_of_available_languages = ("sv", "fi", "en")
    while True:
        if command in list_of_available_languages:
            return command
        else:
            print("Ogiltigt språk. Försök igen.")
            print("Viallinen kieli. Yritä uudestaan.")
            print("Invalid language. Please try again.")

while True:
    command = input("Språk/Kieli/Language (sv, fi, en): ")
    language = language_check(command)
    if language == "sv":
        command = input("Skriv in \"kommandon\" \n för att se möjliga alternativ. Skriv sluta för att avsluta: ")
        if command == "avsluta":
            break
       
    if language == "en":
        command = input("Skriv in kommando eller skriv kommandon \n för att se möjliga alternativ. Skriv sluta för att avlutsa")
        if command == "exit":
            break
    else:
        #Defaults to Finnish
        command = input("Skriv in kommando eller skriv kommandon \n för att se möjliga alternativ. Skriv sluta för att avlutsa")
        if command == "lopeta":
            break
    file_to_work_with = af(language, command)
    ftww = file_to_work_with.area_to_work_with()
        
    

    

