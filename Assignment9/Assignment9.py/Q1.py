def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def sum_of_series(n):
    if n == 0:
        return 0
    else:
        return fact(n) + sum_of_series(n-1)
    
n=int(input('enter number:'))
res=sum_of_series(n)
print(f"Sum of the series is: {res}")
    