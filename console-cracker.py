import hashlib
import time
import argparse
from time import sleep
import decrypt
import encrypt

# parsing arguments from terminal input
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist')  # wordlist
parser.add_argument('-f', '--hashfile')  # hash to decrypt
parser.add_argument('-a', '--algorithm')  # hashing algorithm,
parser.add_argument('-m', '--mode')  # encrypt/decrypt
parser.add_argument('-p', '--password')  # word to encrypt
args = parser.parse_args()

# reading wordlist and hash file
if(args.mode.lower() == 'decrypt'):
    with open(args.wordlist, errors='ignore') as f:
        content = f.read().splitlines()
    with open(args.hashfile) as f:
        hash = f.readline().splitlines()

# current timestamp
start = time.time()

# encrypt/decrypt
print("Selected algorithm : " + args.algorithm)

if(args.mode.lower() == 'decrypt'):
    print("Trying to crack the hash " + hash[0] + "...")
    print("Hash cracked, the decoded string is : " + str(decrypt.decrypt(args.algorithm, content, hash[0])))
elif(args.mode.lower() == 'encrypt'):
    print("The " + args.algorithm + " hash for " + args.password + " is : " + encrypt.encrypt(args.algorithm,args.password))

# timestamp when finished
end = time.time()

print("Time elapsed : " + str(end - start) + " seconds")
