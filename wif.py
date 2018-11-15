#!/usr/bin/python3

import binascii
import ecdsa
import hashlib
import base58

def wif_to_private_key(wif):
    first_encode = base58.b58decode(wif)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-8]
    return private_key.lower()

def private_key_to_wif(pk):
    # Step 1: here we have the private key
    private_key_static = pk
    # Step 2: let's add 80 in front of it
    extended_key = "80"+private_key_static
    # Step 3: first SHA-256
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    # Step 4: second SHA-256
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    # Step 5-6: add checksum to end of extended key
    final_key = extended_key+second_sha256[:8]
    # Step 7: finally the Wallet Import Format is the base 58 encode of final_key
    wif = base58.b58encode(binascii.unhexlify(final_key))
    return wif

def private_key_to_public(pk):
    pk_bytes = binascii.unhexlify(pk)
    public_key_bytes = ecdsa.SigningKey.from_string(
        pk_bytes, curve=ecdsa.SECP256k1).verifying_key.to_string()
    public_key_hex = binascii.hexlify(public_key_bytes)
    btc_byte = b'04'
    return btc_byte + public_key_hex

k1 = "69630650804510e161cf977024ea41fe630942bb6b9429c804b15ef7e865111801"
k2 = "22bc6dc8b10ca296ccffcab76ade66eb0e3224b334c212098cbe8491f172caeb01"

img = "2f9235c0d7d983da80ac9757f728c0f1ce24ab4763909dda314281510d984e16"
dec2 = "884f383405b2cec233d65dd0a90e6bbb65c361a3165c2eb1cde6d839effaf5af"
hash = "273e2b95648fd3cbad0d7fe3ed820e783c0b12fdbe29b57bfb2d1f243d92b1a5"

address = "39uAUwEFDi5bBbdBm5ViD8sxDBBrz7SUP4"
msg = "https://bitcoinchallenge.codes/"
sig = "H03LFItN9jUXus+nwJd9wriCvTxXki2WxiQ5v5qWXbMjW1gPzK6BGmr4wAm0xsT2Is0/Qv0rXg+OSnehP1e4TvA="

xor = bin((
    int(k1, 16) ^
    int(k2, 16) ^
    int(hash, 16)
    ))[2:]

# xor = xor.replace('0', '|')
# xor = xor.replace('1', '0')
# xor = xor.replace('|', '1')

xor_str = hex(int(xor,2))[2:]
# print(xor_str)
print(private_key_to_wif(xor_str))
# print(private_key_to_public(k2))
# wif = "KxPEUpQ5BE75UGRUVjNmf8dQuWsmP9jqL3FUUjavdRW69MEcmg6C"
# print(wif_to_private_key(address))
