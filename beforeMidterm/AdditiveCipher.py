import string


class AdditiveCipher:
    def __init__(self):
        self.alpha = string.ascii_letters

    def encrypt(self, plaintext, key):
        ciphertext = ""
        for letter in plaintext:
            char = self.alpha.find(letter)
            loc = (char + key) % 26
            ciphertext += self.alpha[loc]
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for letter in ciphertext:
            char = self.alpha.find(letter)
            loc = (char - key) % 26
            plaintext += self.alpha[loc]
        return plaintext

    def brute_force(self, ciphertext):
        for key in range(26):
            plaintext = ""
            for char in ciphertext:
                char = self.alpha.find(char)
                loc = (char - key) % 26
                plaintext += self.alpha[loc]
            print(f"key: {key} | plaintext: {plaintext}")


if __name__ == "__main__":
    obj = AdditiveCipher()
    plaintext = "hello"
    key = 15
    print("Your plain Text is:", plaintext)

    ciphertext = obj.encrypt(plaintext=plaintext, key=key)
    print("Your cipher Text is:", ciphertext)

    decrypted = obj.decrypt(ciphertext=ciphertext, key=key)
    print("Your decrypted Text is:", decrypted)
