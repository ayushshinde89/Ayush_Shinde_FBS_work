n=int(input("enter a number:"))
 
if(n<=1):
    print('number is not prime nor composite')

else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not prime")
            break
    else:
        print(f'{n} is prime')
        