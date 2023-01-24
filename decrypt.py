import json

with open("key.json", 'r') as f:
    assci = json.load(f);

password = ''.join([chr(i) for i in assci])

print(password)
