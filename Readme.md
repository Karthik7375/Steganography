# Image Steganography Tool

This project implements an image steganography tool using Python, Flask, and OpenCV, allowing you to hide secret messages within images.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [How it Works](#how-it-works)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Future Scope](#future-scope)

## Introduction

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. This project provides a user-friendly web application to hide text messages within images, leveraging the Least Significant Bit (LSB) technique.

## Features

* Encode text messages into images.
* Decode messages from images.
* Password protection for encoded messages.
* User-friendly web interface.
* Drag-and-drop file upload.
* File name and type selection.

## Technologies Used

* **Python:** Core language for the application logic.
* **Flask:** Web framework for building the web application.
* **OpenCV:** Image processing library for handling images.
* **HTML/CSS/JS:** Front-end technologies for user interface and interactivity.
* **Base64:** Encoding and decoding passwords.

## How it Works

The project uses the LSB steganography technique. It embeds the message and an encoded password into the least significant bits of the image pixels. A delimiter marks the end of the message, and the password is used to authenticate the decoding process.

## Installation

1.  Clone the repository: `git clone https://github.com/Karthik7375/Steganography.git`
2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate (For Windows) or source venv/bin/activate (For Linux/MacOs)
    ```
3.  Install dependencies: `pip install -r requirements.txt`

## Usage

1.  Run the Flask application: `python app.py`
2.  Access the web interface in your browser: `http://127.0.0.1:5000/`

### Encoding

1.  **Upload an Image:**
    * Click or drag and drop a JPG, JPEG, or PNG image into the upload area.
2.  **Enter a Message:**
    * Type the message you want to hide in the text area labeled "Message."
3.  **Enter a Password:**
    * Enter a password in the "Password" field. This password will be required to decode the message.
4.  **Enter Filename:**
    * Enter the filename  you want to save the encoded image as. (It is saved as a png file)
5.  **Click "Encode":**
    * Click the "Encode" button to embed the message into the image.
6.  **Download the Encoded Image:**
    * The encoded image will be displayed, and you can download it.

### Decoding

1.  **Upload Encoded Image:**
    * Click or drag and drop the encoded PNG image into the upload area.
2.  **Enter Password:**
    * Enter the same password that was used during encoding.
3.  **Click "Decode":**
    * Click the "Decode" button to extract the message.
4.  **View Decoded Message:**
    * The decoded message will be displayed on the screen.

## Project Structure

```
image-steganography/
├── app.py          # Flask application
├── encode.py       # Encoding logic
├── decode.py       # Decoding logic
├── templates/      # HTML templates
│   ├── index.html
│   ├── encode.html
│   └── decode.html
├── static/         # Static files (CSS, JavaScript)
│   └── style.css
├── encrypted_images/        # Directory for uploaded images
└── requirements.txt # List of Python dependencies
```

## Future Scope

* Implement more robust steganography algorithms.
* Support different file formats (audio, video).
* Integrate proper password hashing and encryption.
* Develop a more advanced graphical user interface.
* Add steganalysis resistance techniques.