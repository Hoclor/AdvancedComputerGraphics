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

    # Display the landscape at 3 levels of detail

    # LOW quality
    display_landscape(landscape, 0.02)

    # MEDIUM quality
    display_landscape(landscape, 0.04)

    # HIGH quality
    display_landscape(landscape, 0.08)
