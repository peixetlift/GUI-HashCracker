import tkinter
from tkinter import *
from tkinter import filedialog
import time
import decrypt
import encrypt

# select wordlist from files

def load_file():
    filename = filedialog.askopenfilename(
        initialdir="./wordlists", title="Select a file", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    file_label.configure(text=filename)


# decrypt hash

def decrypt_func(hashstr,filename):

    with open(filename, errors='ignore') as f:
        content = f.read().splitlines()

    start = time.time()
    result = decrypt.decrypt(algorithm_textbox.get().lower(),content,hashstr)
    output_label.configure(text="Hash cracked : " +
                           str(result), bg="#000066", fg="#ff0000")
    end = time.time()
    time_label.configure(text="Time elapsed : " +
                         str(end-start), bg="#000066", fg="#ffffff")


# encrypt string

def encrypt_func():
    output_label.configure(text="Hash : " + str(encrypt.encrypt(algorithm_textbox.get(), hash_textbox.get())), bg="#000066", fg="#ff0000")


#change decrypt <--> encrypt

def change_mode():
    if(title_label.cget("text") == "Decrypt hashes"):
        title_label.configure(text="Encrypt words")
        text_label1.configure(text="Word ------>")
        decrypt_button.grid_remove()
        encrypt_button.grid(row=6, column=3)
        load_wordlist_button.grid_remove()
        file_label.grid_remove()
    else:
        title_label.configure(text="Decrypt hashes")
        text_label1.configure(text="Hash ------>")
        encrypt_button.grid_remove()
        decrypt_button.grid(row=6, column=3)
        file_label.grid(row=7, column=2)
        load_wordlist_button.grid(row=6, column=2)


# window

window=tkinter.Tk()
window.geometry("1050x550")
window.title("HASH CRACKER")


# grid configuration

for i in range(0, 5):
    window.grid_columnconfigure(i, weight=1)

for i in range(0, 15):
    window.grid_rowconfigure(i, weight=1)


# images

decrypt_img=PhotoImage(
    file="./images/decrypt-logo-small.png")
select_wlist_img=PhotoImage(
    file="./images/selectwlist-small.png")
bg_img=PhotoImage(
    file="./images/wallpaper-encr.png", master=window)
encrypt_img=PhotoImage(
    file="./images/encrypt-logo-small.png", master=window)


# labels

img_label=tkinter.Label(window, image=bg_img)
img_label.place(x=0, y=0, relwidth=1, relheight=1)
title_label=tkinter.Label(window, text="Decrypt hashes",
                            bg="#000066", fg="#ffffff")
title_label.grid(row=1, column=2)
text_label1=tkinter.Label(window, text="Hash ------> ",
                            bg="#000066", fg="#ffffff")
text_label1.grid(row=4, column=1)
text_label2=tkinter.Label(
    window, text="Hashing algorithm ------> ", bg="#000066", fg="#ffffff")
text_label2.grid(row=3, column=1)
text_label3=tkinter.Label(
    window, text="Supported algorithms :\nmd5, sha1, sha256, nltm", bg="#000066", fg="#ffffff")
text_label3.grid(row=3, column=3)
file_label=tkinter.Label(
    text="No wordlist selected", bg="#000066", fg="#ffffff")
file_label.grid(row=7, column=2)
hash_label=tkinter.Label(text="", bg="#000066", fg="#ffffff")
output_label=tkinter.Label(text="", bg="#008DD4")
output_label.grid(row=8, column=2)
time_label=tkinter.Label(text="", bg="#007EBD")
time_label.grid(row=10, column=2)


# buttons

load_wordlist_button=tkinter.Button(
    window, image=select_wlist_img, padx=5, pady=5, borderwidth=0, command=lambda: load_file(), bg="#000066", fg="#ffffff")
load_wordlist_button.grid(row=6, column=2)
decrypt_button=tkinter.Button(
    window, image=decrypt_img, padx=5, pady=5, borderwidth=0, command=lambda: decrypt_func(hash_textbox.get(), file_label.cget("text")), bg="#000066", fg="#ffffff")
decrypt_button.grid(row=6, column=3)
encrypt_button=tkinter.Button(
    window, image=encrypt_img, padx=5, pady=5, borderwidth=0, command=lambda: encrypt_func(), bg="#000066", fg="#ffffff")
change_mode_button=tkinter.Button(
    window, text="Change Mode", padx=5, pady=5, borderwidth=10, command=lambda: change_mode(), bg="#000066", fg="#ffffff")
change_mode_button.grid(row=13, column=2)


# textboxes

hash_textbox=tkinter.Entry(window)
hash_textbox.grid(row=4, column=2)
algorithm_textbox=tkinter.Entry(window)
algorithm_textbox.grid(row=3, column=2)


window.mainloop()
