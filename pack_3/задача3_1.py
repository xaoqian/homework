parentheses = {"(": ")", "{": "}", "[": "]"}
star = []
f = input("введите скопки:")
def determine():
    if f in parentheses:
        if f == "(" or "(" or "[" or "{":
            print('validity')
            for i in star:
                star.append(i)
                print(star)
        elif f == "[)" or "({[)]" or "{{{":
            print('error')
        else:
            print('неизвестно')
    else:
        print('неизвестно')
determine()
