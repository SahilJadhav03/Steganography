import cv2
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def decrypt_image():
    img_path = filedialog.askopenfilename(title="Select an encrypted image")
    img = cv2.imread(img_path)

    if img is None:
        messagebox.showerror("Error", "Failed to load the image")
        return

    pas = entry_password.get()

    if not pas:
        messagebox.showerror("Error", "Password is missing")
        return

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
root.title("Image Decryption Tool")

label_password = Label(root, text="Enter Password:")
label_password.pack()

entry_password = Entry(root, show="*")
entry_password.pack()

button_decrypt = Button(root, text="Decrypt Image", command=decrypt_image)
button_decrypt.pack()

root.mainloop()
