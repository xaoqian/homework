num=int(input("введите положитeльное число ："))
сумма=0
i=1
while i<=num/2:
    if num%i==0:
        сумма+=i
    i=i+1
if сумма==num:
    print ("yes!")
else:
    print('no')
