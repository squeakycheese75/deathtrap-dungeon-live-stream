from src.charachter import Hero, Monster
from src.battle import Fight
from src.data import get_page

name  = input("What is you name brave adventurer?")

hero = Hero(name)
hero.show()

location = 387

while hero.is_alive:
    resval = get_page(location)
    for p in resval['narrative']: 
        print(p)

    for e in resval['events']:
        if e['name'] == 'fight':
            print(e)
            monster = Monster(e['stats'], e['name'])
            fight = Fight(hero, monster)
            while hero.is_alive and monster.is_alive:
                fight.round() 

  
    for option in resval['options']:
        print(option['choice'])
    
    choice = ''
    while choice not in resval['valid_choices']:
        choice = input('Would you like to:')

    location = [obj for obj in resval['options'] if obj['key'] == choice][0]['page']