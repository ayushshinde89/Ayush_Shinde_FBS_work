str=input('enter a string:')
new_str=''

for i in range(len(str)):
    if i%2==0:
        new_str+=str[i]
print(f'string after removing odd index values:{new_str}')        