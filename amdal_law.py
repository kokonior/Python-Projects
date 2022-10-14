# import important package
import numpy as np
import matplotlib.pyplot as plt

# calculate speed_up based b and s
def amdal(b, s):
    # code here
    return 1 / (1 - b + (b / s))


# create range number with numpy
x = np.arange(10, 1000)

# use looping to implement amdal law
b = 0.6
y = [amdal(b, n) for n in x]

# plot
plt.plot(x, y)
plt.show()
