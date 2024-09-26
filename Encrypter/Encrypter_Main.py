import json

with open("Encryption_Codes.json", "r") as files:
    codes = json.load(files)

print(codes)