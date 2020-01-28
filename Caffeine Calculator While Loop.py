#!/usr/bin/env python3

print("Caffeine Calculator")
print("===================")
print()

choice = "y"
while choice.lower() == "y":
    caffeine = 95
    cups_of_coffee = int(input("How many cups of coffee did you have today? "))
    mg = (cups_of_coffee * caffeine)
    print()
    print("You have had", mg, "mg of caffeine today.")
    print()
    choice = input("Calculate again? (y/n): ")
    print()
print("Bye!")
