# prime numbers from 1-200


for x in range (1, 200):
    
    if x>1:
        for i in range (2, x):
            if (x % i) == 0 :
             break
        else:
             print (x)