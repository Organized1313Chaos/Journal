# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
print(token)

# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext
print(d)
