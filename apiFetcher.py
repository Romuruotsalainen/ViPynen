import pandas as pd
import urllib.request
import requests
import json

class apiFetcher:
    def __init__(self, lang, query):
        self.lang = lang
        self.query = query
        
        dictionary = pd.read_csv("dictionary.csv")
        if self.lang == "sv":
            self.query = dictionary[(dictionary["swedish"] == self.query)]["finnish"].iloc[0]
        elif self.lang == "en":
            self.query = dictionary[(dictionary["english"] == self.query)]["finnish"].iloc[0]
            
    """
    Everything fetched through Vipunens API need to use the Finnish query words. If lang is anything
    but "fi" the query must be translated. The translations is stored in a separate csv-file called dictionary.csv.
    """
                
    def area_to_work_with(self):
        #This function does not download files and save them locally, but work with them in the computer's memory
        api = "http://api.vipunen.fi/api/resources/" + self.query + "/data"
        json_data = requests.get(api).json() 
        return json_data

    def initiate_download(self):
        if area_to_download in areas:
            for namn in areas:
              api = "http://api.vipunen.fi/api/resources/" + self.query + "/data"
              json_data = requests.get(api).json()
              with open(namn + ".json", "w") as filen:
                json.dump(json_data ,filen)
            else:
                print("Error: Name not in Vipunen. \n Try again or enter X to see list of available names")
