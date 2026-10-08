str=input('enter a string:')
words=str.split()
word_count={}
for i in words:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1

for word,count in word_count.items():
    print(f'{word}: {count}')