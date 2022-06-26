import multiprocessing as mp
import numpy as np
import time
import concurrent.futures as cf


cpu = mp.cpu_count()
data = list(range(100))


# size = len(data) // cpu

# data = [list(array) for array in np.array_split(np.array(data), len(data) // size)]



def search(num, data):
    data = sorted(data)
    minn = 0
    maxx = len(data)-1
    mid = maxx//2

    while True : 
        print(data)
        if len(data) == 0:
            print("data tidak ditemukan")
            return False
        elif num == data[mid] :
            print("data ditemukan = " + str(data[mid]))
            return True
        elif num < data[mid] : 
            data = data[minn:mid]
            maxx = len(data) - 1
            mid = maxx//2

        else :
            data = data[mid + 1: maxx + 1]
            maxx = len(data) - 1
            mid = maxx//2

t1 = time.perf_counter()
search(100,data)

t2 = time.perf_counter()

print(t2 - t1)