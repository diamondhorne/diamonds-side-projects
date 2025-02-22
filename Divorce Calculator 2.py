import time
import sys 
import os 
python = sys.executable
script = os.path.abspath(__file__)
os.execl(python, python, script)

#Actual Code *down arrow*
print("Welcome to the Divorce Calculator 2.0")
print("Type any even number to start")
number = int(input())
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0: #initial check to see if user is retarted.
        print("Good job. You are not a disappointment.")
        time.sleep(1) 
    else: 
        print("You are a disappointment. Restarting the program...")
except ValueError:
    print("An error has occured.")

