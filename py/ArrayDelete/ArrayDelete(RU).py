import time
# Данный вариант реализации создает внутри функции новый массив
# Первоначальный очищается , и каждый оригинальный 
# элемент добавляется в новый массив
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
# Во втором случае, массив очищается от дубликатов 
# каждого последующего элемента

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
        memory[0] = array[count]
        memory[1] = count
    return array


# После проверки двух методов я заметил, что первый работает значительно дольше
# поскольку принцип очищения у обоих функций схож, я предполагаю, что дело в
# обработчике исключений в первом варианте
a = []
b = []
array=[{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
for i in range(10000):
    for j in array:
        a.append(j)
        b.append(j)
start_time = time.time()
print(newDel(a))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(delDub(b))
print("--- %s seconds ---" % (time.time() - start_time))
