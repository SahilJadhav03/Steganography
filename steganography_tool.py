import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to encrypt the message into the image
def encrypt_image():
    img_path = filedialog.askopenfilename(title="Select an image for encryption")
    img = cv2.imread(img_path)

    if img is None:
        messagebox.showerror("Error", "Failed to load the image")
        return

    msg = entry_msg.get()
    password = entry_password.get()

    if not msg or not password:
        messagebox.showerror("Error", "Message or Password is missing")
        return

    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0

    # Embed the message in the image
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        if n >= img.shape[0]:
            n = 0
            m += 1
        z = (z + 1) % 3

    encrypted_img_path = "encrypted_image.png"
    cv2.imwrite(encrypted_img_path, img)
    messagebox.showinfo("Success", "Message encrypted and image saved as " + encrypted_img_path)


# Function to decrypt the message from the image
def decrypt_image():
    encrypted_img_path = filedialog.askopenfilename(title="Select an encrypted image")
    img = cv2.imread(encrypted_img_path)

    if img is None:
        messagebox.showerror("Error", "Failed to load the image")
        return

    pas = entry_password.get()

    if password != pas:
        messagebox.showerror("Error", "Incorrect password")
        return

    # Decrypt the message
    message = ""
    n, m, z = 0, 0, 0
    c = {i: chr(i) for i in range(255)}

    while True:
        char = c[img[n, m, z]]
        if char == '\0':  # Stop if we encounter null character
            break
        message += char
        n += 1
        if n >= img.shape[0]:
            n = 0
            m += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decrypted Message", message)


# GUI setup
root = Tk()
root.title("Image Steganography Tool")

label_msg = Label(root, text="Enter Message to Encrypt:")
label_msg.pack()

entry_msg = Entry(root)
entry_msg.pack()

label_password = Label(root, text="Enter Password:")
label_password.pack()

entry_password = Entry(root, show="*")
entry_password.pack()

button_encrypt = Button(root, text="Encrypt Image", command=encrypt_image)
button_encrypt.pack()

button_decrypt = Button(root, text="Decrypt Image", command=decrypt_image)
button_decrypt.pack()

root.mainloop()
