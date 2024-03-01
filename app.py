# import libraries
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from detect_text import *
import os

# Define the app
app = Flask(__name__)

# Define the directory
upload_folder = "static/images"
app.config['UPLOAD'] = upload_folder

# Main route
@app.route("/")
def index():
    return render_template("index.html")

#Capture image
@app.route("/capture", methods = ["POST"])
def capture_image():
    capture()
    return render_template("index.html")

# Upload and display the image from the upload directory
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template("index.html")

# Detect the text of the image
@app.route("/text", methods=["POST"])
def text_detection():
    show_image(convert_result(image_input(), resize_image(), box_detect(), conf_labels=False))
    return render_template("index.html")

# Run the app 
if __name__ == "__main__":
    app.run(host="0.0.0.0")