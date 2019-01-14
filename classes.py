class Object():
    def __init__(self, color):
        self.color = color
        self.size = width, height = 30, 30

    def destruction(self):
        global points
        points += 50

class Pill(Object):
    def __init__(self, color1, color2):
        self.color = [color1, color2]
        self.size = width, height = 30, 30
    def destruction(self):
        super().destruction()

class Virus(Object):
    def __init__(self, color):
        super().__init__()



