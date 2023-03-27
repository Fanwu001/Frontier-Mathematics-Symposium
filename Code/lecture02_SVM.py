import random
y=[0]*100
y[0]=0
a=0.6
i=1
while i<101:
    y[i]=a*y[i-1]+random.gauss(0,1)
print(y[0])
