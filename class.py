#Blake Martin
#8-29-2019
import random
import sys
import time

#Lists and dicts:
paths=["trivia","real world scenarios","battle"]
bosses=["NUMBER NANCY", "POKEMON PAUL", "THE BOSS"]
trial=[]
numbers=[]
myDict={"Jordan_attacks":"A. Crazy Choke\nB. Aggressive Abomination\nC. Wheezy Wack\nD. Silly Salmon", "Kristofer_attacks":"A. Pinball Potshot\nB. Wise Whack\nC. Lucky Leaf\nD. Yo Yank"   , "Parker_attacks": "A. Finesse Fight\nB. No looker\nC. Thunder Talk\nD. Loose Logic", "Abby_attacks": "A. Musical Monster\nB. Sweet Spike \nC. Dumb Dagger\nD. Omnipotent Oboe" }
myList=["A","B","C","D"]
block_opt=["1","2","3","4"]   
block_opt2=["2","3"]
special=[]

#For minefield:
board_numbers1={}
board_numbers2={}
for i in range(1,26):
    board_numbers1[i]=str(i)
    board_numbers2[i]=str(i)
moves=[]
possible_moves1=[]
for i in range(1,6):
    possible_moves1.append(str(i))
possible_moves2=[]
for i in range(1,26):
    possible_moves2.append(str(i))
mines=[]
stuck_cache=[]
#correct_path={1:"X", 2:"X", 3:"+", 4:"+", 5:"X", 6:"X", 7:"X", 8:"X", 9:"+", 10:"X ", 11:"+ ", 12:"+ ", 13:"+ ", 14:"+ ", 15:"X ", 16:"+ ", 17:"X ", 18:"X ", 19:"X ", 20:"X ", 21:"+ ", 22:"X ", 23:"X ", 24:"X ", 25:"X "}

#For Battleship
upper_board={}
lower_board={}
for i in range(1,17):
    upper_board[i]=str(i)
    lower_board[i]=str(i)
possible_hides=[]
for i in range(1,17):
    possible_hides.append(str(i))
possible_battleship_moves=[]
possible_computer_moves=[]
for i in range(1,17):
    possible_battleship_moves.append(str(i))
    possible_computer_moves.append(i)
boss_hits=[]
hide_previous_choices=[]


#Making the Characters:
class person():
    def __init__(self, name, gender, speciality, charact, lives, hp):
        self.name = name
        self.gender = gender
        self.speciality = speciality
        self.charact = charact
        self.lives = lives
        self.hp = hp
    def profile(self):
        return(self.name + "\n" + "Gender:" + self.gender + "\n" + "Special Ability: " + self.speciality + "\n" + "Characteristics: " + self.charact + "\n" + "Hp: " + str(self.hp) + "\n"+"\n")
    def lives_lost(self):
        self.lives-=1
        if self.lives>0:
            print("\nYou have lost a life. You now have "+str(self.lives)+" lives left\n")
        else:
            sys.exit("You are out of lives. You have lost. Try again!")
    def lives_won(self):
        self.lives+=1
        print("\nCongratulations!! You have gained a life back!! You now have "+str(self.lives)+" lives left")
        time.sleep(3)
    def hp_lost(self, hp_off):
        self.hp -= hp_off
        if self.hp <= 0:
            print("Oh no!!! You have lost all your hp.")
            character.lives_lost()
            if self.name=="Parker":
                self.hp=1000
            else:
                self.hp=500
        else:
            print("You have lost "+str(hp_off)+" hp. You now have "+str(self.hp)+" hp left.\n")

class bad_person():
    def __init__(self, name, charact, hp):
        self.name = name
        self.charact = charact
        self.hp = hp
    def profile(self):
        return(self.name + "\n" + "Characteristics: " + self.charact + "\n" + "Hp: " + str(self.hp) + "\n"+"\n")
    def hp_lost(self, hp_lost):
        self.hp-=hp_lost
        if self.hp<=0:
            print("\nCongratulations!!! You have defeated "+self.name+".")
            character.lives_won()
            return False
        else:
            print("\nYay!!! Your attack worked!!! "+str(self.name)+" now has "+str(self.hp)+" hp!")
            return True
    def boss_hp(self,hp_lost):
        self.hp-=hp_lost
        if self.hp<=0:
            print("\nCongratulations!!! You have defeated The Boss!!!")
            character.lives_won()
            character.lives_won()
            time.sleep(5)
        else:
            print("\n"*40+"You have hit The Boss!!! You must hit him 1 more time to defeat him!!!")
            time.sleep(5)
    


Jordan = person("Jordan", "Female", "Silly Salmon", "Powerful and beautiful, but clinically crazy", 3, 500)
Kris = person("Kristofer", "Male", "Yo Yank", "Wise and lucky, but a very low attack", 3, 500)
Parker = person("Parker", "Male", "Loose Logic", "High health and can finesse, but doesnt attack very accurately", 3, 1000)
Abby = person("Abby", "Female", "Omnipotent Oboe", "Sweet and dodges a lot, but not very inetlligent", 3, 500)
Nancy = bad_person("Number Nancy", "Luckiest, most powerful number user in the world", 1000)
Paul = bad_person("Pokemon Paul", "Potent Pokemon trainer", 1000)
Boss = bad_person("The Boss", "The biggest, baddest, most brilliant boss on the planet", 2000)
#Intro into the game, will show charcter names and ask if player wants their profile
print("\n"*40+"Lets play a game of skill, intellection, battle, a little bit of luck:")
while True:
    profile_opt=input("Choose your character: "+"\n"+"Jordan"+"\n"+"Kristofer"+"\n"+"Parker"+"\n"+"Abby"+"\n"+"\n"+"Do you want a profile for each character? Y for yes, N for No"+"\n"+"\n")
    if profile_opt.lower()== "n":
        print("\n")
        break
    else:
        print("\n"+ Jordan.profile()+"\n"+Kris.profile()+"\n"+Parker.profile()+"\n"+Abby.profile())
        break



#Character selection
while True:
    character=input("What is your selection?: ")
    if character.lower()=="jordan":
        character=Jordan
        break
    elif character.lower()=="kristofer":
        character=Kris
        break
    elif character.lower()=="parker":
        character=Parker
        break
    elif character.lower()=="abby":
        character=Abby
        break
    else:
        print("I'm sorry, that is not a valid selection. Please try again: "+"\n")



#Three categories: 
#Trivia (Kris and Parker benefited)
#The real world (Jordan and Abby are benefited)
#Battle (Each has their own advantage)
#Game path options
print("\n"*35+"Congratulations!!! Hopefully you have chosen the correct character."+"\n"+"\n"+"You will start out with three lives. A wrong answer or battle loss will result in loss of a life in most cases. The game is over when you lose all lives or complete all three paths."+"\n")
print("Depending on what character you chose, you may be benefited in a certain category."+"\n")
input("Are you ready to play?: ")
print("\n")



def choose():
    while len(paths)>0:
        print("\n"*40)
        print("Here are your options: \n")
        for i in range(0,len(paths)):
            print(paths[i].upper())
        choice=input("\nWhat is your selection: ")
        if choice.lower() not in paths:
            print("I'm sorry, that is not an option. You may have already elected this path. Please try again: ")
            time.sleep(4)
        else:
            paths.remove(choice.lower())
            if choice.lower()=="trivia":
                trivia()
            elif choice.lower()=="battle":
                battle()
            #else:
                #boss()

        

#Trivia
def trivia():
    while len(trial) in range (0,3):
        print("\n"*40)
        questions={1:"What is the velocity of an object at the very top of the arc?", 2:"The beaver is the national emblem of which country?", 3:"What is the legal minimum weight of a bowling ball?", 4:"What is the highest posted speed limit in the U.S.?", 5:"Who discovered the concept of gravity first?", 6:"Who is Harvard named after?", 7:"What is William Shakespeare's birth and death date?", 8: "Where was Coca-Cola founded?", 9: "What are the first 5 digits of pi?", 10:"Who wrote 'The Art of War?'" }
        options1={1:"A. Negative\nB. Postive\nC. Not enough info\nD. 0", 2: "A. Canada\nB. U.S.A\nC. France\nD. Greenland", 3: "A. 12 lbs\nB. 10 lbs\nC. 4 lbs\nD. There is no minimum.", 4:"A. 90 mph\nB. 85 mph\nC. 80mph\nD. 75mph", 5:"A. Albert Einstein\nB. Stephen Hawking\nC. Isaac Newton\nD. Ernest Rutherford\n", 6:"A. John Harvard\nB. Timothy Harvard\nC. George Harvard\nD. Lewis Harvard",7:"A. December 2nd\nB. May 6th\nC. July 4th\nD. April 23rd", 8:"A. Watertown, Wisconsin\nB. Atlanta, Georgia\nC. San Francisco, California\nD. Jacksonville, Florida", 9:"A. 3.1514\nB. 3.4151\nC. 3.1415 \nD. 3.1414", 10:"A. Li Bai\nB. Mao Zedong\nC. Lo Xun\nD. Sun Tzu"}
        options2={1:"A. Negative\nB. 0\nC. Positive", 2:"A. Canada\nB. U.S.A\nC. Greenland", 3:"A. 8 lbs\nB. 4 lbs\nC. There is none", 4:"A. 80 mph\nB. 75 mph\nC. 90 mph\nD. 85 mph", 5:"A. Isaac Newton\nB. Albert Einstein", 6:"A. Timothy Harvard\nB. John Harvard", 7:"A. December 2nd\nB. July 10th\nC. April 23rd", 8:"A. Watertown, Wisconsin\nB. Atlanta, Georgia\nC. San Francisco, California", 9:"A. 3.1415\nB. 3.1514", 10:"A. Sunn Tzu\nB. Mao Zedong\nC. Li Bai"}
        girls=[Jordan, Abby]
        #guys=[Kris, Parker]
        #Options 1 is harder than Options 2
        answer_key1={1:"d", 2:"a", 3:"d", 4:"b", 5:"c", 6:"a", 7:"d", 8:"b", 9:"c", 10:"d"}
        answer_key2={1:"b", 2:"a", 3:"c", 4:"d", 5: "a", 6:"b", 7:"c", 8:"b", 9:"a", 10:"a"}
        options_for_trivia=["a","b","c","d"]
        x = random.randint(1,10)
        while True:
            if x not in numbers:
                numbers.append(x)
                break
            else:
                x = random.randint(1,10)

        print(questions[x])
        if character in girls:
            print(options1[x])
            answer=input("\nType the letter of your selection: ")
            while True:
                if answer.lower() in options_for_trivia:
                    break
                else:
                    answer=input("\nI'm sorry. That is not a valid selection. Please try again: ")
            if answer.lower()==answer_key1[x]:
                print("\n"*40+"Correct!!!")
                time.sleep(3)
                trial.append(x)
            else:
                print("\n\n"*40+"I'm sorry, that is incorrect.\n")
                character.lives_lost()
                time.sleep(4)
        else:
            print(options2[x])
            answer_2=input("\nType the letter of your selection: ")
            while True:
                if answer.lower() in options_for_trivia:
                    break
                else:
                    answer=input("\nI'm sorry. That is not a valid selection. Please try again: ")
            if answer_2.lower()==answer_key2[x]:
                print("\n"*40+"Correct!!!")
                time.sleep(3)
                trial.append(x)
            else:
                print("\n\n"*40+"I'm sorry, that is incorrect.\n")
                character.lives_lost()
                time.sleep(4)

def battle():
    print("\n"*40)
    print("\nInstructions:\n\nWelcome to battle. Your character, "+ str(character.name) + ", has "+str(character.hp)+ " health points")
    print("You will have to beat the 2 characters and the boss to move on. Each is a unique battle.\n")
    input("Are you ready?: ")
    while len(bosses)>0:
        print("\n"*40)
        for i in range (0,len(bosses)):
            print("\n"+bosses[i]+"\n")
        bad_guy=input("Who would you like to battle?: ")
        if bad_guy.lower()=="index":
            print("\n"+Nancy.profile()+"\n"+"\n"+Paul.profile()+"\n"+"\n"+Boss.profile()+"\n"+"\n")
            continue
        elif bad_guy.upper() in bosses:
                if bad_guy.upper()=="NUMBER NANCY":
                    print("\n"*40)
                    nancy()
                    bosses.remove("NUMBER NANCY")
                    continue
                elif bad_guy.upper()=="POKEMON PAUL":
                    paul()
                    bosses.remove("POKEMON PAUL")
                    continue
                else:
                    boss()
                    bosses.remove("THE BOSS")
                    continue

        else:
            print("I'm sorry. That is not a valid selection.")
            time.sleep(3)
            continue
    #character.hp_lost(600)
def nancy():
    #rules
    print("\nInstructions:\n\nNancy will select an integer between the range given (If range is 1-4, it could be 1 or 4). You must type in an integer to try and match hers.\n\nIf you do match, you will do damage to her. If you do not match, she will do damage to you.\n\n")
    print("Number Nancy: You have chosen the wrong battle. Welcome to your defeat!!!\n\n")
    numbers=["1","2","3","4","5","6"]
    while Nancy.hp>0:
        x=random.randint(1,6)
        y=random.randint(1,6)
        while True:
            if x>y:
                z=random.randint(y,x)
                guess=input("\nSelect a number between "+str(y)+" and "+str(x)+": ")
                while True:
                    if guess in numbers:
                        guess=int(guess)
                        break
                    else:
                        guess=input("I'm sorry, that is not a valid selection. Please try again: ")     
                if guess==z:
                    if character==Jordan:
                        print("\n"*40)
                        Nancy.hp_lost(500)
                    elif character==Parker:
                        print("\n"*40)
                        Nancy.hp_lost(200)
                    else:
                        print("\n"*40)
                        Nancy.hp_lost(300)
                else:
                    if character==Abby:
                        if guess==z+1:
                            print("\n"*40)
                            print("Congratulations Abby!!! You have dodged Nancy's attack!")
                        elif guess==z-1:
                            print("\n"*40)
                            print("Congratulations Abby!!! You have dodged Nancy's attack!")
                        else:
                            print("\n"*40)
                            Abby.hp_lost(100)
                    elif character==Kris:
                        print("\n"*40)
                        guess_2=input("\n\nThat is an incorrect guess. Because of the character you have chosen, you get another guess!!!: ")
                        while True:
                            if guess_2 in numbers:
                                guess_2=int(guess_2)
                                break
                            else:
                                guess_2=input("I'm sorry, that is not a valid selection. Please try again: ")
                        if guess_2==z:
                            print("\n"*40)
                            Nancy.hp_lost(200)
                        else:
                            print("\n"*40)
                            Kris.hp_lost(100)
                    else:
                        print("\n"*40)
                        character.hp_lost(100)
                break
            elif y>x:
                z=random.randint(x,y)
                guess=input("\nSelect a number between "+str(x)+" and "+str(y)+": ")
                while True:
                    if guess in numbers:
                        guess=int(guess)
                        break
                    else:
                        guess=input("I'm sorry, that is not a valid selection. Please try again: ")
                if guess==z:
                    if character==Jordan:
                        Nancy.hp_lost(500)
                    elif character==Parker:
                        Nancy.hp_lost(200)
                    else:
                        Nancy.hp_lost(300)
                else:
                    if character==Abby:
                        if guess==z+1:
                            print("Congratulations Abby!!! You have dodged Nancy's attack!")
                        elif guess==z-1:
                            print("Congratulations Abby!!! You have dodged Nancy's attack!")
                        else:
                            Abby.hp_lost(100)
                    elif character==Kris:
                        guess_2=input("\n\nThat is an incorrect guess. Because of the character you have chosen, you get another guess!!!: ")
                        while True:
                            if guess_2 in numbers:
                                guess_2=int(guess_2)
                                break
                            else:
                                guess_2=input("I'm sorry, that is not a valid selection. Please try again: ")
                        if guess_2==z:
                            Nancy.hp_lost(200)
                        else:
                            Kris.hp_lost(100)
                    else:
                        character.hp_lost(100)
                break
            else:
                x=random.randint(1,6)
                y=random.randint(1,6)
                continue
def paul():
    print("\n"*40+"Instructions:\n\nYou will have to battle Paul in the style of Pokemon. \n\nType 'A' , 'B' , 'C' , or 'D' to choose an attack. The value of your attack is random, except your special (if not blocked) is worth a lot \n\nOnce you use your special attack, it will disappear for three turns.\n\nYou will be asked to choose an integer between 1 and 4. If guessed correctly, you will block his attack. He can also block yours.")
    print("\nPokemon Paul: Hi kid, want to see my Pokemon?? You will be defeated by it!!!\n")
    input("Are you ready to lose?: ")
    print("\n"*40)
    while Paul.hp>0:
        pokemon()
      
def pokemon():
    myDict={"Jordan_attacks":"A. Crazy Choke\nB. Aggressive Abomination\nC. Wheezy Wack\nD. Silly Salmon", "Kristofer_attacks":"A. Pinball Potshot\nB. Wise Whack\nC. Lucky Leaf\nD. Yo Yank"   , "Parker_attacks": "A. Finesse Fight\nB. No looker\nC. Thunder Talk\nD. Loose Logic", "Abby_attacks": "A. Musical Monster\nB. Sweet Spike \nC. Dumb Dagger\nD. Omnipotent Oboe" }
    if "D" not in myList:
        if len(special)==3:
            myList.append("D")
            myDict={"Jordan_attacks":"A. Crazy Choke\nB. Aggressive Abomination\nC. Wheezy Wack\nD. Silly Salmon", "Kristofer_attacks":"A. Pinball Potshot\nB. Wise Whack\nC. Lucky Leaf\nD. Yo Yank"   , "Parker_attacks": "A. Finesse Fight\nB. No looker\nC. Thunder Talk\nD. Loose Logic", "Abby_attacks": "A. Musical Monster\nB. Sweet Spike \nC. Dumb Dagger\nD. Omnipotent Oboe" }
        else:
            special.append("1")
            myDict={"Jordan_attacks":"A. Crazy Choke\nB. Aggressive Abomination\nC. Wheezy Wack\n", "Kristofer_attacks":"A. Pinball Potshot\nB. Wise Whack\nC. Lucky Leaf\n"   , "Parker_attacks": "A. Finesse Fight\nB. No looker\nC. Thunder Talk\n", "Abby_attacks": "A. Musical Monster\nB. Sweet Spike \nC. Dumb Dagger\n" }


    print("Your attacks are: ")
    print(myDict[str(character.name)+"_attacks"])
    attack=input("\nType the letter of the attack you want to use: ")
    while True:
        if attack.upper() not in myList:
            attack=input("That is not a valid selection. Please try again: ")
        elif attack.upper()=="D":
            myList.remove("D")
            special.clear()
            if character==Jordan:
                myDict["Jordan_attacks"]="A. Crazy Choke\nB. Aggressive Abomination\nC. Wheezy Wack"
            elif character==Kris:
                myDict["Kristofer_attacks"]="A. Pinball Potshot\nB. Wise Whack\nC. Lucky Leaf"
            elif character==Parker:
                myDict["Parker_attacks"]="A. Finesse Fight\nB. No looker\nC. Thunder Talk"
            else:
                myDict["Abby_attacks"]="A. Musical Monster\nB. Sweet Spike \nC. Dumb Dagger"
            break
        else:
            break
    x=random.randint(1,4)
    y=random.randint(1,4)
    t=random.randint(1,4)
    a=random.randint(100,300)
    b=random.randint(100,300)
    c=random.randint(100,300)
    d=random.randint(300,500)
    z=random.randint(50,200)
    hp_numbers={"A":a , "B":b , "C":c , "D":d}

    
    if character==Jordan:
        if y==x:
            print("\nPaul blocked your attack!!!")
        elif x==t:
            print("\nBecuase you are so crazy, you accidently attacked yourself!!\n\n")
            character.hp_lost(hp_numbers[attack.upper()]*2)
        #elif y==t:
            #print("Becuase you are so crazy, you accidently attacked yourself!!\n\n")
            #character.hp_lost(hp_numbers[attack.upper()]*2)
        else:
            #print("\nYour attack worked!!!\n")
            Paul.hp_lost(hp_numbers[attack.upper()]*2)
        while Paul.hp>0:
            block=input("\nPlease select a number 1-4 (can be 1 or 4) to block: ")
            while True:
                if block in block_opt:
                    block=int(block)
                    break
                else:
                    block=input("I'm sorry, that is not a valid selection. Please try again: ")
            if block==x:
                print("\nCongratulations!!! You have blocked Paul's attack!\n")
                break
            else:
                print("\nYou did not block Paul's attack\n")
                character.hp_lost(z)
                break
    elif character==Kris:
        if y==x:
            print("\nPaul blocked your attack!!!")
        elif x==t:
            print("\nYou lost focus on the battle and lost your turn!!!\n\n")
        else:
            #print("\nYour attack worked!!!\n")
            Paul.hp_lost(hp_numbers[attack.upper()]-100)
        while Paul.hp>0:
            block=input("\nPlease select a number 1-4 (can be 1 or 4) to block: ")
            while True:
                if block in block_opt:
                    block=int(block)
                    break
                else:
                    block=input("I'm sorry, that is not a valid selection. Please try again: ")
            if block==x:
                print("\nCongratulations!!! You have blocked Paul's attack!\n")
                break
            elif block==x-1:
                print("\nCongratulations!!! You have blocked Paul's attack!\n")
                break
            elif block==x+1:
                print("\nCongratulations!!! You have blocked Paul's attack!\n")
                break
            else:
                print("\nYou did not block Paul's attack\n")
                character.hp_lost(z)
                break
    elif character==Parker:
        if y==x:
            print("\nPaul blocked your attack!!!")
        elif x==t:
            print("\nYou missed your target and hit yourself!!!\n\n")
            character.hp_lost(hp_numbers[attack.upper()])
        else:
            #print("\nYour attack worked!!!\n")
            Paul.hp_lost(hp_numbers[attack.upper()])
        while Paul.hp>0:
            block=input("\nPlease select a number 1-4 (can be 1 or 4) to block: ")
            while True:
                if block in block_opt:
                    block=int(block)
                    break
                else:
                    block=input("I'm sorry, that is not a valid selection. Please try again: ")
            if block==x:
                print("\nCongratulations!!! You have blocked Paul's attack!\n")
                break
            else:
                print("\nYou did not block Paul's attack\n")
                character.hp_lost(z)
                break
    else:
        if y==x:
            print("\nPaul blocked your attack!!!")
        elif x==t:
            print("\nYou couldn't think quickly enough and lost your turn!\n\n")
        else:
            #print("\nYour attack worked!!!\n")
            Paul.hp_lost(hp_numbers[attack.upper()]-100)
        while Paul.hp>0:
            block=input("\nPlease select a number, 2 or 3 to block: ")
            while True:
                if block in block_opt2:
                    block=int(block)
                    break
                else:
                    block=input("I'm sorry, that is not a valid selection. Please try again: ")
            j = random.randint(2,3)
            if block==j:
                print("\nCongratulations!!! You have blocked Paul's attack!")
                break
            else:
                print("\nYou did not block Paul's attack\n")
                character.hp_lost(z)
                break
def boss():
    minefield()
    print("\n"*40+"You have made it to the boss!!!")
    time.sleep(2)
    print("\nUh Oh...")
    time.sleep(2)
    print("\nThe boss has hidden himself!!!")
    time.sleep(2)
    print("\nYou must attack him blindly to defeat him!!! Good luck!")
    time.sleep(2)
    print("\nWelcome to the final battle!!! You will select an integer between 1-16 to hide. The boss is hidden on the other side. You can change where you are hiding after every turn. You can not hide in a space that has been attacked.\n\nWhen asked to attack, you will have to type the number of space you want to fire at on the other side of the board.\n\nIf the boss hits you, you will lose a life. You must hit the boss 2 times to defeat him")
    input("\n\nAre you ready for the final boss battle?: ")
    battle_ship()
correct_path={}
def path_maker():
    
    column_1=[1,6,11,16]
    column_2=[5,10,15,20]
    row_1=[1,2,3,4,5]
    row_2=[21,22,23,24,25]

    first_pick= random.randint(1,5)
    correct_path[first_pick]="+"
    if first_pick>1:
        if first_pick==5:
            acceptable_choices = [first_pick-1, first_pick+5]
        else:
            acceptable_choices= [first_pick+1, first_pick-1, first_pick+5]
        
    else:
        acceptable_choices= [first_pick+1, first_pick+5]


    while True:
        
        choice=random.choice(acceptable_choices)
        while True:
            if choice in correct_path:
                choice=random.choice(acceptable_choices)
            else:
                break
        while True:
            if choice+1 in correct_path:
                if choice-1 in correct_path:
                    if choice+5 in correct_path:
                        if choice in row_1:
                            choice=random.choice(acceptable_choices)
                            print("Hello")
                        else:   
                            if choice-5 in correct_path:
                                choice=random.choice(acceptable_choices)
                            else:
                                break
                    else:
                        break
                else:
                    break
            else:
                break
        correct_path[choice]="+ "
        acceptable_choices.clear()
        if choice in column_1:
            acceptable_choices=[choice+1, choice+5]
        elif choice in column_2:
            acceptable_choices=[choice-1, choice+5]
        elif choice in row_1:
            acceptable_choices=[choice-1, choice+1, choice+5]
        elif choice in row_2:
            break
        else:
            acceptable_choices=[choice-1, choice+1, choice-5, choice+5]

    for i in range (1,26):
        if i not in correct_path:
            correct_path[i]="X "
        else:
            continue
row_2=[21,22,23,24,25]
def minefield():
    path_maker()
    print("\n"*40+"Welcome to the boss battle!!! This will be the hardest test. No characters will have any special advantage in this mode.\n\nFirst, you will have to cross the minefield. Type the number of the space you would like to move to. You may only move forward, back, and sideways. No diagnol movement is allowed. You can not move to a space you already chose.\n\nIf you land on a mine, you will recieve an 'X' on that space and return to the space you were at. 4 'X's on the board will result in loss of a life and cause you to start over with the same path. ")
    input("\nAre you ready: ")
    while True:
        while len(moves)<1:
            while True:
                board()
                #print(correct_path)
                move=input("Where would you like to move?: ")
                if move in possible_moves1:
                    board_numbers1[int(move)]=correct_path[int(move)]
                    stuck_cache.append(int(move))
                    if correct_path[int(move)]=="X ":
                        mines.append("X")
                        #print("hello")
                        continue
                    else:
                        moves.append(move)
                        break
                else:
                    print("That is not a valid move. Please try again.\n ")
        board()
        move=input("Where would you like to move?: ")
        while True:
            if move in possible_moves2:
                if move in moves:
                    move=input("You have already selected this space. Please select again: ")
                for i in range(0,21,5):
                    if int(moves[len(moves)-1]) == (i+1):
                        if int(move) == i:
                            move=input("That is not a valid move. Please select again: ")
                        else:
                            break
                    elif int(moves[len(moves)-1]) == i:
                        if int(move) == i+1:
                            move=input("That is not a valid move. Please select again: ")
                        else:
                            break
                    else:
                        continue
                stuck_cache.append(int(move))
                #print(stuck_cache)
                if int(move) == int(moves[len(moves)-1])-1:
                    board_numbers1[int(move)]=correct_path[int(move)]
                    if correct_path[int(move)] == "+":
                        moves.append(move)
                    elif correct_path[int(move)] == "+ ":
                        moves.append(move)
                    else:
                        mines.append("X")
                    break
                elif int(move) == int(moves[len(moves)-1])+1:
                    board_numbers1[int(move)]=correct_path[int(move)]
                    if correct_path[int(move)] == "+":
                        moves.append(move)
                    elif correct_path[int(move)] == "+ ":
                        moves.append(move)
                    else:
                        mines.append("X")
                    break
                elif int(move) == int(moves[len(moves)-1])+5:
                    board_numbers1[int(move)]=correct_path[int(move)]
                    if correct_path[int(move)] == "+":
                        moves.append(move)
                    elif correct_path[int(move)] == "+ ":
                        moves.append(move)
                    else:
                        mines.append("X")
                    break
                elif int(move) == int(moves[len(moves)-1])-5:
                    board_numbers1[int(move)]=correct_path[int(move)]
                    if correct_path[int(move)] == "+":
                        moves.append(move)
                    elif correct_path[int(move)] == "+ ":
                        moves.append(move)
                    else:
                        mines.append("X")
                    break
                else:
                    move=input("That is not a valid move. Please select again: ")
            else:
                move=input("That is not a valid move. Please select again: ")
        if len(mines)>3:
            print("\n"*40)
            character.lives_lost()
            time.sleep(5)
            board_numbers1.clear()
            moves.clear()
            mines.clear()
            stuck_cache.clear()
            for i in range(1,26):
                board_numbers1[i]=str(i)

        elif int(move) in row_2:
            break
        else:
            cache=[]
            for check in range(1,6,4):
                if int(moves[len(moves)-1])-check in stuck_cache:  
                    cache.append(1)
                    if int(moves[len(moves)-1])+check in stuck_cache:
                        cache.append(1)
                elif int(moves[len(moves)-1])+check in stuck_cache:
                    cache.append(1)
                    if int(moves[len(moves)-1])-check in stuck_cache:  
                        cache.append(1)
                else:
                    continue
            #print(len(cache))
            #print(stuck_cache)
            #print(moves[len(moves)-1])
            #print(moves)
            row_1=[1,2,3,4,5]
            if int(moves[len(moves)-1]) in row_1:
                if len(cache) == 3:
                    print("\n"*40)
                    print("Oh no, you have trapped yourself!!!")
                    character.lives_lost()
                    time.sleep(5)
                    board_numbers1.clear()
                    moves.clear()
                    mines.clear()
                    stuck_cache.clear()

                    for i in range(1,26):
                        board_numbers1[i]=str(i)
            elif len(cache) == 4:
                print("\n"*40)
                print("Oh no, you have trapped yourself!!!")
                character.lives_lost()
                time.sleep(5)
                board_numbers1.clear()
                moves.clear()
                mines.clear()
                stuck_cache.clear()
                for i in range(1,26):
                    board_numbers1[i]=str(i)
            else:
                continue



def battle_ship():
    battle_ship_moves=[]
    last_boss_hide=[]
    yellow_numbers=[1,4,13,16]
    green_numbers_row_1=[2,3]
    green_numbers_row_2=[14,15]
    green_numbers_column_1=[5,9]
    #green_numbers_column_2=[9,12]
    blue_numbers=[6,7,10,11]
    while Boss.hp>0:
        if len(battle_ship_moves)<1:
            computer_hide=random.randint(1,17)
            last_boss_hide.append(computer_hide)
            battle_ship_moves.append(1)
        else:
            possible_computer_hide=[]
            if last_boss_hide[0] in blue_numbers:
                possible_computer_hide.append(last_boss_hide[0]+1)
                possible_computer_hide.append(last_boss_hide[0]-1)
                possible_computer_hide.append(last_boss_hide[0]+4)
                possible_computer_hide.append(last_boss_hide[0]-4)
                possible_computer_hide.append(last_boss_hide[0])
            elif last_boss_hide[0] in yellow_numbers:
                if last_boss_hide[0]==1:
                    possible_computer_hide.append(1)
                    possible_computer_hide.append(2)
                    possible_computer_hide.append(5)
                elif last_boss_hide[0]==13:
                    possible_computer_hide.append(13)
                    possible_computer_hide.append(9)
                    possible_computer_hide.append(14)
                elif last_boss_hide[0]==16:
                    possible_computer_hide.append(16)
                    possible_computer_hide.append(15)
                    possible_computer_hide.append(12)
                else:
                    possible_computer_hide.append(4)
                    possible_computer_hide.append(3)
                    possible_computer_hide.append(8)
            else:
                if last_boss_hide[0] in green_numbers_row_1:
                    possible_computer_hide.append(last_boss_hide[0]+1)
                    possible_computer_hide.append(last_boss_hide[0]-1)
                    possible_computer_hide.append(last_boss_hide[0]+4)
                    possible_computer_hide.append(last_boss_hide[0])
                elif last_boss_hide[0] in green_numbers_row_2:
                    possible_computer_hide.append(last_boss_hide[0]+1)
                    possible_computer_hide.append(last_boss_hide[0]-1)
                    possible_computer_hide.append(last_boss_hide[0]-4)
                    possible_computer_hide.append(last_boss_hide[0])
                elif last_boss_hide[0] in green_numbers_column_1:
                    possible_computer_hide.append(last_boss_hide[0]+1)
                    possible_computer_hide.append(last_boss_hide[0]+4)
                    possible_computer_hide.append(last_boss_hide[0]-4)
                    possible_computer_hide.append(last_boss_hide[0])
                else:
                    possible_computer_hide.append(last_boss_hide[0]-1)
                    possible_computer_hide.append(last_boss_hide[0]+4)
                    possible_computer_hide.append(last_boss_hide[0]-4)
                    possible_computer_hide.append(last_boss_hide[0])
            while True:
                computer_hide = random.choice(possible_computer_hide)
                print(computer_hide)
                print(possible_computer_hide)
                print(last_boss_hide)
                if upper_board[computer_hide]=="X":
                    continue
                elif upper_board[computer_hide]==" X":
                    continue
                else:
                    last_boss_hide.clear()
                    last_boss_hide.append(computer_hide)
                    break
        #print(computer_hide)
        board2()
        hide_choice=input("Where would you like to hide?: ")
        while True:
            if hide_choice in possible_hides:
                hide_previous_choices.append(hide_choice)
                if len(hide_previous_choices)>1:
                    lower_board[int(hide_previous_choices[len(hide_previous_choices)-2])]= str(hide_previous_choices[len(hide_previous_choices)-2])

                break
            else:
                hide_choice=input("That space is not available. Please select again: ")
        if int(hide_choice)<10:
            lower_board[int(hide_choice)]="+"
        else:
            lower_board[int(hide_choice)]=" +"
        board2()
        battleship_move=input("Where would you like to attack?: ")
        while True:
            if battleship_move in possible_battleship_moves:
                possible_battleship_moves.remove(battleship_move)
                break
            else:
                battleship_move=input("That space is not available. Please select again: ")
        if int(battleship_move)==computer_hide:
            Boss.boss_hp(1000)
            clear_board()
            battle_ship_moves.clear()
            last_boss_hide.clear()
        else:
            if int(battleship_move)<10:
                upper_board[int(battleship_move)]="X"
            else:
                upper_board[int(battleship_move)]=" X"
            computer_move=random.randint(1,17)
            while True:
                if computer_move in possible_computer_moves:
                    if computer_move==int(hide_choice):
                        print("\n"*40+"Oh no!!! The Boss has hit you!!!\n")
                        character.lives_lost()
                        time.sleep(5)
                        clear_board()
                        battle_ship_moves.clear()
                        last_boss_hide.clear()
                        break
                    else:
                        possible_computer_moves.remove(computer_move)
                        possible_hides.remove(str(computer_move))
                        if computer_move<10:
                            lower_board[computer_move]="X"
                        else:
                            lower_board[computer_move]=" X"
                        break

                else:
                    computer_move=random.randint(1,17)
            

                
        

    
    

#Minefield Board
def board():
    print("\n"*40)
    print(" "*7+"START")
    print("-"*20)
    for i in range(1,6):
        if board_numbers1[i]=="+ ":
            print("|"+board_numbers1[i]+"|", end="")
        elif board_numbers1[i]=="X ":
            print("|"+board_numbers1[i]+"|", end="")
        else:
            print("|"+board_numbers1[i]+" |", end="")
    print("\n"+"-"*20)
    for i in range(6,10):
        if board_numbers1[i]=="+ ":
            print("|"+board_numbers1[i]+"|", end="")
        elif board_numbers1[i]=="X ":
            print("|"+board_numbers1[i]+"|", end="")
        else:
            print("|"+board_numbers1[i]+" |", end="")
    print(end=""+"|"+board_numbers1[10]+"|")
    print("\n"+"-"*20)
    for i in range(11,16):
        print("|"+board_numbers1[i]+"|", end="")
    print("\n"+"-"*20)
    for i in range(16,21):
        print("|"+board_numbers1[i]+"|", end="")
    print("\n"+"-"*20)
    for i in range(21,26):
        print("|"+board_numbers1[i]+"|", end="")
    print("\n"+"-"*20)
    print(" "*8+"END")
#Battleship board
def board2():
    print("\n"*40)
    print(" "*4+"THE BOSS")
    print("-"*16)
    for i in range(1,5):
        print("|"+upper_board[i]+" |",end="")
    print("\n"+"-"*16)
    for i in range(5,9):
        print("|"+upper_board[i]+" |",end="")
    print("\n"+"-"*16)
    print("|"+upper_board[9]+" |",end="")
    for i in range(10,13):
        print("|"+upper_board[i]+"|",end="")
    print("\n"+"-"*16)
    for i in range(13,17):
        print("|"+upper_board[i]+"|",end="")
    print("\n"+"-"*16)
    print("\n"+"-"*16)
    print("\n"+"-"*16)
    for i in range(13,17):
        print("|"+lower_board[i]+"|",end="")
    print("\n"+"-"*16)
    print("|"+lower_board[9]+" |",end="")
    for i in range(10,13):
        print("|"+lower_board[i]+"|",end="")
    print("\n"+"-"*16)
    for i in range(5,9):
        print("|"+lower_board[i]+" |",end="")
    print("\n"+"-"*16)
    for i in range(1,5):
        print("|"+lower_board[i]+" |",end="")
    print("\n"+"-"*16)
    print(" "*5+str(character.name))
#Clear the battleship board
def clear_board():
    upper_board.clear()
    lower_board.clear()
    possible_hides.clear()
    possible_battleship_moves.clear()
    possible_computer_moves.clear()
    for i in range(1,17):
        upper_board[i]=str(i)
        lower_board[i]=str(i)
        possible_hides.append(str(i))
        possible_battleship_moves.append(str(i))
        possible_computer_moves.append(i)
#TO DO:
    # Continue at line 785 to write conditions on where the computer can hide. It varies depending on row and column
    # In battleship, make so you can only move like a rook, and cant move on already attacked spaces 
# 
# 
# 
# Create Real World Scenerios
# Play around with every mode and format consistently throughout the whole game.
# 
#   

#
#  

choose()



