from math import *
import numpy as np
from dotted_dict import DottedDict
from my_elements import *

def my_machine(Qx_init, Qy_init, n_segments, turn, bunch, twiss, flag_oct = False, k3_int=None):
    Qx_segment = Qx_init/n_segments
    Qy_segment = Qy_init/n_segments
    if turn ==1:
        print('flag oct', flag_oct) #check elements
    for i in range(n_segments):
        rotation(Qx_segment,Qy_segment,turn,bunch,twiss)
        if flag_oct:
            octupole_map(k3_int/n_segments, bunch)
        
    return 