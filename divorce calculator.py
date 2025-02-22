import time
import os
import sys

def restart():
    print("Restarting the program...")
    python = sys.executable
    script = os.path.abspath(__file__)
    os.execl(python, python, script)

print("welcome to the divorce calculator, type any even number to start")
kids = "good"
wife = "good"
number = int(input())

if number % 2 == 0:
    print("ok bro dat is even :)")
    time.sleep(2)
    print("so like, how are the kids")
    print("1: good   2: bad")
    kids_input = int(input())  # Convert input to integer
    if kids_input == 1:
        print("ah that's nice.")
        time.sleep(2)
        print("how's the wife?")
        wife_input = input()
        if wife_input == wife:
            print("nice and happy together I see")
            time.sleep(2)
            print("nice talk bro i gtg cya")
            restart()
        else:
            print("get a divorce idk")
            restart()
    else:
        print("since the program is retarded ima just say no")
        restart()
else:
    print("BRO WHAT THE FLIP THATS ODD I HATE YOU")
    restart()
