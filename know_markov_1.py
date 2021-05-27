import matplotlib.pyplot as plt
import numpy as np

N = 1000
sigma = 1

fSignal = np.zeros(N)
fNoise = np.random.normal(0, sigma, N)
for i in range(1, N):
    fSignal[i] = fSignal[i-1] + fNoise[i]

plt.plot(fNoise)
plt.plot(fSignal)
plt.grid(True)
plt.show()
