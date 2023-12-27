import string


class MultiplicativeCipher:
    def __init__(self):
        self.alpha = string.ascii_letters

    def isValidKey(self, key):
        return key % 2 == 1 and key != 13 and 1 <= key <= 25

    def encrypt(self, key, plaintext):
        if not self.isValidKey(key):
            raise ValueError("Invalid key1. It must be an odd number between 1 and 26 (excluding 13).")
        ciphertext = ""
        for letter in plaintext:
            index = self.alpha.find(letter)
            loc = (index * key) % 26
            ciphertext += self.alpha[loc]
        return ciphertext

    def decrypt(self, key, ciphertext):
        if not self.isValidKey(key):
            raise ValueError("Invalid key1. It must be an odd number between 1 and 26 (excluding 13).")
        plaintext = ""
        keyInverse = 0
        for counter in range(1, 26, 2):
            if (key * counter) % 26 == 1:
                keyInverse = counter
                break
        for letter in ciphertext:
            index = self.alpha.find(letter)
            loc = (index * keyInverse) % 26
            plaintext += self.alpha[loc]
        return plaintext

    def brute_force(self, ciphertext):
        for potential_key in range(1, 26, 2):
            plaintext = ""
            keyInverse = 0
            for counter in range(1, 26, 2):
                if counter == 13:
                    continue
                if (potential_key * counter) % 26 == 1:
                    keyInverse = counter
                    break
            for letter in ciphertext:
                index = self.alpha.find(letter)
                loc = (index * keyInverse) % 26
                plaintext += self.alpha[loc]
            print(f"Key {potential_key}: {plaintext}")


if __name__ == "__main__":
    obj = MultiplicativeCipher()
    plaintext = "hello"
    key = 7
    print("Your plain Text is:", plaintext)

    ciphertext = obj.encrypt(plaintext=plaintext, key=key)
    print("Your cipher Text is:", ciphertext)

    decrypted = obj.decrypt(ciphertext=ciphertext, key=key)
    print("Your decrypted Text is:", decrypted)
