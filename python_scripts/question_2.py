#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 2a: Decompose the heart-shaped object in question 1 into Bezier curves and show all control
    points for each Bezier curve.
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import operations
from geomdl.visualization import VisMPL
from question_1 import generate_heart

# Set up the visualisation settings
vis_config = VisMPL.VisConfig(legend=False, ctrlpts=True) # Set ctrlpts=True to plot control points with the curves
vis_comp = VisMPL.VisCurve2D(vis_config)

#
# Create the decomposed heart
#

# Generate the heart
heart = generate_heart()

# Decompose the B-Spline into Bezier curves
heart_bezier = operations.decompose_curve(heart)

# Set evaluation delta
heart_bezier.delta = 0.001

# Print output information
print("Displaying the decomposed heart. Note that each set of control points for each Bezier curve is given a different colour, but that colour does not necessarily match up with the relevant Bezier curve. Each different coloured segment represents a different Bezier curve.")

# Draw the control point polygon and the bezier curves from the decomposition
heart_bezier.vis = vis_comp
heart_bezier.render()

"""
    Question 2b: Describe any extra geometrical property is required to maintain for supporting proper shape
    editing of the heart-shaped object through the decomposed Bezier curves. Show how such property is applied.

    This question is answered in the question_2b.pdf file.
"""