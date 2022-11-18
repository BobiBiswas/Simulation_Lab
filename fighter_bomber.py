import random
from random import randrange
from math import sqrt
import matplotlib.pyplot as plt

def pursuit():
    flag,vf,time=0,20,0
    xf=randrange(0,1001)
    yf=randrange(0,1001)
    xb=randrange(0,1001)
    yb=randrange(0,1001)

    while flag ==0:
        d=(yb-yf)*(yb-yf)+(xb-xf)*(xb-xf)
        distance=sqrt(d)
        plt.plot(xb,yb,'r*')
        plt.plot(xf,yf,'g*')

        print("time",time,"xf=",xf,"yf=",yf,"xb=",xb,"yb=",yb,"distance=",distance)

        if distance<=100:
            print("The bomber plane was shot down  at",time)
            flag=1
        elif distance>900:
            print("The bomber plane escape from sight at",time)
            flag=1
        else:
            xf=xf+vf*(xb-xf)/distance
            yf=yf+vf*(yb-xf)/distance
            xb=randrange(0,1001)
            yb=randrange(0,1001)
            time=time+1
pursuit()
plt.show()
