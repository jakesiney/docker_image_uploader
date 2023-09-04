from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filenamex
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


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0"  # Listen for connections directed _to_ any address
    )
