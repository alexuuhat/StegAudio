#!/usr/bin/env python3
"""
StegAudio - Alexuuhat
"""

import wave
import argparse
import hashlib
import sys


HELP = """
Usage:
  python3 decrypt.py -i encoded.wav
  python3 decrypt.py -i encoded.wav --key "1234"

Notes:
  • Works with both locked (encrypted) and normal messages
  • If key is wrong → output will be garbage
"""


def decrypt_message(encrypted_bytes, key):
    """Decrypt using XOR with SHA-256 hashed key"""
    hashed = hashlib.sha256(key.encode()).digest()
    decrypted = bytearray()

    for i, byte in enumerate(encrypted_bytes):
        decrypted.append(byte ^ hashed[i % len(hashed)])

    try:
        return decrypted.decode()
    except UnicodeDecodeError:
        return "[!] Wrong key or corrupted message"


def decode_audio(input_file, key=None):
    try:
        with wave.open(input_file, 'rb') as audio:
            frames = bytearray(audio.readframes(audio.getnframes()))
    except wave.Error:
        print("[!] Error: Not a valid WAV file")
        sys.exit(1)

    # Extract bits until EOF marker
    bits_list = []
    for byte in frames:
        bits_list.append(str(byte & 1))
        if ''.join(bits_list[-16:]) == "1111111111111110":
            bits_list = bits_list[:-16]
            break

    bits = ''.join(bits_list)

    if len(bits) % 8 != 0:
        print("[!] Error: Invalid or corrupted audio")
        sys.exit(1)

    # Convert binary → bytes
    extracted_bytes = bytearray()
    for i in range(0, len(bits), 8):
        extracted_bytes.append(int(bits[i:i+8], 2))

    # If key provided (locked message)
    if key:
        print("[+] Key mode enabled → decrypting…")
        return decrypt_message(extracted_bytes, key)

    # Without key (normal text)
    try:
        return extracted_bytes.decode()
    except UnicodeDecodeError:
        return "[!] Message appears encrypted. Use correct key."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-i', '--input', required=False)
    parser.add_argument('--key', required=False)
    parser.add_argument('--help', action='store_true')

    args = parser.parse_args()

    if args.help or not args.input:
        print(HELP)
        sys.exit(0)

    message = decode_audio(args.input, args.key)

    print("\n==========================")
    print(" Extracted Message:")
    print("==========================")
    print(message)
    print("==========================\n")
