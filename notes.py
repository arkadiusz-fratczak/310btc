#!/usr/bin/python3

from itertools import permutations
import base64
import binascii
import wif
import pixel_carve as pc

def ceasar(str, key):
    hex = '0123456789abcdef'
    new_str = []
    for i in range(len(str)):
        str_char = str[i]
        key_char = key[i % len(key)]
        str_idx = hex.index(str_char)
        key_idx = hex.index(key_char)

        new_char_idx = str_idx - key_idx
        new_char = hex[new_char_idx]

        new_str.append(new_char)

    return ''.join(new_str)

def threes(str):
    threes = []
    for i in range(0, len(str), 3):
        threes.append(str[i:i+3])
    return threes

def threes_dec(str):
    return [int(h, 16) for h in threes(str)]

def read_wordlist():
    wordlist = []
    with open('/home/afratczak/projects/310btc/english.txt') as fin:
        for e in fin.readlines():
            wordlist.append(e.rstrip())
    return wordlist

wordlist = read_wordlist()

#511 b20 332 328 410 530
#22b 0fe 52e d0f 7a1 65b
#52c 7e7 511 2f6 56f c4b
row1 = '511b20332328410530'
row2 = '22b0fe52ed0f7a165b'
row3 = '52c7e75112f656fc4b'

str  = row1 + row2 + row3
key = '20181002'

decrypted = ceasar(str, key)
threes_res = threes(decrypted)
threes_dec_res = threes_dec(decrypted)
threes_word = [wordlist[d - 1] for d in threes_dec_res[6:]]

print(decrypted)
print(threes_res)
print(threes_dec_res)
print(threes_word)
print("---")
#cry buyer grain save vault sign lyrics rhythm music fury horror mansion

letters = 'L3 02 7 485 9F'
# ps = permutations(letters)
pwd = 'L379F48502'

# 511 B20 332 328 410 530
# 245 651 58F C2C 03A 717
# 401 9AC 36A 53F 4C6 B26
# 332 328 410 530 491 312
row1b = '511b20332328410530'.lower()
row2b = '24565158FC2C03A717'.lower()
row3b = '4019AC36A53F4C6B26'.lower()
row4b = '332328410530491312'.lower()

str  = row1b + row2b + row3b + row4b
key = '20181002'

decrypted = ceasar(str, key)
threes_res = threes(decrypted)
threes_dec_res = threes_dec(decrypted)
threes_word = [wordlist[d - 1] for d in threes_dec_res[6:]]

print(decrypted)
print(threes_res)
print(threes_dec_res)
print(threes_word)
print("---")
#cry buyer grain save vault sign lyrics rhythm music fury horror mansion
#debris slim immune lock actual tide gas vapor fringe pole flat glance

pwd2 = '02L3F95847'

# Z465/ # 67 8e b9 fc
# key = '678eb9fc'
# key = '4776a9fa'
# key = 'Z465/'

#0.1 KzkZxdhRGxB7eX4u1skXkfJ7VB8JfPp7Nfos3jiF7PQUNMh2SHDE
k1 = "69630650804510e161cf977024ea41fe630942bb6b9429c804b15ef7e865111801"
print("k1:", wif.private_key_to_wif(k1))

#0.2 KxPEUpQ5BE75UGRUVjNmf8dQuWsmP9jqL3FUUjavdRW69MEcmg6C
k2 = "22bc6dc8b10ca296ccffcab76ade66eb0e3224b334c212098cbe8491f172caeb01"
print("k2:", wif.private_key_to_wif(k2))

hash = "273e2b95648fd3cbad0d7fe3ed820e783c0b12fdbe29b57bfb2d1f243d92b1a5"
img = "2f9235c0d7d983da80ac9757f728c0f1ce24ab4763909dda314281510d984e16"
dec2 = "884f383405b2cec233d65dd0a90e6bbb65c361a3165c2eb1cde6d839effaf5af"


address = "39uAUwEFDi5bBbdBm5ViD8sxDBBrz7SUP4"
msg = "https://bitcoinchallenge.codes/"
sig = "H03LFItN9jUXus+nwJd9wriCvTxXki2WxiQ5v5qWXbMjW1gPzK6BGmr4wAm0xsT2Is0/Qv0rXg+OSnehP1e4TvA="

xor = (
    int(k1, 16) ^
    int(k2, 16) ^
    int(hash, 16)
)

xor_str = pc.to_hex(xor)
#xor_str = 'bf3df4cf2312bea094143ade8b3027878fb92b253ade2bd1a52eebb25333676c'
#print(xor_str)
print(wif.private_key_to_wif(xor_str))
