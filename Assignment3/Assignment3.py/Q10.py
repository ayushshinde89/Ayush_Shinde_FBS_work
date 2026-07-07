gender=(input('enter your gender:'))
age=int(input('enter your age:'))

#check conditions
if(gender=='F'):
    if(age>=18):
        print('girl is eligible for marrige.')
else:
    if(age>=21):
        print('male is eligible for marrige')    