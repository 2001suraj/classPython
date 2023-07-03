topHeading='''
____________________________________________________________

            Sunway Electricity Bill
                Kathmadnu, Nepal
____________________________________________________________

'''


def calculate(unit):
   
    
    if(unit <=80):
        amount = unit * 4
    elif (unit>80 and unit <=150):
        intitalAmount = 80 * 4 + (unit-80)*10
        discountAmount = (((unit-80)*10) * 2)/100
        print("discount amount ", discountAmount)
        amount =  intitalAmount - discountAmount 
    elif ( unit>150 and unit<=250):
        intitalAmount = 80*4+(150-80)*10 + (unit - 150)*15
        discountAmount = (((unit-80)*10) * 2)/100 + (((unit-150)*15 )* 5)/100
        print("discount amount ", discountAmount)
        
        amount = intitalAmount - discountAmount 
    elif ( unit>250 and unit<=350):
        intitalAmount = 80*4+(150-80)*10 + (250-150)*15 + (unit-250)*18
        discountAmount = (((unit-80)*10) * 2)/100 + (((250-150)*15 )* 5)/100 + (((unit-250)*18 )*10)/100
        print("discount amount ", discountAmount)
        
        amount = intitalAmount - discountAmount 
    elif ( unit>350 and unit<=500):
        intitalAmount = 80*4+(150-80)*10 + (250-150)*15 + (350-250)*18 + (unit-350)*20
        discountAmount = (((unit-80)*10 )* 2)/100 +( ((250-150)*15) * 5)/100 + (((350-250)*18 )*10)/100 + (((unit-350)*20)*12)/100
        print("discount amount ", discountAmount)
        
        amount = intitalAmount - discountAmount 
    else:
        intitalAmount = 80*4+(150-80)*10 + (250-150)*15 + (350-250)*18 + (500-350)*20 + (unit-500)*22
        discountAmount = (((150-80)*10 )* 2)/100 +( ((250-150)*15) * 5)/100 + (((350-250)*18 )*10)/100 + (((500-350)*20)*12)/100 + (((unit-500)*22)*15)/100
        print("discount amount ", discountAmount)
        
        amount = intitalAmount - discountAmount 
        
    return amount


sNmae =  input(" Enter the Customer Name :  ")
cAdress =  input(" Customer Address  : ")
unitConsumed = int(input(" Unit Consumed : "))


# finalValue = "Mr",sNmae,"you  have consumed",unitConsumed,"units ,and  yout have  to pay ", totalAmount

calculated  = calculate(unitConsumed)
print(topHeading)
print("Cusomter Name : ",sNmae)
print("Current Address : ", cAdress)
print("Unit Consumed :" , unitConsumed)
print()
print("Mr",sNmae,"you  have consumed",unitConsumed,"units, and  yout have  to pay Rs. ", calculated)






