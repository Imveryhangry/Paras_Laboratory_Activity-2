import random

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "gambler" and password == "gambler123":
        print("Login successful!")
        return 20
    else:
        print("Invalid username or password!")
        return 0

def spin(balance):
    while balance > 0:
        print(f"\n--- Current Balance: ${balance} ---")
        try:
            bet = int(input("Enter your bet amount (0 to quit): "))
            if bet == 0: break
            if bet > balance:
                print("You can't bet more than you have!")
                continue
                
            pick = int(input("Pick a number (1-20): "))
            if not (1 <= pick <= 20):
                print("Pick a number between 1 and 20!")
                continue

            result = random.randint(1, 20)
            print(f"The winning number is: {result}")

            if pick == result:
                reward = bet * 10
                balance += reward
                print(f"WINNER! You won ${reward}!")
            else:
                balance -= bet
                print(f"LOSE! Better luck next time.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"Game over. Final balance: ${balance}")

def main():
    current_balance = login_user()
    if current_balance > 0:
        spin(current_balance)

if __name__ == "__main__":
    main()