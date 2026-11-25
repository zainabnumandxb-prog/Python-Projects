
secret_code = 5
guess = 0 

while guess != secret_code:
    guess = int(input("Enter your guess (between 1 and 5): "))
    if guess != secret_code:
        print("Incorrect guess. Try again.")

print("Congratulations! You've guessed the secret code.")

