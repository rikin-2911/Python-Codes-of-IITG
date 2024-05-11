import numpy as np     
from numpy import random as rn    
def coin_toss_experiment(num_trials):
    coin_tosses = np.random.randint(2, size = num_trials)
    sample_mean = np.mean(coin_tosses)
    return sample_mean

list = [10, 100, 10000, 10000, 1000]
for num_trials in list:
    sample_mean = coin_toss_experiment(num_trials)
    print(sample_mean)

""" This the probability of the outcomes,
 for how many times we flip te coins""" 
   