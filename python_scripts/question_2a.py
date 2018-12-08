#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 1: Construct a parametric curve to represent a heart-shaped object. Produce both a scaled-up
    and a scaled-down version of the object by modifying the control points of the parametric curve.
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import operations
from geomdl.visualization import VisMPL

# Set up the visualisation settings
vis_config = VisMPL.VisConfig(ctrlpts=True) # Set ctrlpts=True to plot control points with the curves
vis_comp = VisMPL.VisCurve2D(vis_config)

#
# Create the B-Spline heart
#

# Create a B-Spline curve
heart = BSpline.Curve()

# Set up the control points
heart.degree = 3
heart.ctrlpts = [[0, -20], [25, 5], [17, 20], [5, 19], [0.2, 13], [0, 8], [-0.2, 13], [-5, 19], [-17, 20], [-25, 5], [0, -20]]

# Auto-generate knot vector
heart.knotvector = utilities.generate_knot_vector(heart.degree, len(heart.ctrlpts))

# Decompose the B-Spline into Bezier curves
heart_bezier = operations.decompose_curve(heart)

# Set evaluation delta
heart_bezier.delta = 0.001

# Draw the control point polygon and the evaluated curve
heart_bezier.vis = vis_comp
heart_bezier.render()
