from labyrinthe import Labyrinth
from position import Position
class Personnage:
    '''Classe qui gère la position '''

    def __init__(self, laby):
        self.labyrinth = laby
        self.labyrinth.load_from_file()
        self.position = self.labyrinth.start
        self.labyrinth.character = self
        self.inventory = []
        self.name = "M"

    def move(self, direction):
        nouvelle_position = self.position + direction
        if nouvelle_position in self.labyrinth.gates : 
            self.position = nouvelle_position
            print("Attention je bouge")
            print(f"{self.position.x}, {self.position.y}")
        else : 
            print("Attention c'est un mur")
            print(f"{self.position.x}, {self.position.y}")
        return self.position


