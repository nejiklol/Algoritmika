def laaamp(N,K,P):
    n = [0] * N
    

    while(K>0):
        p = len(P)-1
        while(p>-1):
            i=1
            #print('P[p]*i-1',P[p]*i-1,'P[p]',P[p],'len(n)',len(n),'K',K)
            while i != 1+len(n)//P[p]:
                #print(i)
                if P[p]*i-1<len(n):
                        n[P[p]*i-1] = invers(n[P[p]*i-1])
                i+=1
            p-=1
        K-=1
    print(n)
    raschet(n)
def raschet(a):
    o = 0
    for i in range(len(a)):
        o=o+a[i]
    print(o)
def invers(a):
    if a == 0:
        return 1
    else:
        return 0
#
#N = 20
#K = 3
#P = [2,3,8]


N = 172
K = 5
P = [19,2,7,13,40,23,16,45,9,1]
laaamp(N,K,P)

    
