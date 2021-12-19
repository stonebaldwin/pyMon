import random

user_input = input("Select a choice (Charmander, Squirtle, or Bulbasaur): ")

options = ["Charmander", "Squirtle", "Bulbasaur"]

computer_input = random.choice(options)

if user_input == computer_input:
    print("It's a Tie! Try Again.")
else:
    if user_input == "Charmander" and computer_input == "Bulbasaur":
        print("The Computer Picked Bulbasaur, You Win!")
    
    if user_input == "Squirtle" and computer_input == "Charmander":
        print("The Computer Picked Charmander, You Win!")

    if user_input == "Bulbasaur" and computer_input == "Squirtle":
        print("The Computer Picked Squirtle, You Win!")

    
    if user_input == "Charmander" and computer_input == "Squirtle":
        print("The Computer Picked Squirtle, You Lose!")
    
    if user_input == "Squirtle" and computer_input == "Bulbasaur":
        print("The Computer Picked Bulbasaur, You Lose!")

    if user_input == "Bulbasaur" and computer_input == "Charmander":
        print("The Computer Picked Charmander, You Lose!")