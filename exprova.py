from sys import argv


# Aux functions
def key_count(word):
    lettere = "abcdefghijklmnopqrstuwxyz"
    n = 0
    b = 0	
    for char in lettere:
		n = n + 1
		char = click
		if char == lettere:
			b = n
		else:		
			if char == "s":
				n = 4
				b = b + 4

			if char == "z":
				n = 4
				b = b + 4
		
			elif char >= 4:
				n = 1
				b += n

			print b
		
# Program init
script, filename = argv
for line in open(filename):
    word = line.strip()
    key_count(word)
    print word
