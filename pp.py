import csv
while True:
    item = input("enter")
    q = int(input('enter'))
    ch = input("enter y to continue")
    if ch!= 'y' :
        break
k = open("products.csv",'r+',newline ='')
c = csv.reader(k)
sw = csv.writer(k)
for i in c:
    if item in i :
        x = int(i[1])
        if x > q :
            sw.writerow = (x - q) 
            if x < 21 :
                print("have to order stock")
        elif x == q :
            sw.writerow (x = 0 )
            print("you have to order stock immedietely")
        elif x == 0 :
            print("out of stock ")
        elif x < q :
            print(f"we don't have required quantity we have only this much of the prdt{x}")
        else:
            pass
    else:
        print("not in the products")


        


    

