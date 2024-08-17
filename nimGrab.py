# Abhay Prasanna Rao
import random 

print("Welcome to NIMGRAB!")
print()

print("By: Abhay Prasanna Rao")
print()

# Constant values
NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3

# Game flow variables
gameOver = False
currentTurn = 0 # 0 = human, 1 = computer NOTE: Alternate between turns 0 and 1 to play the game

while gameOver == False:  # or we can use (while True)
    x = input("Do you want to [p]lay, [i]nstructions, or [q]uit?: ")
    if x == 'p':
        print("You selected to play!")
        number=random.randint(4,8)
        while number>0:
            if currentTurn==0:               
                print("HUMAN TURN: ", end="")
                print(f"There are {number} items left in the item pool")
                i=0
                while i<number:
                    print("/", end="")
                    i+=1
                print()
                picked=int(input("pick a value between [1,3]: "))
                list=(1,2,3)
                while picked not in list:
                    print("Error! \n")
                    print("Invalid input. Enter a value between [1,3]")
                    picked=int(input("pick a value between [1,3]"))
                print(f"{picked} items taken from the item pool.")
                number=number-picked
                i=0
                while i<number:
                    print("/", end="")
                    i+=1
                if number<=0:
                    print("You lost! Better luck next time.")
                    break
                print()
                print("------------------------------------------------")
                currentTurn+=1
            else:
                print("COMPUTER TURN: ", end="")
                print(f"There are {number} items left in the item pool")
                i=0
                while i<number:
                    print("/", end="")
                    i+=1
                print()
                picked1=random.randint(1,3)
                if number==3:
                    picked1=random.randint(1,2)
                    number-=picked1
                elif number==2:
                    picked1=1
                    number-=picked1
                elif number==1:
                    print("Congrats, you won!")
                    currentTurn-=1
                    break
                else:
                    number-=picked1
                print(f"{picked1} items taken from the item pool")
                i=0
                while i<number:
                    print("/", end="")
                    i+=1
                print()
                print("------------------------------------------------")
                currentTurn-=1 

    elif x == 'i':
        print("You selected to read the instructions! ")
        print()
        print( '''The instructions of the game are thus:\n
            Each player, the human and the computer, take turns removing objects from a pool. \n
            Each player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total.\n
            The game progresses until the last item is removed from the pool.\n
            The player to take the last item loses the game\n''')

    elif x == 'q':
        print()
        print("You selcted to quit!\n")
        print("Have a Good Day! Bye!\n")
        break

    else:
        print("Error! Enter p, q or i ")


