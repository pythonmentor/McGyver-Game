from labyrinthe import Labyrinth
from personnage import Character

class Game:

    def __init__(self):
        self.labyrinth = Labyrinth()
        self.perso = Character(self.labyrinth)
        self.user = None
        self.running = False

    def test_move(self):
        self.user = input('In which direction do you want to go ? U for Up, D for Down, L for Left, R for Right...').upper()
        while self.user !="R" and self.user != "L" and self.user != "U" and self.user != "D":
            self.user = input('In which direction do you want to go ? U for Up, D for Down, L for Left, R for Right...').upper()
            if self.user =="R" and self.user == "L" and self.user == "U" and self.user == "D":
                break
            else : 
                print("You didn't enter a valid direction")
        return self.user

    def start(self):
        self.labyrinth.generate_item_position()
        self.running = True
        while self.running:
            self.labyrinth.display()
            if self.perso.position in self.labyrinth.item:
                self.perso.pick_up_object()
            self.test_move()
            if self.user == 'Q':
                self.running = False
            else : 
                self.perso.move(self.user)
            if self.perso.position == self.labyrinth.arrival:
                self.perso.fight()
                self.running = False
def main():
    jeu = Game()
    jeu.start()

if __name__ == "__main__":
    main()