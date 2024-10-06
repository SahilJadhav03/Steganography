import cv2
import os

# Load the image
img = cv2.imread("yogesh.jpg")

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for character encoding and decoding
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Variables for pixel coordinates
n = 0
m = 0
z = 0

# Encrypt the message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Embed the message character in the image
    n += 1
    m += 1
    z = (z + 1) % 3  # Loop over the 3 color channels (R, G, B)

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image
os.startfile("encryptedImage.jpg")

# Decryption process
message = ""
n = 0
m = 0
z = 0

# Input passcode for decryption
pas = input("Enter passcode for Decryption: ")

# Check if the passcode is correct
if password == pas:
    # Decrypt the message
    for i in range(len(msg)):
        message += c[img[n, m, z]]  # Retrieve the message character from the image
        n += 1
        m += 1
        z = (z + 1) % 3  # Loop over the 3 color channels (R, G, B)

    # Print the decrypted message
    print("Decrypted message:", message)
else:
    # Authentication failure
    print("You are not Authenticated")
