import csv
import time
import random
import sys
from memory_profiler import memory_usage
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


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
    size=len(array)
    insertionSort(array)
    #########################
    timeAfter=time.time()
    timeElapsed=timeAfter-timeBefore
    memory_used = memory_usage()[0]
    with open("sortare_rezultat.csv",mode='w',newline='') as csv_out:
        csv_writer=csv.writer(csv_out)
        csv_writer.writerow(array)
    print(timeElapsed," seconds")
    print(f"Memory used: {memory_used} MB")
 
