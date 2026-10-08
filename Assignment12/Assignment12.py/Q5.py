str=(input('enter a string:'))
count=0

for i in range(len(str)):
    if str[i] in 'aeiouAEIOU':
        count+=1
print(f'number of vowels in string is: {count}')        