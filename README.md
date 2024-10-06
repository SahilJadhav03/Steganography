# Secret Message Encryption Tool

This project is a Python-based tool that encrypts and hides a secret message inside an image using pixel manipulation techniques. It also provides a secure way to decrypt the message with a passcode, ensuring only authorized users can retrieve the hidden information.

# Features:

Message Encryption: Hide a secret message inside an image by encoding the message into the pixel values of the image.
Password Protection: Set a passcode during encryption to ensure only users with the correct password can decrypt the message.
Message Decryption: Retrieve the hidden message from the encrypted image by using the correct passcode.
Easy to Use: Minimal user input required; simply provide a message and passcode, and the tool handles the rest.

# How It Works:
The tool reads an image file.
It encodes each character of the secret message into the image's pixel values by replacing specific color channel data with the ASCII values of the characters.
The modified image is saved and can be viewed like any other image, with the message hidden within the pixels.
To decrypt the message, the user must input the correct passcode, and the hidden message is retrieved from the pixel data.

# Usage:
Install the necessary libraries: opencv-python
Run the script and provide an image file along with your secret message and passcode.
Use the same script for decryption by inputting the correct passcode.
