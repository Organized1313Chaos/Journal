from cryptography.fernet import Fernet
lookup = {'hello': "I don't know", "iugujk kn": "adas"} 

key = Fernet.generate_key()

f = Fernet(key)
ans = {}

for k,v in lookup.items():  
    ans[k] = f.encrypt(v.encode('utf-8')).decode('utf-8')
# ans = {k: f.encrypt(v.encode('utf-8')).decode('utf-8') for k, v in lookup}

if key:
    f = Fernet(key)
    for k,v in ans.items():
        res = f.decrypt(v).decode('utf-8')
        print(res)
