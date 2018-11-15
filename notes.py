#!/usr/bin/python3

from itertools import permutations

row1 = '511b20332328410530'
row2 = '22b0fe52ed0f7a165b'
row3 = '52c7e75112f656fc4b'
str  = row1 + row2 + row3
# key = '678eb9fc'
key = '20181002'
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

new_str = ''.join(new_str)
threes = []
for i in range(0, len(new_str), 3):
    threes.append(new_str[i:i+3])

threes_dec = [int(h, 16) for h in threes]

wordlist = []
with open('/home/arek/projects/310btc/english.txt') as fin:
    for e in fin.readlines():
        wordlist.append(e.rstrip())

threes_word = [wordlist[d - 1] for d in threes_dec[6:]]

print(new_str)
print(threes)
print(threes_dec)
print(threes_word)
print("---")
#cry buyer grain save vault sign lyrics rhythm music fury horror mansion

letters = 'L3 02 7 485 9F'
# ps = permutations(letters)
#
# for p in ps:
#     print(p)

pwd = 'L379F48502'

row1b = '511b20332328410530'.lower()
row2b = '24565158FC2C03A717'.lower()
row3b = '4019AC36A53F4C6B26'.lower()
row4b = '332328410530491312'.lower()
rowxb = '0678eb9fc'
str  = row1b + row2b + row3b + row4b
print(str)
# 511 B20 332 328 410 530
# 245 651 58F C2C 03A 717
# 401 9AC 36A 53F 4C6 B26
# 332 328 410 530 491 312

# Z465/ # 67 8e b9 fc
key = '20181002'
# key = '678eb9fc'
# key = '4776a9fa'

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

new_str = ''.join(new_str)
print(new_str)

threes = []
for i in range(0, len(new_str), 3):
    threes.append(new_str[i:i+3])
print(threes)

threes_dec = [int(h, 16) for h in threes]
print(threes_dec)

wordlist = []
with open('/home/arek/projects/310btc/english.txt') as fin:
    for e in fin.readlines():
        wordlist.append(e.rstrip())

threes_word = [wordlist[d - 1] for d in threes_dec]
print(threes_word)

#cry buyer grain save vault sign lyrics rhythm music fury horror mansion
#debris slim immune lock actual tide gas vapor fringe pole flat glance

pwd2 = '02L3F95847'
