#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 4: Generate three different levels of details of the landscape in question 3. The method used to
generate levels of details is expected to preserve important features of the landscape.
"""

from question_3 import *

if __name__ == "__main__":
    # Generate the landscape
    landscape = generate_landscape()
    print("Question 4: generating the landscape from Question 3 with varying levels of detail.")
    # Plot it at the 3 levels of detail first
    
    # LOW quality
    display_landscape(landscape, 0.02)

    # MEDIUM quality
    display_landscape(landscape, 0.04)

    # HIGH quality
    display_landscape(landscape, 0.08)
    while True:
        UserInput = input("To plot again with the default values (delta = [0.02, 0.04, 0.08]), type: 'default'.\n\
To plot with your own values, simply type 'delta' or 'sample_size', then at the next prompt type in your desired value.\n\
To quit this program, type 'quit'\n\
Input: ").lower()

        if UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
            print('Quitting Question 4 program.')
            break
        elif UserInput == 'default':
            # Display the landscape at 3 levels of detail

            # LOW quality
            display_landscape(landscape, 0.02)

            # MEDIUM quality
            display_landscape(landscape, 0.04)

            # HIGH quality
            display_landscape(landscape, 0.08)
        elif UserInput == 'delta':
            try:
                delta = float(input("Delta value: "))
            except ValueError:
                print(e)
                continue
            print("test")
            display_landscape(landscape, delta)
        elif UserInput == 'sample_size':
            try:
                delta = 1/float(input("Sample size: "))
            except ValueError:
                continue
            display_landscape(landscape, delta)
