import time
import random
from plotter import Plotter

# This functions remove dublicate values from arrays 

def newDel(array):
    newArray = []
    count = 0

    
    while array!=[]:                 
        delete = array[count]        
        newArray.append(array[count])
        TF = True
        
        while TF:                    
            try:                     
                array.remove(delete)
            except:
                TF = False
            
            
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


    
# Second one works faster as i think because of "try except" block
# below are the tests and checking the running time of the functions
def testTime(func):
    a = []
    testArray = []
    for n in range(1000,30000,2000): 
        for i in range(n):
            a.append(random.randint(0,n))
        start_time = time.time()
        a = func(a)
        testArray.append(a,n)
        funcName = func.__name__
        print(funcName ,'test with', n , "=== %s seconds ===" % (time.time() - start_time))
        
    to_plot = [{
    "title": funcName,
    "type": "plot",
    "data": [testArray[0], testArray[1]]
    }]

    pl = Plotter(to_plot)
    pl.show()
    

testTime(newDel)
testTime(delDub)


