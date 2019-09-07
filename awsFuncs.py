import boto3
""" framePath: path to frame image
    return: list of 3-tuples of the form (celebrity Name, Confidence, URL) 
    obtain list of all the celebrities in the frame with the confidence level"""
def getCelebsFromFrame(frame):
    client=boto3.client('rekognition')
    with open(frame, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})
    celebs=[]
    for celebrity in response['CelebrityFaces']:
        if len(celebrity['Urls']) > 0:
            url = celebrity['Urls'][0]
        else:
            url = None
        celebs.append( (celebrity['Name'], celebrity['MatchConfidence'], url) )
    return celebs

# def getTextFromFrame(screenPath):
    # screen: path to jpg screencap
    # return: string of text in the image (or a list if necessary)
    # """analyze frame and retrieve all relevant text from it"""

