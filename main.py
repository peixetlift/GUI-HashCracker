import hashlib
import time
import argparse
from time import sleep
import hashing
import bruteforce

# parsing arguments from terminal input
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist')  # wordlist
parser.add_argument('-f', '--hashfile')  # hash
parser.add_argument('-m', '--mode')  # hashing algorith,
args = parser.parse_args()

# reading wordlist and hash file
with open(args.wordlist, errors='ignore') as f:
    content = f.read().splitlines()
with open(args.hashfile) as f:
    hash = f.readline().splitlines()

# current timestamp
start = time.time()

# crack hash
print(args.mode)
if(args.mode == 'sha1'):
    hashing.sha1(content, hash)
elif(args.mode == 'md5'):
    hashing.md5(content, hash)
elif(args.mode == 'sha256'):
    hashing.sha256(content, hash)
elif(args.mode == 'nltm'):
    hashing.nltm(content, hash)

# timestamp when finished
end = time.time()

print("Time elapsed : " + str(end - start) + " seconds")
