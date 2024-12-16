import time


class Circle:
    radius = None
    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        return (self.radius)

    def set_radius(self,new_radius):
        self.radius = new_radius

Circle1 = Circle(100)
print(Circle1.get_radius())

time.sleep(3)

Circle1.set_radius(156)
print(Circle1.get_radius())


