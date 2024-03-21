

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
    
    def take_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def strike(self, target):
        damage = self.__level * 2
        target.take_damage(damage)
        print(f"{self.get_name()} atacou {target.get_name()} e causou {damage}% de dano 😱")
    
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
            choice = input("Escolha: 1 para ataque normal ou 2 para o ataque especial! ")

            if choice == "1":
                self.hero.strike(self.enemy)
            else:
                print("Escolha inválida, escolha a opção 1 ou 2 😊")

        if self.hero.get_life() > 0:
            print("\n Parabéns você venceu a batalha 🎉\n")
        else:
            print("Você foi derrotado 😵‍💫")


# Creating Game Instance
game = Game()
game.start_battle()