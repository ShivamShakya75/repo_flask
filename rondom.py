import random
randnumber = random.randint(1,100)
userguess = none
guesses = 0

while(userguess !=randnumber):
    userguess = int(input("enter your guess: ")
            guesses +=1
            if (userguess == randnumber):
                print("you guesses it right")

            else:
                if(userguess>number):
                    print("you guesses it wrong! enter a smaller number")
                else:
                    print("you guesses it wrong! enter a large number")

print(f"you guessed the number is {guesses} guesses")

