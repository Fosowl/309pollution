class Vector():
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x_, y_, z_ = 0):
        self.x = x_
        self.y = y_
        self.z = z_
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
