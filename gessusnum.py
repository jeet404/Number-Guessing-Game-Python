import random

MAX_CHANCE = 5
difficulty_levels = [
    ("   1. Low    (Number From 1 to 10)                   ",10), 
    ("   2. Medium (Number From 1 to 50)                   ",50),
    ("   3. High   (Number From 1 to 100)                  ",100)]

print("*********************************************************")
print("**        Welcome to the Guess the Number Game         **")
print("** Here is the total three levels available as follows **")
[print(f"**{difficulty_levels[i][0]}**") for i in range(len(difficulty_levels))]
print("*********************************************************")
print("\n\n")

while True:
    print("*********************************************************")
    print("**              Choose Difficulty Level                **")
    print("*********************************************************")
    [print(f"**{difficulty_levels[i][0]}**") for i in range(len(difficulty_levels))]
    print("*********************************************************")

    ch = int(input("Enter Your Choice : "))
    random_number = random.randint(1, difficulty_levels[ch-1][1])
    
    print(f"\nNumber of guesses is limited to only {MAX_CHANCE} times... \n")
    number_of_guesses = 0
    while(number_of_guesses<MAX_CHANCE):
        guess_number = int(input("Guess the number : "))
        if guess_number < random_number:
            print("Your Entered Number is Less Then Desired Number. \n")
        elif guess_number > random_number:
            print("Your Entered Number is Grater Then Desired Number. \n")
        else:
            print("\nCongratulations You Won\n",number_of_guesses+1,"Guesses You Took to Finish. \n")
            break
        number_of_guesses += 1
        print(MAX_CHANCE-number_of_guesses,"Chances left\n")
    else:
        print("Sorry, you loss the game..\nDisired Number is :", random_number)
    print() if input("Do You Want to Play Again?\n(Y/N) : ") in ["Y", "y"] else exit() 