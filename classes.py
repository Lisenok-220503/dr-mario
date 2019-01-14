class Object():
    def __init__(self, color):
        self.color = color
        self.size = width, height = 30, 30

class Pill(Object):
    def __init__(self, color1, color2):
        self.color = [color1, color2]
        self.size = width, height = 30, 30

class Virus(Object):
    def __init__(self, color):
        super().__init__()
        
