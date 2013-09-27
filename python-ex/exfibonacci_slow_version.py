def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(raw_input(">>> "))
b= []

for i in range(n):
    b.append(fibonacci(i))
print b
