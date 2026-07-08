id=5650
password=str('Ayush')

for i in range(1,4):
    id1=int(input('enter your id:'))
    passw=str(input('enter your password:'))

    if (id==id1 and password==passw):
        print('login successful')
        break
    else:
        print('re enter id and password')