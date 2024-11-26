import random

print(hash("Hello")) #  equal to 2
print(hash("Hello")) #  equal to 1
print(hash("Hellu")) # different/very different from  1 or 2
print(hash( (1, 4, 2, "Hi") ))
print(hash(1372189312))

secret_key = "njd2121321312ofnjmaldko23"

def encrypt_password(password):
    hashed_password = hash(secret_key, password)
    return hashed_password