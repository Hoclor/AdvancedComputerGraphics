#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 1: Construct a parametric curve to represent a heart-shaped object. Produce both a scaled-up
    and a scaled-down version of the object by modifying the control points of the parametric curve.
"""

from geomdl import BSpline
from geomdl import utilities
from geomdl import Multi
from geomdl.visualization import VisMPL

# Heart creation function
def generate_heart(scale=1):
    # Create a B-Spline curve
    heart = BSpline.Curve()

    # Set up the control points
    heart.degree = 3
    heart.ctrlpts = [[0, -20], [25, 5], [17, 20], [5, 19], [0.2, 13], [0, 8], [-0.2, 13], [-5, 19], [-17, 20], [-25, 5], [0, -20]]


    # Scale the heart up/down according to the input scale
    heart.ctrlpts = [[scale*x, scale*y] for x,y in heart.ctrlpts]

    # Auto-generate knot vector
    heart.knotvector = utilities.generate_knot_vector(heart.degree, len(heart.ctrlpts))

    # Set the evaluation delta
    heart.delta = 0.001

    # Evaluate the curve
    heart.evaluate()

    # Return the heart curve
    return heart

# Heart/multi-curve display function
def display_curve(curve, ctrlpts=True):
    # Generate the visualisation configuration
    vis_config = VisMPL.VisConfig(legend=False, ctrlpts=ctrlpts)
    vis_comp = VisMPL.VisCurve2D(vis_config)
    # Draw the control point polygon and the evaluated curve
    curve.vis = vis_comp
    curve.render()

# Display the heart at three scales on the same plot
def default():
    # Create the heart
    heart = generate_heart()
    
    print("Question 1: generating and displaying a heart at different scales.")
    # Display the heart at three scales
    heart_1 = generate_heart(0.5)
    heart_2 = generate_heart(1)
    heart_3 = generate_heart(2)

    # Set up a MultiCurve to allow displaying all three hearts on one plot
    three_hearts = Multi.MultiCurve()
    three_hearts.delta = 0.001
    three_hearts.add([heart_1, heart_2, heart_3])
    # Display the MultiCurve
    display_curve(three_hearts)

if __name__ == "__main__":
    # First display the heart at three scales
    default()

    while True:
        print()
        UserInput = input("To display again with the default values (scale = [0.5, 1, 2]), type: 'default'.\n\
To display with your own scale, simply type your desired scale (> 0).\n\
To display several scales in one plot, with control points, type 'multi_points', followed by your desired scales (one per line), followed by 'done'\n\
To display several scales in one plot, without control points, type 'multi_no_points', then proceed as above\n\
To quit this program, type 'quit'\n\
Input: ").lower()

        if UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
            # Exit the program
            print('Quitting Question 1 program.')
            break
        elif UserInput == 'default':
            # Display the heart at three scales
            default()
        elif UserInput == 'multi_points':
            # Display multiple scales on one plot, with control points showing
            # Create the multi curve
            multi_heart = Multi.MultiCurve()
            multi_heart.delta = 0.001
            # Enter a while loop to capture each input scale
            user_quits = False
            while(True):
                UserInput = input("Next scale value: ").lower()
                if UserInput == 'done':
                    # Leave the loop with user_quits = False
                    break
                elif UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
                    print('Quitting Question 1 program.')
                    user_quits = True
                    break
                else:
                    # Expect a scale value input
                    try:
                        scale = float(UserInput)
                    except ValueError as e:
                        print('Unexpected input: {}. To quit, type \'quit\'. To plot your hearts, type \'done\'.'.format(UserInput))
                        continue
                    heart = generate_heart(scale)
                    multi_heart.add(heart)
            if user_quits:
                # User wants to quit the program
                break
            # If user did not type quit, and he gave > 0 scales, plot the hearts
            if len(multi_heart.evalpts) > 0:
                display_curve(multi_heart)
        elif UserInput == 'multi_no_points':
            # Display multiple scales on one plot, without control points showing
            # Create the multi curve
            multi_heart = Multi.MultiCurve()
            multi_heart.delta = 0.001
            # Enter a while loop to capture each input scale
            user_quits = False
            while(True):
                UserInput = input("Next scale value: ").lower()
                if UserInput == 'done':
                    # Leave the loop with user_quits = False
                    break
                elif UserInput == 'quit' or UserInput == 'q' or UserInput == 'exit':
                    print('Quitting Question 1 program.')
                    user_quits = True
                    break
                else:
                    # Expect a scale value input
                    try:
                        scale = float(UserInput)
                    except ValueError as e:
                        print('Unexpected input: {}. To quit, type \'quit\'. To plot your hearts, type \'done\'.'.format(UserInput))
                        continue
                    heart = generate_heart(scale)
                    multi_heart.add(heart)
            if user_quits:
                # User wants to quit the program
                break
            # If user did not type quit, and he gave > 0 scales, plot the hearts
            if len(multi_heart.evalpts) > 0:
                display_curve(multi_heart, ctrlpts=False)
        else:
            # Take a single scale and plot the heart with that scale on its own
            try:
                scale = float(UserInput)
            except ValueError as e:
                print('Unexpected input: {}'.format(UserInput))
                continue
            if scale <= 0:
                print("Illegal scale: {}".format(scale))
                continue
            # All checks passed, so generate and display the heart
            heart = generate_heart(scale)
            display_curve(heart)
