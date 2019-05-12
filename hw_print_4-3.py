import matplotlib.pyplot as plt

m=1
omega=1
b=1
a=4
n=1
num=10**6
delta = (n*a+b-((n-1)*a+b))/num
x=(n-1)*a + b
X=[]
V=[]
for i in range(num):
    if x <= (n*a-b):
        v=0
    else:
        v=1/2*m*(omega**2)*(b**2-(x-n*a)**2)
    X.append(x)
    V.append(v)
    x=x+delta

plt.plot(X,V)
plt.xlabel('x')
plt.ylabel('V')
plt.title('V-x Figure in 4.3')
plt.savefig('1.png', dpi=150)