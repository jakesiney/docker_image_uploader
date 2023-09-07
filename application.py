from flask import Flask, render_template, request, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os


application = Flask(__name__)

UPLOAD_FOLDER = "static/images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    images = [file for file in files if allowed_file(file)]
    return render_template('index.html', images=images)


@application.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = os.path.join(
            application.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect('/')
    return redirect('/')


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    application.run(
        # debug=True,
        # host="0.0.0.0"  # Listen for connections directed _to_ any address
    )
