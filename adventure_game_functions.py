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
        else:
            print(f'''\nWhat a taste''')

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
        elif i > 82:
            Link.decrease('health', 1)
            print(f"\nYep, it was poison...")
            if Link.get('health') > 0:
                print(f'''After a long sleep you finally open your eye's.\nIt's certainly a miracle, that you still alive.
You've only lost cople decade's of your life.
Your Health --> {Link.get('health')}''')
            elif Link.get('health') < 1:
                print(f"That was a damn good poison, best of what you've tried so far.")
        else:
            print("\nNot bad, it even reminded you taste of a beer in a local tavern down the street. It wasn't poison. What a relief!")
        
def weapon_shield(weapon, shield):
    if weapon == 1:
        Link.increase('health', 4)
        Link.increase('attack', 2) 
        print(f'''\nYou've been gazing into the void of the room when suddenly something starts sparking behind the rock.
It's an old sword, a silent witness of days gone by.
As you pick it up, you feel its heavy weight, and the might of all its previous owners fills your arms.
You obtain a power that you couldn't even imagine before
Health --> {Link.get('health')}
Attack --> {Link.get('attack')}''')
    if shield == 1:
        Link.increase('health', 4)
        Link.increase('defence', 2)
        print(f'''\nWadeing through endless labyrints of an old dungeon, you suddenly realize there's might be a danger ahed.
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

def entrance():
    print(f'''In the depths of the ancient cave, shadows danced upon weathered stone walls. 
Whispering echoes told tales of forgotten realms.
A mystical aura enveloped the air, beckoning brave souls to uncover its secrets and face the perils within.
You see a giant passage which leads you in dark depth, ahed.''')
    input('')
    print(f'''You've alredy take's your way to a passage when suddenly, a small hole in a wall got in to your sigtht.
You lean against it and saw a room full of bottles and beakers. Looks like an alchemy lab.
Aquaring too much presure to the wall, make's it crumbling and soonly collapsed under your waight.
Now you got to choose whith way should you go...''')
    input('')
    while True:
        try:
            choice = int(input('1. Take the way through an old cave passage.\n2. Enter laboratory\nYou choose ==> '))
            if choice == 1:
                return 'passage'
            elif choice == 2:
                return 'lab'
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print("Invalid input. Please enter a number.")

def laboratory():
    print(f'''\nWithin the timeworn laboratory's dim-lit chambers, arcane contraptions stood dormant, their purpose shrouded in mystery.
Cracked vials and faded parchments adorned the cluttered tables, remnants of forgotten experiments that echoed with the whispers of forgotten sorcery.''')
    input('')
    print(f'''Beneath a pile of an old rusty equioment you see a flacon with a bright red substance, seems a result of an old experiment.''')
    while True:
        try:  
            choice = int(input("1. Take a potion\n2. Not risk it\nYou choose ==> "))
            if choice == 1:
                print("As the healing potion touched their lips, renewed vigor surged within.")
                Link.increase('health', 3)
                print(f"Your Health ==> {Link.get('health')}")
                input('')
                break
            elif choice == 2:
                print("It's better not to play with such ansient magic. Good choice.")
                input('')
                break
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    
def armory():
    print(f'''\nIn the dusty recesses of the ancient armory, rows of rusted weapons stood sentinel.
A lingering scent of valor and battles long past permeated the air.
Shields adorned with heraldry bore witness to a bygone era of knights and conquest.''')
    weapon_shield(0,1)
    input('')
    print(f'''From an armory there's 2 way's out. One of which lead to the next room, apear as trainee field.
The other look's like a barracks door''')

def rope_bridge():
    print('''\nDeep within the heart of a cavernous abyss, a fragile rope bridge spanned the darkness.
Dim torchlight flickered, revealing stalactites that dripped with anticipation.
Each cautious step echoed, harmonizing with the distant whispers of forgotten spirits lurking in the shadows''')
    while True:
        try:
            choice = int(input('''\nDo you dare to trespass? \n1. Go ahed \n2. Turn back \nYou choose ==> '''))
            if choice == 1:
                bridge_poison_calc(1, 0)
                return 'trespass'
            elif choice == 2: 
                return 'go back'
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print('Invalid input. Please enter a number.')

def trainee_field():
    print(f'''\nIn the hidden recesses of the cave, a training field emerged, bathed in a mystical glow.
Novice warriors honed their skills amidst rugged terrain, guided by seasoned masters.
Echoes of clashing blades and resolute shouts reverberated, echoing through the hallowed chambers.
''')
    input('')
    weapon_shield(1, 0)
    input('')

def barracks():
    print('''\nWithin the cavern's embrace, a makeshift barracks stood as a haven for weary warriors.
Flickering torches cast dancing shadows upon stone walls adorned with tattered banners.
Tense whispers of camaraderie mingled with the distant rumblings of imminent conflict.''')
    input('')
    print(f'''In the heart of the chamber, a spectral knight stood, his ethereal armor gleaming with an otherworldly light.
Haunting eyes pierced the darkness, revealing a tortured soul bound to the mortal realm, forever guarding ancient secrets with a spectral sword at the ready.''')
    input('')
    hp = Link.get('health')
    if fight(Link, Ghost_knight):
        Link.set('health', hp)
        print("\nAfter a fight, Link falls into a deep sleep and restores his HP.")
        weapon_shield(1, 0)
    else:
        print("R.I.P Link")

def empty_room():
    print(f'''\nWithin the cavern's depths, an empty room awaited discovery.
A solitary round table, weathered and worn, stood as a relic of forgotten gatherings.
Shadows whispered secrets as if time itself held its breath, waiting for the return of forgotten lore.''')
    while True:
        try:
            choice = int(input(f'''\nOn a table you found a small flask with a green mixture. Looking healthy right?\n1. Try a taste \n2. Pass away \nYou choose ==> '''))
            if choice == 1:
                bridge_poison_calc(0, 1)
                print(f'''After this small adventture you leed to the exit''')
                break
            elif choice == 2:
                print("\nWhat a will. but i assume it's for the better")
                break            
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print("Invalid input. Please enter a number.")

def arena():
    print(f'''\nNestled deep within the cave's heart, an arena of destiny emerged.
The air crackled with anticipation as colossal stone pillars framed the battleground.
Spectators of fate watched in awe, their hearts pounding with the echoes of impending clash between hero and monstrous foe.''')
    input('')
    print('''Right in it's centre you see a giant figure this fight will be the last!''' )
    input('')
    fight(Link, Ganon)
    if Link.get('health') > 0:
        print('''You finally pass through all bariers in a way to this.''')
        input('')
        print(f'''Within the hidden recesses of the cave, a room adorned with gleaming treasure unfolded.
Golden jewels and ancient artifacts shimmered, casting a mesmerizing radiance.
Whispers of greed and awe intertwined as adventurers beheld the riches that stirred their desires.''')
        input('')
        print('...The End...')
    else:
        print(f'''That was a rough fight, and no one killed the beast before. So didn't our hero...''')
        input('')
        print('...The End...')

def make_choice(first_option, second_option):
    while True:
        try:    
            print(f'''\nNow you got 2 options: \n1. {first_option} \n2. {second_option}''')
            choice = int(input("You choose ==> "))
            if choice == 1:
                return first_option
            elif choice == 2:
                return second_option
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print('Invalid input. Please enter a number.')






