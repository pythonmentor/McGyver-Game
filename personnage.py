from labyrinthe import Labyrinth
from position import Position
class Character:
    '''Class that manages the character, his position, his movements, how he pick up the objects and how he reacts to the guard.'''

    def __init__(self, laby):
        self.labyrinth = laby
        self.labyrinth.load_from_file()#We must use the method of the Labyrinth class to load the start position of our character
        self.position = self.labyrinth.start
        self.labyrinth.hero = self
        self.inventory = []
        self.name = "M"

    def move(self, direction):
        '''Manage the character's movement by going to the position class and the Labyrinth class to find out if moving is possible or not.'''
        nouvelle_position = self.position + direction
        if nouvelle_position in self.labyrinth.gates : 
            self.position = nouvelle_position
        return self.position
        
    def pick_up_object(self):
        self.inventory.append(self.position)
        print("You have picked up an object")
        print(f"You have {len(self.inventory)} objects in your inventory")

    def fight(self):
        if len(self.inventory) == 3 : 
            print("You win !")
        else :
            print("You lose !")