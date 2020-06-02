from random import randint
import numpy as np


# Randomly shuffles a list
def shuffle(my_list):
    i = len(my_list) - 1
    while i > 0:
        j = randint(0, i)
        my_list[j], my_list[i] = my_list[i], my_list[j]
        i = i - 1
    return my_list


# Sets players to random, even teams
def get_teams(num_teams, players):
    shuffled_players = np.array(shuffle(players))
    return np.array_split(shuffled_players, int(num_teams))
