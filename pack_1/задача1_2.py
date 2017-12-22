def number():
    a = int(input())
    print(a)
    if a == '0':
        print('error')
    elif a == '1':
        print(1)
    else:
        for i in range(1, a):
            print(i)
number()
	
