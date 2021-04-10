import hashlib

# defining functions for encoding strings


def md5(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.md5(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]


def sha1(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.sha1(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]


def sha256(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.sha256(content[i].encode())
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]


def nltm(content, hashstr):
    for i in range(0, len(content)):
        result = hashlib.new('md4', content[i].encode('utf-16le'))
        if(result.hexdigest().lower() == hashstr.lower()):
            return content[i]


def decrypt(algorithm, content, hash):
    if(algorithm.lower() == 'sha1'):
        return sha1(content, hash)
    elif(algorithm.lower() == 'md5'):
        return md5(content, hash)
    elif(algorithm.lower() == 'sha256'):
        return sha256(content, hash)
    elif(algorithm.lower() == 'nltm'):
        return nltm(content, hash)
