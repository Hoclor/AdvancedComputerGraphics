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
heart.vis = vis_comp
heart.render()

#
# Scaled up Heart
#

heart_upscaled = BSpline.Curve()
scale = 2 # Any 1.0 < scale should work

# Set up the control points
heart_upscaled.degree = 3
heart_upscaled.ctrlpts = heart.ctrlpts[:]
# Scale the heart up by multiplying all ctrlpts by *scale*, as the heart is centered around the origin this will also plot at the same place
heart_upscaled.ctrlpts = [[scale*x, scale*y] for x,y in heart_upscaled.ctrlpts]

# Auto-generate knot vector
heart_upscaled.knotvector = utilities.generate_knot_vector(heart_upscaled.degree, len(heart_upscaled.ctrlpts))

# Set evaluation delta
heart_upscaled.delta = 0.001

# Evaluate curve
heart_upscaled.evaluate()

# Draw the control point polygon and the evaluated curve
heart_upscaled.vis = vis_comp
heart_upscaled.render()

#
# Scaled down Heart
#

heart_downscaled = BSpline.Curve()
scale = 0.5 # Any 0 < scale < 1.0 should work (barring floating point inaccuracies) for downscaling

# Set up the control points
heart_downscaled.degree = 3
heart_downscaled.ctrlpts = [[0, -20], [25, 5], [17, 20], [5, 19], [0.2, 13], [0, 8], [-0.2, 13], [-5, 19], [-17, 20], [-25, 5], [0, -20]]
heart_downscaled.ctrlpts = [[scale*x, scale*y] for x,y in heart_downscaled.ctrlpts]

# Auto-generate knot vector
heart_downscaled.knotvector = utilities.generate_knot_vector(heart_downscaled.degree, len(heart_downscaled.ctrlpts))

# Set evaluation delta
heart_downscaled.delta = 0.001

# Evaluate curve
heart_downscaled.evaluate()

# Draw the control point polygon and the evaluated curve
heart_downscaled.vis = vis_comp
heart_downscaled.render()