def initial_display():
    initial='''    Sunway Tax calculation System
                        Maitidevi
                        2023/07/18
            '''
    print(initial)

# def tax_calcualtion_married(Cust_yearlyincome):
#     if(Cust_yearlyincome<500000):jhv++
            
# def tax_calculation_Unmarried(Cust_yearlyincome):
#         pass

def inputinformation():
    customers= []
    Cust_num = int(input("Enter number of customer :"))
    for i in range (Cust_num):
        customer=[]
        Cust_Name = input ( F" Enter the customer name {i+1}:")
        Cust_address = input("Enter the customer address:")
        Cust_Marital_status = input(" Enter the maritail status (M/U):")
        Cust_Monthlyincome = int(input("Enter the montly salary:"))
        Cust_yearlyincome= Cust_Monthlyincome *12
        customer = [Cust_Name, Cust_address, Cust_Marital_status, Cust_Monthlyincome]
        customers.append(customer)
        if (Cust_Marital_status=='M' or Cust_Marital_status=='m'):
            tax_calcualtion_married(Cust_yearlyincome)
        else:
            tax_calculation_Unmarried(Cust_yearlyincome)
        return customers
            

#function call
initial_display()
inputinformation()


#if (marital_status:= 'M'):
#        calculate_married(yearly_income):
#elif :
#        calculate_unmarried(yearly_income):
#def calculate_married(yearlyincome):
    # if (yearlyincome<500000):