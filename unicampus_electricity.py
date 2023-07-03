
import time
currSec = time.time()
currTime = time.ctime(currSec)

def heading():
    topic='''
____________________________________________________________

 ***************** Unicampus Electricity Comapany **********
                Putalisadak, Kathmandu  
\t \t''' + currTime +'''    
                      
____________________________________________________________

'''
    return print(topic)

def getInput():
    customerName =  input(" Enter the Customer Name :  ")
    Address =  input(" Customer Address  : ")
    unitConsumed = int(input(" Unit Consumed : "))
    phone = input(" Enter Phone number : ")
    return (customerName, Address, unitConsumed, phone)
    


def calculate(unit):
    if(unit <=80):
        amount = unit * 4
    elif (unit>80 and unit <=150):
        intitalAmount = 80 * 4 + (unit-80)*10
        discountAmount = ((unit-80)*10) * 0.05
        charge =  intitalAmount *0.05
        amount =  intitalAmount - discountAmount + charge
    elif ( unit>150 and unit<=250):
        intitalAmount = 80*4+(150-80)*10 + (unit - 150)*12
        charge =  ((150-80)*10 ) *0.05  + ((unit - 150)*12) *0.05
        discountAmount = ((150-80)*10) * 0.05 + ((unit-150)*12 )* 0.08
        amount = intitalAmount - discountAmount  + charge
    elif ( unit>250 and unit<=350):
        intitalAmount = 80*4+(150-80)*10 + (250-150)*12 + (unit-250)*15
        charge = ((150-80)*10 ) *0.05  + ((250 - 150)*12) *0.05 + ((unit-250)*15)*0.08
        discountAmount =((150-80)*10) * 0.05 + ((250-150)*12 )* 0.08 + ((unit-250)*15 )*0.1
        amount = intitalAmount - discountAmount  + charge
    elif ( unit>350 and unit<=500):
        intitalAmount = 80*4+(150-80)*10 + (250-150)*12 + (350-250)*15 + (unit-350)*18
        charge =  ((150-80)*10 ) *0.05  + ((250 - 150)*12) *0.05 + ((350-250)*15)*0.08 +((unit-350)*18)*0.1
        discountAmount = ((150-80)*10 )* 0.05 +( (250-150)*12) * 0.08 + ((350-250)*15 )*0.1 + ((unit-350)*18)*0.12
        amount = intitalAmount - discountAmount + charge
    else:
        intitalAmount = 80*4+(150-80)*10 + (250-150)*12 + (350-250)*15 + (500-350)*18 + (unit-500)*20
        charge =  ((150-80)*10 ) *0.05  + ((250 - 150)*12) *0.05 + ((350-250)*15)*0.08 +((500-350)*18)*0.1 +  ((unit-500)*20)*0.12
        discountAmount = ((150-80)*10 )* 0.05 +( (250-150)*12) * 0.08 + ((350-250)*15 )*0.1 + ((500-350)*18)*0.12 + ((unit-500)*20)*0.15
        amount = intitalAmount - discountAmount  + charge
    return amount, intitalAmount,charge, discountAmount


def billformat():
    heading()
    print("Cusomter Name : ",customerName )
    print("Current Address : ", Address)
    print("Total Unit Consumed :" , unitConsumed)
    print("Phone number : ", phone)
    print("total discount", discountAmount)
    print("charge Amount :", charge)
    print()
    print("Mr",customerName,"you  have consumed",unitConsumed,"units, and  yout have  to pay Rs. ", amount)


customerName, Address, unitConsumed, phone= getInput()
amount, intitalAmount,charge, discountAmount = calculate(unitConsumed)
billformat()









