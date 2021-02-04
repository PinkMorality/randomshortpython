import random

lower_limit = int(input("Enter lower limit for guess. "))
upper_limit = int(input("Enter upper limit for guess. "))

number = random.randint(lower_limit,upper_limit)
print(f"Guess the number between {lower_limit} and {upper_limit}. ")

while True:
    guess = int(input("Guess a number. "))
    if guess == number:
        print("You got the correct number!")
        break
    elif guess > upper_limit or guess < lower_limit:
        print("You guessed out of bounds.")
    elif guess > number:
        print("You guessed to large.")
    elif guess < number:
        print("You guessed to small.")