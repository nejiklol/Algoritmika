import random
def solution(A):
    a = [0] * A
    intersect = 0
    c = []
    for i in range(len(a)):
        a[i] = random.randint(0,20)
        if a[i] >= len(a):
            intersect += len(a) - 1
        else:
            c.append([i-a[i],i+a[i]])
            if a[i] == 0 :
                c.append([i,i])
    ###
    c=sorted(c)
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i][0]<c[j][1]:
                print(c[i][0],c[i][1])
    
    print (intersect)
    print (a)
    print (c)
solution(10)
    
