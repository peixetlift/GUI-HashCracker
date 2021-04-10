# Usage for console version

### Decrypt mode (-m decrypt) :
-f : specify the hash that has to be cracked (in .txt format)<br>
-w : specify the wordlist (dictionary) to brute-force<br>
-a : Specify the hashing algorithm (Supports md5,sha1,sha256 and NLTM)<br>

```
python3 console-cracker.py -m decrypt -f <hashfile> -w <wordlist> -a <hashing algorithm>
```

### Encrypt mode (-m encrypt) :
-a : Specify the hashing algorithm (Supports md5,sha1,sha256 and NLTM)<br>
-p : Specify the word/password that you want to encrypt<br>

```
python3 console-cracker.py -m decrypt -p <word> -a <hashing algorithm>
```

# Usage for GUI version

```
python3 gui-cracker.py
```
### Decrypt mode :

1st - Specify hashing algorithm <br>
2nd - Specify hash to be cracked<br>
3rd - Select a wordlist<br>
4th - Decrypt (Click the button)<br>

### Encrypt mode :

1st - Specify hashing algorithm <br>
2nd - Specify word to encrypt<br>
3rd - Encrypt (Click the button)<br>

***

### Requirements
- tkinter module : run ```sudo apt-get install python3-tk```
