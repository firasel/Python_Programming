import hashlib

email = "md@gmail.com"
pwd = "MyPass"
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = "md@gmail.com"
your_password = "MyPass"

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()

if email == your_email and pwd_hash == hashed_your_password:
    print("Right user")
else:
    print("Worng password")

print(pwd_hash, hashed_your_password)
