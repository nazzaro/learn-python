from sys import argv


# Aux functions
def key_count(word):
    lettere = "abcdefghijklmnopqrstuvwxyz"
    c = 0
    for letter in word:
        n = 0
        for char in lettere:
            
            n = n + 1

            if char == "s":
                n = 4
                if letter != "s":
                    n = 0
            elif char == "z":
                n = 4
            elif n >= 4:
                n = 1
            if letter == char:
                c += n
    return c
            
        
# Program init
script, filename = argv
res = 0
for line in open(filename):
    word = line.strip()
    res += key_count(word)
print res
