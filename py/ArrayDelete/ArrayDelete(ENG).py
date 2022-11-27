import time
import random
import matplotlib.pyplot as plt

# This functions remove dublicate values from arrays 

def newDel(array):
    newArray = []
    count = 0

    
    while array!=[]:                 
        delete = array[count]        
        newArray.append(array[count])
        
        
        while delete in array:
            array.remove(delete)
            
            
            
    return newArray


def delDub(array):
    
    count = 0
    memory = [array[count],0]
    while True:
        while count!=len(array):
            if (array[count]==memory[0]) & (count!=memory[1]):
                array.pop(count)
                count=count-1

            count+=1
        count = memory[1]+1
        if count==len(array):
            break
        memory = [array[count],count]
    return array


    
# Second one works slower as i think because in "delDub" the algorithm calls the array "memory",
# after removing elements from the main array
# below are the tests and checking the running time of the functions
def testTime(func):
    funcArrayTest = []
    Time = []
    x = []
    for n in range(1000,15000,7000): 
        for i in range(n):
            funcArrayTest.append(random.randint(0,n))
        start_time = time.time()
        result = func(funcArrayTest)
        endTimer=(time.time() - start_time)
        x.append(n)
        Time.append(endTimer)
        funcName = func.__name__
    return [x,Time,funcName]
    

a = testTime(newDel)
b = testTime(delDub)

# Diagram shows that first is more optimal than "newDel" much slower than "delDub"
fig=plt.figure()
fig.show()
ax=fig.add_subplot(111)
ax.plot(a[0],a[1],c='b',marker="^",ls='--',label=a[2],fillstyle='none')
ax.plot(b[0],b[1],c='g',marker=(8,2,0),ls='--',label=b[2])

plt.legend(loc=2)
plt.draw()



