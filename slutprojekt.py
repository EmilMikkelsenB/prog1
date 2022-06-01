import random
#klasser eller karaktärer man kanköra som i en dictonary
avaliable_classes = {
    #klassen tank har 500hp och 20 attack
        "tank": {
                "health": 500,
                "attack": 500
        },
    #klassen assasin har 300hp och 50 attack
        "assasin": {
                "health": 300,
                "attack": 50
        },


}
#en funktion där man väljer klass som spelare
def class_choice():
    #visar vilka som finns
    print(*avaliable_classes)

    choosen_class = input("Välj en klass, ")
    #plockar värden från dictonary
    if choosen_class in avaliable_classes.keys():
            pc_class = avaliable_classes[choosen_class]
            health  = pc_class["health"]
            attack = pc_class["attack"]
    
    return health,attack

#funktion där spelarens val sätts igång.
def player():
    #kallar på funktionen så att variablerna kommer
    health,attack  = class_choice()
    player_hp = health
    player_atk = attack
    #printar spelare för att enkelt se skillnad
    print('------spelare------')
    
    print(player_hp,'hp')
    print(player_atk, 'atk')
    return player_hp,player_atk
#andra "spelaren"
def cpu():
    #händer samma sak som i class choice funktionen fast för datorn denna gång
    cpu_class = random.choice(list((avaliable_classes)))
    
    #hämtar värden från dict:en
    cc_class = avaliable_classes[cpu_class]
    cpu_hp  = cc_class["health"]
    cpu_atk = cc_class["attack"]
#printar cpu för enkelt kunna se skillnad
    print('\n------CPU-------')
    print(cpu_class)
    print(cpu_atk)
    print(cpu_hp)
    return cpu_hp,cpu_atk

def turn():
    turn = random.randint(1,2)
    if turn == 1:
        player_turn = True
        cpu_turn = False
    if turn == 2:
        player_turn = False
        cpu_turn = True
    return player_turn, cpu_turn
    

def game():
    player_points = 0

    player_turn,cpu_turn = turn()
    player_hp,player_atk = player()
    cpu_hp,cpu_atk = cpu()
    
    while player_hp > 0:
        if player_turn == True:
                print('\nDin tur')
                move_choice = int(input('Vad vill du göra? Attackera(1), Läka(2) '))
                if move_choice == 1:
                    cpu_hp -= player_atk
                    print('Du attackerade fienden och gjorde', player_atk, 'i skada. Fienden har nu', cpu_hp, 'hp')
                    if cpu_hp <= 0:
                        #väljer en ny fiende
                        print('\nDu dödade datorn, en ny fiende uppstod')
                        player_points += 1
                        print('du har nu',player_points,'poäng')
                        cpu_hp = 0
                        cpu_hp , cpu_atk = cpu()

                elif move_choice == 2:
                    player_hp += random.randint(20,30)
                    print('Du läkte och har nu', player_hp,'hp')
                player_turn = not player_turn
                cpu_turn = not cpu_turn

        

        if cpu_turn == True:
            print('\nDatorns Tur')
            cpu_move_choice = random.randint(1,2)
            if cpu_move_choice == 1:
                player_hp -= cpu_atk
                print('Datorn attackerade dig och skadade', cpu_atk, 'du har nu', player_hp,'hp')
            elif cpu_move_choice == 2:
                cpu_hp += random.randint(20,30)
                print('Datorn läkte och har nu', cpu_hp,'hp')


            player_turn = not player_turn
            cpu_turn = not cpu_turn
    if player_hp <= 0:
        name_save = input('du förlorade, skriv in ditt namn för topplistan: ')
        score_save = {
            'Namn':[],
            'Poäng':[]
        }
        score_save['Namn'].append(name_save)
        score_save['Poäng'].append(player_points)
        print(score_save)
        return score_save

def sort():
    score_save = game()
    print(score_save)
    list(score_save.items())

game()   
#sort()