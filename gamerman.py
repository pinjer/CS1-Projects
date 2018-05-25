import time
import random


# game function
def game():


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the worst game of 2018!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(3)

    print("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    ch1 = str(input("Do you take it? [y/n]: "))

    # STICK TAKEN
    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You have taken the stick!")
        stick = 1

    # STICK NOT TAKEN
    else:
        print("You did not take the stick.")
        stick = 0

    print("As you proceed further into the cave, you see a small glowing object")
    ch2 = str(input("Do you approach the object? [y/n]"))

    # APPROACH SPIDER
    if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You approach the object...")
        time.sleep(.5)
        print("As you draw closer, you begin to make out the object as an eye!")
        time.sleep(.5)
        print("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [Y/N]"))

        # FIGHT SPIDER
        if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:

            # WITH STICK
            if stick == 1:
                print("You only have a stick to fight with!")
                print("You quickly jab the spider in it's eye and gain an advantage")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                BATTLE INITIATED                ")
                print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(2, 3))
                edmg1 = int(random.randint(1, 4))
                health = 5
                gato = input("You remember you have a Gatorade® In your bag. Drink it? [y/n] ")
                while True:
                    if gato in ['y', 'Y', 'Yes', 'YES', 'yes']:
                        print("You have drank the Gatorade®. Youo have the newlyfound strength of 1000 Alligators.")

                        drank = 0
                        if health <= 5:
                            print("Your health is maximum; you cannot be healed right now.")
                            time.sleep(.1)
                            print("However, it does wake you up a bit.")
                            break
                        else:
                            health = +1
                            print("Your health goes up 1.")
                            print(health,"/5")
                            break
                    elif gato in ['n', 'N', 'NO', 'no']:
                        print("That's cool too. It's limited edition though.")
                        print("""        ==========================
                                  FROST  || LIME AND FRUIT PUNCH ||
                                         ==========================""")
                        drank = 0
                        break
                    else:
                        print("Sorry, I don't understand that.\n")
                # while True:
                #     if edmg1 > fdmg1:
                #         print("The spider has dealt more damage than you!")
                #         complete = 0
                #
                #
                #     elif fdmg1 < 5:
                #         print("You didn't do enough damage to kill the spider, but you manage to escape")
                #         complete = 0
                #
                #
                #      else:
                #    print("You killed the spider!")
                #         complete = 0
                #
#IF YOU DAMAGE THE SPIDER OVER 7. GIVE A BETTER DESCRIPTION OF IT
            # WITHOUT STICK
            else:
                print("You don't have anything to fight with!")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                  Fighting...                   ")
                print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(1, 8))
                edmg1 = int(random.randint(1, 5))
                print("you hit a", fdmg1)
                print("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print("The spider has dealt more damage than you!")
                    complete = 0
                    return complete

                elif fdmg1 < 5:
                    print("You didn't do enough damage to kill the spider. You're not giving up now.")
                    complete = 0
                    return complete

                else:
                    print("You killed the spider!")
                    complete = 0
                    return complete

# make if statement mid fight if drank = 0 as a prompt to drink gatorade
        # DON'T FIGHT SPIDER
        print("You choose not to fight the spider.")
        time.sleep(1)
        print("As you turn away, it ambushes you and impales you with it's fangs!")
        complete = 0
        return complete

    # DON'T APPROACH SPIDER
    else:
        print("You turn away from the glowing object, and attempt to leave the cave...")
        time.sleep(1)
        print("But something won't let you....")
        time.sleep(2)
        complete = 0
        return complete

    # game loop
    alive = True
    while alive:

        complete = game()
        if complete == 1:
            alive = input('You managed to escape the cavern alive! Would you like to play again? [y/n]: ')
            if alive in ['y', 'Y', 'YES', 'yes', 'Yes', ]:
                alive

            else:
                break

        else:
            alive = input('You have died! Would you like to play again? [y/n]: ')
            if alive in ['y', 'Y', 'YES', 'yes', 'Yes', ]:
                alive

            else:
                break
game()