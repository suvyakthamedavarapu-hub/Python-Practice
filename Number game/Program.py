import random
secret = random.randrange(1,100)
chance =0
while chance < 5:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret:
        print("You won!")
        break
    if guess < secret:
        print("Go Higher!")
    if guess > secret:
        print("Go Lower!")

    chance += 1
    if chance == 5:
        print("Game Over.. The answer was ",secret)
