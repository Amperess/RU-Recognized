import requests
import json

textEngineURL = "https://www.googleapis.com/customsearch/v1";
searchKey = "AIzaSyBVwcr0dHzMlgMk_EC5pbYMrq1WwSpDIZw"
textSearchCX = "004446501613873659339:okwte2qeapo"

"""
 audioTextChunks: list of strings, each is distinct dialogue piece
 return: list of strings of top 5 responses
"""
def reverseSearchText(audioTextChunks):
    for text in audioTextChunks:
        response = requests.get(textEngineURL, params={"key":searchKey, "cx":textSearchCX, "q":text})
        entries = response.json()['items']
        entries = [[entry['title'], entry['snippet']] for entry in entries]
        entries = entries[:10]
        for entry in entries:
            entry[0] = entry[0].replace('\n', '')
            entry[1] = entry[1].replace('\n', '')

# def reverseSearchImage(screen):
    # screen: openCV frame object
    # return: list of strings of top 5 responses

# def parseResponseText(respText):
    # respText: list of strings of top 5 responses
    # return: list of strings of 5 guesses
