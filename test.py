#gap = ' '*3
#heading = f"{"item" : 4s} {gap} {"MRP" : 3s} {gap} {"QTY": 3s} {gap} {"Ammount": 7s} 
"""from num2words import num2words 
import time
f = open("et.txt",'w')
time = time.asctime()
f.write(time)
f.close()
open("<filename>.csv", "w").writelines(list(filter(lambda x: x != "", map(lambda x: x.strip().replace("[", "").replace("]", ""),open("<filename>.csv").readlines()))))
k = open ("et.txt")
p = k.readline()
print(type(p))
print(p.split())
f.close() """
 
import csv
def read():
    with open('bill.csv', 'r', newline='') as f:
        sr=csv.reader(f)
        for i in sr:
            for j in i:
                print(j)
read()
