import time
import sys 
import os
import random

# Actual Code *down arrow*
print("Welcome to the Divorce Calculator 2.0")
name = input("Name:")
married = input("Are you married?:")
if married == "no":
    print("This will instead determine the chance of your parents getting a divorce")
    print("Okay, " + name + " Welcome to the dumbass checkpoint. Type any even number to start")
    number = int(input())
    try:
        if number % 2 == 0:
            print("Good job " + name + ". You are not a disappointment.")
            mother = input("So, what's your mother's name?")
            print(mother + ". okay.")
            father = input("Same about your dad. What's his name?")
            print(father + ".. okay.")
            time.sleep(1)
            print("I can assure you those two TOTALLY matter in this calculation. This may take a minute as it uses AI to do all calculations.")
            time.sleep(1) 
            print("Calculating.") 
            time.sleep(1)
            print("Calculating..")
            time.sleep(1)
            print("Calculating...")
            percentage = random.randint(0, 100)
            print("Your chance of your parents getting a divorce is " + str(percentage) + "%")
        else:
            print("You are a disappointment " + name + ". Quitting...")
    except ValueError:
        print("An error has occurred.")
else:
    print("Okay, " + name + " Welcome to the dumbass checkpoint. Type any even number to start") #super hard question
    number = int(input())
    try:
        if number % 2 == 0: # initial check to see if user is okay in the head.
            print("Good job " + name + ". You are not a disappointment.")
            time.sleep(1) 
            print("Calculating.") 
            time.sleep(1)
            print("Calculating..")
            time.sleep(1)
            print("Calculating...")
            percentage = random.randint(0, 100)
            print("Your chance of getting a divorce is " + str(percentage) + "%")
        else: 
            print("You are a disappointment " + name + ". Quitting...")
    except ValueError:
        print("An error has occurred. Please enter a valid number.")

