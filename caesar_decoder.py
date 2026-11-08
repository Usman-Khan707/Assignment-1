#!/usr/bin/env python3
"""Caesar brute-forcer: print all 25 possible decryptions of a shifted string."""
import sys

def shift(text, k):
    out = []
    for ch in text:
        if ch.isupper():
            out.append(chr((ord(ch) - 65 - k) % 26 + 65))
        elif ch.islower():
            out.append(chr((ord(ch) - 97 - k) % 26 + 97))
        else:
            out.append(ch)          # leave spaces/punctuation alone
    return "".join(out)

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 caesar_decoder.py 'KDFNHU'")
    ciphertext = " ".join(sys.argv[1:])
    for k in range(1, 26):
        print(f"shift {k:2d}: {shift(ciphertext, k)}")

if __name__ == "__main__":
    main()
