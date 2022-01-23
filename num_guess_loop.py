# !/usr/bin/env python3
# Created By: Jedidiah.
# Date: Jan 20, 2022
# This program doesn't let users exit until they get they guess the right number.

import random


def main():
    max_num_string = input("Enter the max number: ")
    try:
        max_num = int(max_num_string)
    except Exception:
        print("Invalid input.")
    else:
        correct_num = random.randint(1, max_num)
        while True:
            user_number = input("Guess a number between 1 and {}: " .format(max_num))
            try:
                user_int = int(user_number)
                if user_int > correct_num:
                    print("Your guess is too high,Try again")

                elif user_int < correct_num:
                    print("Your guess was too low, Try again")

                elif user_int == correct_num:
                    print("You guessed right.")
                    break
            except Exception:
                print("invalid input")

    print("Thanks for playing")


if __name__ == "__main__":
    main()
    