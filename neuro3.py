from math import exp, sqrt

def f_net(net):
    return (1-exp(-net))/(1+exp(-net))

def net(x, w):
    n = 0
    for i in range(len(x)):
        n += x[i]*w[i]
    return n

norma = 5
eps = 0.001
x1, x2 = [1, -1], [1, 0]
t = [-0.1, 0.2, 0.2]
w1 = [0.5, 0.5]
w2 = [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]
y = [0, 0, 0]
delta1, delta2 = [0, 0], [0, 0, 0]
J, M = len(x2), len(y)
err = 1
count = 1

print("Target: ", end = "")
for r in t: print(round(r,3), end = "\t")
print("\n№\ty\t\t\t w1\t\t w2\t\t\t\t\t\terr")
while (err > eps):
    print(count, end = "\t")
    count+=1
    err = 0
    for i in range(1,J):                    #1 этап
        x2[i] = f_net(net(x1,w1))
    for i in range(M):
        y[i] = f_net(net(x2,w2[i]))
    for r in y: print(round(r,3), end = "\t")

    w_delta = [0, 0]                        # 2 этап
    for i in range(M):
        err += (t[i]-y[i])*(t[i]-y[i])
        delta2[i] = (1-y[i]*y[i])*(t[i]-y[i])/2
        for j in range(J):
            w_delta[j] += delta2[i]*w2[i][j]
    for i in range(J):
        delta1[i] = (1-x2[i]*x2[i])*w_delta[i]/2
        
    for i in range(J):                      # 3 этап
        w1[i] += norma*x1[i]*delta1[1]
    for i in range(M):
        for j in range(J):
            w2[i][j] += norma*x2[j]*delta2[i]
    print("|", end = " ")
    for i in range(J):
        print(round(w1[i],3), end = "\t")
    print("|", end = "  ")
    for i in range(M):
        for j in range(J):
            print(round(w2[i][j],3), end = "\t")
    err = sqrt(err)
    print(err)


