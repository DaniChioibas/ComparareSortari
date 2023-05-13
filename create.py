import csv
import random

array=[]
#for i in range(1000000,0,-1):    ### Pentru generarea numerelor in ordine descrescatoare
#    array.append(i)
for i in range(0,1000000):        ### Pentru generarea numerelor aleatoriu
    array.append(random.randint(1,10000000))

with open("sortare_1000k.csv",mode='w',newline='') as csv_out:
    csv_writer=csv.writer(csv_out)
    csv_writer.writerow(array)
