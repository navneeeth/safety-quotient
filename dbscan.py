#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:30:56 2020

@author: navneethkrishna
"""

from sklearn.preprocessing import StandardScaler
import graphing
from sklearn.cluster import DBSCAN
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from matrixStored import matrix

x_value = graphing.x
y_value = graphing.y
places = graphing.place
pincodes_list = graphing.pincodes_list
print(x_value)
print(y_value)
print(places)
print(pincodes_list)
x = []
y = []
for item in x_value:
    x.append(float(item))
for item in y_value:
    y.append(float(item))
X = list(zip(x, y))
print(X)
flag = 0
j = 0
count = 0
distMatCount = []
countArray = []
#print(matrix[0][0])
'''
for i in matrix:
    while flag != 1:
        if(places[j] == i[0]):
            placeName = places[j]
            flag = 1
        else:
            j = j + 1
    if(i[0] == placeName and float(i[2])<100):
            count += 1
    else:
        flag = 0
        countArray.append(count)
        count = 0
        j = 0
distMatCount = list(zip(places, countArray))
print(distMatCount)
'''
import csv
with open('distMatrix.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(row[0] != 'Source'):    
            while flag != 1:
                if(places[j] == row[0]):
                    placeName = places[j]
                    flag = 1
                else:
                    j += 1
            if(row[0] == placeName and float(row[2])<25):
                count += 1
            else:
                flag = 0
                countArray.append(count)
                count = 0
                j = 0
distMatCount = list(zip(places, countArray))
print(distMatCount)

scaler = StandardScaler()
#scaler.fit(X)
#print(scaler.mean_)
scaled_matrix = scaler.fit_transform(X)
clustering = DBSCAN(eps=0.3, min_samples=4).fit(scaled_matrix)
#print(clustering.labels_)
obtained_labels = clustering.labels_
print(len(clustering.labels_))
print(len(scaled_matrix))
core_samples_mask = np.zeros_like(obtained_labels, dtype=bool)
core_samples_mask[clustering.core_sample_indices_] = True
print(core_samples_mask)
n_clusters_ = len(set(obtained_labels)) - (1 if -1 in obtained_labels else 0)
n_noise_ = list(obtained_labels).count(-1)
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
#print('Homogeneity: %0.3f' %metrics.homogeneity_score())
print('Silhouette Coefficient: %0.3f' %metrics.silhouette_score(X, obtained_labels))
unique_labels = set(obtained_labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
plt.xlim(-3.005, 3.005)
plt.ylim(-3.005, 3.005)
plt.xticks(np.arange(-3.005, 3.005, 0.005))
plt.yticks(np.arange(-3.005, 3.005, 0.005))
plt.gcf().set_size_inches(240, 240)
for k, col in zip(unique_labels, colors):
    if k == -1:
        #Black used for noise
        col = [0, 0, 0, 1]
    class_member_mask = (obtained_labels == k)
    xy = scaled_matrix[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:,1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
    xy = scaled_matrix[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:,1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' %n_clusters_)
#plt.show()
plt.savefig('images/dbscanimage1.eps', format='eps', dpi=1200)
