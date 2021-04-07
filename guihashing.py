import hashlib
import tkinter
from tkinter import *

# defining functions for encoding strings

def guimd5(content, hash):
    for i in range(0, len(content)):
        result = hashlib.md5(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            return content[i]
            break


def guisha1(content, hash):
    for i in range(0, len(content)):
        result = hashlib.sha1(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            return content[i]
            break

def guisha256(content, hash):
    for i in range(0, len(content)):
        result = hashlib.sha256(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            return content[i]
            break

def guinltm(content, hash):
    for i in range(0, len(content)):
        result = hashlib.new('md4', content[i].encode('utf-16le'))
        if(result.hexdigest().lower() == hash[0].lower()):
            return content[i]
            break