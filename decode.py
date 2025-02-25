# decode.py
"""  
import cv2

def decode_message(image_path, original_message_len):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Encrypted image not found."

    c = {i: chr(i) for i in range(256)}
    message = ""
    m, n, z = 0, 0, 0

    for _ in range(original_message_len):
        try:
            message += c[img[n, m, z]]
        except IndexError:
            return "Error: Image might be corrupted or password incorrect."
        n += 1
        m += 1
        z = (z + 1) % 3
    return message
    """ 

import cv2
import base64

def decode_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Encrypted image not found."

    c = {i: chr(i) for i in range(256)}
    message = ""
    m, n, z = 0, 0, 0

    while True:
        try:
            char = c[img[n, m, z]]
        except IndexError:
            return "Error: Image might be corrupted or password incorrect."
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3

        if "|||END|||" in message:
            break

    try:
        encoded_password, actual_message = message.split("|||", 1)
        actual_message = actual_message.replace("|||END|||", "") # Remove Delimiter
        decoded_password = base64.b64decode(encoded_password).decode('utf-8')
        if decoded_password == password:
            return actual_message
        else:
            return "Error: Incorrect password."
    except ValueError:
        return "Error: Could not decode message (invalid format)."