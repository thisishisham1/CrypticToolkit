import math
import random
import string

from sympy import mod_inverse


class Rsa:
    def __init__(self):
        self.alpha = string.ascii_letters

    @staticmethod
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):  # check divilability
            if num % i == 0:
                return False
        return True

    def generateRandomPrime(self):
        while True:
            number = random.randint(1000, 5000)
            if self.isPrime(number):
                return number

    def generateKeypair(self):
        p = self.generateRandomPrime()
        q = self.generateRandomPrime()

        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = random.randint(2, phi_n - 1)
        while e < phi_n:

            # e must be co-prime to phi and
            # smaller than phi.
            if math.gcd(e, phi_n) == 1:
                break
            else:
                e += 1

        d = mod_inverse(e, phi_n)  # d= e^-1 mod phi_n

        public_key = (e, n)
        private_key = (d, n)

        return public_key, private_key

    def encrypt(self, message, public_key):
        if isinstance(message, int):
            numericMessage = message
        elif isinstance(message, str):
            numericMessage = 1
            for letter in message:
                numericMessage *= self.alpha.find(letter) + 1
        else:
            raise ValueError("Input must be either an integer or a string.")
        e, n = public_key
        return pow(numericMessage, e, n)

    @staticmethod
    def decrypt(ciphertext, private_key):
        d, n = private_key
        return pow(ciphertext, d, n)


if __name__ == "__main__":
    rsa_instance = Rsa()

    # Generate key pair
    public_key, private_key = rsa_instance.generateKeypair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Encrypting a string
    plaintext_string = "hello"
    encrypted_result_string = rsa_instance.encrypt(plaintext_string, public_key)
    print(f'Encrypted String "{plaintext_string}": {encrypted_result_string}')

    # Encrypting a numeric value
    plaintext_number = 12345
    encrypted_result_number = rsa_instance.encrypt(plaintext_number, public_key)
    print(f'Encrypted Number {plaintext_number}: {encrypted_result_number}')

    # Decrypting the results
    decrypted_result_string = rsa_instance.decrypt(encrypted_result_string, private_key)
    decrypted_result_number = rsa_instance.decrypt(encrypted_result_number, private_key)

    print(f'Decrypted String: {decrypted_result_string}')
    print(f'Decrypted Number: {decrypted_result_number}')
