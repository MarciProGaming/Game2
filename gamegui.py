import random
import tkinter as tk
from tkinter import messagebox


def welcome():
    messagebox.showinfo("Welcome",
                        "Welcome to my game.\nIt is still in early development, so there could be bugs and problems.\nIn case you find anything, please leave a report on my github under the following project:\nhttps://github.com/MarciProGaming/Game2")


def show_characters():
    character_info = """
The first one is the Barbarian. A close combat character, so you don't need to avoid enemies.
- Health: 350
- Shield: 50
Special abilities: Tornado (Spins around the enemies causing huge damage to them. 120s cooldown)

-------------------------------------------------------------------------------

The second one is the Archer. A ranged combat character, so you don't need to get too close to the enemies.
- Health: 275
- Shield: 70
- 20% Experience Boost
Special abilities: Arrow shower (Arrows rain from the sky, multiple enemies. 90s cooldown)

-------------------------------------------------------------------------------

The third one is the Medic. Mixed range of combat, a bit weaker, but can heal itself.
- Health: 220
- Shield: 65
- 30% Experience Boost
Special abilities: Heal (Heals 20% of the characters full health. 75s cooldown)"""
    messagebox.showinfo("Character Information", character_info)


def save_name():
    global character_name
    character_name = name_entry.get()


def choose_character():
    global health, shield, experience, damage, xpboost, character_name
    if not character_name:
        messagebox.showerror("Error", "Please enter your character's name.")
        return

    charactertype = char_var.get()
    if charactertype == "Barbarian":
        health, shield, experience, damage, xpboost = barbhealth, barbshield, 0, 100, 1.0
    elif charactertype == "Archer":
        health, shield, experience, damage, xpboost = archhealth, archshield, 0, 80, 1.2
    elif charactertype == "Medic":
        health, shield, experience, damage, xpboost = medhealth, medshield, 0, 60, 1.3
    else:
        messagebox.showerror("Error", "Please choose a character before starting the game.")
        return

    chosen_character = f"""
    You've chosen the character '{charactertype}' named '{character_name}'
    ---------------------------------------------------
    Health: {health}
    Shield: {shield}
    Experience: {experience}
    Damage: {damage}
    """
    messagebox.showinfo("Character Chosen", chosen_character)

    # Close the current window and open the new game window
    root.destroy()
    open_game_window()


def open_game_window():
    game_window = tk.Tk()
    game_window.geometry('400x400')
    game_window.title("Game Window")

    # Real-time stats
    health_var.set(f"Health: {health}")
    experience_var.set(f"Experience: {experience}")
    shield_var.set(f"Shield: {shield}")
    damage_var.set(f"Damage: {damage}")
    name_var.set(f"Name: {character_name}")

    # Frame for stats
    stats_frame = tk.Frame(game_window)
    stats_frame.pack(pady=10)

    tk.Label(stats_frame, textvariable=name_var).pack()
    tk.Label(stats_frame, textvariable=health_var).pack()
    tk.Label(stats_frame, textvariable=experience_var).pack()
    tk.Label(stats_frame, textvariable=shield_var).pack()
    tk.Label(stats_frame, textvariable=damage_var).pack()

    # Frame for action buttons
    buttons_frame = tk.Frame(game_window)
    buttons_frame.pack(side=tk.BOTTOM, pady=20)

    tk.Button(buttons_frame, text="Attack", command=attack).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Rest", command=rest).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Explore", command=explore).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Shop", command=shop).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Special Ability", command=special_ability).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Quit", command=game_window.quit).pack(side=tk.LEFT, padx=5)

    game_window.mainloop()


def attack():
    global experience
    experience += 10
    experience_var.set(f"Experience: {experience}")


def rest():
    global health
    health += 20
    health_var.set(f"Health: {health}")


def explore():
    global incombat, enhp, endmg
    if incombat == 1:
        print(character_name + " is currently under attack, and can't go past the enemy.")
    elif incombat == 0:
        currentenemy = random.choices(enemies)
        enhp = random.randint(3, 15)
        print(character_name + " found an enemy.")
        print("\n-----------------------------------------------------")
        print(f"Enemy type: {str(currentenemy)}")
        print(f"Health: {str(enhp)}")
        print("-----------------------------------------------------\n")
        incombat = 1



def shop():
    messagebox.showinfo("Shop", "Welcome to the shop! (Feature not implemented yet)")


def special_ability():
    messagebox.showinfo("Special Ability", "Special ability activated! (Feature not implemented yet)")


def exit_game():
    root.destroy()

# Lists

enemies = ["Dragon", "Goblin"]

# Variables
charactertype = "No character chosen"
character_name = ""
health, shield, experience, damage, xpboost = 0, 0, 0, 0, 0
incombat = 0

# Enemy stats
enhp = 0
endmg = 0

# Barbarian
barbhealth = 350
barbshield = 50

# Archer
archhealth = 275
archshield = 70

# Medic
medhealth = 220
medshield = 65

# Main window
root = tk.Tk()
root.geometry('400x300')
root.title("Simple Tkinter Game")
welcome()


# Show Characters Button
characters_button = tk.Button(root, text="Show Characters", command=show_characters)
characters_button.pack(pady=10)

# Character name input
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()
save_name_button = tk.Button(root, text="Save Name", command=save_name)
save_name_button.pack()

# Character selection
char_var = tk.StringVar(value="Choose a character")
character_menu = tk.OptionMenu(root, char_var, "Barbarian", "Archer", "Medic")
character_menu.pack(pady=10)

# Start Game Button
start_game_button = tk.Button(root, text="Start Game", command=choose_character)
start_game_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=10)

# Stats variables
health_var = tk.StringVar()
experience_var = tk.StringVar()
shield_var = tk.StringVar()
damage_var = tk.StringVar()
name_var = tk.StringVar()

# Start the main loop
root.mainloop()
