import math
import random
from sympy import mod_inverse


def generate_large_prime():
    return random.choice([i for i in range(1000, 5000) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))])


def generate_keypair():
    p = generate_large_prime()
    q = generate_large_prime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while not (phi_n > e > 1 == math.gcd(e, phi_n)):
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def pad_message(message, n):
    k = len(bin(n)) - 2  # Size of the modulus in bits
    m = len(bin(message)) - 2  # Size of the message in bits

    if m > k - 2 * 8 - 2:
        raise ValueError("Message too long")

    padded_message = message << 8  # Append a 0 byte at the end
    padded_message ^= random.randint(0, 2 ** 8 - 1)  # XOR with a random byte
    return padded_message


def unpad_message(padded_message):
    return padded_message >> 8  # Remove the appended byte


def encrypt(message, public_key):
    e, n = public_key
    padded_message = pad_message(message, n)
    return pow(padded_message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    padded_message = pow(ciphertext, d, n)
    return unpad_message(padded_message)


