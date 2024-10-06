import cv2
import os

# Read the image
img = cv2.imread("yogesh.jpg")

# Get the secret message and password from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries to map characters to their ASCII values and vice versa
char_to_ascii = {}
ascii_to_char = {}

# Fill the dictionaries with values from 0 to 254
for i in range(255):
    char_to_ascii[chr(i)] = i
    ascii_to_char[i] = chr(i)

# Initialize variables to navigate through the image pixels
row = 0
col = 0
channel = 0

# Encode the secret message into the image by storing ASCII values in pixels
for i in range(len(msg)):
    img[row, col, channel] = char_to_ascii[msg[i]]  # Place ASCII value of character into the pixel
    row += 1
    col += 1
    channel = (channel + 1) % 3  # Cycle through R, G, B channels

# Save the modified image with the encoded message
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image to view it
os.startfile("encryptedImage.jpg")

# Decryption process
decrypted_msg = ""
row = 0
col = 0
channel = 0

# Prompt user to enter password for decryption
entered_password = input("Enter passcode for Decryption: ")

if password == entered_password:
    # Extract the message by converting pixel values back to characters
    for i in range(len(msg)):
        decrypted_msg += ascii_to_char[img[row, col, channel]]
        row += 1
        col += 1
        channel = (channel + 1) % 3  # Cycle through R, G, B channels

    print("Decrypted message: ", decrypted_msg)
else:
    print("Authentication failed. Incorrect passcode.")
