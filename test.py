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




def between(l,t):
    sum = 0
    date = ''
    invi = ''
    pro = ''
    id = ''
    stocks = ''
    for i in l:
        if len(i) == 3:
            for j in t:
                if i[0].lower() in j[0].lower():
                    stocks += j[1] + ',' + ' '
            pro += i[0] + ',' + ' '
            id += str(i[1]) + ',' + ' '
        else:
            date += i[0] + ',' + ' '
            invi += str(i[1]) + ',' + ' '
            sum += i[2]

    print('Dates: ', date)
    print('Invoice no: ', invi)
    print('Product id: ', id)
    print('Products: ', pro)
    print('Total amount sold: ', sum)








    def checking():
    global date
    global i1
    global q1
    global v 
    global f
    global j 
    x = input("Enter the date you want to check :")
    if x in date :
        while True:
            for  i in f:
                sum = 0 
                items = 0
                quantity = 0
                while True:
                    
                    print(v)
                    print(g)
                    print(j)
                    read()
                    break
                break
            break
