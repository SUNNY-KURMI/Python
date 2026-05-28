# Rock Paper Scissors Game

import random
options = ("rock","paper","scissors")

Comp_input = random.choice(options)
user_input = input("Enter Your Move (rock , paper or scissors or q to quit): ")
# user_score = 0
# comp_score = 0

while True :
    if user_input == "q" :
        user_input = input("Enter Your Move (rock , paper or scissors or q to quit): ")
        break
    elif user_input == "rock":
        if Comp_input == "paper":
            print(Comp_input)
            print(f"Sorry!! You Lost Try Again")
            break
        elif Comp_input == "scissors":
            print(Comp_input)
            print(f"You Won The Game Play Again")
            break
        # elif Comp_input == user_input:
        #     print(f"Game is Tie {Comp_input}")
    elif user_input == "paper":
        if Comp_input == "rock":
            print(Comp_input)
            print(f"You Won The Game Play Again")  
            break
        elif Comp_input == "scissors":
            print(Comp_input)
            print(f"Sorry!! You Lost Try Again")
            break

    elif user_input == "scissors":
        if Comp_input == "paper":
            print(Comp_input)
            print(f"Sorry!! You Lost Try Again")
            break
        elif Comp_input == "rock":
            print(Comp_input)
            print(f"You Won The Game Play Again")
            break
    elif user_input == Comp_input:
        print(f"Game is Tie Moves Are Matched {Comp_input}")
        break
    

        