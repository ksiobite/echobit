from cryptography.fernet import Fernet

def Crypted_Message(message):
    secret = f'{message}'.encode('utf-8')
    _Cipher = Fernet.generate_key()
    key = Fernet(_Cipher)

    encrypted_message = key.encrypt(secret)
    return encrypted_message
