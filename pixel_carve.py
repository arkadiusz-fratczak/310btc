#!/usr/bin/python3

from PIL import Image
import base64

def read_last_bit_of_row(data, row, width):
    red = []
    green = []
    blue = []
    alpha = []
    for col in range(width):
        r = bin(data[col, row][0])[-1]
        g = bin(data[col, row][1])[-1]
        b = bin(data[col, row][2])[-1]
        a = bin(data[col, row][3])[-1]
        red.append(r)
        green.append(g)
        blue.append(b)
        alpha.append(a)
    return(red, green, blue, alpha)

def read_last_bit_of_column(data, col, height):
    red = []
    green = []
    blue = []
    alpha = []
    for row in range(height):
        r = bin(data[col, row][0])[-1]
        g = bin(data[col, row][1])[-1]
        b = bin(data[col, row][2])[-1]
        a = bin(data[col, row][3])[-1]
        red.append(r)
        green.append(g)
        blue.append(b)
        alpha.append(a)
    return(red, green, blue, alpha)

def to_hex(int_number):
    return hex(int_number)[2:]

def to_bytes(int_number):
    return bytes.fromhex(to_hex(int_number))

def negate(int_number):
    to_bin = bin(int_number)[2:]
    to_bin = to_bin.replace('0', '|')
    to_bin = to_bin.replace('1', '0')
    to_bin = to_bin.replace('|', '1')
    return int(to_bin, 2)

img = Image.open('/home/afratczak/projects/310btc/challenge.png')
data = img.load()
img.close()

width = 2944
height = 1912

red, green, blue, alpha = read_last_bit_of_row(data, 310, width)

red_channel_x = ''.join(red)
green_channel_x = ''.join(green)
blue_channel_x = ''.join(blue)
alpha_channel_x = ''.join(alpha)
#print("r_x:", red_channel_x)
#print("g_x:", green_channel_x)
#print("b_x:", blue_channel_x)
#print("a_x:", alpha_channel_x)

red, green, blue, alpha = read_last_bit_of_column(data, 310, height)

red_channel_y = ''.join(red)
green_channel_y = ''.join(green)
blue_channel_y = ''.join(blue)
alpha_channel_y = ''.join(alpha)
#print("r_y:", red_channel_y)
#print("g_y:", green_channel_y)
#print("b_y:", blue_channel_y)
#print("a_y:", alpha_channel_y)

xor = (
    int(red_channel_x[:width], 2) ^
    int(alpha_channel_x[:width], 2)
)

print(to_bytes(xor))
print(to_bytes(negate(xor)))

b64 = base64.b64decode(to_bytes(negate(xor)))
print(b64)

# with open('/home/arek/projects/310btc/alphachannelfile', 'wb') as fout:
#     fout.write(decoded_hex)
