import random
import copy
def rollD6():
    return random.randint(1, 6)

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
    print(f"Round {rounds + 1}")

    current_rolls = []

    for each_player in players:
        roll=rollD6()

        each_player['rolls'].append(roll)
        current_rolls.append(roll)
        print(f"{each_player['name']} rolled a {roll}")

    input("Press Enter to continue...")

    max_roll = max(current_rolls)

    winners = []

    for each_player in players:
        if each_player['rolls'][-1] == max_roll:
            each_player['wins'] += 1
            print(f"{each_player['name']} wins this round!")

            winners.append(each_player['name'])
            print(f"winners this round: {winners}")

    for each_player in players:
        if each_player['wins'] >= winning_score:
            print(f"\n {each_player['name']} wins the game!")
            gameover = True
    if gameover is False:
        input("this hated battle of dice is still going on, who will win?")
        rounds += 1



filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write("player information:\n")

        for each_player in players:
            file.write(
                f"Name: {each_player['name']}\n"
                f"* Email: {each_player['email']}\n"
                f"* Country: {each_player['country']}\n"
                f"* Wins: {each_player['wins']}\n"
                f"* Rolls: {each_player['rolls']}\n"
            )
            file.write(f"Round {round_number + 1} rolls:\n")
            for r in range(rounds):
                rolls_str = ""

            for i, each_player in enumerate(players):
                rolls_str += f"{each_player['name']}: rolled {each_player['rolls'][r]}\n"

                if i < len(players) - 1:
                    rolls_str += ", "

            file.write(rolls_str + "\n")
    




        print ("\ngame over! Result saved successfully")