from collections import Counter

all_games = open('input-day-2.txt', 'r')

games = all_games.read().split('\n')

# print(games[0])

# PART 1

# 12 red cubes, 13 green cubes, 14 blue cubes
# each game can have several rounds - need to check that each and every round is possible

game_dict = {}

base_rules = Counter({'red': 12, 'green': 13, 'blue': 14})
colors = ['red', 'green', 'blue']

def possible_round(cubes):
    colors = cubes.split(', ')
    print(colors)


def check_max(game):
    counts_only = [int(x) for x in game.split() if x.isnumeric()]
    # we know the game can't work because at least one round has something higher than 14
    if (max(counts_only) > 14):
        return False
    # we need to check and see which color had a count 12, 13, or 14 to find out if the rule is broken
    elif (max(counts_only) <= 14 and max(counts_only)>=12):
        return 'extra check'
        print(counts_only)
    # all the numbers are less than 12, which means that there's no chance of a round falling outside of the game cube count restrictions
    else:
        return 'possible'

    
total = 0
for g in range(len(games)):
    after = games[g].split(':')[1].strip()
    # checking if there is any number higher than 14 present
    if (check_max(after) == 'possible'):
        total = total + (g+1)
    elif (check_max(after) == 'extra check'):
        # function for extra check
        rounds = [x.strip() for x in after.split(';')]
        for r in rounds:
            possible_round(r)
        #print(rounds)
    elif (check_max(after) == False):
        continue
    
    #print(rounds)


