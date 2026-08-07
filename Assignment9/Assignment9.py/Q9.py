def cal(m,n):
    if n==0:
        return 1
    else:
        return m*cal(m,n-1)
    
m=int(input('enter base:'))    
n=int(input('enter power:'))    

res=cal(m,n)
print(res)