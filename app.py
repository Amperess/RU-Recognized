import os
from flask import Flask, flash, request, redirect, url_for
import urllib
from werkzeug.utils import secure_filename
from collections import Counter

import videoProcessing
import revSearchFuncs
import imdbFuncs
import awsFuncs

UPLOAD_FOLDER = 'movies'
ALLOWED_EXTENSIONS = {'mp4', "MP4"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    dirname = ""
    filename = ""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dirname = os.path.join(app.config['UPLOAD_FOLDER'], filename[:-4])
            os.mkdir(dirname)
            file.save(os.path.join(dirname,  filename))
            file.save(os.path.join("static", filename))
            return redirect(url_for('display_video',
                                    dirname = dirname, filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload New File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/display', methods=['GET', 'POST'])
def display_video():
    dirname = request.args.get('dirname')
    filename = request.args.get('filename')

    if request.method == 'POST':
        return redirect(url_for('process_file', dirname = dirname, filename=filename))

    return '''
        <!doctype html>
        <h1>Continue</h1>
        <form method=post enctype=multipart/form-data>
          <input type=submit value=Search>
        </form>
        <iframe style="min-height:auto; width:auto;" src="{}"></iframe>
    '''.format("static/"+filename)


# A route to handle processing mp4
@app.route('/upload', methods=['GET'])
def process_file():
    dirname = request.args.get('dirname')
    filename = request.args.get('filename')
    videoPath = '/'.join([dirname, filename])

    audioPath = videoProcessing.getAudio(videoPath)
    audioText = videoProcessing.getAudioText(audioPath)
    respText = revSearchFuncs.reverseSearchText(audioText)

    # screenText = getTextFromFrame(screenPath)
    # respText2 = reverseSearchText(screenText)

    framePaths = videoProcessing.getFrames(dirname, videoPath)

    celebs = []
    for framePath in framePaths:
        celebs.extend(awsFuncs.getCelebsFromFrame(framePath))

    celebHash = {}
    for celeb in celebs:
        if celeb[0] in celebHash:
            celebHash[celeb[0]] += 1
        else:
            celebHash[celeb[0]] = 1

    print(celebHash)
    celebList = [(key, val) for key, val in celebHash.items()]
    celebList = sorted(celebList, key = lambda x: x[1], reverse = True)
    print(celebList)
    guess2 = imdbFuncs.getGuessesFromCelebs(celebList)

    movieCounter = Counter()
    for guess in guess2:
        movieCounter[guess[0]] += guess[1]

    for movie in movieCounter.keys():
        movieCounter[movie] += respText.count(movie)

    bruteCount = Counter()
    if len(movieCounter.keys()) == 0:
        bruteCount = imdbFuncs.bruteForce(respText)

    if len(bruteCount) > 0:
        movieCounter = bruteCount

    print(movieCounter.most_common())

    if len(movieCounter.most_common(1)) < 1:
        return '''
        <!doctype html>
        <title>The answer is!</title>
        <h1>We got nothing. Big sad!</h1>
        '''
    else:
        finalGuess = movieCounter.most_common(1)[0][0]
        return '''
        <!doctype html>
        <title>The answer is!</title>
        <h1>This is most likely <span style="color:magenta;">{}</span></h1>
        '''.format(finalGuess)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
