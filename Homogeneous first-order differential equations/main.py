# Differential Function: dy/dx=(x+3*y)/(2*x) with input x and y
# Using Euler's Method

import matplotlib.pyplot as plt, numpy as np 
def func(y,x): 
    return (x+3*y)/(2*x)

# Initial Condition
y0 = int(input("Enter the value of y: ")) 
x0 = int(input("Enter the value of x: "))

# Discretization process
ndata = 6 
xn = 0.2 
x = np.linspace(x0,xn,ndata) 
y = np.zeros(ndata) 
y[0] = y0 
h = x[1]-x[0] 
for i in range(0,ndata-1): 
    y[i+1] = y[i] + h*func(y[i],x[i]) 

#plot    
plt.plot(x,y,marker='x',color='black')

#Plot Title
plt.title("(Your Title)") 
plt.xlabel("Axis X")

#Plot Label
plt.ylabel("Axis Y") 
plt.show()