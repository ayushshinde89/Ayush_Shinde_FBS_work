ticket=int(input('enter ticket amount per person:'))

age1=(int(input('enter age of first person:')))

if (age1<12):
    amount1=ticket -(ticket*30/100)
elif (age1>59):
    amount1=ticket -(ticket*50/100)
else:
    amount1=ticket   

p2=(int(input('enter age of second person:')))
if (age1<12):
    amount2=ticket -(ticket*30/100)
elif (age1>59):
    amount2=ticket -(ticket*50/100)
else:
    amount2=ticket   

p3=(int(input('enter age of third person:')))
if (age1<12):
    amount3=ticket -(ticket*30/100)
elif (age1>59):
    amount3=ticket -(ticket*50/100)
else:
    amount3=ticket   

p4=(int(input('enter age of forth person:')))
if (age1<12):
    amount4=ticket -(ticket*30/100)
elif (age1>59):
    amount4=ticket -(ticket*50/100)
else:
    amount4=ticket  

p5=(int(input('enter age of fifth person:')))
if (age1<12):
    amount5=ticket -(ticket*30/100)
elif (age1>59):
    amount5=ticket -(ticket*50/100)
else:
    amount5=ticket 
  
total=amount1+amount2+amount3+amount4+amount5

print(f'total ticket amount is:{total}')


