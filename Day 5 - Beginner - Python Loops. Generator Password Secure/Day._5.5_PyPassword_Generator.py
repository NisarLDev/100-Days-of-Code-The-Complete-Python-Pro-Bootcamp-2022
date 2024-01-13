# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 25

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(f"This is a Secure Password generated {pwd}")
#Source: 

# https://geekflare.com/es/password-generator-python-code/ Author Bala Priya C.