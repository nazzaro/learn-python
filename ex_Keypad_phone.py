lettere = "abcdefghijklmnopqrstuwxyz"
n = 0
  
for click in lettere:
    n = n + 1
   
    if click == "s":
 	    n = 4
    
    elif click == "z":
	    n = 4
    
    elif n >= 4:
	    n = 1

    print click, n
