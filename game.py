from labyrinthe import Labyrinth
from personnage import Personnage
class Game:

    def __init__(self):
        "Initialisation"
        self.labyrinth = Labyrinth()
        self.perso = Personnage(self.labyrinth)
        self.user = None
        self.running = False

    def start(self):
        "démarrage"
        self.labyrinth.generate_item_position()
        self.running = True
        while self.running:
            print(f"La position du personnage est {self.labyrinth.character.position.x}")
            self.labyrinth.display()
            self.user = input('Dans quelle direction souhaitez vous allez ? ...').upper()
            if self.user == 'Q':
                self.running = False
            else : 
                self.perso.move(self.user)

def main():
    jeu = Game()
    jeu.start()

if __name__ == "__main__":
    main()