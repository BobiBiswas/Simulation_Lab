a=100
b=50
c=0
t=.1
k1=.008
k2=.002
t1=0

for i in range(60):
    print("a=",round(a,2),"b=",round(b,2),"c=",round(c,2),"t=",round(t1,2))
    a1=a+(k2*c-k1*a*b)*t
    b1=b+(k2*c-k1*a*b)*t
    c1=c+(2*k1*a*b-k2*c)*t
    a=a1
    b=b1
    c=c1
    t1=t1+t