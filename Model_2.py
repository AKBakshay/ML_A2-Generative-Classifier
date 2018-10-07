from sklearn.svm import LinearSVC
import numpy as np
import matplotlib.pyplot as plt
import math

with open("binclassv2.txt", "r") as f:
    dataL = f.readlines()

Data = []
for num in dataL:
    Data.append(num.split(","))

D = 2  # D represents dimensionality of data

X = np.zeros((len(Data), D))
y = np.zeros((len(Data)))
i = 0
j = 0
for a in Data:
    for b in a:
        if j == 2:
            y[i] = int(b)
        else:
            X[i][j] = float(b)
        j += 1
    i += 1
    j = 0


clf = LinearSVC(random_state=0, tol=1e-4)
clf.fit(X, y)
param = clf.coef_
b = clf.intercept_
t = np.linspace(-10, 40, 10)

pX = X[y[:] == 1]
nX = X[y[:] == -1]
plt.plot(pX[:, 0], pX[:, 1], "bo", nX[:, 0], nX[:, 1], "ro")
plt.plot(t, -(b+t*param[0][0])/param[0][1], "-k")
plt.show()
