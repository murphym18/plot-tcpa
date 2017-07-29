import math

class Test:
    def __init__(self, data):
        """
        The parameter data is a list and the elements are floats. Here is what's inside:
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
        funcs_a = [(lambda t: self.p1[i] + self.v1[i]*t) for i in range(3)]
        funcs_b = [(lambda t: self.p2[i] + self.v2[i]*t) for i in range(3)]
        self.x1 = funcs_a[0]
        self.y1 = funcs_a[1]
        self.z1 = funcs_a[2]
        self.x2 = funcs_b[0]
        self.y2 = funcs_b[1]
        self.z2 = funcs_b[2]

    def dist(t):
        """
        Finds the distance from drone A to drone B at time t
        """
        dx = self.x1(t) - self.x2(t)
        dy = self.y1(t) - self.y2(t)
        dz = self.z1(t) - self.z2(t)
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def find_tcpa():
        """
        Finds the time, t, where the distance from drone A to drone B is smallest
        """
        raise NotImplementedError()


