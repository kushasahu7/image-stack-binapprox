# Write your list_stats function here.
import math;
import numpy as np
import time
import statistics
import matplotlib.pyplot as plt
def list_stats_1 (arr) :
    size = len(arr)
    arr.sort()
    mid = math.floor(size/2)
    mean = sum(arr)/size if size > 0 else 0
    median = 0
    if size > 0: 
        if size % 2 == 0:
            median = (arr[mid-1]+arr[mid])/2
        else:
            median = arr[mid]
    return np.round(median, 5), np.round(mean, 5)

def list_stats_2 (arr) :
    mean = np.mean(arr)
    median = np.median(arr)
    return np.round(median, 5), np.round(mean, 5)

def list_stats_3 (arr) :
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    return np.round(median, 5), np.round(mean, 5)




# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
    rang = np.arange(1, 8)
    print(rang)
    normal = []
    numpyS = []
    stats = []
    for i in rang:
        arr = np.random.randn(10**i)
        start = time.perf_counter()
        m = list_stats_1(arr)
        end = time.perf_counter() - start
        normal.append(end)
        
        start = time.perf_counter()
        m = list_stats_2(arr)
        end = time.perf_counter() - start
        numpyS.append(end)
        
        start = time.perf_counter()
        m = list_stats_3(arr)
        end = time.perf_counter() - start
        stats.append(end)
    
    plt.plot(rang, normal, label = 'Inbuilt functions')
    plt.plot(rang, numpyS, label = 'numpy stats')
    plt.plot(rang, stats, label = 'Statistics import')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.legend()
    plt.show()
  
a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
  print('nbytes         :', obj.nbytes)
  print('size x itemsize:', obj.size*obj.itemsize)
