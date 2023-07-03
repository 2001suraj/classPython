radius = int(input("Enter the radius : "))
pie =  3.14

def areaCircle(radius):
    solution = pie * pow(radius,2)
    return  solution
area =  areaCircle(radius)

def cirCircle(radius):
    solution =  2 * pie *radius
    return solution

cir = cirCircle(radius) 

print( "Area = ",area)
print("Circumference = ",cir)
