# Cryptography_Project
The repository is a final project for CS 789 using EIGamal and RSA

To run, please use command line and simply enter:
```
python main.py
```
(The `main.py` intergrated Unittest and normal main function abilities)

Then you will see:
```
1. RSA
2. ElGamal
3. all
Please choose an cryptogaphy method:
```

Here are some sample output for every choice:

RSA:
```
Please choose an cryptogaphy method:1
test_RSA (__main__.TestRSA) ... [Pub Key:303367]  [Pri Key:1632103]  [Text:1056269]

--- MyRSA Encryption ---
[Enc Text]: 484860
--- MyRSA Decryption ---
[Dec Text]: 1056269
--- MyRSA Eavesdrop ---
[n: 1942691]  [pub: 303367]  [ciphertext: 484860]
[final dec cipher text: 1056269]:
ok

----------------------------------------------------------------------
Ran 1 test in 14.023s

OK
```

ElGamal:
```
Please choose an cryptogaphy method:2
test_ElGamal (__main__.TestElGamal) ...
--- MyElGamal Encryption ---
[A] [text:3145]  [k=4018] [4637 1238]
--- MyElGamal Decryption ---
[B] [text:3145]  [l=2609] [4637 4126]
[enc text : 2349]    [dec text : 3145]
--- MyElGamal Eavesdrop ---
Eavesdrop calc [a : 3628]  [k : 1429]  [l : 20]
[final dec cipher text: 3145]:
ok

----------------------------------------------------------------------
Ran 1 test in 0.775s

OK
```

Both:
```
Please choose an cryptogaphy method:3
test_RSA (__main__.TestRSA) ... [Pub Key:421361]  [Pri Key:1748681]  [Text:738163]

--- MyRSA Encryption ---
[Enc Text]: 255510
--- MyRSA Decryption ---
[Dec Text]: 738163
--- MyRSA Eavesdrop ---
[n: 2458307]  [pub: 421361]  [ciphertext: 255510]
[final dec cipher text: 738163]:
ok
test_ElGamal (__main__.TestElGamal) ...
--- MyElGamal Encryption ---
[A] [text:2304]  [k=1513] [1500 1500]
--- MyElGamal Decryption ---
[B] [text:2304]  [l=1549] [1500 2934]
[enc text : 309]    [dec text : 2304]
--- MyElGamal Eavesdrop ---
Eavesdrop calc [a : 1888]  [k : 1]  [l : 10]
[final dec cipher text: 2304]:
ok

----------------------------------------------------------------------
Ran 2 tests in 15.652s

OK
```
Exception:
```
Please choose an cryptogaphy method:4
choose not support. exit
```


