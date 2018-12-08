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


# Fix file path
# os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# 2D CURVE 1
#

# Create a B-Spline curve
heart = BSpline.Curve()

# Set up the control points
heart.degree = 3
heart.ctrlpts = [[0, -20], [25, 5], [17, 20], [5, 19], [0.2, 13], [0, 8], [-0.2, 13], [-5, 19], [-17, 20], [-25, 5], [0, -20]]


# Auto-generate knot vector
heart.knotvector = utilities.generate_knot_vector(heart.degree, len(heart.ctrlpts))

# Set evaluation delta
heart.delta = 0.001

# Evaluate curve
heart.evaluate()

# Draw the control point polygon and the evaluated curve
vis_config = VisMPL.VisConfig(ctrlpts=True)
vis_comp = VisMPL.VisCurve2D(vis_config)
heart.vis = vis_comp
heart.render()
