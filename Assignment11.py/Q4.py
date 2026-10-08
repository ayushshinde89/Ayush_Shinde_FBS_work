def bubbleSort(li):
    size=len(li)
    for i in range(size-1):
        for j in range(size-1):
            if (li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
               

li=[60,50,40,30,20,10]        
bubbleSort(li)
print(li)
                
print(f'second largest element is {li[-2]}')