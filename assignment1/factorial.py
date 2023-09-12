def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial_iterative(num)}")



# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)

# # Test the function
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"The factorial of {num} is {factorial_recursive(num)}")
