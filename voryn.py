import random, time

class User:
    def __init__(self, char: str, dmg: int, hp: int):
        self.char = char
        self.dmg = dmg
        self.hp = hp
        self.defending = False

class Opponent:
    def __init__(self, name: str, hp: int, dmg: int):
        self.c_name = name
        self.c_hp = hp
        self.c_dmg = dmg

computer_player = Opponent("Rat", random.randint(60, 120), random.randint(20, 30))
computer_player2 = Opponent("Bigger Rat", random.randint(70, 120), random.randint(25, 35))
computer_player3 = Opponent("Rat King", random.randint(100, 200), random.randint(30, 45))

def random_encounter():
    if random.randint(1, 5) == 2 or 3:
        return True
        
print("""-----------------------------
|                             |
|      Hello Adventure        |   
|                             |
|     Welcome to Voryn        |
|            by: walt         |""")
print("""-----------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                |
|  The Town of Voryn is being overran by rats,   |
|    choose a hero to clean up the sewers.       |
|              Good Luck!                        |
|           Pick your hero:                      |
|                                                |
|      1.Warrior 2.Rogue 3.Paladin               |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
print("""========================================
|    Warrior            Rogue           |
|    HP:200             HP:750          |
|    DMG:25-45          DMG:60-80       |
|                                       |
|            Paladin                    |
|            HP:125                     |
|            DMG:45-65                  |
========================================""")

warrior = "Warrior"
rogue = "Rogue"
paladin = "Paladin"

while True:
 char = input("Choose your Champion:\n")
 if char == "1":
    player = User(warrior, random.randint(25, 45), 200)
    break
 if char == "2":
     player = User(rogue, random.randint(60 ,80), 75)
     break
 if char == "3":
     player = User(paladin, random.randint(45, 65), 125)
     break
 else:
     print("Invalid Choice")


print("++++++++++++++++++++++++++++++")
print("   Your Champion:", player.char ," ")
print("      Health:", player.hp,"     ")
print("      Damge:", player.dmg,"     \n")



while True:
    i = 0
    print("""++++++++++++++++++++++++++++++
           Welcome to Voryn       
    ______________________________
          1. Inn   2.Sewers       
    ______________________________""")
    route= input("Choose your destination:\n")
    if route == "1":
        heals = True
        while heals == True:
            if player.char == warrior and player.hp <= 250:
                player.hp = 250
                print("You are now well rested. Current HP:", player.hp)
                i = 0
                break
            elif player.char == paladin and player.hp <= 150:
                player.hp = 150
                print("You are now well rested. Current HP:", player.hp)
                i = 0
                break
            elif player.char == rogue and player.hp <= 100:
                player.hp = 100
                print("You are now well rested. Current HP:", player.hp)
                i = 0
                break
        continue



    if route == "2":
        print("Entering the Sewers\n")
        direction1 = input("""Which direction?\n 
        1. Left or 2.Right 3.Exit""")
        if direction1 == "1":
            print("You went Left")
            if random_encounter() == True:
                playing = True
                while playing:
                    if player.hp > 0 and computer_player.c_hp > 0:
                        print(player.char, ' is fighting' , computer_player.c_name, "Health:", computer_player.c_hp)
                        action = input("Choose an option: 1.Attack or 2.Defend\n")
                        if action == "1": 
                            computer_player.c_hp = computer_player.c_hp - player.dmg
                            time.sleep(2)
                            print(player.char, "attacked", computer_player.c_name)
                            print(computer_player.c_name, " is now at", computer_player.c_hp)
                        if action == "2":
                            print(player.char,  "is defending")
                            player.defending = True
                            time.sleep(2)
                            continue
                        else:
                            print("invalid Choice")
                    if computer_player.c_hp > 0 and player.defending == False:
                            time.sleep(2)
                            print(computer_player.c_name, "Attacked", player.char, "for", computer_player.c_dmg)
                            player.hp = player.hp - computer_player.c_dmg
                            print(player.char, "is now at Health:", player.hp)
                    elif computer_player.c_hp > 0 and player.defending == True:
                        print(player.char, "Blocked", computer_player.c_name, "'s Attack")
                    elif player.hp <= 0:
                        print("Game Over\n")
                        playing = True
                        break
                    elif player.hp > 0 and computer_player.c_hp <= 0:
                        print(computer_player.c_name, "Defeated\n")
                        playing = False
        
        elif direction1 == "2":
            print("You went Right. Nothing seems to be in here\n")
        elif direction1 == "3":
            print("You have left the Sewers\n")
            i = 0
            continue
        else:
            print("Not a valid way\n")
            continue

        direction2 = input("""Which way?\n
        1. Left or 2. Right 3. Exit""")
        if direction2 == "1":
            print("You went Left\n")
            if random_encounter() == True:
                  playing = True
                  while playing:
                        if player.hp > 0 and computer_player2.c_hp > 0:
                            print(player.char, ' is fighting' , computer_player2.c_name, "Health:", computer_player2.c_hp)
                            action = input("Choose an option: 1.Attack or 2.Defend\n")
                        if action == "1": 
                            computer_player2.c_hp = computer_player2.c_hp - player.dmg
                            time.sleep(2)
                            print(player.char, "attacked", computer_player2.c_name)
                            print(computer_player2.c_name, " is now at", computer_player2.c_hp)
                        if action == "2":
                            print(player.char,  "is defending")
                            player.defending = True
                            time.sleep(2)
                            continue
                        else:
                            print("invalid Choice")
                        if computer_player2.c_hp > 0 and player.defending == False:
                            time.sleep(2)
                            print(computer_player2.c_name, "Attacked", player.char, "for", computer_player2.c_dmg)
                            player.hp = player.hp - computer_player2.c_dmg
                            print(player.char, "is now at Health:", player.hp)
                        elif computer_player2.c_hp > 0 and player.defending == True:
                            print(player.char, "Blocked", computer_player2.c_name, "'s Attack")
                        elif player.hp <= 0:
                            print("Game Over")
                            i = 0
                        elif player.hp > 0 and computer_player2.c_hp <= 0:
                            print(computer_player2.c_name, "Defeated")
                            playing = False
        elif direction2 == "2":
            print("You went Right. Nothing seems to be in here\n")
        elif direction2 == "3":
            print("You have left the Sewers\n")
            i = 0
            continue
        else:
            print("Invalid Way\n")
            continue

        direction3 = input("""Which way now?\n
        1. Left or 2. Right 3. Exit\n""")
        if direction3 == "2":
                print("You went Right\n")
                playing = True
                while playing:
                    if player.hp > 0 and computer_player3.c_hp > 0:
                        print(player.char, ' is fighting' , computer_player3.c_name, "Health:", computer_player3.c_hp)
                        action = input("Choose an option: 1.Attack or 2.Defend\n")
                    if action == "1": 
                        computer_player3.c_hp = computer_player3.c_hp - player.dmg
                        time.sleep(2)
                        print(player.char, "attacked", computer_player3.c_name)
                        print(computer_player3.c_name, " is now at", computer_player3.c_hp)
                    if action == "2":
                        print(player.char,  "is defending")
                        player.defending = True
                        time.sleep(2)
                        continue
                    else:
                        print("invalid Choice\n")
                        x = 0
                        if computer_player3.c_hp > 0 and player.defending == False:
                            time.sleep(2)
                            print(computer_player3.c_name, "Attacked", player.char, "for", computer_player3.c_dmg)
                            player.hp = player.hp - computer_player3.c_dmg
                            print(player.char, "is now at Health:", player.hp)
                        elif computer_player3.c_hp > 0 and player.defending == True:
                            print(player.char, "Blocked", computer_player3.c_name, "'s Attack")
                        elif player.hp <= 0:
                            print("Game Over")
                            i = 0
                        elif player.hp > 0 and computer_player3.c_hp <= 0:
                            print(computer_player3.c_name, "Defeated\n")
                            playing = False
        elif direction3 == "1":
                print("You ran into a wall, Try again")
                direction3 = "2"
        elif direction3 == "3":
                print("You have left the Sewers\n")
                i = 0
                continue
        else:
            print("Invalid Direction")
            x = 0
            continue
    else:
        print("invalid Route") 
        i = 0 

    if player.hp > 0 and computer_player.c_hp <= 0 and computer_player2.c_hp <=0 and computer_player3.c_hp <=0:
        print("""           Congratulations! \n
         You cleared all the rats out of the Sewers & Beat the Game!""")
        break


    
    
