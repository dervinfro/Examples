#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:14:36 2021

@author: user

https://towardsdatascience.com/silhouette-coefficient-validating-clustering-techniques-e976bb81d10c
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X= np.random.rand(50,2)
Y= 2 + np.random.rand(50,2)
Z= np.concatenate((X,Y))
Z=pd.DataFrame(Z) #converting into data frame for ease

sns.scatterplot(Z[0], Z[1])

KMean= KMeans(n_clusters=2)
KMean.fit(Z)
label_1=KMean.predict(Z)

print('Silhouette Score(n=2):{}'.format(silhouette_score(Z, label_1)))

KMean= KMeans(n_clusters=3)
KMean.fit(Z)
label_2=KMean.predict(Z)
print('Silhouette Score(n=3):{}'.format(silhouette_score(Z, label_2)))
# sns.scatterplot(Z[0],Z[1],hue=label,palette='deep')