import random


class Caracter:
    def __init__(self, name, attack, health, defence):
        self.name = name
        self.attack = attack
        self.health = health
        self.defence = defence
    
    def increase(self, parameter, value):
        if parameter == 'attack':
            new_attack = self.get('attack') + value
            self.set('attack', new_attack)
        elif parameter == 'health':
            new_health = self.get('health') + value
            self.set('health', new_health)
        elif parameter == 'defence':
            new_defence = self.get('defence') + value
            self.set('defence', new_defence)
    
    def decrease(self, parameter, value):
        if parameter == 'attack':
            new_attack = self.get('attack') - value
            self.set('attack', new_attack)
        elif parameter == 'health':
            new_health = self.get('health') - value
            self.set('health', new_health)
        elif parameter == 'defence':
            new_defence = self.get('defence') - value
            self.set('defence', new_defence)

    def get(self, parameter):
        if parameter == 'attack':
            return self.attack
        elif parameter == 'health':
            return self.health
        elif parameter == 'defence':
            return self.defence
        elif parameter == 'name':
            return self.name
        
    def chance(self, parameter):
        if parameter == 'hit':
            chance_to_hit = 20 * self.attack + 7 * self.health
            return chance_to_hit
        elif parameter == 'parry':
            chanse_to_parry = 9 * self.attack + 4 * self.health
            return chanse_to_parry
        elif parameter == 'block':
            chance_to_block = 3 + self.defence + 2 * self.health
            return chance_to_block

    def roll(self, parameter):
        if parameter == 'hit':
            i = random.randint(1, 100)
            if i <= self.chance('hit'):
                return True
            else:
                return False
        elif parameter == 'parry':
            i = random.randint(1, 100)
            if i <= self.chance('parry'):
                return True
            else:
                return False
        elif parameter == 'block':
            i = random.randint(1, 100)
            if i <= self.chance('block'):
                return True
            else:
                return False

    def set(self, parameter, value):
        if parameter == 'attack':
            self.attack = value
        elif parameter == 'health':
            self.health = value
        elif parameter == 'defence':
            self.defence = value

Link = Caracter('Link',1.0 ,10.0 , 0.0)
Ganon = Caracter('Ganon',2.5 ,15.0, 22.0)
Ghost_knight = Caracter('Ghost Knight',1.5,8,15.0)

def bridge_poison_calc(bridge, poison):
    if bridge == 1:
        i = random.randint(0, 100)
        if i > 70:
            print(f"\nUnfortunatly bridge brakes and you've fell in to a cold water.")
            input('')
            alligator_sleep_calc(1, 0)
        elif i <= 70:
            print(f"\nBridge was pretty stable, you going forward")
    elif poison == 1:
        i = random.randint(0, 100)
        if i <= 70:
            alligator_sleep_calc(0, 1)
        elif i > 70:
            return

def alligator_sleep_calc(alligator, sleep):
    if alligator == 1:
        i = random.randint(0, 100)
        if i <= 15:
            print(f"\nALLIGATORS!!! ALL OVER THE PLACE!!!")
            Link.decrease('health', 1)
            if Link.get('health') > 0:
                print(f'''\nYou was so lucky to make it to a nearest shore. But you got bitten pretty badly.
You feel hot blood flowing by your arm.
Your Health --> {Link.get('health')}''')
            elif Link.get('health') < 1:
                print(f"\nWell, it is, what it is. A hero was eaten by a bunch of stupid lizards. What a shame.")
        elif i > 15:
            print(f"Hopefully, you just got wet. It could've ended much worse...")
    elif sleep == 1:
        i = random.randint(0, 100)
        if i <= 15:
            Link.decrease('defence', 1)
            print(f"\nIt wasn't a heal potion, rather some kind of nasty ogre secretions.\nAfter vomiting you lied down and lost consciousness.\nYour Defence --> {Link.get('defence')}")
        elif i >= 83:
            Link.decrease('health', 1)
            print(f"\nYep, it was poison...")
            if Link.get('health') > 0:
                print(f'''After a long sleep you finally open your eye's.\nIt's certainly a miracle, that you still alive.
You've only lost cople decade's of your life.
Your Health --> {Link.get('health')}''')
            elif Link.get('health') < 1:
                print(f"That was a damn good poison, best of what you've tried so far.")
        else:
            print("Not bad, it even reminded you taste of a beer in a local tavern down the street. It wasn't poison. What a relief!")
        
def weapon_shield(weapon, shield):
    if weapon == 1:
        Link.increase('health', 4)
        Link.increase('attack', 2) 
        print(f'''You've been gazing into the void of the room when suddenly something starts sparking behind the rock.
It's an old sword, a silent witness of days gone by.
As you pick it up, you feel its heavy weight, and the might of all its previous owners fills your arms.
You obtain a power that you couldn't even imagine before
Health --> {Link.get('health')}
Attack --> {Link.get('attack')}''')
    if shield == 1:
        Link.increase('health', 4)
        Link.increase('defence', 2)
        print(f'''Wadeing through endless labyrints of an old dungeon, you suddenly realize there's might be a danger ahed.
Why else there're so many bone's lie's all over?...
After quick look around, you've decided to pick up a round hoplite shield, which fortunately lay near.
Health --> {Link.get('health')}
Defence --> {Link.get('defence')}''')

def get_recognize():
    i = random.randint(1, 100)
    if i > 70:
        return True
    else:
        return False

def punch(attacker, defender):
    if attacker.roll('hit'):
        print(f"{attacker.get('name')} try's to slash meat out of a {defender.get('name')}'s bones")
        if defender.roll('parry'):
            print(f"Right in the eye! What a parry!\n{attacker.get('name')}'s lost {Link.get('attack') / 2} Health")
            attacker.decrease('health', Link.get('attack') / 2)
            print(f"{attacker.get('name')} remain's {attacker.get('health')} HP")
        elif defender.roll('block'):
            print(f"It was a good try, but {defender.get('name')} blocked attack")
            print(f"{defender.get('name')} remain's {defender.get('health')} HP")
        else:
            print(f"This hit land's right in target, {defender.get('name')} lost {Link.get('attack')} HP")
            defender.decrease('health', Link.get('attack'))
            print(f"{defender.get('name')} remain's {defender.get('health')} HP")
    else:
        print(f"What a shame, {attacker.get('name')} can't even pull up his weapon..") 

def fight(aggressor, victim):
    if get_recognize():
        while aggressor.get('health') > 0 and victim.get('health') > 0:
            punch(victim, aggressor)
            input('')
            if aggressor.get('health') > 0 and victim.get('health') > 0:
                punch(aggressor, victim)
                input('')
        if Link.get('health') == 0 or Link.get('health') < 0:
            print(f"Link gasped for breath, blood staining his trembling hands.\nWith a final sigh, his eyes dimmed, his legend coming to an end.")
            input('')
            return False
        else:
            print(f"{victim.get('name')}'s menacing presence faltered as he fell to his knees, his once formidable strength fading.\nWith a pained groan, darkness claimed him, his reign of terror extinguished.")
            input('')
            return True
    else:
        while aggressor.get('health') > 0 and victim.get('health') > 0:
            punch(aggressor, victim)
            input('')
            if aggressor.get('health') > 0 and victim.get('health') > 0:
                punch(victim, aggressor)
                input('')
        if Link.get('health') == 0 or Link.get('health') < 0:
            print(f"Link gasped for breath, blood staining his trembling hands.\nWith a final sigh, his eyes dimmed, his legend coming to an end.")
            input('')
            return False
        else:
            print(f"{victim.get('name')}'s menacing presence faltered as he fell to his knees, his once formidable strength fading.\nWith a pained groan, darkness claimed him, his reign of terror extinguished.")
            input('')
            return True

