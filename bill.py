#hi
from num2words import num2words 
import csv 
#import time
#import random
net_ammount = 0
b = 0
def number ():
    f = open ("bill.csv","a")
    sw = csv.writer(f)
    number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
    tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    global net_ammount
    net_ammount
    if net_ammount>99999:
        print("Cant solve for more than 5 digits")
    else:
        d=[0,0,0,0,0]
        i=0
        while net_ammount>0:
            d[i]=net_ammount%10
            i+=1
            net_ammount=net_ammount//10
            num=""
            if d[4]!=0:
                if(d[4]==1):
                    num+=tens[d[3]]+ " Thousand "
                else:
                    num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "
            else:
                if d[3]!=0:
                    num+=number[d[3]]+ " Thousand "
                if d[2]!=0:
                    num+=number[d[2]]+" Hundred "
                if d[1] != 0:
                    if (d[1] == 1):
                        num += tens[d[0]]
                    else:
                        num += nty[d[1]] + " " + number[d[0]]
                else:
                    if d[0] != 0:
                         num += number[d[0]]
                sw.writerow([num])
        
s = []
f = open("bill.csv",'a' , newline='')
def invoice():
    
    global b
    import csv 
    import time
    import random
    f = open("bill.csv",'a',newline='')
    sw = csv.writer(f,delimiter='\t')
    k = ["                                  Srikaanth stores                             "]
    sw.writerow(k)
    address = [["                No 13,Madipakkam Main road, Madipakkam\n                 chennai-600091 MOBILE NUMBER : 8778092772                                                          "]]
    sw.writerow(                                    address                                       )
    g = " 1234ZXVC26520YN"
    print("only 4 counters are there")
    cn = int(input("               which counter is billling in         "))
    if cn > 4:
        cn = 4
    sw.writerow([   f"                 GSTIN {g}       "                             f" counter no {cn}  " ]                                            )
    d = {"1": "card","2":"UPI","3":"food card","4":"cash"}
    print(d.items())
    t_payment = input("what kind of payment is done   ")
    if t_payment ==  "1":
        t_payment = "card" 
    elif t_payment == "2" :
        t_payment = "upi"
    elif t_payment == "3":
        t_payment = "food card"
    elif t_payment == "4":
        t_payment = "cash" 
    else:
        print("Invalid choice,enter number from 1 to 4")
    sw.writerow([f"                              Payment mode : {t_payment} "                               ])
    time = time.asctime()
    t = time.split()
    sw.writerow([            f"                Bill No : {b}            "   f"{time} "           ])
    lines = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ")
    sw.writerow([                    lines                                 ])
    particulars = 'Particulars'
    mrp = 'MRP'
    qty = 'QTY'
    ammount = 'Total'
    gap = ' '*10
    heading = f"{'Name':12s}{gap} {'mrp':3s}{gap} {'qty':4s}{gap} {'total':3s} "
    sw.writerow([heading])
    am = 0 
    q = 0 
    i1 = 0
    while True :
        item = input("enter the item  ")
        mrp = str(float(input("enter the price  ")))
        qty = str(int(input("enter the quantity  ")))
        m1 = float(mrp)
        q1 = float(qty)
        a1 = round(q1*m1)
        amount = a1
        r = [item,mrp,qty,amount]
        result = f"{r[0]:12s}{gap}{r[1]:3s}{gap}{r[2]:4s}{gap}{r[3]:3d}"
        am += a1
        q +=  q1
        i1 += 1
        s.append([item,float(mrp),q,am])
        gst = 25/100
        am2 = round(am*gst)
        sw.writerow([result])
        sw.writerow([                    lines                                 ])
        ch = input("enter y to continue ").lower()
        if ch != 'y' :
            end = f"Total items : {i1} " , f" Total quantity : {q} " , f" Total Ammount : {am} "
            sw.writerow([f"Total items : {i1} " , f" Total quantity : {q} " , f" Total Ammount : {am} "])
            
            global net_ammount
            net_ammount = am + am2
            sw.writerow([f"Ammount to be paid : {net_ammount}"])
            sw.writerow([f"Ammount in words : {num2words(net_ammount)} only"])
            while True :
                if t_payment == "cash" :
                    print(net_ammount)
                    gc = int(input("enter the cash you want to give"))
                    if gc == net_ammount:
                        sw.writerow([f" {net_ammount} recevied ammount"])
                        sw.writerow(["   Balance paid : 0"])
                    elif gc > net_ammount:
                        sw.writerow([f"  Recevied Ammount : {gc}"])
                        x = gc-net_ammount
                        sw.writerow([f"  Balance Ammount : {x}"])
                    else:
                        print("please your given ammount is lesser than the required ammount")
                        y = net_ammount - gc 
                        print(f"{y} is the balance to pay")
                        r  = int(input("enter the above ammount to close the transcation "))
                        if r == y : 
                            sw.writerow([f" {net_ammount} Recevied Ammount"])
                            sw.writerow([["  Balance paid : 0 "]])
                        if r > y :
                            gc+=r
                            sw.writerow([f"  Recevied ammount : {gc} "])
                            h = gc - net_ammount
                            sw.writerow([f"  Balance ammount : {h} "])
                else :
                    sw.writerow([f"   Recived Ammount : {net_ammount}"])
                    sw.writerow([  f" Balance Paid : 0"])
                break
            break


        


                
    
    
def start():
    global b
    print("hi")
    sw = csv.writer(f,delimiter='\t')
    lines = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ")
    ki = input("please enter y to bill ").lower()
    if ki == 'y':
        while True :
            b+=1
            invoice()            
            co = input("are you going to bill for another customer? If yes enter y ").lower()
            sw.writerow(                    lines                                 )
            if co != 'y':
                break
        
    else:
        print("Thank you")
        
start()


            
    

