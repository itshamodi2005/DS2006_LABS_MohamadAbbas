import random
import copy


def rollD6():
    return random.randint(1, 6)

def rollD12():
    return random.randint(1, 12)

winning_score = 3


Player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []  
}

players = []
number_of_players = int(input("Enter number of players: "))

for i in range(number_of_players):
    player = copy.deepcopy(Player_info)

    player["name"] = input(f"Enter name of player {i+1}: ")
    player["email"] = input(f"Enter email of player {i+1}: ")
    player["country"] = input(f"Enter country of player {i+1}: ")

    players.append(player)

gameover = False
rounds = 0

while gameover is False:
    print(f"\n--- Round {rounds + 1} ---")

    current_totals = []  

    for each_player in players:
        
        d6 = rollD6()
        d12 = rollD12()
        total = d6 + d12

        
        each_player['rolls'].append((d6, d12, total))
        current_totals.append(total)

        print(f"{each_player['name']} rolled D6={d6}, D12={d12}, Total={total}")

    input("Press Enter to continue...")

    max_total = max(current_totals)

    winners = []
    for each_player in players:
        if each_player['rolls'][-1][2] == max_total:   
            each_player['wins'] += 1
            winners.append(each_player['name'])

    print(f"Round winners: {winners}")

    for each_player in players:
        if each_player['wins'] >= winning_score:
            print(f"\n {each_player['name']} wins the game!")
            gameover = True
    if gameover is False:
        input("This heated battle of dice is still going on... Who will win?")
        rounds += 1


filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    file.write("=== Game Summary ===\n\n")
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"Email: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n"
            f"Rolls:\n"
        )
        
        for r, roll in enumerate(each_player['rolls']):
            d6, d12, total = roll
            file.write(f"  Round {r+1}: D6={d6}, D12={d12}, Total={total}\n")
        file.write("\n")

print("\nGame over! Result saved successfully.")
