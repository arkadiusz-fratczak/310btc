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
