import math
import random
from collections import OrderedDict

class MyElGamal:
    def __init__(self, start = 1234, end = 12345):
        self.rand_start = start
        self.rand_end = end
        self.rand_prime = 0
        self.root = 0
        self.k = 0
        self.B1 = 0
        self.B2 = 0
        self.C1 = 0
        self.C2 = 0

        self.text = 0           # Origin text
        self.enc_text = 0       # Encrypted text
        self.dec_text = 0       # Decrypted text
        self.cipher = 0         # Eavesdrop text
        pass

    # Check if it is primitive root
    def MyElGamal_IsRoot(self, g, prime):
        for i in range(1, prime - 1):
            # If g^i mod p is equal to 1, g is not a primitive root
            if (g**i) % prime == 1:
                return False
        return True

    # Obtain the primitive root
    def MyElGamal_GetPriRoot(self, prime):
        g = random.randrange(2, prime)
        if self.MyElGamal_IsRoot(g, prime):
            return g
        while not self.MyElGamal_IsRoot(g, prime):
            g = random.randrange(2, prime)
        return g

    def MyElGamal_Mod(self, input, prime):
        for i in range(1, prime):
            if ((input % prime) * (i % prime)) % prime == 1:
                return i
        return -1

    # Determine if it is prime
    def MyElGamal_GenPrime(self, num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num**0.5) + 1, 2):
            if (num % i) == 0:
                return False
        return True

    # Baby-step-giant-step
    # Find discrete log
    def MyElGamal_DisLog(self, base, num, p):
        order = p - 1
        map1 = {}
        m = math.ceil(math.sqrt(order))
        for j in range(0, m):
            map1[j] = base**j % p

        map1 = OrderedDict(sorted(map1.items()))
        c = self.MyElGamal_Mod(base, p)
        check = c**m % p
        for i in range(0, m):
            for k in map1.keys():
                if map1[k] == num * (check ** i) % p:
                    return i*m + k

    def MyElGamal_Encrypt(self):
        print("\n--- MyElGamal Encryption ---")
        # Generate public/private key
        self.rand_prime = random.randrange(self.rand_start, self.rand_end)
        while not self.MyElGamal_GenPrime(self.rand_prime):
            self.rand_prime = random.randrange(self.rand_start, self.rand_end)
        self.root = self.MyElGamal_GetPriRoot(self.rand_prime)
        a = random.randrange(self.rand_start, self.rand_prime)
        # A only know k
        self.k = random.randrange(self.rand_start, self.rand_prime)
        self.text = random.randrange(0, self.rand_prime)
        self.C1 = self.root ** a % self.rand_prime
        self.C2 = self.C1 ** self.k % self.rand_prime
        print("[A] [text:%d]  [k=%d] [%d %d]" % (self.text, self.k, self.C1, self.C2))
    
    def MyElGamal_Decrypt(self):
        print("--- MyElGamal Decryption ---")
        # B decrypt, using rand_start ~ rand_prime
        l = random.randrange(self.rand_start, self.rand_prime)
        self.B1 = self.C1
        self.B2 = self.B1 ** l % self.rand_prime
        print("[B] [text:%d]  [l=%d] [%d %d]" % (self.text, l, self.B1, self.B2))
        # Check if it is equal
        C1ForB = self.C2 ** l % self.rand_prime
        B1ForC = self.B2 ** self.k % self.rand_prime
        # B inverse
        dec = self.MyElGamal_Mod(C1ForB, self.rand_prime)
        self.cipher = self.enc_text = self.text * B1ForC % self.rand_prime
        self.dec_text = (self.cipher * dec % self.rand_prime)
        print("[enc text : %d]    [dec text : %d]" % (self.enc_text, self.dec_text))
        return self.cipher
        pass

    def MyElGamal_Eavesdrop(self, cipher):
        print("--- MyElGamal Eavesdrop ---")
        print("Eavesdrop calc [a : %d]  [k : %d]  [l : %d]" % (self.MyElGamal_DisLog(self.root, self.C1, self.rand_prime), 
            self.MyElGamal_DisLog(self.C1, self.C2, self.rand_prime),
            self.MyElGamal_DisLog(self.B1, self.B2, self.rand_prime))
            )
        dec_cip_text = cipher * self.MyElGamal_Mod(self.C2 ** self.MyElGamal_DisLog(self.C1, self.B2, self.rand_prime) % self.rand_prime, self.rand_prime) % self.rand_prime
        print("[final dec cipher text: %d]: " % dec_cip_text)
        return dec_cip_text
        pass
