import numpy as np
import math

def _make_funcs(p, v):
    def m(i):
        return lambda t: p[i] + t * v[i]
    return m(0), m(1), m(2)

class Test:
    def __init__(self, data):
        """
        The parameter data is a list and the elements are floats. Here is what's inside data:
        drone_A_init_pos_x
        drone_A_init_pos_y
        drone_A_init_pos_z
        
        drone_A_velocity_x
        drone_A_velocity_y
        drone_A_velocity_z
        
        drone_B_init_pos_x
        drone_B_init_pos_y
        drone_B_init_pos_z
        
        drone_B_velocity_x
        drone_B_velocity_y
        drone_B_velocity_z
        """
        self.p1 = [float(data[i]) for i in range(0, 3)]
        self.v1 = [float(data[i]) for i in range(3, 6)]
        self.p2 = [float(data[i]) for i in range(6, 9)]
        self.v2 = [float(data[i]) for i in range(9, 12)]
        self.x1, self.y1, self.z1 = _make_funcs(self.p1, self.v1)
        self.x2, self.y2, self.z2 = _make_funcs(self.p2, self.v2)

    def dist(self, t):
        """
        Finds the distance from drone A to drone B at time t
        """
        dx = self.x1(t) - self.x2(t)
        dy = self.y1(t) - self.y2(t)
        dz = self.z1(t) - self.z2(t)
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def find_tcpa(self):
        """
        Finds the time, t, where the distance from drone A to drone B is smallest
        """
        p1 = np.array(self.p1)
        p2 = np.array(self.p2)
        v1 = np.array(self.v1)
        v2 = np.array(self.v2)
        dp = p2 - p1
        dv = v2 - v1
        print(dp)
        print(dv)
        return -np.dot(dv, dp) / np.dot(dv, dv)
        #raise NotImplementedError()


