from random import randint

print("This in an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()

n = randint(1, 99)
n = 42
tries = 0

while True:
    print("What's your guess between 1 and 99?")
    guess_input = input(">> ")

    if guess_input == "exit":
        print("Goodbye!")
        exit(0)

    try:
        guess = int(guess_input)
    except:
        print("That's not a number.")
        continue

    tries += 1
    if guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        break

if n == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")

if tries == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!")
    print(f"You won in {tries} attempts!")
