class Board:
    def __init__(self):
        self.width = 250
        self.height = 450
        self.board = [[0] * 250 for _ in range(450)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    