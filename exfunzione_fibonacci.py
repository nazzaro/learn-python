def fibonacci(a):
    for a in range(0, a):
        if a == 0:
            return 0
        elif a == 1:
            return 1
        else:
            return fibonacci(a- 1) + fibonacci(a -2)

b = 0
a = int(raw_input(">>> "))
b = line.strip(fibonacci(a))
print b

