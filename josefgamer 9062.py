import random
import time

health = 5
bosshealth = 10
foedmg = int(random.randint(2, 3))  # spider's damage
mydmg = int(random.randint(1, 4))  # your damage
#IM SO FRUSTRATED WITH THIS GAME. I CAN'T FIGURE OUT HOW TO FIX IT AAAA

def p():
    print()


def h():
    time.sleep(.1)


def dmg():
    global bosshealth
    global foedmg
    global health
    global mydmg
    global drank
    global gato
    print("The attacker did ", foedmg, "points of damage.")
    print("You currently have ", health, "/5 health points remaining.")
    print("The enemy currently has ", bosshealth, " HP.")

    health = health - foedmg
    bosshealth = bosshealth - mydmg

    if bosshealth <= 0:
        print("The enemy is defeated!");
    elif health < 0:
        print("You are dead.")
    elif health <= 3 and drank == 0:
        gato = input("You remember you have a Gatorade® In your bag. Drink it? [Y/N] ")
        while True:
            if gato in ['y', 'Y', 'Yes', 'YES', 'yes']:
                print("You have drank the Gatorade®. You have the newlyfound strength of 1000 Alligators.")
                drank = 0
                if health <= 5:
                    print("Your health is maximum; you cannot be healed right now.")
                    time.sleep(.1)
                    print("However, it does wake you up a bit.")
                    break
                else:
                    health = +1
                    print("Your health goes up 1.")
                    print(health, "/5")
                    break
            elif gato in ['n', 'N', 'NO', 'no']:
                print("That's cool too. It's limited edition though.")
                print("""                       ==========================
                                        . FROST  || LIME AND FRUIT PUNCH ||
                                                ==========================""")
                drank = 0
                break
            else:
                print("Sorry, I don't understand that.\n")


# make sure that the  randint is inside of the loop so it assigns new values
# create one of those hangman list thingies fo ra boss health bar maybe
# game function
def game():
    global alive
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the worst game of 2018!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(1)

    print("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    ch1 = str(input("Do you take it? [Y/N]: "))

    # STICK TAKEN
    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You have taken the stick!")
        stick = 1

    # STICK NOT TAKEN
    else:
        print("You did not take the stick.")
        stick = 0
    p()
    print("As you proceed further into the cave, you see a small glowing object.")
    ch2 = str(input("Do you approach the object? [Y/N]"))

    # APPROACH SPIDER
    if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        p()
        print("You approach the object...")
        h()
        print("As you draw closer, you begin to make out the object as an eye!")
        h()
        print("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [Y/N]"))

        # FIGHT SPIDER
        if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:
            # WITH STICK
            pass
        if stick == 1:
            print("You only have a stick to fight with!")
            print("You quickly jab the spider in it's eye and gain an advantage.")
            bosshealth = 8
            bosshealth = bosshealth - 1
            print("You reduce the spider's health by one. It's HP is now 7/8.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                BATTLE INITIATED                ")
            print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
            print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)

            health = 5
            gato = input("You remember you have a Gatorade® In your bag. Drink it? [Y/N] ")

            while True:
                global drank
                if gato in ['y', 'Y', 'Yes', 'YES', 'yes']:
                    print("You have drank the Gatorade®. You have the newlyfound strength of 1000 Alligators.")

                    drank = 0
                    if health <= 5:
                        print("Your health is maximum; you cannot be healed right now.")
                        time.sleep(.1)
                        print("However, it does wake you up a bit.")
                        break
                    else:
                        health = +1
                        print("Your health goes up 1.")
                        print("Your health is ", health, "/5")
                        break
                elif gato in ['n', 'N', 'NO', 'no']:
                    print("That's cool. It's limited edition.")
                    print("""                ==========================
                                      FROST  || LIME AND FRUIT PUNCH ||
                                             ==========================""")
                    drank = 0
                    break
                else:
                    print("Sorry, I don't understand that.\n")
                while foehealth > 0:
                    global mydmg
                    global foedmg
                    foedmg = int(random.randint(2, 3))  # spider's damage
                    mydmg = int(random.randint(1, 4))  # your damage
                    if mydmg == 4:
                        print("You do 4 damage. It's super effective!")
                        time.sleep(0.1)
                        print("It seems the spider is disoriented.")
                        # complete = 0
                        dmg()
                    elif mydmg == 3:
                        print("You do 3 damage. It's effective!")
                        dmg()
                        # complete = 0
                    # create a function to make an if else statement for the health guys
                    # if health lower than 3 and drank = 0 prompt gatorade.
                    elif mydmg == 2:
                        print("You do 2 damage. It's not effective.")
                        dmg()
                    elif mydmg == 1:
                        print("You do 1 damage. It's not effective at all.")
                        dmg()


                # IF YOU DAMAGE THE SPIDER OVER 7. GIVE A BETTER DESCRIPTION OF IT
                # WITHOUT STICK
                else:
                    print("You don't have anything to fight with!")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                BATTLE INITIATED                ")
                print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                foehealth = 7
                while foehealth > 0:
                    foedmg = int(random.randint(2, 3))  # spider's damage
                    mydmg = int(random.randint(1, 2))  # your damage
                    if mydmg == 4:
                        print("You do 4 damage. It's super effective!")
                        time.sleep(0.1)
                        print("It seems the spider is disoriented.")
                        # complete = 0
                        dmg()
                    elif mydmg == 3:
                        print("You do 3 damage. It's effective!")
                        dmg()
                        # complete = 0
                    # create a function to make an if else statement for the health guys
                    # if health lower than 3 and drank = 0 prompt gatorade.
                    elif mydmg == 2:
                        print("You do 2 damage. It's not effective.")
                        dmg()
                    elif mydmg == 1:
                        print("You do 1 damage. It's not effective at all.")
                        dmg()
                    elif bosshealth <= 0:
                        print("You have defeated him.")
                    elif health <= 0:
                        print("You have died.")
                        break
        else:
            print("You choose not to fight the spider.")
            time.sleep(1)
            print("As you turn away, it ambushes you and impales you with it's fangs!")
            print("You take one point of damage. Your health is now 4/5.")
            health = health -1


            # make if statement mid fight if drank = 0 as a prompt to drink gatorade
            # DON'T FIGHT SPIDER

            # complete = 0

    # DON'T APPROACH SPIDER
    else:
        print("You turn away from the glowing object, and attempt to leave the cave...")
        time.sleep(1)
        print("But something won't let you....")
        time.sleep(2)
        # complete = 0

        # game loop
        # game loop broke the code fix afterwards


game()
