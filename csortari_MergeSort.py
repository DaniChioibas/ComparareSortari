import csv
import time
import random
import sys
def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
    mergeSort(array)

    #########################
    timeAfter=time.time()
    timeElapsed=timeAfter-timeBefore
    with open("sortare_rezultat.csv",mode='w',newline='') as csv_out:
        csv_writer=csv.writer(csv_out)
        csv_writer.writerow(array)
    print(timeElapsed," seconds")
 
