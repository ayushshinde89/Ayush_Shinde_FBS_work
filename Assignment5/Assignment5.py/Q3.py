n=int(input('enter number of passengers:'))
ticket=int(input('enter per person ticket cost: '))

pay=0
for i in range(1,n+1):
    
    age=int(input(f'enter age of passenger {i}:'))
    if age<12:
        pay+=ticket-(ticket*30)/100
    elif age>59:
        pay+=ticket-(ticket*50)/100
    else:
        pay+=ticket
          

print(f'total cost of ticket is {pay}')