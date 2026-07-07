import random
captcha=random.randint(1000,9999)

id='1771'
password='rohan'

id1=(input('enter your id:'))
passw=(input('enter your password:'))

print(captcha)

captcha1=int(input('enter captcha:'))

if(id1==id and password==passw):
    if(captcha==captcha1):
        print('login succesfully')

    else:
        print('invalid credentials or captcha')    