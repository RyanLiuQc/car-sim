import numpy as np
import math

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
    def __init__(self, s: float = 0, e_y: float = 0, e_psi: float = 0, v: float = 0, L: float = 0.5):
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

        self.L = L # wheelbase in meters
    
    # tells me WHERE the car is RELATIVE to curve if controls input GAS and STEERING
    # updates the STATE of the car based on where it was on the track
    def update(self, a: float, delta: float, kappa: float, dt: float) -> None: 
        """
        a: new acceleration
        delta: new steering angle
        kappa: curvature at current s
        dt: time step
        """ 
        
        # helper heading angle derivative
        psi_dot = self.v / self.L * math.tan(delta) 
        print("psi_dot: ",psi_dot)

        # differentiate state variables
        denominator  = (1 - self.e_y*kappa)
        # make sure that s_dot update is realistic
        if abs(denominator) < 1e-5:
            denominator = 1e-5 if denominator>=0 else -1e-5

        s_dot = (self.v * math.cos(self.e_psi)) / denominator
        e_y_dot = self.v * math.sin(self.e_psi)
        e_psi_dot = psi_dot - kappa * s_dot
        v_dot = a

        # update state
        self.s += s_dot * dt
        self.e_y += e_y_dot * dt
        self.e_psi += e_psi_dot * dt 
        self.v += a * dt

        # make e_psi between (-pi, pi)
        self.e_psi = (self.e_psi + math.pi) % (2*math.pi) - math.pi

if __name__ == "__main__":
    car = KinematicBicycleModel(v = 1, L = 2)
    print(f's: {car.s}, e_y: {car.e_y}, e_psi: {car.e_psi}, v: {car.v}')
    car.update(a=0,delta=math.pi/4, kappa=0, dt=1)
    print(f's: {car.s}, e_y: {car.e_y}, e_psi: {car.e_psi}, v: {car.v}')
    car.update(a=0,delta=0, kappa=0, dt=1)
    print(f's: {car.s}, e_y: {car.e_y}, e_psi: {car.e_psi}, v: {car.v}')



        



