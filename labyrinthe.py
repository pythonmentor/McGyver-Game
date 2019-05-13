from position import Position
import random
class Labyrinth :

    def __init__(self):
        self.gates = []
        self.walls = []
        self.item = []
        self.start= None
        self.arrival = None
        self.hero = None
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
        while self.start in self.item:
            self.item = random.sample(self.gates, 3)
        return self.item

    def display(self):
        for num_line in range(self.height+2):
            for num_column in range(self.width+2):
                if num_column == 15 : 
                    print()
                if Position(num_line, num_column) in self.item:
                    if Position(num_line,num_column) == self.hero.position:
                        print(self.hero.name ,end="")
                    elif Position(num_line,num_column) in self.hero.inventory:
                        print("#",end="")
                    else :
                        print('O', end="")
                elif Position(num_line,num_column) == self.hero.position:
                    print(self.hero.name ,end="")
                elif Position(num_line, num_column) in self.gates:
                    print(" ",end="")
                elif Position(num_line, num_column) in self.walls:
                    print('X', end="")
        


'''Il manque la méthode pour afficher le labyrinthe à chaque fois que le héros se déplace, il manque la classe Objet et Garde qui gère 
l'ajout des trois objets à l'inventaire du hero, l'endormissement du garde pour passer la porte'''