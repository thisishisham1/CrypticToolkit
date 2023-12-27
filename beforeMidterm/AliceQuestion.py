import string


class AliceQuestion:
    def __init__(self):
        self.alpha = string.ascii_lowercase + string.digits  # for (0:9)

    def additive(self, key, plaintext):
        ciphertext = ""
        for letter in plaintext:
            index = self.alpha.find(letter)
            index = (index + key) % 36
            ciphertext += self.alpha[index]
        return ciphertext

    def multiplicative(self, key, plaintext):
        ciphertext = ''
        for letter in plaintext:
            index = self.alpha.find(letter)
            index = (index * key) % 36
            ciphertext += self.alpha[index]
        return ciphertext

    def affine(self, key1, key2, plaintext):
        ciphertext = ''
        for letter in plaintext:
            index = self.alpha.find(letter)
            lec = (index * key1 + key2) % 36
            ciphertext += self.alpha[lec]
        return ciphertext


if __name__ == "__main__":
    obj = AliceQuestion()
    plaintext = "hello1"
    key = 7
    key1, key2 = 7, 2
    print("Your plain Text is:", plaintext)

    ciphertext_1 = obj.additive(plaintext=plaintext, key=key)
    print("Your encryption Text by alice additive is:", ciphertext_1)

    ciphertext_3 = obj.multiplicative(plaintext=plaintext, key=key)
    print("Your encryption Text by alice multiplicative is:", ciphertext_3)

    ciphertext_3 = obj.affine(plaintext=plaintext, key1=key1, key2=key2)
    print("Your encryption Text by alice affine is:", ciphertext_3)
