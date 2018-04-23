# David Crowley g00364706
#52167 project
from scipy.spatial import ConvexHull
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
features = iris.data.T

# http://www.tarekatwan.com/index.php/2017/12/methods-for-testing-linear-separability-in-python/
#create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Target'] = pd.DataFrame(iris.target)
df.head()
plt.clf()
plt.figure(figsize = (10, 6))
names = iris .target_names
label = (iris.target).astype(np.int)
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
for i in range(len(names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[2,3]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=names[i]) 
    for j in hull.simplices:
        plt.plot(bucket[j,0], bucket[j,1], colors[i])
plt.grid(False)
plt.legend()
plt.show()


# https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.02-Simple-Scatter-Plots.ipynb
#  explores four different dimensions of the data: 
# the (x, y) location of each point corresponds to the sepal length and width, 
# the size of the point is related to the petal width, 
# and the color is related to the particular species of flower.
#
plt.clf()
plt.style.use('seaborn-whitegrid') 


plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);
plt.legend()
plt.show()

# trying sepal

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Target'] = pd.DataFrame(iris.target)
df.head()
plt.clf()
plt.figure(figsize = (10, 6))
names = iris .target_names
label = (iris.target).astype(np.int)
colors = ['b','r','g']
plt.title('Sepal Width vs Sepal Length')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
for i in range(len(names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=names[i]) 
    for j in hull.simplices:
        plt.plot(bucket[j,0], bucket[j,1], colors[i])
plt.grid(False)
plt.legend()
plt.show()





