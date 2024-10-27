from os import getenv

print("API KEY FROM ENV: ", getenv("API_KEY"))
print("PASSWORD FROM ENV: ", getenv("SECRET_PASSWORD"))
print("PASSWORD FROM ENV: ", getenv("INT"), type(getenv("INT")))