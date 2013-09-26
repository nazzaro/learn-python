def fibonacci(n):
    b = []
    
    for i in range(n+1):
        if i == 0:
            b.append(0)
        elif i == 1:
            b.append(1)
        else:
            b.append(b[i - 1] + b[i - 2])
            # fibonacci(n - 1) + fibonacci(n - 2)
            
    return b


a = int(raw_input(">>> "))   
print fibonacci(a)
