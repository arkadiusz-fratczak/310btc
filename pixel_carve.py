#!/usr/bin/python3

from PIL import Image
import base64

img = Image.open('/home/arek/projects/310btc/challenge.png')
data = img.load()
img.close()

red = []
green = []
blue = []
alpha = []

width = 2944
height = 1912
y=310
for x in range(width):
    r = bin(data[x, y][0])[-1]
    g = bin(data[x, y][1])[-1]
    b = bin(data[x, y][2])[-1]
    a = bin(data[x, y][3])[-1]
    red.append(r)
    green.append(g)
    blue.append(b)
    alpha.append(a)
red_channel = ''.join(red)
green_channel = ''.join(green)
blue_channel = ''.join(blue)
alpha_channel = ''.join(alpha)

print("r:", red_channel)
print("rev r:", red_channel[::-1])
print("g:", green_channel)
print("b:", blue_channel)
print("a:", alpha_channel)

xor = bin((
    int(red_channel[::-1], 2)# ^
    # int(green_channel, 2) ^
    # int(blue_channel, 2) ^
    # int(alpha_channel, 2)
    ))[2:]
print("r^g^b^a", xor)
print(bytes.fromhex(hex(int(xor,2))[2:]))
xor = xor.replace('0', '|')
xor = xor.replace('1', '0')
xor = xor.replace('|', '1')
print("~(r^g^b^a):", xor)
print(bytes.fromhex(hex(int(xor,2))[2:]))

# b64 = base64.b64decode(decoded_hex)
# print(b64)

# with open('/home/arek/projects/310btc/alphachannelfile', 'wb') as fout:
#     fout.write(decoded_hex)

#hash
#273e2b95648fd3cbad0d7fe3ed820e783c0b12fdbe29b57bfb2d1f243d92b1a5

#0.1 KzkZxdhRGxB7eX4u1skXkfJ7VB8JfPp7Nfos3jiF7PQUNMh2SHDE
#69630650804510e161cf977024ea41fe630942bb6b9429c804b15ef7e865111801

#0.2 KxPEUpQ5BE75UGRUVjNmf8dQuWsmP9jqL3FUUjavdRW69MEcmg6C
#22bc6dc8b10ca296ccffcab76ade66eb0e3224b334c212098cbe8491f172caeb01

#U2FsdGVkX19Q3I//VCH0U3cVtITZ3ckILJnUcdPX3Gs5qjdF1UjZ3mAftGivtFYD\nN5ZCSkBynnVqBawl4p8wKO0O8zI6D0A1+VEVCUyEvEeNoUfGcS0El9d93vsPxbg7\nD5avufQsScgsk3QEtq9/M4Do32OKFeq00/3NrxWOsMmh3AXmDzuuZ0qmZaI7re16\nFcXIrmPPiQDOHRc7wt0ng6qLiNz7VqESRTdxPOahKFRkWT8sT+Ur2y+2iZ2LEaxN\nM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0os\njH9DqbM6DUptu3HJbAVwXQ==
#Ur2y+2iZ2LEaxN\nM7UZqcPwYgm6FoKOVjnqdeg30R27jc6AoFPyRZ2g8+EJMp3n/pf94oSCLEWkc0os\njH9DqbM6DUptu3HJbAVwXQ==
