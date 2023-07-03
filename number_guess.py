import random
ran = random.randrange(0,100)
for i in range(ran):
    user = int(input("enter the  number : "))
    if(i == user):
        print("win")
        
    else:
        print('loss')
        
