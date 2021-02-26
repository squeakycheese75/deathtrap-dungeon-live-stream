from src.dice import roll_dice

class Hero:
    def __init__(self, name: str):
        self.name = name
        self.skill = 0
        self.luck = 0
        self.stamina = 0
        self.cast_character()
    
    def cast_character(self):
        self.skill = roll_dice() + 6
        self.luck = roll_dice() + 6
        self.stamina = roll_dice() + roll_dice() + 12

    @property
    def is_alive(self):
        return self.stamina > 0

    def get_skill(self) -> int:
        return self.skill
    
    def get_name(self) -> int:
        return self.name

    def show(self):
        print(f"Name {self.name}  skill {self.skill} stamina {self.stamina} luck: {self.luck}")


class Monster:
    def __init__(self, stats: dict, name: str):
        self.name = name
        self.stamina = stats['stamina']
        self.skill = stats['skill']
    
    @property
    def is_alive(self):
        return self.stamina > 0

    def get_skill(self) -> int:
        return self.skill

    def get_name(self) -> int:
        return self.name



    