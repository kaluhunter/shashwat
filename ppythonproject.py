import os
import mysql.connector
import datetime
import time







mydb=mysql.connector.connect(user="root",password="12341234",host="localhost",database="air_ticket_reservation")
mycursor=mydb.cursor()


def main():
    print(" Welcome to AIR TICKET RESERVATION .....")
    time.sleep(2)
    
    def registration ():
        L=[]
        ID= int(input("Enter your id ->"))
        L.append(ID)
        Name= input("enter your name -> ")
        L.append(Name)
        Address=input ("enter your address ->")
        L.append(Address)
        TravelDate=input("enter date of boarding ->")
        L.append(TravelDate)
        Source=input("enter your source place ->")
        L.append(Source)
        Destination=input ("enter your destination ->")
        L.append(Destination)

        cust=(L)
        sql="insert into PData(ID,Name,Address,TravelDate,Source,Destination)values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,cust)
        mydb.commit()
        print ("Your entery is sucessfully save...")
        menuset()
        

        
            
    def classtype ():
        print("do you want to see available class types: press 1 for yes")
        ch=int(input("enter your choice"))
        if ch==1:
            sql="select* from classtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
        menuset()
        

    def ticketprice():
        print("Following rooms are available")
        print ("1. First class :- 5000")
        print ("2. Business class :- 4000")
        print ("3. Economy class :- 3000")
        x= int (input ("enter your choice"))
        n=int (input ("no. of passengers"))
        if x==1:
            print(n*5000," is your payable amount ")
        elif x==2:
            print (n*4000,"is your payable amount ")
        elif x==3:
            print(n*3000,"is your paybale amount ")
        else:
            print("please choose a class type")
        menuset()
        


    def menuview():
        print (" Do you want to see available menu for food : if yes enter 1")
        ch=int (input("Enter your choice"))
        if ch==1 :
            sql="select* from food"
            mycursor.execute(sql)
            rows =mycursor.fetchall()
            for x in rows():
                print (x)
        else:
            print("invalid choice.... to see the menu ")
        menuset()
        


    def orderitem():
        global s
        print (" Do you want to order any item : Enter 1 for yes")
        ch=int(input("ENTER HERE  "))
        if ch==1 :
            sql="select* from food"
            mycursor.execute(sql)
            rows =mycursor.fetchall()
            if rows:
                print("Available food items:")
                for x in rows:
                    print(x)
            else:
                print("No food items for you.")
            
            
            
            print ("From the above list what you want to order ")
            d= int (input("Enter your choice"))
            if d==1:
                print ("you selected tea")
                a=int(input("enter the quantity"))
                s=10*a
                print("Your payable amount is",s)
            elif d==2:
                print ("you selected coffee")
                a=int(input("enter the quantity"))
                s=20*a
                print("Your payable amount is",s)
            elif d==3:
                print ("you selected cold drink")
                a=int(input("enter the quantity"))
                s=30*a
                print("Your payable amount is",s)
            elif d==4:
                print ("you selected samosa")
                a=int(input("enter the quantity"))
                s=10*a
                print("Your payable amount is",s)
            elif d==5:
                print ("you selected sandwich")
                a=int(input("enter the quantity"))
                s=50*a
                print("Your payable amount is",s)
            elif d==6:
                print ("you selected dhokla")
                a=int(input("enter the quantity"))
                s=30*a
                print("Your payable amount is",s)
            elif d==7:
                print ("you selected kachori")
                a=int(input("enter the quantity"))
                s=20*a
                print("Your payable amount is",s)
            elif d==8:
                print ("you selected milk")
                a=int(input("enter the quantity"))
                s=20*a
                print("Your payable amount is",s)
            elif d==9:
                print ("you selected noodles")
                a=int(input("enter the quantity"))
                s=50*a
                print("Your payable amount is",s)
            elif d==10:
                print ("you selected pasta")
                a=int(input("enter the quantity"))
                s=50*a
                print("Your payable amount is",s)
            else:
                print("please enter your choice from the menu again")
            menuset()
                


    def luggagebill():
        global z
        print("Do you want to see the rate of luggage : Enter 1 for yes")
        if ch==1:
            sql="select* from luggage"
            mycursor.execute(sql)
            rows =mycursor.fetchall()
            for x in rows():
                print (x)
            y = int(input(" Extra weight of luggage"))
            z=y*1000
            print("your bill is ",z)
        return z
        menuset()
        runagain()
    def lb():
        print(z)
    
    def snack():
        print (s)
    def ticketamount():
        a=input("Enter customer name")
        print (a,"here your bills are")
        print (lb,"is your luggage bill")
        print (snack,"is your food bill")
        
        menuset()
        
    def menuset():
        print (" THESE ARE THE OPTIONS  ")
        print ("Press 1: to enter customer data")
        print ("Press 2: to view class ")
        print ("Press 3: to view ticketamount")
        print ("Press 4: to view food menu ")
        print ("Press 5: to order food ")
        print ("Press 6: to view luggage bill")
        print ("Press 7: to view complete amount")
        print ("Press 8: to exit ")

        uip= int(input("ENTER YOUR CHOICE:- "))
        if  uip==1:
            registration()
            
        elif uip==2:
            ticketprice()
            
            
        elif uip==3:
            classtype()
            menuset()
        elif uip==4:
            menuview()
            
        elif uip==5:
            orderitem()
            
        
        elif uip==6:
            luggagebill()
            
        elif uip==7:
            ticketamount()
            
        elif uip==8:
            quit()
        else :
            print("Enter correct choice")
    menuset()
    runagain()
    def runagain():
        run = input("\n want to run again :y/n")
        while(run.lower()=="y"):
            if platform.system()=="windows":
                print(os.system("cls"))
        else:
            print(os.system("clear"))
        menuset()
        run=input("\n want to run again y/n")
        runagain()
    
        
main()            
   
    
        
