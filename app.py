import os
from flask import Flask, flash, request, redirect, url_for
import urllib
from werkzeug.utils import secure_filename

import videoProcessing

UPLOAD_FOLDER = 'movies'
ALLOWED_EXTENSIONS = {'mp4', "MP4"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
            return redirect(url_for('process_file',
                                    dirname = dirname, filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# A route to handle processing mp4
@app.route('/upload', methods=['GET'])
def process_file():
    dirname = request.args.get('dirname')
    filename = request.args.get('filename')
    videoPath = '/'.join([dirname, filename])

    # celebs = getCelebsFromVideo(videoPath)
    # guess1 = getGuessesFromCelebs(celebs)

    # audioText = videoProcessing.getAudioText(videoProcessing.getAudio(videoPath))
    # audioTextChunks = getAudioChunks(audioText)
    # respText = reverseSearchText(audioTextChunks)
    # guess2 = parseResponseText(respText)

    # guess3 = []
    # framePaths = videoProcessing.getFrames(dirname, videoPath)

    # print("back in app.py with framePaths: ", framePaths)
    # iterate through screencaps:
    #   respText2 = reverseSearchImage(screenPath)
    #   guess3.extend(parseResponseText(respText2))
    #   screenText = getTextFromFrame(screenPath)
    #   respText3 = reverseSearchText(screenText)
    #   guess3.extend(parseResponseText(respText3))

    # finalGuesses = merge(guess1, guess2, guess3)

    return "Hello World " + videoPath

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
