import numpy as np


# using frenet coordinates
# state parameters: 
#       s (arc length of path), 
#       e_y (lateral deviation), 
#       e_psi (heading error), 
#       v (velocity)
# 
# using standard x,y coordinates
#       x, y, psi, v

class KinematicBicycleModel:

    # defining initial state. 
    def __init__(self, s, e_y, e_psi, v):
        """
        state parameters: 
              s (arc length of path), 
              e_y (lateral deviation), 
              e_psi (heading error), 
              v (velocity)
        """
        self.s = s # (m)
        self.e_y = e_y # (rad)
        self.e_psi = e_psi # (rad)
        self.v = v # (m/s)
    
    # tells me WHERE the car is RELATIVE to curve if controls input GAS and STEERING
    # updates the STATE of the car based on where it was on the track
    def update(): 
        pass



