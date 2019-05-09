class Position:
    '''Classe qui gére toutes les positions dans le labyrinthe x étant le numéro de ligne et y le numéro de colonne'''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        
    
    def move_down(self):
        self.x = self.x +1
        return Position(self.x, self.y)
       
    
    def move_up(self):
        self.x = self.x -1
        return Position(self.x, self.y)


    def move_left(self):
        self.y = self.y-1
        return Position(self.x, self.y)
    
    def move_right(self):
        self.y = self.y +1
        return Position(self.x, self.y)

    def __add__(self, direction):
        if direction == "U":
            return self.move_up()
        elif direction =="D":
            return self.move_down()
        elif direction == "L":
            return self.move_left()
        elif direction =='R':
            return self.move_right()


    def __eq__(self, item_to_compare):
        if self.x == item_to_compare.x and self.y == item_to_compare.y:
            return True
        else :
            return False