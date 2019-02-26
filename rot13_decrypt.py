#!/usr/bin/env python

def rot13decrypt(t):
    a_number = ord("A")
    z_number = ord("Z")
    decrypt_number = ord(t) - 13
    if decrypt_number == a_number:
        return chr(decrypt_number)
    elif a_number < decrypt_number:
        return chr(decrypt_number)
    elif a_number > decrypt_number:
        different = (a_number - decrypt_number)
        return chr(z_number - different + 1)

g = (rot13decrypt(t)for t in "enter_the_flag_you_want_to_decrypt")
print("".join(g))
