def form_teams():
    players = []
    number_of_players = int(input("Number of players: "))
    for i in range(number_of_players):
        name = input("Name: ")
        skill_level = input("Skill (Beginner/Intermediate/Advanced): ")
        player = (name, skill_level)
        players.append(player)
    return players
def group_by_skill(players):
    grouped = {}
    for name, skill_level in players:
        if skill_level not in grouped:
            grouped[skill_level] = []
        grouped[skill_level].append(name)
    return grouped
players = form_teams()
print("Players:", players)
grouped_players = group_by_skill(players)
print("Grouped:", grouped_players)