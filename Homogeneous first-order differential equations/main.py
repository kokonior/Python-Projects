import matplotlib.pyplot as plt, numpy as np 
def func(y,x): 
    return (x+3*y)/(2*x) 
y0 = 1 
x0 = 1 
ndata = 6 
xn = 0.2 
x = np.linspace(x0,xn,ndata) 
y = np.zeros(ndata) 
y[0] = y0 
h = x[1]-x[0] 
for i in range(0,ndata-1): 
    y[i+1] = y[i] + h*func(y[i],x[i]) 
plt.plot(x,y,marker='x',color='black') 
plt.title("(Your Title)") 
plt.xlabel("Axis X") 
plt.ylabel("Axis Y") 
plt.show()