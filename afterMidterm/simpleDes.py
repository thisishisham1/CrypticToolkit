class SimplestDes:
    def __init__(self):
        self.key = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # straight box when generate key
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]  # compression box when generate key
        self.key1 = [0] * 8
        self.key2 = [0] * 8
        self.IP = [1, 4, 6, 8, 3, 5, 2, 7]  # initial permutation
        self.EP = [4, 1, 2, 3, 2, 3, 4, 1]  # expanded permutation
        self.P4 = [2, 1, 4, 3]  # straight box
        self.IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
        self.S0 = [[0, 2, 1, 3], [1, 0, 3, 2], [1, 3, 2, 0], [3, 0, 2, 1]]
        self.S1 = [[1, 3, 0, 2], [0, 2, 3, 1], [0, 3, 0, 2], [2, 1, 0, 3]]

    def key_generation(self):
        key_ = [self.key[self.P10[i] - 1] for i in range(10)]
        # divide the key
        Ls = key_[:5]
        Rs = key_[5:]

        Ls_1 = self.shift(Ls, 1)
        Rs_1 = self.shift(Rs, 1)

        key_ = Ls_1 + Rs_1

        self.key1 = [key_[self.P8[i] - 1] for i in range(8)]

        Ls_2 = self.shift(Ls, 2)
        Rs_2 = self.shift(Rs, 2)

        key_ = Ls_2 + Rs_2

        self.key2 = [key_[self.P8[i] - 1] for i in range(8)]

        print("Your Key-1:", self.key1)
        print("Your Key-2:", self.key2)

    def swap(self, array, n):
        l = array[:n]
        r = array[n:]
        output = r + l
        return output

    def shift(self, ar, n):
        for _ in range(n):
            temp = ar[0]
            ar = ar[1:] + [temp]
        return ar

    def binary_(self, val):
        if val == 0:
            return "00"
        elif val == 1:
            return "01"
        elif val == 2:
            return "10"
        else:
            return "11"

    def function_(self, ar, key_):
        left = ar[:4]
        right = ar[4:]

        ep = [right[self.EP[i] - 1] for i in range(8)]  # expanded to left hand side

        ar = [key_[i] ^ ep[i] for i in range(8)]

        l_1 = ar[:4]  # s1
        r_1 = ar[4:]  # s2

        row = int(str(l_1[0]) + str(l_1[3]), 2)
        col = int(str(l_1[1]) + str(l_1[2]), 2)
        val = self.S0[row][col]
        str_l = self.binary_(val)

        row = int(str(r_1[0]) + str(r_1[3]), 2)
        col = int(str(r_1[1]) + str(r_1[2]), 2)
        val = self.S1[row][col]
        str_r = self.binary_(val)

        r_ = [int(str_l[i]) for i in range(2)] + [int(str_r[i]) for i in range(2)]

        r_p4 = [r_[self.P4[i] - 1] for i in range(4)]  # s-box

        left = [left[i] ^ r_p4[i] for i in range(4)]

        output = left + r_
        return output

    def encrypt(self, plaintext):
        arr = [plaintext[self.IP[i] - 1] for i in range(8)]
        arr1 = self.function_(arr, self.key1)
        after_swap = self.swap(arr1, len(arr1) // 2)
        arr2 = self.function_(after_swap, self.key2)
        ciphertext = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        return ciphertext

    def decrypt(self, ar):
        arr = [ar[self.IP[i] - 1] for i in range(8)]
        arr1 = self.function_(arr, self.key2)
        after_swap = self.swap(arr1, len(arr1) // 2)
        arr2 = self.function_(after_swap, self.key1)
        decrypted = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        return decrypted


if __name__ == "__main__":
    obj = SimplestDes()
    obj.key_generation()

    plaintext = [1, 0, 0, 1, 0, 1, 1, 1]
    print("Your plain Text is:", plaintext)

    ciphertext = obj.encrypt(plaintext)
    print("Your cipher Text is:", ciphertext)

    decrypted = obj.decrypt(ciphertext)
    print("Your decrypted Text is:", decrypted)
