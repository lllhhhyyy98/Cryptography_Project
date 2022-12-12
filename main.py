import unittest
from MyRsa import *
from MyElGamal import *

class TestRSA(unittest.TestCase):
    def test_RSA(self):
        test1 = MyRsa()
        test1.MyRsa_Encrypt()
        test1.MyRsa_Decrypt()

        # check
        self.assertEqual(test1.MyRsa_GetDecText(), test1.MyRsa_GetText())
        self.assertEqual(test1.MyRsa_Eavesdrop(test1.n, test1.pub, test1.enc_text), test1.MyRsa_GetText())

class TestElGamal(unittest.TestCase):
    def test_ElGamal(self):
        test1 = MyElGamal()
        test1.MyElGamal_Encrypt()
        c = test1.MyElGamal_Decrypt()

        # check
        self.assertEqual(test1.dec_text, test1.text)
        self.assertEqual(test1.MyElGamal_Eavesdrop(c), test1.text)

if __name__ == "__main__":
    print("1. RSA")
    print("2. ElGamal")
    print("3. all")
    choose = int(input("Please choose an cryptogaphy method:"))

    t_rsa = unittest.TestLoader().loadTestsFromTestCase(TestRSA)
    t_elgamal = unittest.TestLoader().loadTestsFromTestCase(TestElGamal)
    # tests = unittest.TestSuite([t_rsa])
    # tests = unittest.TestSuite([t_elgamal])
    if choose == 1:
        tests = unittest.TestSuite([t_rsa])
        unittest.TextTestRunner(verbosity=2).run(tests)
    elif choose == 2:
        tests = unittest.TestSuite([t_elgamal])
        unittest.TextTestRunner(verbosity=2).run(tests)
    elif choose == 3:
        tests = unittest.TestSuite([t_rsa, t_elgamal])
        unittest.TextTestRunner(verbosity=2).run(tests)
    else:
        print("choose not support. exit")