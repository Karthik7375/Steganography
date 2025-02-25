# encode.py

"""
import cv2

def encode_message(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Image not found."

    d = {chr(i): i for i in range(256)}
    m, n, z = 0, 0, 0
    for char in message:
        try:
            img[n, m, z] = d[char]
        except IndexError:
            return "Error: Message too long for image."
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_image_path = "encrypted_images/encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    return encrypted_image_path
    """ 
    
import cv2
import base64
import os

def encode_message(image_path, message, password,filename="encryptedImage"):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Image not found."

    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    full_message = encoded_password + "|||" + message + "|||END|||" # Add delimiter

    d = {chr(i): i for i in range(256)}
    m, n, z = 0, 0, 0
    for char in full_message:
        try:
            img[n, m, z] = d[char]
        except IndexError:
            return "Error: Message or password too long for image."
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_image_path = "encrypted_images/" + filename + '.png'
    cv2.imwrite(encrypted_image_path, img)
    return encrypted_image_path