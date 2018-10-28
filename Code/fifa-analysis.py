# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:05:38 2018

@author: Hardik Galiawala
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('fifa-dataset/CompleteDataset.csv')
value = data['Value'].str.replace('€', '')
value = value.str.replace('M', '')
value = value.str.replace('K', '')
data['Value_new'] = value.astype('float64') * 1000000

wage = data['Wage'].str.replace('€', '')
wage = wage.str.replace('K', '')
data['Wage_new'] = wage.astype('float64') * 1000

processed = data[['Age', 'Value_new', 'Wage_new', 'Overall', 'Potential', 'Special', 
                 'Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control', 'Composure', 'Crossing', 'Curve', 'Dribbling', 
                 'Finishing', 'Free kick accuracy',
                 'GK diving', 'GK handling', 'GK kicking', 'GK positioning', 'GK reflexes', 
                 'Heading accuracy', 'Interceptions', 'Jumping', 'Long passing', 'Long shots', 'Marking', 'Penalties', 'Positioning', 'Reactions', 'Short passing', 'Shot power', 'Sliding tackle', 'Sprint speed', 'Stamina', 'Standing tackle', 'Strength', 'Vision', 'Volleys', 'CAM', 'CB', 'CDM', 'CF', 'CM', 'ID', 'LAM', 'LB', 'LCB', 'LCM', 'LDM', 'LF', 'LM', 'LS', 'LW', 'LWB', 'RAM', 'RB', 'RCB', 'RCM', 'RDM', 'RF', 'RM', 'RS', 'RW', 'RWB', 
                 'ST', 'Preferred Positions']]

processed = processed.fillna(0)


processed_test = processed
print(processed_test.shape[0])

for col in ['Age', 'Overall', 'Potential', 'Special', 
                 'Acceleration', 'Aggression', 
                 'Agility', 'Balance', 'Ball control', 'Composure', 'Crossing', 'Curve', 'Dribbling', 
                 'Finishing', 
                 'Free kick accuracy', 'GK diving', 'GK handling', 'GK kicking', 'GK positioning', 'GK reflexes', 'Heading accuracy', 'Interceptions', 'Jumping', 'Long passing', 'Long shots', 'Marking', 'Penalties', 'Positioning', 'Reactions', 'Short passing', 'Shot power', 'Sliding tackle', 'Sprint speed', 'Stamina', 'Standing tackle', 'Strength', 'Vision', 'Volleys', 'CAM', 'CB', 'CDM', 'CF', 'CM', 'ID', 'LAM', 'LB', 'LCB', 'LCM', 'LDM', 'LF', 'LM', 'LS', 'LW', 'LWB', 'RAM', 'RB', 'RCB', 'RCM', 'RDM', 'RF', 'RM', 'RS', 'RW', 'RWB', 
                 'ST']:
    for row in range(processed.shape[0]):
        processed.loc[row, col] = pd.eval(processed.loc[row, col])
    
processed.to_csv('plot_patterns.csv', header = True, index = False)
