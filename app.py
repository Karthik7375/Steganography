from flask import Flask, render_template, request, redirect, url_for
import os
from encode import encode_message
from decode import decode_message

app = Flask(__name__)
UPLOAD_FOLDER = 'encrypted_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")

@app.route("/encode", methods=["GET", "POST"])
def encode():
    encrypted_image_path = None
    if request.method == "POST":
        image = request.files["image"]
        message = request.form["message"]
        password = request.form["password"]
        filename = request.form["filename"]
        
        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            result = encode_message(image_path, message, password,filename)
            if isinstance(result, str) and result.startswith("Error"):
                return render_template("encode.html", error=result)
            else:
                encrypted_image_path = result

    return render_template("encode.html", encrypted_image=encrypted_image_path)


@app.route("/decode", methods=["GET", "POST"])
def decode():
    decrypted_message = None
    if request.method == "POST":
        image = request.files["image"]
        password = request.form["password"]

        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            decrypted_message = decode_message(image_path, password)
            if isinstance(decrypted_message, str) and decrypted_message.startswith("Error"):
                return render_template("decode.html", error=decrypted_message)

    return render_template("decode.html", decrypted_message=decrypted_message)

if __name__ == "__main__":
    app.run(debug=True)