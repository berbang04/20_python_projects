import string,secrets

pwd_length=12
letters=string.ascii_letters
digits=string.digits
special_chars=string.punctuation
alphabet=letters+digits+special_chars

password=''
for i in range(pwd_length):
    password+=''.join(secrets.choice(alphabet))
print(password)    
    
