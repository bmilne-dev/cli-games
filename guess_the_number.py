# a simple number guessing game using randint().

from random import randint

print("guess the number between 1 and 20")
print("you get 5 guesses, and each time I "
    "will tell you whether you're too high "
    "or too low.")

number = randint(1,20)

guess = int(input("Your guess (1-20): "))

n = 0
while n < 5:
    if guess < number:
        print("Too low.")
        guess = int(input("Your guess (1-20): "))
    elif guess > number:
        print("Too high.")
        guess = int(input("Your guess (1-20): "))
    elif guess == number:
        print("You got it!!")
        break
    n += 1
       




