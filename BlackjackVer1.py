#random anvönds för att slumpmässigt välja kort från däcket
import random

#gör däcket som används för att dra kort ut senare
def deck_generator():
    #färg på korten
    classes = ['♥', '♦', '♠', '♣']
    #däck utan färger
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung", "ess"]
    #här läggs korten från deck + färg in senare
    full_deck = []
    #lägger in skapar och lägger in kort, med färg och siffra
    for x in classes:
        for number in deck:
            #Lägger till ett mellanslag mellan färg och siffa, används senare
            full_deck.append(x + ' ' + str(number))
        #blandar runt kortleken
        random.shuffle(full_deck)
    return full_deck

#Ger värde till korten    
def score_count(player_hand):
    score = 0
    for cards in player_hand:
        #Här används mellanslaget innan som en form av sepation av nummret och siffran, detta görs för att kunna avläsa siffran, och gör det till en int igen
            if cards.split(" ")[1].isnumeric():
                score += int(cards.split(" ")[1])
            if cards.split(' ')[1] == "knekt":
                score += 10
            if cards.split(' ')[1] == "dam":
                score += 10
            if cards.split(' ')[1] == "kung":
                score += 10
            #ifall korten + ess blir större än 21 blir esset automatiskt en 1a, annars är det en 11
            if cards.split(' ')[1] == "ess":
                if score + 11 >= 21:
                    score += 1
                else: 
                    score += 11
    return score
#ger korten värde för dealern, likt för spelaren över
def score_count_dealer(dealer_hand):
    dealer_score = 0
    for cards in dealer_hand:
            if cards.split(" ")[1].isnumeric():
                dealer_score += int(cards.split(" ")[1])
            if cards.split(' ')[1] == "knekt":
                dealer_score += 10
            if cards.split(' ')[1] == "dam":
                dealer_score += 10
            if cards.split(' ')[1] == "kung":
                dealer_score += 10
             #ifall korten + ess blir större än 21 blir esset automatiskt en 1a, annars är det en 11    
            if cards.split(' ')[1] == "ess":
                if dealer_score + 11 >= 21:
                    dealer_score += 1
                else: 
                    dealer_score += 11 
    return dealer_score
#förbereder spelet
def setup():
    full_deck = deck_generator()
    player_hand = [(random.choice(full_deck)),(random.choice(full_deck))]
    dealer_hand = [(random.choice(full_deck))]
    return player_hand, dealer_hand

#spelet startar
def game_start():
    #importerar variabler och kallar på funktioner
    player_hand , dealer_hand = setup()
    score = score_count(player_hand)
    dealer_score = score_count_dealer(dealer_hand)
    full_deck = deck_generator()
    #Stand = inte hit, quit = spelet klart
    stand = False
    quit = False
    #Inledande text, hur många kort du har och ifall man vill dra fler
    print('du har ', *player_hand)
    print('Totalt:',score)
    print('Husets första kort är', *dealer_hand)
    print('totalt:',dealer_score)

    #Själva spelet
    while quit == False:
        #BLACKJACK!
        if player_hand == 21:
            print('du fick blackjack och vann!')
            quit = True

        #dra ett till kort = hit
        #Medans stand = false kan man forstätta dra kort, tills man är över 21 dvs
        while stand == False:
            hit = input('Vill du dra ett till kort?: ')
            if hit == 'ja':
                player_hand.append(random.choice(full_deck))
                score = score_count(player_hand)
                print('du har nu', *player_hand)
                print('Totalt:',score)
            #ifall man har över 21 förlorar man
            if score > 21:
                print('Du kom över 21, du förlorade')
                quit= True 
        #stand, alltså inte ta ett till kort
            else:
                print('du har',*player_hand)
                stand = True
                quit = True

        #Ifall dealern ska ta mer kort, det brukar oftas hända runt 17
        if dealer_score < 17:
            while dealer_score < 17:
                dealer_hand.append(random.choice(full_deck))
                dealer_score = score_count_dealer(dealer_hand)
        print('dealern har:',*dealer_hand)
        print('totalt:',dealer_score)

        #resultats redovisning
        if quit == True:
            if dealer_score > 21:
                print('dealern kom över 21, du vann')
                
            elif score > dealer_score:
                print('du van över dealern, med:', score, 'dealern hade:', dealer_score)
            elif score < dealer_score:
                print('du hade mindre än dealern och förloade')
            elif score == dealer_score:
                print('det blev lika')


#startar spelet    
game_start()