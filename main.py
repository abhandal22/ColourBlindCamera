from distutils.log import debug
from fileinput import filename
from flask import Flask, render_template, request, session, abort
import os, uuid, datetime
from werkzeug.utils import secure_filename  
from main import convertColour, mergeImages
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use a service account.
cred = credentials.Certificate('colorblindcamera-6ff9a-firebase-adminsdk-kjk85-58631cc25a.json')
app_firebase = firebase_admin.initialize_app(cred, {"storageBucket": "colorblindcamera-6ff9a.appspot.com"})
db = firestore.client()
bucket = storage.bucket()

# blob = bucket.blob("images/lion1.png")
# blob.upload_from_filename("lion1.png")
blob = bucket.blob("images")

UPLOAD_FOLDER = os.path.join("staticFiles", "uploads")
ALLOWED_EXTENSIONS = {".png"}

app = Flask(__name__, template_folder="templates", static_folder="staticFiles")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = os.urandom(12)

@app.route('/')
def main():  
    imageElements = displayImages()
    return render_template("home.html", imageDisplay=imageElements)

@app.route('/invalid')
def invalid():  
    imageElements = displayImages()
    return render_template("homeInvalid.html", imageDisplay=imageElements)

def displayImages():
    imageElements = ""
    users_ref = db.collection(u'Images')
    docs = users_ref.stream()
    for doc in docs:
        imageTag = f"<img src='{doc.to_dict()['Image URL']}'>\n"
        imageElements += imageTag
    return imageElements


def saveImage(img :Image):
    filename = uuid.uuid4().hex
    img.save(os.path.join(UPLOAD_FOLDER, filename) + ".png")
    blob = bucket.blob("images/" + filename + ".png")
    blob.upload_from_filename(os.path.join(UPLOAD_FOLDER, filename) + ".png")
    os.remove(os.path.join(UPLOAD_FOLDER, filename) + ".png")
    filename = filename + ".png"
    blob.make_public()
    publicURL = blob.public_url
    obj = { "Image Name" : filename, "Image URL" : publicURL }
    doc_ref = db.collection(u'Images').document(obj["Image Name"])
    doc_ref.set(obj)
    session["uploaded_img_url"] = blob.generate_signed_url(datetime.timedelta(seconds=300), method="GET")
  
@app.route('/upload', methods = ['POST', 'GET'])  
def success():  
    if request.method == 'POST':  
        uploaded_img = request.files["image"]
        severity = int(request.form["severity"])
        type = request.form["type"]
        print(type)
        img_filename = secure_filename(uploaded_img.filename)
        if img_filename != "":
            file_type = os.path.splitext(img_filename)[1]
            if file_type not in ALLOWED_EXTENSIONS:
                abort(400)
            uploaded_img = Image.open(uploaded_img)
            uploaded_img.thumbnail([704, 576])
            converted_img = convertColour(uploaded_img, severity, type)
            merged_img = mergeImages(uploaded_img, converted_img)
            saveImage(merged_img)
            return app.redirect("/upload")
        else:
            return app.redirect("/invalid")
    else:
        imageElements = displayImages()
        image = session["uploaded_img_url"]
        return render_template("home2.html", imageDisplay=imageElements, user_image=image)

@app.route('/display')
def display():
    img_url = session.get("uploaded_img_url", None)
    return render_template("home.html", user_image = img_url)

if __name__ == '__main__':  
    app.run(debug=True)