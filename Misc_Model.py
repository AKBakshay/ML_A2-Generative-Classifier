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

# input complete

mean = np.zeros((2, D))
N_p = 0
N_n = 0

for i in range(len(Data)):
    if y[i] == -1:
        N_n += 1
        mean[0] += X[i]
    else:
        N_p += 1
        mean[1] += X[i]

mean[0] = mean[0]/N_n
mean[1] = mean[1]/N_p

covariance = 0

for i in range(len(Data)):
    if y[i] == -1:
        covariance += np.dot(X[i]-mean[0], X[i]-mean[0])
    else:
        covariance += np.dot(X[i]-mean[1], X[i]-mean[1])

covariance = covariance/((N_n+N_p)*D)  # check for factor of D


pX = X[y[:] == 1]
nX = X[y[:] == -1]


plt.plot(pX[:, 0], pX[:, 1], "bo", nX[:, 0], nX[:, 1], "ro")
# plt.show()

# Finding the equation of the boundary
K = 1
# print(K)
k = math.sqrt(K)

C1 = K-1
C2 = K*np.dot(mean[0], mean[0])-np.dot(mean[1], mean[1])-2*covariance*D*math.log(k)

C3 = -K*(mean[0, 0]) + mean[1, 0]
C4 = -K*(mean[0, 1]) + mean[1, 1]


t = np.linspace(-10, 40, 1000)

plt.plot(t, -C2/(2*C4)-t*C3/C4, "k-")

plt.show()
