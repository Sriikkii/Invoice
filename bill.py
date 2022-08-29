#hi
import csv 
#import time
#import random
net_ammount = 0
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
f = open("bill.csv",'a')
def invoice():
    
    import csv 
    import time
    import random
    f = open("bill.csv",'a')
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
    elif t_payment == "4":
        t_payment = "cash" 
    else:
        print("Invalid choice,enter number from 1 to 4")
    sw.writerow([f"                              Payment mode : {t_payment} "                               ])
    n = 0
    while True:
        if n == 0 :
            n+=1
            gg = input("enter y to break")
            if gg != 'y':
                break
            else:
                break
    time = time.asctime()
    sw.writerow([            f"                Bill No : {n}            "   f"{time} "           ])
    lines = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ")
    sw.writerow([                    lines                                 ])
    particulars = 'Particulars'
    mrp = 'MRP'
    qty = 'QTY'
    ammount = 'Ammount'
    gap = ' '*11
    heading = f"{ 'particulars':7s} {gap} {'mrp':3s} {gap} { 'qty':6s} {gap} { 'ammount':8s} "
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
        result = f"{r[0]:7s} {gap} {r[1]:3s} {gap} {r[2]:6s} {gap} {r[3]:8d}"
        am += a1
        q +=  q1
        i1 += 1
        s.append([item,float(mrp),q,am])
        gst = 25/100
        am2 = round(am*gst)
        sw.writerow([result])
        sw.writerow([                    lines                                 ])
        ch = input("enter y to continue").lower()
        if ch != 'y' :
            sw.writerow([f"Total items : {i1} " , f" Total quantity : {q} " , f" Total Ammount : {am} "])
            
            global net_ammount
            net_ammount = am + am2
            sw.writerow([f"Ammount to be paid : {net_ammount}"])
            sw.writerow([number()])
            if t_payment == 1 :
                sw.writerow([f"Recieved ammount : {net_ammount}"])
                sw.writerow(["Balance paid : 0"])
            elif t_payment == 2:
                sw.writerow([f"Recieved ammount : {net_ammount}"])
                sw.writerow(["Balance paid : 0"])
            elif t_payment == 3:
                sw.writerow([f"Recieved ammount : {net_ammount}"])
                sw.writerow(["Balance paid : 0"])
            elif t_payment == 4:
                ca = int(input("enter the ammount to give "))
                if ca > net_ammount :
                    sw.writerow([f"Recieved ammount : {ca}"])
                    ba = ca - net_ammount
                    sw.writerow([f"Balance paid : "])
                elif ca == net_ammount :
                    sw.writerow([f"Recieved ammount : {net_ammount}"])
                    sw.writerow(["Balance paid : 0"])
                else:
                    print("invalid ammount your ammount need to greater than equal to net ammount")
                    sw.writerow([                    lines                                 ])
                    sw.writerow(["Thank you visit again "])
                    sw.writerow(["Goods once sold cannot return back"])
            break
    
    
def start():
    print("hi")
    sw = csv.writer(f)
    lines = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ")
    ki = input("please enter y to bill ").lower()
    if ki == 'y':
        while True :
            invoice()
            co = input("are you going to bill for another customer? If yes enter y ").lower()
            sw.writerow([                    lines                                 ])
            if co != 'y':
                break
    else:
        print("Thank you")
        
start()


            
    

