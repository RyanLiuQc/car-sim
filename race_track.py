import matplotlib.pyplot as plt
import numpy as np
import math


import bicycle_model


class RaceTrack:

    # the curves are polylines 
    def __init__(
            self, 
            outerCurve: list[tuple[int,int]], # list of points (x,y) 
            innerCurve: list[tuple[int,int]]
            ):
        
        self.outerCurve = outerCurve
        self.innerCurve = innerCurve
        
        # get centerCurve
        self.centerCurve = self._get_centerCurve()
        
        self.s = self._get_list_of_all_path_distance_at_idx_of_corresponding_point()

    def _get_list_of_all_path_distance_at_idx_of_corresponding_point(self) -> list[float]:
        l = []
        s = 0
        for i in range(len(self.centerCurve)):
            p = self.centerCurve[i]
            d = math.sqrt(p[0]**2 + p[1]**2)            
        return l

    def _get_centerCurve(self) -> list[tuple[int,int]]:
        centerCurve = []

        # transform to numpy array
        inner = np.array(self.innerCurve)
        outer = np.array(self.outerCurve)

        len_inner = len(inner)
        len_outer = len(outer)
        for i in range(len_inner):
            # get tangent:
            prev_pt = inner[i-1]
            next_pt = inner[(i+1) % len_inner]

            p_i = inner[i]
            best_t = float('inf') # initial shortest distance along normal b/w inner and outer
            best_intersection = None

            d_in = next_pt - prev_pt # directional vector of inner

            length_d_in = np.linalg.norm(d_in)

            if length_d_in == 0: continue
            unit_tangent_inner = d_in / length_d_in

            # get normal 2 possible normal 
            # we might not have inner and outer in non looping tracks 
            # so find the normal that points to the other curve
            unit_normal_CCW = np.array([-unit_tangent_inner[1], unit_tangent_inner[0]]) # counter clock wise 
            unit_normal_CW = -unit_normal_CCW


            
            for j in range(len_outer):
                a = outer[j]
                b = outer[(j+1) % len_outer] # prevent index out of bound
                v = b - a # segment vector of outer 

                w = a - p_i #vector from inner pt to outer

                w_cross_v = w[0]*v[1] - w[1]*v[0]

                
                # try both normal to find the one that outputs the shortest distance
                for n in (unit_normal_CCW, unit_normal_CW): 
                    n_cross_v = n[0]*v[1] - n[1]*v[0]
                    
                    if abs(n_cross_v) < 1e-8:
                        continue

                    # distance between 2 segment
                    t = w_cross_v / n_cross_v 

                    w_cross_n = w[0]*n[1] - w[1]*n[0]

                    # percentage on outer segment where intersection of 2 lines meet
                    u = w_cross_n / n_cross_v

                    # verify that distance is positive and intersection happens within the segment
                    if t>0 and 0 <= u <= 1:
                        if t < best_t:
                            # update distance and intersection segment
                            best_t = t
                            best_intersection = p_i + best_t*n
                    
            # update best intersection
            if best_intersection is not None:
                midpoint = (p_i + best_intersection) / 2
                centerCurve.append((midpoint[0], midpoint[1]))
            else:
                pass
                # fallback to ensure that the number of points in centerCurve is the same as
                # number of points in inner curve
                # centerCurve.append((p_i[0], p_i[1]))

        centerCurve.append(centerCurve[0])
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
    innerCurve = build_ellipse_polyline(10,5)

    environment = RaceTrack(outerCurve, innerCurve)
    environment.visualize()

