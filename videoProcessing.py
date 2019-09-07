import cv2
# def getAudioText(videoPath):
    # videoPath: path to video
    # return: string of audio in video

# def getAudioChunks(audioText):
    # audioText: string of audio in video
    # return: list of strings of distinct lines

"""
 dirname: subdirectory name where to save frames
 videoPath: full video file path
 return: names of frame paths
"""
def getFrames(dirname, videoPath):
    vidObj = cv2.VideoCapture(videoPath)
    framePaths = []

    currentFrameNo = 0
    success = True
    frameRate = vidObj.get(cv2.CAP_PROP_FPS)
    totalFrames = vidObj.get(cv2.CAP_PROP_FRAME_COUNT)
    frameCount = 0

    while success and currentFrameNo < totalFrames:
        # read from currentFrameNo
        vidObj.set(cv2.CAP_PROP_POS_FRAMES, currentFrameNo)

        success, image = vidObj.read()

        framePath = "/".join([dirname, "frame{0}.jpg".format(frameCount)])

        print("Saving to ", framePath)
        print("\n\n\n\n\n\n\n\n")
        cv2.imwrite(framePath, image)
        framePaths.append(framePath)
        frameCount += 1
        currentFrameNo += frameRate

    print("Returning from getFrames", len(framePaths))
    return framePaths
