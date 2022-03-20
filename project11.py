num = 18
number_of_guesses = 1
print("The number is between 1 to 60 and divisible by 2 and 3")
print("You have 6 guesses")

while (number_of_guesses<=6):
    guess = int(input("Enter the number :\n"))
    if guess>18:
        print("The number you entered is too high. Guess again!")
    elif guess<18:
        print("The number you enter is too low. Guess again!")
    else:
        print("Hurray! You guessed it right")
        print("It took you", 6-number_of_guesses, "guesses to guess the number.")
        break
    print("Number of Guesses left =", 6-number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if number_of_guesses>6:
    print("Game Over!")
    