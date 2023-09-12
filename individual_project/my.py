import random

def ComputerRandomNumberGen():
    return random.randint(1, 3)

def displayComputerChoice(computer_choice):
    choices = {
        1: 'R',
        2: 'P',
        3: 'S'
    }
    print(f"Computer has chosen: {choices[computer_choice]}")

def displayUserChoice():
    user_choice = int(input("Enter your choice: 1 for Rock, 2 for Paper, 3 for Scissors: "))
    choices = {
        1: 'R',
        2: 'P',
        3: 'S'
    }
    print(f"You have chosen: {choices[user_choice]}")
    return user_choice

def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'TIE'
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return 'USER'
    else:
        return 'COMPUTER'

def display_static_Info(result, user_name, user_address, user_phone):
    with open("result.txt", "w") as file:
        file.write(f"Winner: {result}\n")
        file.write(f"User Name: {user_name}\n")
        file.write(f"User Address: {user_address}\n")
        file.write(f"User Phone: {user_phone}\n")

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    user_name = input("Enter your name: ")
    user_address = input("Enter your address: ")
    user_phone = input("Enter your phone number: ")

    while True:
        user_choice = displayUserChoice()
        computer_choice = ComputerRandomNumberGen()
        displayComputerChoice(computer_choice)

        winner = DetermineWinnerOfRPS(user_choice, computer_choice)

        if winner == 'TIE':
            print("It's a tie! Play again.")
        else:
            print(f"{winner} wins the game!")
            display_static_Info(winner, user_name, user_address, user_phone)
            break


main()
