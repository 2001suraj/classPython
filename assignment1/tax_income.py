def initialdisplay():
    displayInfo = '''
    -----------------------------------------------------------------------
    
                Sunway Tax Calculation System
                    Maitedevi, Kathmandu
                        2023- july - 12
    
    -----------------------------------------------------------------------
    
    '''
   
    return displayInfo

def Marrriedcalculate(income):
    annualIncome = income *12

    if(annualIncome <= 600000):
            taxper = 0.01
            taxamt=annualIncome *taxper
            netIncome = annualIncome+ taxamt
    elif(annualIncome >=500000 and annualIncome <=800000):
            taxper = 0.1
            taxamt=0.01*600000 + ((annualIncome-800000) * taxper)
            netIncome =  annualIncome -taxamt
    elif( annualIncome >=800000 and annualIncome <= 1100000):
            taxper = 0.2
            taxamt=0.01*600000 + 0.1*800000 +((annualIncome-1100000) * taxper)
            netIncome =  annualIncome - taxamt
    elif(annualIncome >=1100000 and annualIncome <= 2000000):
            taxper = 0.3
            taxamt=0.01*600000 + 0.1*800000 +0.2*1100000 +((annualIncome-2000000) * taxper)
            netIncome =  annualIncome - taxamt
    elif(annualIncome >=2000000 and annualIncome <= 5000000):
            taxper = 0.36
            taxamt=0.01*600000 + 0.1*800000 +0.2*1100000 +0.3*2000000+((annualIncome-5000000) * taxper)
            netIncome =  annualIncome - taxamt
    else:
            taxper = 0.39
            taxamt=0.01*600000 + 0.1*800000 +0.2*1100000 +0.3*5000000+((annualIncome-5000000) * taxper)
            netIncome =  annualIncome - taxamt
    return (taxper,annualIncome,taxamt, netIncome) 
            
def unMarriedCalculation(income):
    annualIncome = income *12
    
    
    if(annualIncome <= 500000):
                taxper = 0.01
                taxamt = annualIncome *taxper
                netIncome = annualIncome- taxamt
    elif(annualIncome >=500000 and annualIncome <=700000):
                taxper = 0.1
                taxamt =  0.01*500000 + ((annualIncome-700000) * taxper)
                netIncome =  annualIncome -taxamt
    elif( annualIncome >=700000 and annualIncome <= 1000000):
                taxper = 0.2
                taxamt = 0.01*500000 + 0.1*700000 +((annualIncome-1000000) * taxper)
                netIncome =  annualIncome -taxamt
    elif(annualIncome >=1000000 and annualIncome <= 2000000):
                taxper = 0.3
                taxamt= 0.01*500000 + 0.1*700000 +0.2*1000000 +((annualIncome-2000000) * taxper)
                netIncome =  annualIncome -taxamt
    elif(annualIncome >=2000000 and annualIncome <= 5000000):
                taxper = 0.36
                taxamt=0.01*500000 + 0.1*700000 +0.2*1000000 +0.3*2000000+((annualIncome-5000000) * taxper)
                netIncome =  annualIncome - taxamt
    else:
                taxper = 0.39
                taxamt=0.01*500000 + 0.1*700000 +0.2*1000000 +0.3*5000000+((annualIncome-5000000) * taxper)
                netIncome =  annualIncome - taxamt

    return (taxper,annualIncome,taxamt, netIncome)           

def getInput():
    customers= []
    Cust_num = int(input("Enter number of customer :"))
    for i in range (Cust_num):
        customer=[]
        Cust_Name = input ( F" Enter the customer name {i+1}:")
        Cust_address = input("Enter the customer address:")
        Cust_Marital_status = input(" Enter the maritail status (M/U):")
        Cust_Monthlyincome = int(input("Enter the montly salary:"))
        customer = [Cust_Name, Cust_address, Cust_Marital_status, Cust_Monthlyincome]
        customers.append(customer)
        if (Cust_Marital_status=='M' or Cust_Marital_status=='m'):
            Marrriedcalculate(Cust_Monthlyincome)
        else:
            unMarriedCalculation(Cust_Monthlyincome)
        return customers
    return customername, address, marriedStatus, Cust_Monthlyincome, customer
    
    # customername =  input("Enter the client Name :")
    # address =  input("Enter the Address : ")
    # marriedStatus= input("Enter the Married Status : ")
    # income = int(input("Enter the Monthly Income : Rs ")) 
       



customername, address, marriedStatus, income ,customer= getInput()          
taxper, annualIncome , taxamt, netIncome = Marrriedcalculate(income) 


def output():
    displayInfo = f'''
    {initialdisplay()}
    Mr/Mrs. {customername} ,   your  yearly tax Amount {taxamt} 
    Montly Income = Rs {income}
    Annual Icome = Rs {annualIncome}
    Net Income = Rs { netIncome}
    {customer}
    '''
    return displayInfo

print(output())