
def greatest(a,b,c):
    if(a>b and  a>c):
        print(" A the greatest number")  
    elif (b>c and b>a):
         print(" B the greatest number")
    else :
        print(" C the greatest number")
        
        
def nestedd(a,b,c):
    if(a>b):
        if(a>c):
         print(" A the greatest number") 
        elif (b>c):
          if(b>a):
             print(" B the greatest number")
    else:
        print(" C the greatest number")
        
            
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))

value =  greatest("Simple  : ",a,b,c)   
value1 =  nestedd( "Nested : ",a,b,c)   
        


