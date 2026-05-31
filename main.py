import json
import random
from datetime import datetime

# Ask user name
name = input("Enter your name: ")

# Greeting
print(f"\nWelcome {name} to Smart Student Assistant!")

# Read JSON file
with open("tips.json", "r") as file:
    data = json.load(file)

# Menu loop
while True:

    print("\n===== MENU =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Study Tip
    if choice == "1":

        tip = random.choice(data["study_tips"])

        print("\nStudy Tip:")
        print(tip)

        with open("output.txt", "a") as file:
            file.write(f"\nStudy Tip: {tip}")

    # Motivation Quote
    elif choice == "2":

        quote = random.choice(data["motivation_quotes"])

        print("\nMotivation Quote:")
        print(quote)

        with open("output.txt", "a") as file:
            file.write(f"\nMotivation Quote: {quote}")

    # Date and Time
    elif choice == "3":

        now = datetime.now()

        current_time = now.strftime("%d-%m-%Y %H:%M:%S")

        print("\nCurrent Date & Time:")
        print(current_time)

        with open("output.txt", "a") as file:
            file.write(f"\nDate & Time: {current_time}")

    # Exit
    elif choice == "4":

        print("\nThank you for using Smart Student Assistant!")
        break

    else:
        print("\nInvalid Choice! Please try again.")