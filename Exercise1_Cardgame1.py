import enum 
import random

# card class holds the characterstic of cards
class Card:
    def __init__(self, id, name, health, agility, damage, attack_range, intelligence):
        self.id = id
        self.name = name
        self.health = health
        self.agility = agility
        self.damage = damage
        self.attack_range = attack_range
        self.intelligence = intelligence

    def print_data(self):
        print ("Card [" + str(self.id)
        + "] [" + str(self.name) 
        + "] [Health = " + str(self.health) 
        + "] [Agility = " + str(self.agility)
        + "] [Damage = " + str(self.damage)
        + "] [Range = " + str(self.attack_range)
        + "] [Intelligence = " + str(self.intelligence)
        + "] ")


# deck class holds the list of cards
class Deck:
    def __init__(self, name):
        self.cards = []
        self.name = name

    # push the card
    def push_card(self, new_card):
        self.cards.append(new_card)
        #new_card.print_data()

    # pop the card
    def pop_card(self):
        if len(self.cards) > 0:
            cur_card = self.cards[len(self.cards) - 1]
            #cur_card = self.cards[0]
            self.cards.remove(cur_card)
            return cur_card
        else:
            return -1

    # get only the card details
    def get_top_card_details(self):
        if len(self.cards) > 0:
            cur_card = self.cards[len(self.cards) - 1]
            return cur_card
        else:
            return -1

    def get_card(self, index):
        if index >= 0 and index < len(self.cards):
            cur_card = self.cards[index]
            self.cards.remove(cur_card)
            return cur_card
        else:
            return -1
            

    # create the cards
    def create_cards(self, names_list):
        for i in range(len(names_list)):
            cur_card = Card(i, names_list[i], 300 - i * 10, 40 - i, 30 - i, 1000 + i * 100, 50 + i * 5)
            self.push_card(cur_card)


    def print_data(self):
        if len(self.cards) <= 0:
            print(self.name + " [ Cards = 0 ]")
        else:            
            print(self.name + " [ Cards = " + str(len(self.cards)) + " ]")
            for cur_card in self.cards:
                cur_card.print_data()

    def shuffle_cards(self):
        #print ("Shuffling cards in " + self.name )
        random.shuffle(self.cards)
        #self.print_data()


    def get_total_cards(self):
        return len(self.cards)


# player class 
class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cards = Deck(name + " Deck")
        self.dice = 0
        self.points = 0
        self.god_spell = False
        self.res_spell = False
    
    def add_card(self, new_card):
        self.cards.push_card(new_card)

    def get_card(self, index):
        return self.cards.get_card(index)

    def get_total_cards(self):
        return self.cards.get_total_cards()

    def get_top_card_details(self):
        return self.cards.get_top_card_details()
        
    def get_top_card(self):
        return self.cards.pop_card()

    def print_data(self):
        self.cards.print_data()


# Game states
class CardGameState(enum.Enum):
    Init = 1,
    MainMenu = 2,
    Playing = 3,
    GameOver = 4,
    RollingDice = 5,


# Card Game manager to handle the game
class CardGameManager:
    players = []
    player_turn = 0
    round_no = 1
    game_state = CardGameState.Init
    
    def __init__(self):
        self.main_deck = Deck("Main Deck")
        self.outdated_deck = Deck("Outdated Deck")


    def create_decks(self):
        print("Creating Cards")
        names_list = [ "Captain Marvel",
        "Thanos",
        "Vision",
        "Doctor Strange",
        "Scarelet witch",
        "Iron Man",
        "Hulk",
        "Wolverine",
        "Black Panther",
        "Captain America",
        "Ant Man",
        "Black Widow",
        "Hawk eye",
        "Spider Man",
        "Nick Fury",
        "Shuri" ]              
        self.main_deck.create_cards(names_list)
        self.outdated_deck.create_cards([])


    def print_all_decks(self):
        self.main_deck.print_data()
        self.outdated_deck.print_data()

    #create two players
    def create_players(self):
        players_01 = Player(1, "Player_01")
        self.players.append(players_01)

        players_02 = Player(2, "Player_02")
        self.players.append(players_02)        

    # give 5 cards to each player
    def distribute_cards(self):
        for i in range(5):
            self.players[0].add_card(self.main_deck.pop_card())
            self.players[1].add_card(self.main_deck.pop_card())


    def print_all_players(self):
        print ("-------- Players --------")
        self.players[0].print_data()
        self.players[1].print_data()

    # initialize the game
    def init_game(self):
        print ("\n-------- Initializing --------")
        CardGameManager.players = []
        CardGameManager.player_turn = 0
        CardGameManager.round_no = 1
        self.main_deck = Deck("Main Deck")
        self.outdated_deck = Deck("Outdated Deck")
        self.game_state = CardGameState.Init
        print("Creating Decks")
        self.create_decks()
        print("Creating Players")
        self.create_players()
        print("Shuffling cards")
        self.main_deck.shuffle_cards()
        print("Distributing cards")
        self.distribute_cards()
        self.game_state = CardGameState.MainMenu

    def on_start_game(self):
        print ("\n ------------ Starting Game ------------\n") 
        self.game_state = CardGameState.RollingDice
        while self.game_state == CardGameState.RollingDice:
            self.rolling_dice()
            if self.players[0].dice == self.players[1].dice and self.players[0].dice != 0:
                print("Draw, rolling again")
            else:
                self.game_state = CardGameState.Playing


    # roll the dice 
    def rolling_dice(self):
        print ("Rolling Dice \n------------")
        for i in range(len(gm.players)):
            self.players[i].dice = random.randrange(1, 7)
            print(str(self.players[i].name) + " is rolling dice and value is [" + str(self.players[i].dice) + "]")


    # set the first player based on dice
    def set_first_player(self):
        CardGameManager.player_turn = 0
        highVal = self.players[0].dice
        for i in range(len(gm.players)):
            if(self.players[i].dice > highVal):
                CardGameManager.player_turn = i
            #print("[" + str(i) + "] : " + str(gm.players[i].dice))        
        print ("--------------------------------")
        print("First turn goes to " + str(self.players[CardGameManager.player_turn].name))
        print ("--------------------------------")

        # giving spells to player
        if CardGameManager.player_turn == 0:
            self.players[0].god_spell = True                                         
            self.players[0].res_spell = True
            self.players[1].res_spell = True
            self.players[1].god_spell = True
        else:
            self.players[0].res_spell = True
            self.players[1].god_spell = True
            self.players[1].res_spell = True
            self.players[0].god_spell = True


    # game play rounds
    def game_play_rounds(self):
        while self.game_state == CardGameState.Playing:
            print ("\n\n--------------------------------")
            print ("Round No " + str(CardGameManager.round_no) + " " + self.players[CardGameManager.player_turn].name + "'s turn")
            print ("--------------------------------")
            print (self.players[0].name + 
                " Cards: " + str(self.players[0].get_total_cards()) + 
                " Points: " + str(self.players[0].points))
            print (self.players[1].name + 
                " Cards: " + str(self.players[1].get_total_cards()) + 
                " Points: " + str(self.players[1].points))
            print ("-------- Menu --------")
            print ("Press P : Play Card ")
            print ("Press G : Use God Spell ")
            print ("Press R : Use Ressurect Spell ")
            #print ("Press Q : Quit Game ")
            print ("-------- x --------")
            choice = input( self.players[CardGameManager.player_turn].name + " Enter the choice : ")
            # todo remove "1"
            if(choice == "1" or choice == "p" or choice == "P"):
                print ("-------- x --------")
                self.attributes_menus()
            elif(choice == "2" or choice == "g" or choice == "G"):
                is_char_selected = False
                if self.players[CardGameManager.player_turn].god_spell == True:
                    while is_char_selected == False:
                        top_card = self.players[CardGameManager.player_turn].get_top_card_details()
                        print ("Current card :  [ " + str(top_card.name) + " ]" )
                        print ("-------- Select Characterstic --------")
                        print ("Press 1 : Select Health [ " + str(top_card.health) + " ]" )
                        print ("Press 2 : Select Agility [ " + str(top_card.agility) + " ]" )
                        print ("Press 3 : Select Damage [ " + str(top_card.damage) + " ]" )
                        print ("Press 4 : Select Attack Range [ " + str(top_card.attack_range) + " ]" )
                        print ("Press 5 : Select Intelligence [ " + str(top_card.intelligence) + " ]" )
                        #print ("Press Q : Quit Game")
                        print ("-------- x --------")
                        choice1 = input("Enter the choice for characterstic : ")
                        self.execute_gods_spell()
                        self.execute_round(choice1)
                        is_char_selected = True
                elif(self.players[CardGameManager.player_turn].god_spell == False):
                    print ("-------- x --------")
                    print("*****Spells Warning:GOD spell can be casted only once by each player. continue with other options from the menu*****")
                    print ("-------- x --------")
                       
                else:
                     continue
                                               
                    # elif(choice == "q" or choice == "Q"):
                    #     self.on_game_end()
                    #     return
              
            elif(choice == "3" or choice == "r" or choice == "R"):
                if self.players[CardGameManager.player_turn].res_spell == True:
                    self.execute_ressurect()
                    self.attributes_menus()
                else:
                    print ("-------- x --------")
                    print("*****Spells Warning:Resurrect spell can be casted only once by each player in the game.Continue to play with other options from Menu***** ")
                    print ("-------- x --------")
                    continue
            # elif(choice == "q" or choice == "Q"):
            #     self.on_game_end()
            #     return        
            else:
                continue

            if(self.players[0].get_total_cards() > 0 and self.players[1].get_total_cards() > 0):
                CardGameManager.round_no += 1
            else:
                print ("--------------------------------")
                print ("Game over screen")
                print ("--------------------------------")
                print(self.players[0].name + " got " + 
                                str(self.players[0].points) + " points")
                print(self.players[1].name + " got " + 
                                str(self.players[1].points) + " points")
                print ("--------------------------------")
                print ("*********************************")
                if self.players[0].points > self.players[1].points:
                    print(self.players[0].name + " Wins the game")
                elif self.players[0].points < self.players[1].points:
                    print(self.players[1].name + " Wins the game")
                else:
                    print("Game is a tie between "+self.players[0].name + " and " +self.players[1].name)
                print ("*********************************")
                print ("--------------------------------\n\n\n")
                self.game_state = CardGameState.GameOver

    

    def execute_ressurect(self):
        print ("\n--------------------------------")
        print("Casting Resurrect spell")
        print ("--------------------------------\n")
        if self.outdated_deck.get_total_cards() > 0:
            #self.outdated_deck.print_data()
            #self.players[CardGameManager.player_turn].print_data()
            cur_card = self.outdated_deck.pop_card()
            self.players[CardGameManager.player_turn].add_card(cur_card)
            self.players[CardGameManager.player_turn].res_spell = False
            #self.outdated_deck.print_data()
            #self.players[CardGameManager.player_turn].print_data()
            print("Resurrection of [ " + cur_card.name + " ] is SUCCESS")
        else:
            print("status : Outdated deck empty")
        print ("--------------------------------\n")


    def execute_gods_spell(self):
        print ("\n--------------------------------")
        print("Casting Gods spell")
        print ("--------------------------------\n")
        self.players[CardGameManager.player_turn].god_spell = False
        self.opponent_cards_menus()


    def opponent_cards_menus(self):
        card_choosen = False        
        if CardGameManager.player_turn == 0:
            opponent_id = 1
        else:
            opponent_id = 0
        total_cards = self.players[opponent_id].get_total_cards()
        while card_choosen == False:
            print ("-------- Select Card --------")
            if total_cards >= 1 :
                print ("Press 1 : Play Card 1")
            if total_cards >= 2 :
                print ("Press 2 : Play Card 2")
            if total_cards >= 3 :
                print ("Press 3 : Play Card 3")
            if total_cards >= 4 :
                print ("Press 4 : Play Card 4")
            if total_cards >= 5 :
                print ("Press 5 : Play Card 5")
            print ("-------- x --------")
            choice = input("Select the card : ")
            if(choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5"):
                choice_int = int(choice) - 1
                if choice_int >= 0 and choice_int < total_cards:
                    #self.players[opponent_id].print_data()
                    selected_card = self.players[opponent_id].get_card(choice_int)
                    self.players[opponent_id].add_card(selected_card)
                    #self.players[opponent_id].print_data()
                    card_choosen = True
                    print("Opponent card [ " + selected_card.name + " ] has been selected from his deck")
                else:
                    continue
            else:
                continue

    # show Characterstic menu
    def attributes_menus(self):
        is_char_selected = False
        while is_char_selected == False:
            top_card = self.players[CardGameManager.player_turn].get_top_card_details()
            print ("Current card :  [ " + str(top_card.name) + " ]" )
            print ("-------- Select Characterstic --------")
            print ("Press 1 : Select Health [ " + str(top_card.health) + " ]" )
            print ("Press 2 : Select Agility [ " + str(top_card.agility) + " ]" )
            print ("Press 3 : Select Damage [ " + str(top_card.damage) + " ]" )
            print ("Press 4 : Select Attack Range [ " + str(top_card.attack_range) + " ]" )
            print ("Press 5 : Select Intelligence [ " + str(top_card.intelligence) + " ]" )
            #print ("Press Q : Quit Game")
            print ("-------- x --------")
            choice = input("Enter the choice : ")
            if(choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5"):
                self.execute_round(choice)
                is_char_selected = True
            # elif(choice == "q" or choice == "Q"):
            #     self.on_game_end()
            #     return
            else:
                continue


    # based on selection execute round based on choice and find winner
    def execute_round(self, choice):
        top_card_01 = self.players[0].get_top_card()
        top_card_02 = self.players[1].get_top_card()
        print ("-------- x --------")
        #print(top_card_01.name + " vs " + top_card_02.name)
        if(choice == "1"):
            print("Health : " + str(top_card_01.health) + " vs " + str(top_card_02.health))
            if top_card_01.health > top_card_02.health:
                self.on_player_wins(0)
            else:
                self.on_player_wins(1)
        if(choice == "2"):
            print("Agility : " + str(top_card_01.agility) + " vs " + str(top_card_02.agility))
            if top_card_01.agility > top_card_02.agility:
                self.on_player_wins(0)
            else:
                self.on_player_wins(1)
        if(choice == "3"):
            print("Damage : " + str(top_card_01.damage) + " vs " + str(top_card_02.damage))
            if top_card_01.damage > top_card_02.damage:
                self.on_player_wins(0)
            else:
                self.on_player_wins(1)
        if(choice == "4"):
            print("Attack Range : " + str(top_card_01.attack_range) + " vs " + str(top_card_02.attack_range))
            if top_card_01.attack_range > top_card_02.attack_range:
                self.on_player_wins(0)
            else:
                self.on_player_wins(1)
        if(choice == "5"):
            print("Intelligence : " + str(top_card_01.intelligence) + " vs " + str(top_card_02.intelligence))
            if top_card_01.intelligence > top_card_02.intelligence:
                self.on_player_wins(0)
            else:
                self.on_player_wins(1)
        
        # move the cards to the outdated deck and shuffle it
        self.outdated_deck.push_card(top_card_01)
        self.outdated_deck.push_card(top_card_02)
        self.outdated_deck.shuffle_cards()
        #self.outdated_deck.print_data()
        #self.players[0].print_data()
        #self.players[1].print_data()


    # on player win update the points, turn
    def on_player_wins(self, cur_player):
        print ("---------------- x ----------------")
        print ("Player " + self.players[cur_player].name + " Wins the round " + str(CardGameManager.round_no))
        print ("---------------- x ----------------")
        # give points to player based on winning
        self.players[cur_player].points += 1
        # change the player turn based on winning
        CardGameManager.player_turn = cur_player


    def on_game_end(self):
        print ("\n ------------ Game End ------------")

# Card Game manager
gm = CardGameManager()

# main function
def main():
    # game loop
    while gm.game_state != CardGameState.GameOver:
        # intialize the game
        gm.init_game()
      
        gm.on_start_game()
       
        gm.set_first_player()
       
        gm.game_play_rounds()

if __name__=="__main__":
    main()

