import hashlib

# defining functions for encoding strings


def md5(content, hash):
    print("Trying to crack the hash " + hash[0] + "...")
    for i in range(0, len(content)):
        result = hashlib.md5(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            print("Hash cracked, the decoded string is : " + content[i])
            break


def sha1(content, hash):
    print("Trying to crack the hash " + hash[0] + "...")
    for i in range(0, len(content)):
        result = hashlib.sha1(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            print("Hash cracked, the decoded string is : " + content[i])
            break


def sha256(content, hash):
    print("Trying to crack the hash " + hash[0] + "...")
    for i in range(0, len(content)):
        result = hashlib.sha256(content[i].encode())
        if(result.hexdigest().lower() == hash[0].lower()):
            print("Hash cracked, the decoded string is : " + content[i])
            break


def nltm(content, hash):
    print("Trying to crack the hash " + hash[0] + "...")
    for i in range(0, len(content)):
        result = hashlib.new('md4', content[i].encode('utf-16le'))
        if(result.hexdigest().lower() == hash[0].lower()):
            print("Hash cracked, the decoded string is : " + content[i])
            break
