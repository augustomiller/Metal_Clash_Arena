

class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def view_details(self):
        return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"
    
class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def view_details(self):
        return f"{super().view_details()}\nHabilidade: {self.get_skill()}\n"

class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def view_details(self):
        return f"{super().view_details()}\nTipo: {self.get_type()}\n"
    
class Game:
    """ Game Orchestrator Class  """

    def __init__(self) -> None:
        self.hero = Hero(name="Iron Man", life=100, level=5, skill="Super Força")
        self.enemy = Enemy(name="Mandarim", life=90, level=4, type="Voador")

    def start_battle(self):
        """ Manages the turn of battles """

        print("Iniciando batalha 🤖💥")

        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos personagens:")
            print(self.hero.view_details())
            print(self.enemy.view_details())

        input("Pressione <Enter> para atacar 👊")
        choice = input("Escolha: 1 para ataque normal ou 2 para o ataque especial!")


# Creating Game Instance
game = Game()
game.start_battle()