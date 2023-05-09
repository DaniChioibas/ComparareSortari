import csv
import time
import random
import sys
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


with open("sortare_10k.csv",mode='r',newline='') as csv_file:
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
    bubbleSort(array)

    #########################
    timeAfter=time.time()
    timeElapsed=timeAfter-timeBefore
    with open("sortare_rezultat.csv",mode='w',newline='') as csv_out:
        csv_writer=csv.writer(csv_out)
        csv_writer.writerow(array)
    print(timeElapsed," seconds")
 
