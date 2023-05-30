from adventure_game_functions import*


print(f'''\nWelcome Hero!\nYour Stats:\nHP ==> {Link.get('health')}\nAttack ==> {Link.get('atack')}\nDef. ==> {Link.get('defence')}''')
print('''\nYou enter the Cave to defete a demonic evil terorise this lands for past 10 years''')
input('')


while Link.get('health') > 0:
        if entrance() == 'passage':
            if rope_bridge() == 'trespass':
                if make_choice('Trainee field', 'Barracks') == 'Trainee field':
                    trainee_field()
                    while True:
                        if make_choice('Passage','Empty room') == 'Passage':
                            if rope_bridge() == 'trespass':
                                arena()
                                break
                            else:
                                continue
                        else:
                            empty_room()
                            arena()
                            break
                else:
                    barracks()
                    if make_choice('Pasage','Enother labratory') == 'Passage':
                        if rope_bridge() == 'trespass':
                            arena()
                            break
                    else:
                        laboratory()
                        arena()
                        break        
            else:
                print("\nSo you choose return back")
                continue
        else:
            laboratory()
            if make_choice('Armory','Go back') == 'Armory':
                armory()
                if make_choice('Trainee field','Barracks') == 'Trainee field':
                    trainee_field()
                    while True:
                        if make_choice('Passage','Empty room') == 'Passage':
                            if rope_bridge() == 'trespass':
                                arena()
                                break
                            else:
                                continue
                        else:
                            empty_room()
                            arena()
                            break
                else:
                    barracks()
                    if make_choice('Pasage','Enother labratory') == 'Passage':
                        if rope_bridge() == 'trespass':
                            arena()
                            break
                    else:
                        laboratory()
                        arena()
                        break
            else:
                print("\nSo you choose return back")
                continue
