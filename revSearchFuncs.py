import requests

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
        print(response.request.url)
        jsonResp = response.json()
        print(jsonResp)

# def reverseSearchImage(screen):
    # screen: openCV frame object
    # return: list of strings of top 5 responses

# def parseResponseText(respText):
    # respText: list of strings of top 5 responses
    # return: list of strings of 5 guesses
