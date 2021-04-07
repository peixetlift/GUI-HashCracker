import hashlib
import tkinter
from tkinter import *

# defining functions for encoding strings

def guimd5(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.md5(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]
            


def guisha1(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.sha1(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]
            

def guisha256(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.sha256(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]
            

def guinltm(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.new('md4', content[i].encode('utf-16le'))
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]
            