

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
    
hero = Hero(name="Iron Man", life="100", level="5", skill="Super Força")
print(hero.view_details())
enemy = Enemy(name="", life="90", level="4", type="Voador")
print(enemy.view_details())