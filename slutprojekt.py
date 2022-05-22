import random
avaliable_classes = {
        "tank": {
                "health": 500,
                "attack": 20
        },
        "assasin": {
                "health": 300,
                "attack": 50
        }

}

def class_choice():
    print(*avaliable_classes)

    choosen_class = input("Välj en klass, ")

    if choosen_class in avaliable_classes.keys():
            pc_class = avaliable_classes[choosen_class]
            health  = pc_class["health"]
            attack = pc_class["attack"]
    
    return health,attack


def player():
    health,attack  = class_choice()
    player_hp = health
    player_atk = attack
    print('------spelare------')
    print(player_hp,'hp')
    print(player_atk, 'atk')
    return player_hp,player_atk

def cpu():
    cpu_class = random.choice(list((avaliable_classes)))
    cc_class = avaliable_classes[cpu_class]
    cpu_hp  = cc_class["health"]
    cpu_atk = cc_class["attack"]

    print('------CPU-------')
    print(cpu_class)
    print(cpu_atk)
    print(cpu_hp)
    return cpu_hp,cpu_atk

def game():
    cpu_hp,cpu_atk = cpu()
    player_hp,player_atk = player()

    print('du attakerade och skadade din fiende med:',player_atk)
    print(cpu_hp - player_atk)
game()

