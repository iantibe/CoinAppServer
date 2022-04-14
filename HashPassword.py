from Constants import Constants
from HashComponents import HashComponents


class HashPassword:

    def __init__(self, hashcomponents: HashComponents):
        self.hashcomponents = hashcomponents

    def generatePasswordBlockForStorage(self, password: str):
        salt = self.hashcomponents.generateSalt()
        pw = self.hashcomponents.hashString(password, salt)
        return self.hashcomponents.generateStorageItem(salt, pw)

    def hashInputPassword(self, password: str, passwordblock: bytes):
        salt = self.hashcomponents.extractSaltFromStorageString(passwordblock)
        return self.hashcomponents.hashString(password, salt)

    def extractPasswordFromStorage(self, passwordblock: bytes):
        return self.hashcomponents.extractPasswordFromStorageString(passwordblock)

if __name__ == '__main__':
    hc = HashComponents(Constants())
    hp = HashPassword(hc)
    passwordblcok = hp.generatePasswordBlockForStorage("test")
    print("stored password to database", passwordblcok)
    print("Extgracted password", hp.extractPasswordFromStorage(passwordblcok))
    print("hashinputpassword", hp.hashInputPassword("test", passwordblcok))
