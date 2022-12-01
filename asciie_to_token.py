import json

with open("asciie_token.json", 'r') as f:
    ascii_token = json.load(f);

token = ''.join([chr(i) for i in ascii_token]);

print(token);
