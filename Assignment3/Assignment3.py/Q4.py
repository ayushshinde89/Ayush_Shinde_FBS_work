a=int(input('enter first side:'))
b=int(input('enter second side:'))
c=int(input('enter third side:'))

if(a+b > c and c+a>b and b+c>a):

    print('based on sides triangle is valid.')

else:
    print('triangle is valid.')