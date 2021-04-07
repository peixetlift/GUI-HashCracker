import tkinter
from tkinter import *
from tkinter import filedialog
import hashing
import time
import guihashing


def load_file():
    filename = filedialog.askopenfilename(initialdir ="/home/ubuntu",title ="Select a file", filetypes =(("Text files", "*.txt*"),("all files","*.*")))
    wordlist[0] = filename
    content_label.configure(text=filename)

def decrypt(is_open,hashstr):
    hashstr=hash_textbox.get()
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
    output_label.configure(text="Hash cracked : " + str(result))
    end = time.time()
    time_label.configure(text="Time elapsed : " + str(end-start))
    

    
is_open = False
wordlist = [""]
hashstr = ""

# window
window = tkinter.Tk()
window.geometry("900x600")
window.title("HASH CRACKER")

# show unused cols/rows
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(8, weight=1)
window.grid_rowconfigure(10, weight=1)

# labels
title_label = tkinter.Label(window, text="Decrypt hashes")
title_label.grid(row=1, column=2)
text_label1 = tkinter.Label(window, text="Hash :")
text_label1.grid(row=3, column=1)
text_label2 = tkinter.Label(window, text="Hashing algorithm :")
text_label2.grid(row=2, column=1)
text_label3 = tkinter.Label(window, text="(md5, sha1, sha256, nltm)")
text_label3.grid(row=2, column=3)
content_label = tkinter.Label(text="No file selected")
content_label.grid(row=5, column=2)
hash_label = tkinter.Label(text="")
output_label = tkinter.Label(text="")
output_label.grid(row=7, column=2)
time_label = tkinter.Label(text="")
time_label.grid(row=9, column=2)



# buttons
load_wordlist_button = tkinter.Button(window, text="Select wordlist", padx=5, pady=5, command=lambda: load_file())
load_wordlist_button.grid(row=4, column=2)
decrypt_button = tkinter.Button(window, text="Decrypt", padx=5, pady=5, command=lambda: decrypt(is_open,hashstr))
decrypt_button.grid(row=4, column=3)
# textboxes
hash_textbox = tkinter.Entry(window)
hash_textbox.grid(row=3, column=2)
algorithm_textbox = tkinter.Entry(window)
algorithm_textbox.grid(row=2, column =2)


window.mainloop()
