import time


def welcome():
    print("Welcome to my game.")
    time.sleep(1)
    print("It is still in early development, so there could be bugs and problems.")
    time.sleep(2)
    print("In case you find anything, please leave a report on my github under the following project.")
    print("https://github.com/MarciProGaming/Game2")
    time.sleep(2)


welcome()

# Variables

global charactertype
charactertype = "No character choosen"

# Modifiers

# Health, damage, shield
closedmg = 0
magicdmg = 0
longdmg = 0
health = 0
shield = 0

# Barbarian
barbclosedmg = 350
barbmagicdmg = 0
barblongdmg = 0
barbhealth = 0
barbshield = 0
modclosedmg = 1
modmagicdmg = 1
modlongdmg = 1
modhealth = 1
modshield = 1

# Archer
archclosedmg = 0
archmagicdmg = 0
archlongdmg = 0
archhealth = 0
archshield = 0
modclosedmg = 1
modmagicdmg = 1
modlongdmg = 1
modhealth = 1
modshield = 1

# Medic
medclosedmg = 0
medmagicdmg = 0
medlongdmg = 0
medhealth = 0
medshield = 0
modclosedmg = 1
modmagicdmg = 1
modlongdmg = 1
modhealth = 1
modshield = 1

# Modifiers
modclosedmg = 1
modmagicdmg = 1
modlongdmg = 1
modhealth = 1
modshield = 1


def characters():
    print("\n\n\n\n\n\n\n\n\n\nThere are 3 types of characters You can choose from:")
    time.sleep(1.5)
    print("\n---------------------------------------------------")
    print("The first one is the Barbarian. A close combat character, so you don't need to avoid enemies.")
    print("- Health: 350")
    print("- +20% damage with close combat weapons")
    print("- -25% damage with magical weapons")
    print("- -50% damage with long range weapons")
    print("\nSpecial abilities: Tornado (Spins around the enemies causing huge damage to them. 120s cooldown)")
    time.sleep(10)
    print("\n")
    print("The second one is the Archer. A ranged combat character, so you don't need to get too close to the enemies.")
    print("- Health: 350")
    print("- -60% damage with close combat weapons")
    print("- +10% damage with magical weapons")
    print("- +20% damage with long range weapons")
    print("\nSpecial abilities: Arrow shower (Arrows rain from the sky, multiple enemies. 90s cooldown)")
    time.sleep(10)
    print("\n")
    print("The third one is the Medic. Mixed range of combat, a bit weaker, but can heal itself.")
    print("- Health: 220")
    print("- -25% damage with close combat weapons")
    print("- +20% damage with magical weapons")
    print("- -5% damage with long range weapons")
    print("\nSpecial abilities: Heal (Heals 20% of the characters full health. 75s cooldown)")
    time.sleep(10)


characters()


def choosecharacter():
    print("Please type in the name of the character you'd like to play with. (Example: Medic)")
    charactertype = input('---->')
    if charactertype == "Barbarian":
        health = barbhealth
        closedmg = barbclosedmg
        longdmg = barblongdmg
        magicdmg = barbmagicdmg
        shield = barbshield
    elif charactertype == "Medic":
        health = medhealth
        closedmg = medclosedmg
        longdmg = medlongdmg
        magicdmg = medmagicdmg
        shield = medshield
    elif charactertype == "Archer":
        health = archhealth
        closedmg = archclosedmg
        longdmg = archlongdmg
        magicdmg = archmagicdmg
        shield = archshield
    else:
        print("You've entered the name incorrectly, please try again!")
    print(f"You've choosen the character '{str(charactertype)}'")
    print("\n---------------------------------------------------")
    print("")
    print("")


choosecharacter()
