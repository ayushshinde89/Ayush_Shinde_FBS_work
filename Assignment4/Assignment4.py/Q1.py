n=int(input("enter a number:"))
i=1
print('even numbers until n')

while(i<=n):
    if i%2==0:
        print(i)
    i+=1

n=int(input('enter a number:')) 

for i in range(1,n+1):
    if i%2==0:
        print(i)