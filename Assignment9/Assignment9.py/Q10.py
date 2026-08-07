def reverse1(n,rev):
    if n==0:
        return rev
    else:
        d=n%10
        return reverse1(n//10,rev*10+d)
    
n=int(input('enter number'))    
res=reverse1(n,0)   
print(res) 
    

    