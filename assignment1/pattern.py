
def pattern():
    num = int(input("Enter the  nunber : "))
    for i in range(0,num):
        for j in range(1,1+i):
            print("*" , end="")
        print()

pattern()
# for i in range(0,5):
    # print("*" *(i+1))