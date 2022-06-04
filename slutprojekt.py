from asyncore import write
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

#bestämmer vem som ska börja matchen
def turn():
    #slumpar ett tal, 1 eller 2. 
    turn = random.randint(1,2)
    if turn == 1:
        #ifall det är 1 är det spelaren som börjar, 2 så är det tvärtom
        player_turn = True
        cpu_turn = False
    if turn == 2:
        player_turn = False
        cpu_turn = True
    return player_turn, cpu_turn
    
#spelet startar
def game():
    #sätter spelarens poäng till noll
    player_points = 0

    #hämtar värden för hp,attack och vems tur det är
    player_turn,cpu_turn = turn()
    player_hp,player_atk = player()
    cpu_hp,cpu_atk = cpu()
    #en loop som gäller medans spelaren är vid liv
    while player_hp > 0:
        #ifall det är spelares tur börjar man här
        if player_turn == True:
                print('\nDin tur')
                #väljer de olika attakerna
                move_choice = int(input('Vad vill du göra? Attackera(1), Läka(2) '))
                if move_choice == 1:
                    #attak, fienden tar skada
                    cpu_hp -= player_atk
                    print('Du attackerade fienden och gjorde', player_atk, 'i skada. Fienden har nu', cpu_hp, 'hp')
                    #ifall du dödar fienden med din attak kommer det en ny, detta gör så man kan få fler poäng
                    if cpu_hp <= 0:
                        #väljer en ny fiende
                        print('\nDu dödade datorn, en ny fiende uppstod')
                        player_points += 1
                        print('du har nu',player_points,'poäng')
                        #återställer hp på datorn 
                        cpu_hp = 0
                        cpu_hp , cpu_atk = cpu()
                #val två, vilket är att läka 
                elif move_choice == 2:
                    #väljer ett slumpat tal mellan 20 och 30, man kan få mer hp än det man böjrar med som en strategi
                    player_hp += random.randint(20,30)
                    print('Du läkte och har nu', player_hp,'hp')

            #ändrar så att värdet blir tvärtemot, alltså att true blir false och att false blir true
                player_turn = not player_turn
                cpu_turn = not cpu_turn

        
        #här börjar datorn, får samma val som spelaren
        if cpu_turn == True:
            print('\nDatorns Tur')
            cpu_move_choice = random.randint(1,2)
            if cpu_move_choice == 1:
                player_hp -= cpu_atk
                print('Datorn attackerade dig och skadade', cpu_atk, 'du har nu', player_hp,'hp')
            elif cpu_move_choice == 2:
                cpu_hp += random.randint(20,30)
                print('Datorn läkte och har nu', cpu_hp,'hp')

            #ändrar så att värdet blir tvärtemot, alltså att true blir false och att false blir true
            player_turn = not player_turn
            cpu_turn = not cpu_turn
    
    return player_points

#funktionenn som skapar highscore listan samt textfilerna
def highscore():
    player_points = game()
    names = []
    points = []

    #skriver in anvädarens namn för att koppa t poängen
    name_save = input('du förlorade, skriv in ditt namn för topplistan: ')
        
    #lägger till poäng och namn i respektvive lista
    names.append(name_save)
    points.append(player_points)

    #öppnar den första textfilen
    with open('HS_unsorted.txt','a') as w:
        #lägger till namn
        for items in names:
            #f" är en formatterad text vilket gör det enklare att läsa för människor 
            w.write(f"{items}.")
        #lägger till poäng
        for items in points:
            w.write(str(items))
        #gör att det blir en ny rad under värdet
        w.write('\n')

    
def load_and_sort():
    #skapar listan för highschores
    highscores = []

    #Öppnar den osorterade listan för att sortera
    read_scores = open('HS_unsorted.txt', 'r')
    for line in read_scores.readlines():
        line_parts = line.split('.')
        line_parts[1] = int(line_parts[1].replace('\n', '')) # tabort newline på scoren och gör till int
        highscores.append([line_parts[0], line_parts[1]]) 
    read_scores.close()

    sorted_list = own_sort(highscores)
    
    with open('HS_sorted', 'w') as w:
        for items in sorted_list:
            w.write(f"{items}.")
        w.write('\n')

    
    return sorted_list 
    
#sorterar nummerna i listan
def own_sort(numbers):
    output = []
    only_strings = [inner[0] for inner in numbers]
    only_numbers = [inner[1] for inner in numbers]
    while only_numbers:

        biggest = max(only_numbers)
        biggest_number_index = only_numbers.index(biggest)
        output.append([only_strings.pop(biggest_number_index), only_numbers.pop(biggest_number_index)])

    print(output)
    return output
#highscore()
load_and_sort()