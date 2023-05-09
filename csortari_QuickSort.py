import csv
import time
import random
import sys
sys.setrecursionlimit(999999) ### Deoarece nu functioneaza pentru mai multe numere
def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
        quickSort(array, pi + 1, high)

with open("sortare_100ki.csv",mode='r',newline='') as csv_file:
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
    quickSort(array,0,size)

    #########################
    timeAfter=time.time()
    timeElapsed=timeAfter-timeBefore
    with open("sortare_rezultat.csv",mode='w',newline='') as csv_out:
        csv_writer=csv.writer(csv_out)
        csv_writer.writerow(array)
    print(timeElapsed," seconds")
 
