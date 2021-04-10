import hashlib

def encrypt(hashing_algorithm, word):
    if(hashing_algorithm.lower() == 'md5'):
        return hashlib.md5(word.encode()).hexdigest()
    elif(hashing_algorithm.lower() == 'sha1'):
        return hashlib.sha1(word.encode()).hexdigest()
    elif(hashing_algorithm.lower() == 'sha256'):
        return hashlib.sha256(word.encode()).hexdigest()
    elif(hashing_algorithm.lower() == 'nltm'):
        return hashlib.new('md4', word.encode('utf-16le')).hexdigest()
