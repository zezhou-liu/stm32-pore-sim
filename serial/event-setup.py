# This script sets up the DNA translocation we want to emulate. It generates signals t
# state chart:
#   0: off state. 
#   1: capture state.
import numpy as np

class translocation:
    def __init__(self):
        self.capture_rate = 0.2 # 
        self.state = 0 # 
