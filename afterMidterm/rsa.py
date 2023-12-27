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


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


