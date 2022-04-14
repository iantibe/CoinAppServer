import hashlib
import os
from Constants import Constants


class HashComponents:

    def __init__(self):
        pass

    def hashString(self, password: str, salt: bytes):
        return hashlib.pbkdf2_hmac(
            Constants.ENCODE_STYLE,
            password.encode(Constants.PASSWORD_ENCODE_STYLE),
            salt,
            Constants.ITERATIONS_OF_SHA256
            )

    def extractSaltFromStorageString(self, passwordblock: bytes):
        return passwordblock[:Constants.RANDOM_SALT_LENGTH]

    def generateStorageItem(self, salt: bytes, password: bytes):
        return salt + password

    def generateSalt(self):
        return os.urandom(Constants.RANDOM_SALT_LENGTH)

    def extractPasswordFromStorageString(self, passwordblock: bytes):
        return passwordblock[Constants.RANDOM_SALT_LENGTH:]




