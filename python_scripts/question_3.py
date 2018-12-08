#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Question 3: Construct a landscape using a parametric surface. The landscape should contain features such
    as mountains, hills, plains, etc.
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Set up the visualisation settings
vis_config = VisMPL.VisConfig(ctrlpts=False) # Set ctrlpts=True to plot control points with the curves
vis_comp = VisMPL.VisCurve2D(vis_config)

#
# SURFACE 1
#

# Create a B-Spline surface instance
surface1 = BSpline.Surface()

# Set up the Bezier surface
surface1.degree_u = 6
surface1.degree_v = 6
surface1.ctrlpts_size_u = 7
surface1.ctrlpts_size_v = 7

surface1.ctrlpts = [[0, 0, 6], [0, 5, 8], [00, 10, -3], [00, 15, 10], [00, 20, 4], [00, 25, -3], [00, 30, 5],
                    [5, 0, 18], [5, 5, 4], [5, 10, 0], [5, 15, 6], [5, 20, 0], [5, 25, 40], [5, 30, 0],
                    [10, 0, 4], [10, 5, 120], [10, 10, 15], [10, 15, 0], [10, 20, 5], [10, 25, 3], [10, 30, 10],
                    [15, 0, 0], [15, 5, 31], [15, 10, 5], [15, 15, 5], [15, 20, -10], [15, 25, -1], [15, 30, 0],
                    [20, 0, 0], [20, 5, -3], [20, 10, 0], [20, 15, -10], [20, 20, 200], [20, 25, 10], [20, 30, 0],
                    [25, 0, 0], [25, 5, -3], [25, 10, 0], [25, 15, 2], [25, 20, -50], [25, 25, 50], [25, 30, 0],
                    [30, 0, 0], [30, 5, -3], [30, 10, 0], [30, 15, 0], [30, 20, -3], [30, 25, 0], [30, 30, 0]]


# Auto-generate knot vector
surface1.knotvector_u = utilities.generate_knot_vector(surface1.degree_u, surface1.ctrlpts_size_u)
surface1.knotvector_v = utilities.generate_knot_vector(surface1.degree_v, surface1.ctrlpts_size_v)

# Set evaluation delta
surface1.sample_size = 10

# Evaluate curve
surface1.evaluate()

# Draw the control point polygon and the evaluated curve
# Prepare the VisConfig
vis_config = VisMPL.VisConfig(ctrlpts=False)

vis_comp2 = VisMPL.VisSurface(vis_config)
surface1.vis = vis_comp2
surface1.render()

pass