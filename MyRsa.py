import math
import random

class MyRsa:
    def __init__(self, start = 1024, end = 2048):
        self.rand_start = start
        self.rand_end = end
        self.n = 0
        self.order = 0
        self.pub = 0
        self.pri = 0
        self.text = 0

        self.enc_text = 0
        self.dec_text = 0

        p1 = self.MyRsa_GetPrime()
        p2 = self.MyRsa_GetPrime()

        self.MyRsa_GetKey(p1, p2)
        print("[Pub Key:%d]  [Pri Key:%d]  [Text:%d]" % (self.pub, self.pri, self.text))

    # collect prime
    def MyRsa_CollectPrime(self, n):
        arr = []
        while n % 2 == 0:
            arr.append(2)
            n = n / 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                arr.append(i)
                n = n / i
        if n > 2:
            arr.append(int(n))
        return arr
    
    # Determine if it is prime
    def MyRsa_GenPrime(self, num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num ** 0.5) + 1, 2):
            if (num % i) == 0:
                return False
        return True

    # mod
    def MyRsa_Mod(self, input, prime):
        for i in range(1, prime):
            if ((input % prime) * (i % prime)) % prime == 1:
                return i
        return -1

    # Generate prime randomly
    def MyRsa_GetPrime(self):
        p = random.randrange(self.rand_start, self.rand_end)
        while not self.MyRsa_GenPrime(p):
            p = random.randrange(self.rand_start, self.rand_end)
        return p
    
    # Generate public/private key
    def MyRsa_GetKey(self, p, q):
        self.n = q * p
        self.order = (q - 1) * (p - 1)
        self.pub = random.randrange(0, self.order)
        while not self.MyRsa_GenPrime(self.pub):
            self.pub = random.randrange(0, self.order)
        self.pri = self.MyRsa_Mod(self.pub, self.order)
        self.text = random.randrange(1, self.order)
        while not self.MyRsa_GenPrime(self.text):
            self.text = random.randrange(1, self.order)

    # Encrypt
    def MyRsa_Encrypt(self):
        print("\n--- MyRSA Encryption ---")
        self.enc_text = self.text ** self.pub % self.n
        print("[Enc Text]: %d" % self.enc_text)
        pass

    # Decrypt
    def MyRsa_Decrypt(self):
        print("--- MyRSA Decryption ---")
        self.dec_text = self.enc_text ** self.pri % self.n
        print("[Dec Text]: %d" % self.dec_text)
        pass

    # Eavesdrop
    def MyRsa_Eavesdrop(self, n1, pub1, text1):
        print("--- MyRSA Eavesdrop ---")
        print("[n: %d]  [pub: %d]  [ciphertext: %d]" % (n1, pub1, text1))
        arr = self.MyRsa_CollectPrime(n1)
        all_order = (arr[0] - 1) * (arr[1] - 1)
        all_pri = self.MyRsa_Mod(pub1, all_order)
        dec_cip_text = text1 ** all_pri % n1
        print("[final dec cipher text: %d]: " % dec_cip_text)
        return dec_cip_text
        pass
    
    def MyRsa_GetText(self):
        return self.text

    def MyRsa_GetEncText(self):
        return self.enc_text
    
    def MyRsa_GetDecText(self):
        return self.dec_text