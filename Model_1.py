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

covariance = np.zeros((D))

for i in range(len(Data)):
    if y[i] == -1:
        covariance[0] += np.dot(X[i]-mean[0], X[i]-mean[0])
    else:
        covariance[1] += np.dot(X[i]-mean[1], X[i]-mean[1])

covariance[0] = covariance[0]/(N_n*D)  # check for factor of D
covariance[1] = covariance[1]/(N_p*D)


pX = X[y[:] == 1]
nX = X[y[:] == -1]


plt.plot(pX[:, 0], pX[:, 1], "bo", nX[:, 0], nX[:, 1], "ro")
# plt.show()

# Finding the equation of the boundary
K = covariance[1]/covariance[0]
# print(K)
k = math.sqrt(K)

C1 = K-1
C2 = K*np.dot(mean[0], mean[0])-np.dot(mean[1], mean[1])-2*covariance[1]*D*math.log(k)

C3 = -K*(mean[0, 0]) + mean[1, 0]
C4 = -K*(mean[0, 1]) + mean[1, 1]
C5 = C3/C1
C6 = C4/C1
C7 = C2/C1
R = C5*C5+C6*C6-C7
t = np.linspace(-C5-np.sqrt(R), -C5+np.sqrt(R), 1000)
plt.plot(t, -C6+np.sqrt(np.abs(R-(t+C5)**2)), "k-", t, -C6-np.sqrt(np.abs(R-(t+C5)**2)), "k-")
# plt.axis([-20, 50, -20, 50])
plt.show()
