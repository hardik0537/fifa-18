# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:37:50 2018

@author: Hardik Galiawala
"""

import seaborn as sns
import pylab as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv('plot_patterns.csv')
data['Pos'] = 'FWD'


p = (data[data['Preferred Positions'].str.contains('ST')]
         .loc[data['Overall']> 70, ['Overall', 'Potential', 'Acceleration', 'Aggression', 
                 'Agility', 'Balance', 'Ball control', 'Composure', 'Crossing', 'Curve', 'Dribbling', 
                 'Finishing', 'Pos']]
    )
parallel_coordinates(p, 'Pos')
