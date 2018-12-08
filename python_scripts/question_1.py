#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 1: Construct a parametric curve to represent a heart-shaped object. Produce both a scaled-up
    and a scaled-down version of the object by modifying the control points of the parametric curve.
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Set up the visualisation settings
vis_config = VisMPL.VisConfig(ctrlpts=False) # Set ctrlpts=True to plot control points with the curves
vis_comp = VisMPL.VisCurve2D(vis_config)

#
# Initial Heart
#
def generate_heart():
    # Create a B-Spline curve
    heart = BSpline.Curve()

    # Set up the control points
    heart.degree = 3
    heart.ctrlpts = [[0, -20], [25, 5], [17, 20], [5, 19], [0.2, 13], [0, 8], [-0.2, 13], [-5, 19], [-17, 20], [-25, 5], [0, -20]]

    # Auto-generate knot vector
    heart.knotvector = utilities.generate_knot_vector(heart.degree, len(heart.ctrlpts))

    # Return the heart
    return heart

def display_heart(heart, scale=1):
    # Scale the heart up/down according to the input scale
    heart.ctrlpts = [[scale*x, scale*y] for x,y in heart.ctrlpts]

    # Set evaluation delta
    heart.delta = 0.001

    # Evaluate curve
    heart.evaluate()

    # Draw the control point polygon and the evaluated curve
    heart.vis = vis_comp
    heart.render()
    # Downscale the heart again to make sure the control points are not permanently altered
    heart.ctrlpts = [[x/scale, y/scale] for x,y in heart.ctrlpts]

if __name__ == "__main__":
    # Create the heart
    heart = generate_heart()
    
    print("Question 1: generating and displaying a heart at different scales.")
    # Display the heart at three scales
    
    # ORIGINAL size
    display_heart(heart, 1)

    # scaled UP
    display_heart(heart, 2)

    # scaled DOWN
    display_heart(heart, 0.5)
    while True:
        UserInput = input("To display again with the default values (scale = [1, 2, 0.5]), type: 'default'.\n\
To display with your own scale, simply type 'scale', then at the next prompt type in your desired value.\n\
To quit this program, type 'quit'\n\
Input: ").lower()

        if UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
            print('Quitting Question 4 program.')
            break
        elif UserInput == 'default':
            # Display the heart at three scales

            # LOW quality
            display_heart(heart, 1)

            # MEDIUM quality
            display_heart(heart, 2)

            # HIGH quality
            display_heart(heart, 0.5)
        elif UserInput == 'scale':
            try:
                scale = float(input("Scale value: "))
            except ValueError:
                print(e)
                continue
            display_heart(heart, scale)
