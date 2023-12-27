import string


class VigenereCipher:
    def __init__(self):
        self.alpha = string.ascii_uppercase

    def encrypt(self, plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        ciphertext = ""
        keyIndex = 0
        for letter in plaintext:
            if letter.isalpha():
                locKeyLetter = self.alpha.find(key[keyIndex])
                locPlaintextLetter = self.alpha.find(letter)
                locCipher = (locPlaintextLetter + locKeyLetter) % 26
                ciphertext += self.alpha[locCipher]
                keyIndex += 1
                if keyIndex == len(key):
                    keyIndex = 0
        return ciphertext

    def decrypt(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        key = key.upper()
        plaintext = ""
        keyIndex = 0
        for letter in ciphertext:
            if letter.isalpha():
                locKeyLetter = self.alpha.find(key[keyIndex])
                locCipherLetter = self.alpha.find(letter)
                locPlaintext = (locCipherLetter - locKeyLetter) % 26
                plaintext += self.alpha[locPlaintext]
                keyIndex += 1
                if keyIndex == len(key):
                    keyIndex = 0
        return plaintext


if __name__ == "__main__":
    obj = VigenereCipher()
    plaintext = "GEEKS FOR GEEKS"
    key = "AYUSH"
    print("Your plain Text is:", plaintext)

    ciphertext = obj.encrypt(plaintext=plaintext, key=key)
    print("Your cipher Text is:", ciphertext)

    decrypted = obj.decrypt(ciphertext=ciphertext, key=key)
    print("Your decrypted Text is:", decrypted)
