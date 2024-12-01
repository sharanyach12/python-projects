print("Welcome to Treasure Island.Your mission is to find the treasure.")
choice1=(input('where do you want to go? Type "left" or "right"'))
if choice1 == "left":
    choice2 = input('what do you want to do? Type "swim" to swim across or type "wait" to wait for the boat')
    if choice2 == "wait":
        choice3 = input("There is a housee with 3 doors .Red,Yellow, and Blue.Which colour do you choose?")
        if choice3 == "red":
            print("It's a room full of fire.Game over!")
        elif choice3 == "Yellow":
            print("You found the treasure.You win!")
        elif choice3 == "Blue":
            print("You entered a room full of beasts.Game over!")
        else:
            print("You chose a door that doesn't exist.Game over!")
            
    else:
        print("you got attacked by angry trout.game over!")
        
else:
    print("you fell into a hole.Game over!")


    