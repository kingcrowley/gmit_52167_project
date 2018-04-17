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

