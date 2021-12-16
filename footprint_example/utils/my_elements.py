from math import *
import numpy as np
from dotted_dict import DottedDict

def rotation(mux,muy,turn,bunch,twiss): 
    twiss.gamma_x = (1. + twiss.alpha_x**2)/twiss.beta_x
    twiss.gamma_y = (1. + twiss.alpha_y**2)/twiss.beta_y
    x1 = (cos(mux) + twiss.alpha_x*sin(mux))*bunch.x + twiss.beta_x*sin(mux)*bunch.px
    px1 = -twiss.gamma_x*sin(mux)*bunch.x+ (cos(mux)-twiss.alpha_x*sin(mux))*bunch.px
    y1 = (cos(muy) + twiss.alpha_y*sin(muy))*bunch.y + twiss.beta_y*sin(muy)*bunch.py
    py1 = -twiss.gamma_y*sin(muy)*bunch.y+ (cos(muy)-twiss.alpha_y*sin(muy))*bunch.py
    bunch.x = x1
    bunch.px = px1
    bunch.y = y1
    bunch.py = py1
    return 


def octupole_map(k3,bunch):
    k3 = k3/6.
    x1  = bunch.x
    px1 = bunch.px - k3*(bunch.x**3-3*bunch.x*bunch.y**2)
    y1  = bunch.y
    py1 = bunch.py - k3*(-3*bunch.x**2*bunch.y+bunch.y**3)
    bunch.x = x1
    bunch.px = px1
    bunch.y = y1
    bunch.py = py1
    return 