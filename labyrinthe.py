from position import Position
import random
class Labyrinth :

    def __init__(self):
        self.gates = []
        self.walls = []
        self.item = []
        self.start= None
        self.arrival = None
        self.character = None
        self.width = None
        self.height = None

    def load_from_file(self):
        with open ('labyrinth.txt', 'r') as f :
            for num_line, line in enumerate(f):
                for num_column, carac in enumerate(line):
                    if carac == "#":
                        self.gates.append(Position(num_line,num_column))
                    elif carac == "X":
                        self.walls.append(Position(num_line, num_column))
                    elif carac == "M":
                        self.start = Position(num_line, num_column)
                        self.gates.append(Position(num_line, num_column))
                    elif carac == "A":
                        self.arrival = Position(num_line,num_column)
                        self.gates.append(Position(num_line, num_column))
                    self.width = num_column
                    self.height = num_line
        

    def generate_item_position(self):
        self.item = random.sample(self.gates, 3)
        return self.item

    def display(self):
        for num_line in range(self.height+1):
            for num_column in range(self.width+1):
                if num_column == 14 : 
                    print()
                if Position(num_line, num_column) in self.item:
                    print('O', end="")
                elif Position(num_line,num_column) == self.character.position:
                    print("M",end="")
                elif Position(num_line, num_column) in self.gates:
                    print("#",end="")
                elif Position(num_line, num_column) in self.walls:
                    print('X', end="")
        


'''Il manque la méthode pour afficher le labyrinthe à chaque fois que le héros se déplace, il manque la classe Objet et Garde qui gère 
l'ajout des trois objets à l'inventaire du character, l'endormissement du garde pour passer la porte'''