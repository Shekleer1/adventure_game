from adventure_game_functions import*

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
            choice = int(input('1. Take the way through an old cave passage.\n2. Enter laboratory\n ==> '))
            if choice == 1:
                return 'passage'
            elif choice == 2:
                return 'lab'
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print("Invalid input. Please enter a number.")



def laboratory():
    print(f'''Within the timeworn laboratory's dim-lit chambers, arcane contraptions stood dormant, their purpose shrouded in mystery.
Cracked vials and faded parchments adorned the cluttered tables, remnants of forgotten experiments that echoed with the whispers of forgotten sorcery.''')
    input('')
    print(f'''Beneath a pile of an old rusty equioment you see a flacon with a bright red substance, seems a result of an old experiment.''')
    while True:
        try:  
            choice = int(input("1. Take a potion\n2. Not risk it\n ==> "))
            if choice == 1:
                print("As the healing potion touched their lips, renewed vigor surged within.")
                Link.increase('health', 3)
                print(f"Your Health ==> {Link.get('health')}")
                input('')
                print(f'''Looking over you mention an armory.
1.Go to the armory. 2. Return back to a passege way.''')
                while True:
                    try:
                        choice = int(input("==> "))
                        if choice == 1:
                            return "armory"
                        elif choice == 2:
                            return 'passage'
                        else:
                            print('Invalid choice. Please enter 1 or 2.')
                    except ValueError:
                        print('Invalid input. Please enter a number.')
            elif choice == 2:
                print("It's better not to play with such ansient magic. Good choice.")
                input('')
                print(f'''Looking over you mention an armory.
1.Go to the armory. 2. Return back to a passege way.''')
                while True:
                    try:
                        choice = int(input("==> "))
                        if choice == 1:
                            return "armory"
                        elif choice == 2:
                            return 'passage'
                        else:
                            print('Invalid choice. Please enter 1 or 2.')
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    
def armory():
    print(f'''In the dusty recesses of the ancient armory, rows of rusted weapons stood sentinel.
A lingering scent of valor and battles long past permeated the air.
Shields adorned with heraldry bore witness to a bygone era of knights and conquest.''')
    weapon_shield(0,1)
    input('')
    print(f'''From an armory there's 2 way's out. One of which lead to the next room, apear as trainee field.
The other look's like a barracks door''')
    while True:
        try:
            choice = int(input("1. Trainee field. 2. Barracks ==> "))
            if choice == 1:
                return 'Trainee field'
            elif choice == 2:
                return 'barracks'
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print('Invalid input. Please enter a number.')



def rope_bridge():
    print('''Deep within the heart of a cavernous abyss, a fragile rope bridge spanned the darkness.
Dim torchlight flickered, revealing stalactites that dripped with anticipation.
Each cautious step echoed, harmonizing with the distant whispers of forgotten spirits lurking in the shadows''')
    while True:
        try:
            choice = int(input('''Do you dare to trespass? 1. Go ahed 2. Turn back ==> '''))
            if choice == 1:
                bridge_poison_calc(1, 0)
                return 'trespass'
            elif choice == 2: 
                return 'return'
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print('Invalid input. Please enter a number.')

def trainee_field():
    print(f'''In the hidden recesses of the cave, a training field emerged, bathed in a mystical glow.
Novice warriors honed their skills amidst rugged terrain, guided by seasoned masters.
Echoes of clashing blades and resolute shouts reverberated, echoing through the hallowed chambers.
''')
    input('')
    weapon_shield(1, 0)
    while True:
        try:
            choice = int(input(f'''two way's: \n1. passage 2. empty room ==> '''))
            if choice == 1:
                return 'passage'
            elif choice == 2:
                return 'empty room'
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print('Invalid input. Please enter a number.')





def barracks():
    print('''Within the cavern's embrace, a makeshift barracks stood as a haven for weary warriors.
Flickering torches cast dancing shadows upon stone walls adorned with tattered banners.
Tense whispers of camaraderie mingled with the distant rumblings of imminent conflict.
''')
    input('')
    print(f'''In the heart of the chamber, a spectral knight stood, his ethereal armor gleaming with an otherworldly light.
Haunting eyes pierced the darkness, revealing a tortured soul bound to the mortal realm, forever guarding ancient secrets with a spectral sword at the ready.''')
    while True:
        try:
            choice = int(input("Would you dare take this fight?\n1. Take the fight\n2. Return ==> "))
            if choice == 1:
                hp = Link.get('health')
                if fight(Link, Ghost_knight):
                    Link.set('health', hp)
                    print("After a fight, Link falls into a deep sleep and restores his HP.")
                    weapon_shield(1, 0)
                else:
                    print("R.I.P Link")
                break
            elif choice == 2:
                return 'return'
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")








