from cryptography.fernet import Fernet
import os

# A public and presentable version of cryptor.py, made for more general use cases
# Uses Fernet cryptography to encrypt and/or decrypt a message


# TODO Put tests and self.SOMETHING = SOMETHING here
def __init__(self):
    print('Nothing')


# Encrypt a message!
def encrypt(message, key):
    plaintxt = bytes(message, encoding='utf-8')
    encr = getKey(name=key)
    ciphrtxt = b'Jej#' + encr.encrypt(plaintxt)
    return ciphrtxt


# Decrypt a message! (That was encrypted using the same key)
def decrypt(message, key):
    ciphrtxt = message
    decr = getKey(name=key)
    if ciphrtxt.split(b'#')[0] == b'Jej':
        plaintxt = decr.decrypt(ciphrtxt.split(b'#')[1])
        return plaintxt
    else:
        raise ValueError('Not encrypted with Cryptor2!')


# Needs to be passed a filename as 'name=' in method calls
def keyGen(**filepath):
    key = Fernet.generate_key()
    if filepath['name'] == '':
        with open('Denj/key.txt', 'wb+') as keyfile:
            keyfile.truncate()
            keyfile.write(key)
    else:
        try:
            with open('Denj/' + filepath['name'] + '.txt', 'w+', encoding='utf-8') as keyfile:
                keyfile.truncate()
                keyfile.write(key)
        except FileNotFoundError:
            print('Invalid filename')


def getKey(**filepath):
    key = ''
    if filepath['name'] == '':
        with open('Denj/key.txt', 'rb') as keyfile:
            key = keyfile.read()
    else:
        try:
            with open('Denj/' + filepath['name'] + '.txt', 'rb', encoding='utf-8') as keyfile:
                key = keyfile.read()
        except FileNotFoundError:
            print('Invalid filename')
    key = Fernet(key)
    return key


# Check to see if a message was encrypted using Cryptor2 based on identifier
def checker(message):
    if type(message) != bytes:
        return False
    result = message.split(b'#')
    if len(result) != 2:
        return False
    elif result[0] != b'Jej':
        return False
    else:
        return True


if __name__ == '__main__':
    message = str(input('Enter message to encrypt...'))
    print('Encrypting message...')
    hey = encrypt(message, '')
    print('Message successfully encrypted. Check Denj/<filename> for result')
    print('Decrypting message...')
    yay = decrypt(message, '')
    print('Decrypted message: {}'.format(yay))
    print('Checking to determine if messages were encrypted using ths program...')
    print(checker(hey))
    print(checker(yay))