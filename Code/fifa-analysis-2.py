# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:05:38 2018

@author: Hardik Galiawala
"""

import seaborn as sns
import pylab as pl
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('processed_data.csv')
#print(data.iloc[:, 1])

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
print(kmeans.cluster_centers_)
pl.figure('K-means with 3 clusters')
pl.scatter(data.iloc[:, 15], data.iloc[:, 16], c=kmeans.labels_)
pl.show()
