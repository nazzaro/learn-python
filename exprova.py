from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

def tastiera():
    
    lettere = "abcdefghijklmnopqrstuwxyz"
    
    n = 0

    for click in lettere:
        n = n + 1
    
    if click == "s":
        n = 4
    
    if click == "z":
        n = 4
    
    elif n >= 4:
        n = 0 + 1
             
    print click, n

