class Vehicle:
    def __init__(self, color, wheels, speed):
        self.color = color
        self.wheels = wheels
        self.speed = speed

    def __str__(self):
        return 'color: {}, wheels: {}, speed: {}'.format(
            self.color, self.wheels, self.speed)