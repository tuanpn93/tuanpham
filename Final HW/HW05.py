import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('iris.data', header=-1)

df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']

df1 = df[df.Class == 'Iris-setosa']

df2 = df[df.Class == 'Iris-versicolor']

df3 = df[df.Class == 'Iris-virginica']

fig, ax = plt.subplots(3, 2, figsize=(20, 30))

ax[0, 0].plot(df1['sepal_length'], df1['sepal_width'], 'bo')
ax[0, 0].set_title("Sepal of Iris-setosa")
ax[0, 0].set_xlabel('length')
ax[0, 0].set_ylabel('width')

ax[0, 1].plot(df1['petal_length'], df1['petal_width'], 'bo')
ax[0, 1].set_title("Pepal of Iris-setosa")
ax[0, 1].set_xlabel('length')
ax[0, 1].set_ylabel('width')

ax[1, 0].plot(df2['sepal_length'], df2['sepal_width'], 'bo')
ax[1, 0].set_title("Sepal of Iris-versicolor")
ax[1, 0].set_xlabel('length')
ax[1, 0].set_ylabel('width')

ax[1, 1].plot(df2['petal_length'], df2['petal_width'], 'bo')
ax[1, 1].set_title("Pepal of Iris-versicolor")
ax[1, 1].set_xlabel('length')
ax[1, 1].set_ylabel('width')

ax[2, 0].plot(df3['sepal_length'], df3['sepal_width'], 'bo')
ax[2, 0].set_title("Sepal of Iris-virginica")
ax[2, 0].set_xlabel('length')
ax[2, 0].set_ylabel('width')

ax[2, 1].plot(df3['petal_length'], df3['petal_width'], 'bo')
ax[2, 1].set_title("Pepal of Iris-virginica")
ax[2, 1].set_xlabel('length')
ax[2, 1].set_ylabel('width')

plt.subplots_adjust(hspace=0.4)

plt.show()

