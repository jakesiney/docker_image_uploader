from flask import Flask, render_template, request, redirect
import os


app = Flask(__name__)

UPLOADS = "static/images"


app.config['UPLOADS'] = UPLOADS


@app.route('/')
def index():
    files = os.listdir(UPLOADS)
    images = [file for file in files]
    return render_template('index.html', images=images)


@app.route('/upload', methods=['POST'])
# create a function to upload files
def upload():
    if request.method == 'POST':
        if request.files:
            image = request.files['file']
            image.save(os.path.join(app.config['UPLOADS'], image.filename))
            return redirect('/')
    return render_template('index.html')


if __name__ == '__main__':
    if not os.path.exists(UPLOADS):
        os.makedirs(UPLOADS)
    app.run(
        debug=True,
        host="0.0.0.0"  # Listen for connections directed _to_ any address
    )
