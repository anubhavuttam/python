# Game Idea

# It’s like rock-paper-scissors but with:

# Snake 🐍

# Water 💧

# Gun 🔫

# Rules:

# Snake drinks water → Snake wins

# Gun kills snake → Gun wins

# Water douses gun → Water wins

# Same choice → Draw

import random

choices = ["snake", "water", "gun"]

user = input("Enter snake, water, or gun: ").lower()

computer = random.choice(choices)

print(f"Computer chose: {computer}")

if user not in choices:
    print("Invalid choice! Please enter snake, water, or gun.")


if user == computer:
    print("it's a draw !")
elif user=="snake":
    if computer=="water":
        print("You win! Snake drinks water.")
    else:
        print("You loose! Gun kills snake.")
elif user=="water":
    if computer=="snake":
        print("You loose! Snake drinks water.")
    else:
        print("You win! Water douses gun.")
elif user=="gun":
    if computer=="snake":
        print("You win! Gun kills snake.")
    else:
        print("You loose! Water douses gun.")

