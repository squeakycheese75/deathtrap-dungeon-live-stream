from src.charachter import Hero, Monster
from src.dice import roll_dice

class Fight:
    def __init__(self, hero: Hero, monster: Monster):
        self.monster = monster
        self.hero = hero
      
    def round(self):
        # Monster roll
        monster_attack_strength = roll_dice() + roll_dice() + self.monster.skill
        # Hero roll
        hero_attack_strength = roll_dice() + roll_dice() + self.hero.skill

        if monster_attack_strength > hero_attack_strength:
            print(f"The {self.monster.get_name} deals a mighty blow")
            self.monster.set_stamina = self.monster.get_stamine
        elif monster_attack_strength < hero_attack_strength:
            print(f"The {self.hero.get_name} bashes the bloddy monster in the face")
        else:
            print("Swing and a miss.  They both look flumoxed!")


#  We got here!!!!!