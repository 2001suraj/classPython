intial_display = '''
----------------********-------------

      Sunway Electricity Bill
            Kathamandu
            
----------------********-------------
'''

print(intial_display)

def calculate(unit):
    if(unit<=80):
        amount =  unit*4
    elif (unit>80 and unit <=150):
        amount = 80 * 4 + (unit-80)*10
    elif(unit>150 and unit <=250):
        amount = 80*4+(150-80)*10 + (unit - 150)*15
    else:
        amount =80*4+(150-80)*10+(250-150)*15 + (unit-250) *20
    return amount

unit = int(input("Enter the Consumed Unit : " ))

jan =  calculate(unit)
print("The bill of jan is Rs,",jan)