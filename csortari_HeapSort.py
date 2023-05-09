import csv
import time
import random
import sys
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
 
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

with open("sortare_300ki.csv",mode='r',newline='') as csv_file:
    csv_reader=csv.reader(csv_file)
    array=[]
    for row in csv_reader:
        for column in row:
            if (column=='\n'):
                break
            array.append(int(column))
    ###
    timeBefore=time.time() ## Initializam timpul,iar apoi incepem sortarea
    ######################### 
    size=len(array)-1
    heapSort(array)

    #########################
    timeAfter=time.time()
    timeElapsed=timeAfter-timeBefore
    with open("sortare_rezultat.csv",mode='w',newline='') as csv_out:
        csv_writer=csv.writer(csv_out)
        csv_writer.writerow(array)
    print(timeElapsed," seconds")
 
