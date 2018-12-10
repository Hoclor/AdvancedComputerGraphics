#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 4: Generate three different levels of details of the landscape in question 3. The method used to
generate levels of details is expected to preserve important features of the landscape.
"""

from question_3 import *

def default():
    # Plot the landscape at the 3 levels of detail first
    landscape = generate_landscape()

    # LOW quality
    print('Displaying LOW quality landscape')
    display_landscape(landscape, 0.08)

    # MEDIUM quality
    print('Displaying MEDIUM quality landscape')
    display_landscape(landscape, 0.04)

    # HIGH quality
    print('Displaying HIGH quality landscape')
    display_landscape(landscape, 0.02)


if __name__ == "__main__":
    # Generate the landscape
    print("Question 4: generating the landscape from Question 3 with varying levels of detail.")
    default()

    landscape = generate_landscape()

    while True:
        UserInput = input("To plot again with the default values (delta = [0.02, 0.04, 0.08]), type: 'default'.\n\
To plot with your own values, simply type 'delta' or 'sample_size', then at the next prompt type in your desired value.\n\
To quit this program, type 'quit'\n\
Input: ").lower()

        if UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
            print('Quitting Question 4 program.')
            break
        elif UserInput == 'default':
            # Run the default function
            default()
        elif UserInput == 'delta':
            try:
                UserInput2 = input("Delta value: ")
                delta = float(UserInput2)
            except ValueError:
                print('Unexpected input: {}'.format(UserInput2))
                continue
            display_landscape(landscape, delta)
        elif UserInput == 'sample_size':
            try:
                UserInput2 = input("Sample size: ")
                delta = 1/float(UserInput2)
            except ValueError:
                print('Unexpected input: {}'.format(UserInput2))
                continue
            display_landscape(landscape, delta)
