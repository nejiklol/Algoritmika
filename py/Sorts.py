import random
import time

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [i for i in A if i < q]
        M = [q] * A.count(q)
        R = [i for i in A if i > q]
        return QuickSort(L) + M + QuickSort(R)
    
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
    return A
def SelectionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i+1, len(A)):
            if A[mini] > A[j]:
                mini = j
        A[i], A[mini] = A[mini], A[i]
    return

A = [1000]
for i in range (0,1000):
    A.append(random.randint(1,1000))


start_time = time.time()
QuickSort(A)
print("--- %s Time of Quick Sort ---" % (time.time() - start_time))

start_time = time.time()
BubbleSort(A)
print("--- %s Time of Bubble Sort ---" % (time.time() - start_time))

start_time = time.time()
SelectionSort(A)
print("--- %s Time of Selection Sort ---" % (time.time() - start_time))        
