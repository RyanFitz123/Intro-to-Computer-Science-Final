import random
import time

class Character:
    def __init__ (self, name):
        self.name = name

    def a1 (self, a1_name):
        self.a1_atk = int(self.atk)
        self.a1_name = a1_name
        self.a1_ult_gain = int(self.ult_gain)
        #Sets up the frame for attack 1

    def b1 (self, b1_name, x, y): #Parameter 2 is a multiplier to change the damage of the second attack. Parameter 3 is a multiplier to change the amound of Ult charge gained for the second attack
        self.b1_atk = int(self.atk * x)
        self.b1_name = b1_name
        self.b1_ult_gain = int(self.ult_gain * y)
        #Sets up from for attack 2

    def ult (self, ult_name, x):
        self.ult_name = str(f"Ultimate: {ult_name}")
        self.ult_atk = self.atk * x
        #Sets up frame for the Ultimate Move
#Creates a parent class so more characters can be made off of it
        
class Fighter (Character):
    def __init__ (self, name, hp, atk, ult_charge, ult_gain):
        Character.__init__(self, name)
        self.hp = int(hp)
        self.atk = int(atk)
        self.move_list = []
        self.ult_charge = ult_charge
        self.ult_gain = ult_gain
        #Initializes the stats for the Fighter Class

    def Display (self):
        print(f"{self.name} is a strong melee based fighter with {self.hp} HP. Their moves are {self.a1_name}, and {self.b1_name}. Their {self.ult_name} is their strongest move!")
        #Displays Fighter Class information

    def Display_Moves (self):
        print(f"\n{self.a1_name}: {self.a1_atk} attack \n{self.b1_name}: {self.b1_atk} attack \n{self.ult_name}: {self.ult_atk} attack, {self.ult_name} ({self.ult_charge_battle}/{self.ult_charge})")
        #Displays Fighter Class moves

#Creates the first class type which is a more standard class

class Weapon_Fighter (Character):
    def __init__ (self, name, hp, atk, ult_charge, ult_gain):
        Character.__init__(self, name)
        self.hp = int(hp)
        self.atk = int(atk)
        self.move_list = []
        self.ult_charge = ult_charge
        self.ult_gain = ult_gain
        #Initializes the stats for the Weapon Fighter Class

    def Display (self):
        print(f"{self.name} is a strong weapon based fighter with {self.hp} HP. Their moves are {self.a1_name}, and {self.b1_name}. Their {self.ult_name} is their strongest move!")
        #Displays Weapon Fighter information
        
    def Display_Moves (self):
        print(f"\n{self.name} Moves: \n{self.a1_name}: {self.a1_atk} attack \n{self.b1_name}: {self.b1_atk} attack \n{self.ult_name}: {self.ult_atk} attack, {self.ult_name} ({self.ult_charge_battle}/{self.ult_charge})")
        #Displays Weapon Fighter moves

#This is a class that differs from the Fighter class because a weapon will do more damage
#The punch is replaced by the weapon and the second move is weaker for balance

bear = Fighter("Bear", 100, 14, 7, 2)
bear.a1("Slash")
bear.b1("Kick", 1.2, 0.5)
bear.ult("Bear Tackle", 2.14)

sword_user = Weapon_Fighter("Sword User", 80, 20, 9, 1)
sword_user.a1("Sword")
sword_user.b1("Kick", 0.6, 2)
sword_user.ult("Piercing Strike", 1.8)

hammer_user = Weapon_Fighter("Hammer User", 110, 13, 8, 1)
hammer_user.a1("Hammer")
hammer_user.b1("Brick Throw", 0.3, 4)
hammer_user.ult("Shot Put", 1.2)
#Creates the classes 

c1 = bear
c2 = sword_user
c3 = hammer_user
#Creates the characters


c1.move_list = (c1.a1_name, c1.b1_name, c1.ult_name)
c2.move_list = (c2.a1_name, c2.b1_name, c2.ult_name)
c3.move_list = (c3.a1_name, c3.b1_name, c3.ult_name)
#Creates a tuple of the character's moves

all_characters = (c1.name, c2.name, c3.name)
#Creates a tuple of every character

def See_Info():
    print("\nCharacter Info:")
    c1.Display()
    c2.Display()
    c3.Display()

    #Function to display information on all characters

def Choose_Character():
    global chosen
    global cpu_chosen
    #Globalizes variables

    #Every output text has \n because I think it makes the formatting nice and easier to read. I can also group related text together like answers which aren't seperated by a line or "double-spaced"
    while True:
        chosen = str(input(f"\nSelect your character: \n [A]: {c1.name} \n [B]: {c2.name} \n [C]: {c3.name} \n [D]: See Character Info \n ")).lower()
        if chosen == "a":
            chosen = c1
        elif chosen == "b":
            chosen = c2
        elif chosen == "c":
            chosen = c3
        elif chosen == "d":
            See_Info()
        try:
            if chosen.name in all_characters:
                break
        except:
            if chosen != "d":
                print("\nInvalid input, please try again")
            continue
        #Creates a menu with multiple options and prevents input error
    
    if chosen == "a":
        chosen = c1
    elif chosen == "b":
        chosen = c2
    elif chosen == "c":
        chosen = c3
    #Connects the input to a character
    try:
        print(f"\nYou have selected: {chosen.name}")
    except:
        print("\nInvalid input, please try again")
        Choose_Character()
        return
    #This is the other Try and Except that will be used in the code actually
    #Outputs what you chose


#Allows you to choose a character and stores it in a variable "chosen"
    while True:
        cpu_chosen = random.randint(1, 3)
        if cpu_chosen == 1:
            cpu_chosen = c1
        elif cpu_chosen == 2:
            cpu_chosen = c2
        elif cpu_chosen == 3:
            cpu_chosen = c3
        if chosen != cpu_chosen:
            break
    print(f"\nCPU has chosen: {cpu_chosen.name}")
    #Assigns a random character to the CPU
    #The CPU will never be the same character as the player. I couldn't figure out why their HP wasn't seperate :')

def Battle(player, cpu):
    global chosen_move
    global cpu_move
    #Globalizes the variables

    print("\nBattle Start!")
    player.hp_battle = int(player.hp)
    cpu.hp_battle = int(cpu.hp)
    player.ult_charge_battle = 0
    cpu.ult_charge_battle = 0
    #Stores the normal HP and Ult values in variables that can safely be modified without affecting the orginial values

    while player.hp_battle > 0 or cpu.hp_battle > 0:
    #The battle will continue as long as each person has above 0 HP
        
        print(f"\nPlayer HP: {player.hp_battle} , Player Ultimate Charge: ({player.ult_charge_battle}/{player.ult_charge}) \nCPU HP: {cpu.hp_battle} , CPU Ultimate Charge: ({cpu.ult_charge_battle}/{cpu.ult_charge})")
        #Creates a menu of multiple options
        
        chosen_move = ""
        cpu_move = ""
        #Resets move values

        while chosen_move not in player.move_list:
            chosen_move = str(input(f"\nSelect your move: \n [A]: {player.a1_name} \n [B]: {player.b1_name} \n [C]: {player.ult_name} ({player.ult_charge_battle}/{player.ult_charge}) \n [D]: See Move Info \n ")).lower()
            if chosen_move == "a":
                chosen_move = player.a1_name
            elif chosen_move == "b":
                chosen_move = player.b1_name
            elif chosen_move == "c":
                if player.ult_charge_battle >= player.ult_charge:
                    chosen_move = player.ult_name
                else:
                    print(f"\nYou can't use your Ultimate Move just yet! Your Ultimate is {player.ult_charge_battle}/{player.ult_charge} charged!")
                #Prevents the Ult from being used too early
            elif chosen_move == "d":
                player.Display_Moves()
            elif chosen_move not in player.move_list:
                print("\nThat move is not in the game, please try again")
        #Connects input to a move and prevents input error
                
        if chosen_move == player.a1_name:
            player.atk = player.a1_atk
            player.ult_charge_battle += player.a1_ult_gain
        elif chosen_move == player.b1_name:
            player.atk = player.b1_atk
            player.ult_charge_battle += player.b1_ult_gain
        elif chosen_move == player.ult_name:
            player.atk = player.ult_atk
            player.ult_charge_battle = 0
            #Resets Ult charge after use
        #Connects the player response to an actual move, and an attack value

        print(f"\nYou use {chosen_move}! You now have {player.ult_charge_battle}/{player.ult_charge} Ultimate Charge!")
        #Outputs your chosen move and updated Ult charge
        time.sleep(0.5)
        #Timer so text doesn't go super fast with all the information
        cpu.hp_battle -= player.atk
        #Damage calculation for the CPU
        print(f"\nYou did {player.atk} damage!")
        #Outputs your damage
        if cpu.hp_battle > 0:
            print(f"\n CPU has {cpu.hp_battle} HP remaining!")  
            #Outputs CPU HP if above 0
        time.sleep(1)

        if cpu.hp_battle <= 0:
            print("\nCPU HP was reduced to 0 \nPlayer wins!")
            break
        #Ends battle if CPU HP is equal to or below 0

        if cpu.ult_charge_battle >= cpu.ult_charge:
            cpu_move = cpu.ult_name
            cpu.atk = cpu.ult_atk
            cpu.ult_charge_battle = 0
            #Resets Ult charge after use
            #If CPU has Ult available they will use it
        else:
            cpu_move = str(random.randint(1, 2))
            if cpu_move == "1": #This is move a1
                cpu_move = cpu.a1_name
                cpu.atk = cpu.a1_atk
                cpu.ult_charge_battle += cpu.a1_ult_gain
            elif cpu_move == "2": #This is move b1
                cpu_move = cpu.b1_name
                cpu.atk = cpu.b1_atk
                cpu.ult_charge_battle += cpu.b1_ult_gain
        #Assigns a random move to the CPU, and an attack value

        print(f"\nCPU used {cpu_move}! CPU now has {cpu.ult_charge_battle}/{cpu.ult_charge} Ultimate Charge!")
        #Outputs the CPU's chosen move and the CPU's updated Ult charge
        time.sleep(0.5)
        player.hp_battle -= cpu.atk
        #Damage calculation for the player
        print(f"\nCPU did {cpu.atk} damage!")
        #Outputs CPU's damage
        if player.hp_battle > 0:
            print(f"\n You have {player.hp_battle} HP remaining!")    
            #Outputs player HP if above 0
        time.sleep(0.5)

        if player.hp_battle <= 0:
            print("\nPlayer HP was reduced to 0 \nCPU wins!")
            break
        #Ends the battle if player HP is below 0

    while True:
        selection = str(input("\nWould you like to play again? \n [A]: Yes \n [B]: Change Character \n [C]: Quit \n ")).lower()
        if selection == "a" or selection == "b" or selection == "c":
            break
        else:
            print("\nInvalid input, please try again")
        #Creates a menu with multiple options
    if selection == "a": #Battle again with same characters
        Battle(chosen, cpu_chosen)
    elif selection == "b": #Battle again with different characters
        Game_Loop()
    elif selection == "c": #Quit the game
        quit()
#This allows battles to happen


while True:
    selection = str(input("\nWhat would you like to do? \n [A]: Start \n [B]: Quit \n ")).lower()
    try:
        if selection == "a" or selection == "b":
            break
        else:
            print("\nInvalid input, please try again")
    except:
        continue
    #I don't like to use these so here is a try and except 
#Starts the game or you can quit

def Game_Loop():
    Choose_Character()
    while True:
        ready = str(input("\nReady to start the battle? \n [A]: Ready \n [B]: Switch Character \n ")).lower()
        if ready == "a" or ready == "b":
            break
        else:
            print("\nInvalid input, please try again")
        #Creates a menu with multiple options
    if ready == "a":
        Battle(chosen, cpu_chosen)
        #Calls the battle function using the player and CPU chosen characters
    elif ready == "b":
        Game_Loop()
        #Calls the Game Loop function so you can choose your character again
#Makes a loop so that you can restart this to play again, choose your character, and not have to choose start or quit

if selection == "a":
    Game_Loop()
    #Starts the Game Loop after you choose to start the game
elif selection == "b":
    quit()
    #Quits the game