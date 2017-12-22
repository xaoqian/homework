a = int(input('a: '))
b = int(input('b: '))
c = input('введите знак: ')


def arithmetic():

    if c =='+' :
        print(a + b)
    elif c == '-' :
        print(a - b)
    elif c =='*' :
        print(a * b)
    elif c =='/' :
        print(a / b)
    else:
        print('неизвестная операция')
arithmetic()
		
