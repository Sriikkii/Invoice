
#import csv 
#import time
#import random
def invoice():
    import csv 
    import time
    import random
    f = open("bill.csv",'w')
    sw = csv.writer(f)
    k = ["                                  Srikaanth stores                             "]
    sw.writerow(k)
    address = ["                No 13,Madipakkam Main road, Madipakkam\n                 chennai-600091 MOBILE NUMBER : 8778092772                                                          "]
    sw.writerow(                                    address                                       )
    g = " 1234ZXVC26520YN"
    cn = int(input("               which counter is billling in         "))
    sw.writerow([   f"                 GSTIN {g}       "                             f" counter no {cn}  " ]                                            )
    t_payment = input("what kind of payment is done   ")
    if t_payment ==  "1":
        t_payment = "card" 
    elif t_payment == "2" :
        t_payment = "upi"
    elif t_payment == "3":
        t_payment = "food card"
    else :
        t_payment = "cash" 
    sw.writerow([f"                              Payment mode : {t_payment} "                               ])
    n = random.randint(1,10000)
    time = time.asctime()
    sw.writerow([            f"                Bill No : {n}            "   f"{time} "           ])
    lines = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ")
    sw.writerow([                    lines                                 ])
    sw.writerow([f"particulars",f"MRP",f"OTY",f"Amount" ])
    am = 0 
    q = 0 
    i1 = 0
    while True :
        item = input("enter the item  ")
        mrp = str(int(input("enter the price  ")))
        qty = str(int(input("enter the quantity  ")))
        m1 = int(mrp)
        q1 = int(qty)
        a1 = q1*m1
        amount = str(a1)
        sw.writerow([f"{item }",f"{ mrp }",f"{ qty}",f"{amount}"                     ])
        am += a1
        q +=  q1
        i1 += 1
        
        ch = input("enter y to continue").lower()
        if ch != 'y':
            break

    sw.writerow([                    lines                                 ])
    sw.writerow([f" Total items : {i1} " , f" Total quantity : {q} " , f" Total Ammount : {am} "])
    
invoice()
    







