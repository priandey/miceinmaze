from __future__ import print_function
import os, sys, time, datetime, json, random
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD , Adam, RMSprop
from keras.layers.advanced_activations import PReLU
import matplotlib.pyplot as plt
%matplotlib inline

visited_mark = 0.8  # Cells visited by the rat will be painted by gray 0.8
rat_mark = 0.5      # The current rat cell will be painteg by gray 0.5
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

maze = np.array([
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  0.,  1.,  0.,  1.,  0.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  0.,  1.,  0.,  1.,  0.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  0.,  1.,  0.,  1.,  0.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.]
                ])

# Actions dictionary
actions_dict = {
                LEFT: 'left',
                UP: 'up',
                RIGHT: 'right',
                DOWN: 'down',
                }

num_actions = len(actions_dict)

# Exploration factor
epsilon = 0.1
