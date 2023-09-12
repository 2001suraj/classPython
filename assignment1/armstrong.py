
0,1,153,370,371

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    return armstrong_sum == num



input_number = int(input("Enter a number: "))
if is_armstrong_number(input_number):
    print("It's an Armstrong number!")
else:
    print("It's not an Armstrong number.")

