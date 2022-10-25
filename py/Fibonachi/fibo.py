def f(x):
    a = [0]
    i=[0,1]
    while len(a)!=x:
        i[0],i[1] = i[1],i[0]+i[1]
        if i[1]%2==0:
            a.append(i[1])
    return a
print(f(5))
