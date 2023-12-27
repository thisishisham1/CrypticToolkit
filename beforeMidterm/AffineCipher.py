import string


class AffineCipher:
    def __init__(self):
        self.alpha = string.ascii_letters

    def isValidKey(self, key1):
        return key1 % 2 == 1 and key1 != 13 and 1 <= key1 <= 25

    def encrypt(self, key1, key2, plaintext):
        if not self.isValidKey(key1):
            raise ValueError("Invalid key1. It must be an odd number between 1 and 26 (excluding 13).")
        ciphertext = ""
        for letter in plaintext:
            index = self.alpha.find(letter)
            lec = (index * key1 + key2) % 26
            ciphertext += self.alpha[lec]
        return ciphertext.upper()

    def decrypt(self, key1, key2, ciphertext):
        if not self.isValidKey(key1):
            raise ValueError("Invalid key1. It must be an odd number between 1 and 26 (excluding 13).")

        plaintext = ""
        keyInverse = 0
        for counter in range(1, 26, 2):
            if counter == 13:
                continue
            if key1 * counter % 26 == 1:
                keyInverse = counter
                break
        for letter in ciphertext:
            index = self.alpha.find(letter)
            lec = ((index - key2) * keyInverse) % 26
            plaintext += self.alpha[lec]
        return plaintext

    def brute_force(self, ciphertext, key1):
        if not self.isValidKey(key1):
            raise ValueError("Invalid key1. It must be an odd number between 1 and 26 (excluding 13).")

        plaintext = ""
        keyInverse = 0
        for counter in range(1, 26, 2):
            if counter == 13:
                continue
            if key1 * counter % 26 == 1:
                keyInverse = counter
                break
        for k2 in range(26):
            for letter in ciphertext:
                index = self.alpha.find(letter)
                lec = ((index - k2) * keyInverse) % 26
                plaintext += self.alpha[lec]
            print(f"Key1: {key1}, Key2: {k2} | Plaintext: {plaintext}")
            plaintext = ""  # Reset plaintext for the next iteration


if __name__ == "__main__":
    obj = AffineCipher()
    plaintext = "hello"
    key1 = 7
    key2 = 2
    print("Your plain Text is:", plaintext)

    ciphertext = obj.encrypt(plaintext=plaintext, key1=key1, key2=key2)
    print("Your cipher Text is:", ciphertext)

    decrypted = obj.decrypt(ciphertext=ciphertext, key1=key1, key2=key2)
    print("Your decrypted Text is:", decrypted)
