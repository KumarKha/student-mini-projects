import random

attempts = 0
computer = random.randint(1,10)

print("The Computer has picked a number between 1 - 100")
print("Please try and guess the number")

while True:
    player  = int(input("Enter a number between 1-100: "))
    attempts += 1 
    
    if player > computer:
        print("Your guess is too high")
    elif player < computer:
        print("Your guess is too low")
    else:
        print("You guessed the number:",computer)
        print("It took:",attempts,"attempts")
        quit()
        
    
    