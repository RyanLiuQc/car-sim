import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import KDTree

import bicycle_model


class RaceTrack:

    # the curves are polylines 
    def __init__(
            self, 
            outerCurve: list[tuple[int,int]], # list of points (x,y)
            # centerCurve: list[tuple[int,int]], 
            innerCurve: list[tuple[int,int]]
            ):
        
        self.outerCurve = outerCurve
        self.innerCurve = innerCurve
        
        # get centerCurve
        self.centerCurve = self._get_centerCurve()

    def _get_centerCurve(self) -> list[tuple[int,int]]:
        centerCurve = []

        # 1 for every find point in inner, tangent

        # 2 find their normal vector (2 side possible) check both side so that it generalizes to non-looping tracks

        # 3 for every outer points, ray casting.
        
        return centerCurve
    
    def visualize(self):
        xs, ys = zip(*self.outerCurve)
        plt.plot(xs,ys)

        xs, ys = zip(*self.centerCurve)
        plt.plot(xs,ys, linestyle="dotted")

        xs, ys = zip(*self.innerCurve)
        plt.plot(xs,ys)

        plt.show()

        

# helper function to generate a polyline of an ellipse
def get_positive_y_value_of_ellipse_at_x(x: int, a: int, b: int) -> float:
    return (math.sqrt((1 - (x/a)**2) * (b**2))) # round for discrete

def build_ellipse_polyline( a: int,b: int) -> list[tuple[int,int]]:
    curve = []
    
    # generate points of positive first half of the curve
    for x in range(-a, a+1):
        y = get_positive_y_value_of_ellipse_at_x(x, a, b)
        curve.append((x,y))
    
    # generate negative y points for the curves
    number_of_points_in_half_curve = a*2 + 1 # same as len(curve) so far
    for i in range(1,number_of_points_in_half_curve):
        pt = curve[number_of_points_in_half_curve-1-i]
        curve.append((pt[0], -pt[1]))

    return curve
        

if __name__ == "__main__":
    outerCurve = build_ellipse_polyline(20,10)
    # centerCurve = build_ellipse_polyline(15,7)
    innerCurve = build_ellipse_polyline(10,5)
    # xs, ys = zip(*outerCurve)


    # plt.plot(xs, ys)
    # plt.show()
    environment = RaceTrack(outerCurve, innerCurve)
    environment.visualize()

