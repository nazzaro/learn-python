n = 0
i= []
c = n 
while n < 999:
    n = n + 1
    
    if n % 3 == 0:
       #print "n:", (n)
       c += n
       #print "Tot_M_3:", c
    elif n % 5 == 0:
       #print "n:", (n)
       c += n 
       #print "Tot_M_5:", c
print c
