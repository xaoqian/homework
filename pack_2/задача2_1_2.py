def factorial(n):
    result = n
    for i in range(1,n):
        result *=i
    return result

number = int(input('введите положительное число：'))
result = factorial(number)
print(result)
