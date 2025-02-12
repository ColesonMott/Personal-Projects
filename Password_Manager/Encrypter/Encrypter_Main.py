# Version: 1.0
import json, random, os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "Encryption_Codes.json")


with open(file_path, "r") as f:
    load = json.load(f)

codes = load


def encrypt(text, load=codes):
    key = random.choice(list(load))
    load = load.get(key)
    encrypted = ""
    for char in text:
        if char in load:
            encrypted += load[char]
            encrypted += load["special"]
        else:
            encrypted += char
    encrypted += key
    return encrypted


def decrypt(text, numLength=6, load=codes):
    key = text[-numLength:]
    load = load.get(key)
    text = text[:-numLength]
    decrypted = ""

    for i in range(0, len(text), numLength+1):
        num = text[i:i+numLength]
        if num in load.values():
            for char in load:
                if load[char] == num:
                    decrypted += char
        else:
            decrypted += num

    return decrypted

