]from flask import Flask, request
import urllib

app = Flask(__name__)


# Home page route
@app.route('/')
def home():
    # put home things here
    return str(response)


# A route to handle uploading/processing mp4
@app.route('/upload', methods=['POST'])
def upload_mp4():

    # video = request.form['Body']

    # celebs = getCelebsFromVideo(video)
    # guess1 = getGuessesFromCelebs(celebs)

    # audioText = getAudioText(video)
    # audioTextChunks = getAudioChunks(audioText)
    # respText = reverseSearchText(audioTextChunks)
    # guess2 = parseResponseText(respText)

    # guess3 = []
    # screens = getFrames(video, rate)
    # for screen in screens:
    #   respText2 = reverseSearchImage(screen)
    #   guess3.extend(parseResponseText(respText2))
    #   screenText = getTextFromFrame(screen)
    #   respText3 = reverseSearchText(screenText)
    #   guess3.extend(parseResponseText(respText3))

    # finalGuesses = merge(guess1, guess2, guess3)

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
