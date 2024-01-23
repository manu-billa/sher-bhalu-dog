import random
import time

# ANSI escape codes for colors
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
END_COLOR = '\033[0m'

fighters = {
    "Sher": {'name': "Sher", 'attacks': ["Bite", "Scratch", "Pounce"], 'max_hitpoints': 150, 'hitpoints': 150, 'luck': 5},
    "Bhalu": {'name': "Bhalu", 'attacks': ["Bite", "Scratch", "Pounce"], 'max_hitpoints': 150, 'hitpoints': 150, 'luck': 5},
    "Dog": {'name': "Dog", 'attacks': ["Bite", "Scratch", "Pounce"], 'max_hitpoints': 150, 'hitpoints': 150, 'luck': 5},
}

print("Welcome to the Fighter Battle Game!")
time.sleep(1)

player_choice = input("Choose your fighter (Sher/Bhalu/Dog): ").capitalize()

player = fighters[player_choice]

opponent_choice = input("Do you want to play against the computer? (yes/no): ").lower()

if opponent_choice == "yes":
    opponent = fighters[random.choice(list(fighters.keys()))]
    print(f"\nYou are battling against the computer's {opponent['name']}!\n")
    time.sleep(1)
elif opponent_choice == "no":
    opponent = fighters[random.choice(list(fighters.keys()))]
    print(f"\nThe computer has chosen {opponent['name']}!\n")
    time.sleep(1)
else:
    print("Invalid choice for opponent. Exiting the game.")
    exit()

rounds = 10

for _ in range(rounds):
    player_luck = random.randint(0, 10)
    opponent_luck = random.randint(0, 10)

    print(f"\n{player['name']}'s turn:")
    time.sleep(1)
    player_attack = input(f"Choose attack ({', '.join(player['attacks'])}): ").capitalize()
    time.sleep(1)

    print(f"{opponent['name']}'s turn:")
    time.sleep(1)
    opponent_attack = random.choice(opponent['attacks'])
    time.sleep(1)

    print(f"{player['name']} attacks with {player_attack} and luck {player_luck}!")
    time.sleep(1)
    print(f"{opponent['name']} defends with {opponent_attack} and luck {opponent_luck}!")
    time.sleep(1)

    player_damage = random.randint(10, 20) + player_luck // 2
    opponent_damage = random.randint(10, 20) + opponent_luck // 2

    if random.random() <= 0.5:
        opponent['hitpoints'] = max(0, opponent['hitpoints'] - player_damage)
        player['luck'] = min(10, player['luck'] + 1)
        print(f"{GREEN}{player['name']} wins this round and deals {player_damage} damage to {opponent['name']}!{END_COLOR}")
        time.sleep(1)
    else:
        player['hitpoints'] = max(0, player['hitpoints'] - opponent_damage)
        opponent['luck'] = min(10, opponent['luck'] + 1)
        print(f"{RED}{opponent['name']} wins this round and deals {opponent_damage} damage to {player['name']}!{END_COLOR}")
        time.sleep(1)

    print(f"\n{player['name']} Hitpoints: {hitpoints_bar(player['hitpoints'], player['max_hitpoints'])}   Luck: {luck_bar(player['luck'])}")
    time.sleep(1)
    print(f"{opponent['name']} Hitpoints: {hitpoints_bar(opponent['hitpoints'], opponent['max_hitpoints'], RED)}   Luck: {luck_bar(opponent['luck'])}")
    time.sleep(1)

print("\nGame Over!")
time.sleep(1)

if player['hitpoints'] > 0 and opponent['hitpoints'] <= 0:
    print(f"{GREEN}{player['name']} wins!{END_COLOR}")
elif player['hitpoints'] <= 0 and opponent['hitpoints'] > 0:
    print(f"{RED}{opponent['name']} wins!{END_COLOR}")
else:
    print("It's a tie!")
