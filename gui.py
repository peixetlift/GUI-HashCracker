import tkinter
from tkinter import *
from tkinter import filedialog
import hashing
import time
import guihashing

# select wordlist from files


def load_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a file", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    wordlist[0] = filename
    content_label.configure(text=filename)

# decrypt hash


def decrypt(is_open, hashstr):
    hashstr = hash_textbox.get()
    if(is_open == False):
        with open(wordlist[0], errors='ignore') as f:
            content = f.read().splitlines()
            is_open = True

    start = time.time()
    if(algorithm_textbox.get().lower() == 'sha1'):
        result = guihashing.guisha1(content, hashstr)
    elif(algorithm_textbox.get().lower() == 'md5'):
        result = guihashing.guimd5(content, hashstr)
    elif(algorithm_textbox.get().lower() == 'sha256'):
        result = guihashing.guisha256(content, hashstr)
    elif(algorithm_textbox.get().lower() == 'nltm'):
        result = guihashing.guinltm(content, hashstr)
    output_label.configure(text="Hash cracked : " + str(result), bg="#000066", fg="#ff0000")
    end=time.time()
    time_label.configure(text = "Time elapsed : " + str(end-start), bg = "#000066", fg = "#ffffff")


is_open=False
wordlist=[""]
hashstr=""

# window
window=tkinter.Tk()
window.geometry("700x450")
window.title("HASH CRACKER")

# grid configuration
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(4, weight=1)
for i in range(0, 15):
    window.grid_rowconfigure(i, weight=1)

# images
decrypt_img=PhotoImage(
    file="./images/decrypt-logo-small.png")
select_wlist_img=PhotoImage(
    file="./images/selectwlist-small.png")
bg_img=PhotoImage(
    file="./images/wallpaper-encr.png", master=window)

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
content_label=tkinter.Label(
    text="No wordlist selected", bg="#000066", fg="#ffffff")
content_label.grid(row=7, column=2)
hash_label=tkinter.Label(text="", bg="#000066", fg="#ffffff")
output_label=tkinter.Label(text="", bg="#008DD4")
output_label.grid(row=8, column=2)
time_label=tkinter.Label(text="", bg="#007EBD")
time_label.grid(row=10, column=2)


# buttons
load_wordlist_button=tkinter.Button(
    window, image=select_wlist_img, padx=5, pady=5, borderwidth=0, command=lambda: load_file(), bg = "#000066", fg = "#ffffff")
load_wordlist_button.grid(row = 6, column = 2)
decrypt_button=tkinter.Button(
    window, image = decrypt_img, padx = 5, pady = 5, borderwidth = 0, command = lambda: decrypt(is_open, hashstr), bg="#000066", fg="#ffffff")
decrypt_button.grid(row=6, column=3)

# textboxes
hash_textbox = tkinter.Entry(window)
hash_textbox.grid(row=4, column=2)
algorithm_textbox = tkinter.Entry(window)
algorithm_textbox.grid(row=3, column=2)


window.mainloop()
