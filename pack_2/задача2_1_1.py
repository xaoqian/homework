def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number=int(input('введите положительное число：'))
result=factorial(number)
print(result)
