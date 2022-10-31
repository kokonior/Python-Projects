# differential function app: dy/dx=(x+a*y)/(b*x) with input x and y
# Using Euler's Method

import matplotlib.pyplot as plt, numpy as np 

# Description
print ("differential function app: dy/dx=(x+a*y)/(b*x) with input x and y")
print ("Using Euler's Method")

# Initial Condition a,b
a = int(input("Enter the value of a: ")) 
b = int(input("Enter the value of b: ")) 

def func(y,x): 
    return (x+a*y)/(b*x)

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
t = str(input("Input your title: ")) 
plt.title(t) 
plt.xlabel("Axis X")

#Plot Label
plt.ylabel("Axis Y") 
plt.show()