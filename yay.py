"""
Main Code(__main__)
Attack and Defend

@author = AlphaBeta906
@email = dragonkingalyx@gmail.com
"""
#VERSION 1.6

from random import choice, randint
from time import sleep
print ("STARTING...")
religionz = ["Cristianity", "Islam", "Hindu"]
doings = ["Compiling", "Machine Code Made", "Calling Functions", "Testing Outputs", "Done"]
enchantments = ["Better Army", "Faster Approval", "Happiness"]
enchants = []
www = "Researched from the research tree with"
index = 0
day = 0
alive_nations = ["Ming", "Xou", "Poland", "Biolstan", "Scomational", "Ryus"]
tribes = ["Tu L'alu", "Mecca","New Astronesia", "Scotland", "Tuvali A'kual"]
religion_mates = []
sleep(1)
for x in range(0, 5):
    b = "Loading" + "." * x
    a = doings[index]
    print (b)
    print (a, end="\n")
    index = index + 1
    sleep(1)
print ("FINISHED!")
ofDed = False
while True:
    nation_name = input("NATION PLS")
    religion = input("RELIGION PLS")
    if nation_name in alive_nations:
        print ("Nation is not usable")
    else:
        break
stuff = ["Requested a alliance with", "Attacked", "Researched from the research tree with", "Funded a revolt on", "Wants you to change religion on"]
allies = []
alive_nations.append(nation_name)
religionz.append(religion)
ded_nations = []
while ofDed == False:
    for turn in range(0, 15):
        n = choice(alive_nations)
        en = len(enchantments)
        day = day + 1
        print ("Day: ", end=" ")
        print (day)
        if n == nation_name:
            do = input("Attack or Allies or Research or Crusade or Skip")
            if do == "Allies":
                a = input("Nation")
                if a in alive_nations:
                    if "Faster Approval" in enchants:
                        c = randint(1, 2)
                    else:
                        c = randint(1, 6)
                    if c == 1:
                        print ("Yay, " + a + " is in youre allies")
                        allies.append(a)
                    else:
                        print ("REQUEST REGECTED")
            elif do == "Research":
                while True:
                 solo_duo = ["Solo", "Duo"]
                 SD = input("Solo or Duo")
                 if SD in solo_duo:
                     break
                if SD == "Solo":
                    tree = choice(enchantments)
                    enchantments.remove(tree)
                    enchants.append(tree)
                    print ("You have the " + tree + " enchantment!")
                elif SD == "Duo":
                     while True:
                         who = input("With who?")
                         if who in allies:
                            tree = choice(enchantments)
                            enchantments.remove(tree)
                            enchants.append(tree)
                            print ("You have the " + tree + " enchantment!")
                            break
            elif do == "Attack":
                while True:
                    nation_list = len(alive_nations)
                    a = input("Nation")
                    if a in alive_nations:
                       if "Better Army" in enchants:
                           c = randint(1, 2)
                       else:
                           c = randint(1, 6)
                       if c == 1:
                           print ("Yay, " + a + " is dead")
                           alive_nations.remove(a)
                           ded_nations.append(a)
                           if a in allies:
                               allies.remove(a)
                               break
                           if a in religion_mates:
                               religion_mates.remove(a)
                       else:
                           print ("You failed")
                           break
                    elif a == "EXIT":
                        break
                    elif nation_list == "0":
                        print ("Congrats!, You now control the world!")
                        quit()
            elif do == "Crusade":
                while True:
                    nation = input("Nation")
                    if nation in alive_nations:
                        break
                    else:
                        print ("Not Alive")
                if "Faster Approval" in enchants:
                    c = randint(1, 2)
                else:
                    c = randint(1, 4)
                if c == "1":
                    print (nation + "is now youre religion")
                    religion_mates.append(nation)
                else:
                    print ("U lost")
            else:
                print ("Okay")
        else:
            x = choice(stuff)
            y = choice(alive_nations)
            z = choice(alive_nations)
            new_tribe = choice(tribes)
            c = randint(1, 2)
            while y == nation_name or y == z:
                x = choice(stuff)
                y = choice(alive_nations)
                z = choice(alive_nations)
            if en == 0:
                while True:
                    x = choice(stuff)
                    if x != a:
                        break
            print (y + " " + x + " " + z)
            if x == "Requested a alliance with" and z == nation_name:
                if y in allies:
                    print ("You already went to alliance of theirs")
                else:
                    yn = input(y + " wanna do a alliance Y/N")
                    if yn == "Y":
                        allies.append(y)
            elif x == "Researched from the research tree with" and z == nation_name:
                if y in allies:
                    research_collab = input("Would you like to research with " + y + "? Y/N")
                    if research_collab == "Y":
                        tree = choice(enchantments)
                        enchantments.remove(tree)
                        enchants.append(tree)
                        print ("You have the " + tree + " enchantment!")
                    else:
                        print ("Ok den")
            elif x == "Attacked" and z == nation_name:
               if "Better Army" in enchants:
                   c = randint(1, 2)
               else:
                   c = randint(1, 6)
               if y in allies:
                   print ("But it did'nt happen")
               if c == 1:
                   print (z + " is ded")
                   alive_nations.remove(nation_name)
                   ded_nations.append(nation_name)
                   sleep(1)
                   if z == nation_name:
                       quit()
               else:
                    print (y + " failed")
            elif x == "Funded a revolt on" and z == nation_name:
                let = input("Would you like to let it free Y/N")
                if let == "Y":
                    tribes.remove(new_tribe)
                    alive_nations.append(new_tribe)
                    print (new_tribe + " is a alive nation")
                elif let == "N":
                    if "Better Army" or "Happiness" in enchants:
                        c = randint(1, 2)
                    else:
                        c = randint(1, 4)
                    if c == "1":
                        print (new_tribe + " lost")
                    else:
                        tribes.remove(new_tribe)
                        alive_nations.append(new_tribe)
                        print (new_tribe + " is a alive nation and u lost")
            elif x == "Wants you to change religion on" and z == nation_name:
                new_r = choice(religionz)
                if y in religion_mates:
                    print ("But they are youre religion")
                else:
                    let = input("Would you like to change religion? Y/N")
                    if let == "Y":
                        print ("Youre religion is " + new_r)
                        religion = new_r
                    else:
                        print ("There is a crusade!")
                        if "Better Army" in enchants:
                            c = randint(1, 2)
                        else:
                            c = randint(1, 4)
                        if c == "1":
                            print ("You defeated dem!")
                        else:
                            print ("You have to change religion by force")
                            sleep(1)
                            print ("Youre religion is " + new_r)
                            religion = new_r
