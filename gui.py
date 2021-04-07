import tkinter
from tkinter import *
from tkinter import filedialog
import hashing
import time
import guihashing


def decrypt():
    filename = filedialog.askopenfilename(initialdir ="/home/ubuntu",title ="Select a file", filetypes =(("Text files", "*.txt*"),("all files","*.*")))
    hash[0] = hash_textbox.get()
    with open(filename, errors='ignore') as f:
        content = f.read().splitlines()
        content_label.configure(text=filename)
        start = time.time()
        if(algorithm_textbox.get() == 'sha1'):
            result = guihashing.guisha1(content, hash)
        elif(algorithm_textbox.get() == 'md5'):
            result = guihashing.guimd5(content, hash)
        elif(algorithm_textbox.get() == 'sha256'):
            result = guihashing.guisha256(content, hash)
        elif(algorithm_textbox.get() == 'nltm'):
            result = guihashing.guinltm(content, hash)
        output_label.configure(text="Hash cracked : " + result)
        end = time.time()
        time_label.configure(text="Time elapsed : " + str(end-start))
        
        #show time elapsed

    

hash = [""]

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
time_label.grid(row=7, column=3)



# buttons
load_wordlist_button = tkinter.Button(window, text="Select wordlist and decrypt", padx=5, pady=5, command=lambda: decrypt())
load_wordlist_button.grid(row=4, column=2)


# textboxes
hash_textbox = tkinter.Entry(window)
hash_textbox.grid(row=3, column=2)
algorithm_textbox = tkinter.Entry(window)
algorithm_textbox.grid(row=2, column =2)


window.mainloop()
