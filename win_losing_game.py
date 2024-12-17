#!/usr/bin/env python3

#WINNING A LOSING GAME FROM GABOR SZEKELY - PARADOXES IN PROBABILITY
#in a game of even trials player A wins a point with 0.45, player B with 0.55 probability
#player with more than half the points wins the game
#find the optimal playing time for A


import random
#import matplotlib.pyplot as plt

def simulate_game(n_trials):
    trials = 0
    points_A = 0
    while trials < n_trials:
        if random.random() < 0.45:
            points_A += 1
        trials += 1
    
    # Player A wins if he has more than half of the points
    return points_A > n_trials / 2

def estimate_win_probability(n_trials, num_simulations=100000):
    wins = sum(simulate_game(n_trials) for _ in range(num_simulations))
    return wins / num_simulations

#win_probs=[]
# Testing for different even numbers of trials
for n in range(2, 21, 2): # From 2 to 20 trials, stepping by 2
    prob = estimate_win_probability(n)
    #win_probs.append(prob)
    print(f"Probability of Player A winning with {n} trials: {prob:.4f}")

#plt.plot(range(2,42,2),win_probs)
#plt.show()
