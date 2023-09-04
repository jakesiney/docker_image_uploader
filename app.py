from flask import Flask, render_template, request, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['UPLOAD_FOLDER'] = "static/images"


class Uploadfileform(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Uploadfileform()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                  app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

    return render_template("index.html", form=form)


@app.route('/files', methods=['GET'])
def files():
    directory = 'static/images'
    if not os.path.exists(directory):
        return jsonify({"error": "Directory not found"})
    files = os.listdir(directory)

    return jsonify({"files": files})


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0"  # Listen for connections directed _to_ any address
    )
