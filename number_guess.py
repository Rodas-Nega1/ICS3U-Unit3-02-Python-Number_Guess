# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks the user to ask a number between 0-9


import constants


def main():
    # this function checks if the user picked a number between 0-9

    # input
    number = int(input("Guess a number between 0-9: "))
    print("")

    # process & output
    if number != constants.ANSWER:
        print("You guessed incorrectly.")

    else:
        print("You guessed correctly!")


if __name__ == "__main__":
    main()
