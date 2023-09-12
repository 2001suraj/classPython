def fibonacci_series(n):
    fibonacci_list = [0, 1] 
    for i in range(2, n):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list


n = int(input("Enter the number of Fibonacci numbers to generate: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    series = fibonacci_series(n)
    print("Fibonacci Series:")
    print(series)



    