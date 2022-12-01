import json

with open("ascii_token.json", 'r') as f:
    ascii_token = json.load(f);

token = ''.join([chr(i) for i in ascii_token]);

print(token);