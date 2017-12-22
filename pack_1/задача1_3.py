a = int(input('a: '))
if a == '0':
        print('error')
elif a =='1' :
        print(' yes ')
else:

    for i in range(2,a) :
        if a % i == 0:
            break
        elif a % i != 0:
            print('yes!')
