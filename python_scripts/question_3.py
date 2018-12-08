#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 3: Construct a landscape using a parametric surface. The landscape should contain features such
    as mountains, hills, plains, etc.
"""

import os
import numpy as np
import random
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Set up the visualisation settings
vis_config = VisMPL.VisConfig(ctrlpts=False) # Set ctrlpts=True to plot control points with the curves
vis_comp = VisMPL.VisCurve2D(vis_config)

def set_x_y(region, x_offset, y_offset):
    """Sets the x and y values of the given region"""
    for x in range(region.shape[0]):
        for y in range(region.shape[1]):
            region[x, y, 0] = x_offset + 5*x
            region[x, y, 1] = y_offset + 5*y
    
    return region

#
# SURFACE 1
#

# Create a B-Spline surface instance
landscape = BSpline.Surface()

# Set up the Bezier surface
landscape.degree_u = 3
landscape.degree_v = 3
landscape.ctrlpts_size_u = 17 # x axis (visually vertical)
landscape.ctrlpts_size_v = 14 # y axis (visually horizontal)

# Use numpy arrays to define each section of the landscape to allow for easier piecewise and global processing

# Define the 7x7 mountain section
mountain = np.array([[0, 0, 10], [0, 0, 8], [0, 0, 8], [0, 0, 10], [0, 0, 10], [0, 0, 25], [0, 0, 10],
                     [0, 0, 12], [0, 0, 24], [0, 0, 48], [0, 0, 24], [0, 0, 44], [0, 0, 65], [0, 0, 20],
                     [0, 0, 10], [0, 0, 29], [0, 0, 65], [0, 0, 40], [0, 0, 28], [0, 0, 33], [0, 0, 24],
                     [0, 0, 10], [0, 0, 15], [0, 0, 55], [0, 0, 31], [0, 0, 15], [0, 0, 13], [0, 0, 8],
                     [0, 0, 10], [0, 0, 5], [0, 0, 25], [0, 0, 48], [0, 0, 38], [0, 0, 40], [0, 0, 14],
                     [0, 0, 10], [0, 0, -3], [0, 0, -3], [0, 0, 23], [0, 0, 70], [0, 0, 80], [0, 0, 30],
                     [0, 0, 10], [0, 0, -8], [0, 0, -4], [0, 0, 15], [0, 0, 40], [0, 0, 35], [0, 0, 20]]).reshape(7,7,3)
# Set its global position - top left
mountain = set_x_y(mountain, 0, 0)

# Define the 7x7 bumpy plains section
bumpy_plains = np.array([[0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10],
                         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 10]]).reshape(7,7,3)
# Create the bumpy plains by randomly adding between 0 and 24 to each control point's z value (except the outside edge - fix these to 10)
for x in range(1, 7):
    for y in range(0, 6):
        bumpy_plains[x, y, 2] += random.randrange(0, 31, 10)
# Set its global position - top right
bumpy_plains = set_x_y(bumpy_plains, 0, 35)



        

# Define the 10x7 hill section
hill = np.array([[0, 0, 10], [0, 0, -8], [0, 0, 4], [0, 0, 8], [0, 0, 10], [0, 0, 10], [0, 0, 10],
                 [0, 0, 10], [0, 0, -10], [0, 0, -10], [0, 0, -10], [0, 0, -10], [0, 0, -10], [0, 0, -10],
                 [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5],
                 [0, 0, 5], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10], [0, 0, 10],
                 [0, 0, 5], [0, 0, 13], [0, 0, 18], [0, 0, 20], [0, 0, 14], [0, 0, 11], [0, 0, 5],
                 [0, 0, 5], [0, 0, 18], [0, 0, 22], [0, 0, 25], [0, 0, 17], [0, 0, 10], [0, 0, 5],
                 [0, 0, 5], [0, 0, 24], [0, 0, 25], [0, 0, 28], [0, 0, 25], [0, 0, 13], [0, 0, 5],
                 [0, 0, 5], [0, 0, 14], [0, 0, 22], [0, 0, 25], [0, 0, 28], [0, 0, 9], [0, 0, 5],
                 [0, 0, 5], [0, 0, 9], [0, 0, 18], [0, 0, 20], [0, 0, 11], [0, 0, 6], [0, 0, 5],
                 [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5]]).reshape(10,7,3)
# Set its global position - bottom left
hill = set_x_y(hill, 35, 0)

# Define the 10x7 lake section
lake = np.array([[0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5],
                  [0, 0, -15], [0, 0, -13], [0, 0, -13], [0, 0, 0], [0, 0, 3], [0, 0, 5], [0, 0, 5],
                  [0, 0, 5], [0, 0, -13], [0, 0, -15], [0, 0, -13], [0, 0, 0], [0, 0, 3], [0, 0, 5],
                  [0, 0, 5], [0, 0, -13], [0, 0, -18], [0, 0, -15], [0, 0, -13], [0, 0, 0], [0, 0, 5],
                  [0, 0, 5], [0, 0, -13], [0, 0, -15], [0, 0, -18], [0, 0, -15], [0, 0, -13], [0, 0, 5],
                  [0, 0, 5], [0, 0, -10], [0, 0, -15], [0, 0, -18], [0, 0, -20], [0, 0, -15], [0, 0, 5],
                  [0, 0, 5], [0, 0, 3], [0, 0, 0], [0, 0, -13], [0, 0, -20], [0, 0, -13], [0, 0, 5],
                  [0, 0, 5], [0, 0, 3], [0, 0, 0], [0, 0, -13], [0, 0, -5], [0, 0, -13], [0, 0, 5],
                  [0, 0, 5], [0, 0, 3], [0, 0, 0], [0, 0, 2], [0, 0, -2], [0, 0, 5], [0, 0, 5],
                  [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5], [0, 0, 5]]).reshape(10,7,3)
# Set its global position - bottom right
lake = set_x_y(lake, 35, 35)

# Auto-generate knot vector
landscape.knotvector_u = utilities.generate_knot_vector(landscape.degree_u, landscape.ctrlpts_size_u)
landscape.knotvector_v = utilities.generate_knot_vector(landscape.degree_v, landscape.ctrlpts_size_v)

# Set evaluation delta
landscape.delta = 0.04

# Evaluate curve
landscape.evaluate()

# Draw the control point polygon and the evaluated curve
# Prepare the VisConfig
vis_config = VisMPL.VisConfig(ctrlpts=False)

vis_comp = VisMPL.VisSurfTriangle(vis_config)
landscape.vis = vis_comp
landscape.render()

pass