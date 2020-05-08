import csv
import os
def add_record():
    while True:
                print("enter 1 for ccvt")
                print("enter 2 for ogi")
                print("enter 3 for iot")
                n=int(input())
                if n==1:
                    record("ccvt.csv")
                    break
                if n==2:
                    record("ogi.csv")
                    break
                if n==3:
                    record("iot.csv")
                    break
                else:
                    print("Invalid choice")
  
    
def record(filename):
    while True:
        import os
        if os.path.exists(filename):
            with open(filename,'a',newline="") as f:
                w=csv.writer(f)
                name=input("enter your name : ")
                gender=input("enter your gender : ")
                phno=input("enter your phno : ")
                
                dob=input("enter your dob : ")                    
                address=input("enter your address :")
                pincode=input("enter pincode of the place")
                region=input("enter your regon: state : ")
                w.writerow([name,gender,phno,dob,address,pincode,region])
                option=input("do you want to enter one more record : y/n : ")
                if option.lower()=='n':
                        break
                     
        else:   
            with open(filename,'a',newline="") as f:
                w=csv.writer(f) 
                w.writerow(['name','gender','phno','dob','address','pincode','region'])
                name=input("enter your name : ")
                gender=input("enter your gender : ")
                phno=input("enter your phno : ")
                
                dob=input("enter your dob : ")                    
                address=input("enter your address :")
                pincode=input("enter pincode of the place")
                region=input("enter your regon: state : ")
                w.writerow([name,gender,phno,dob,address,pincode,region])
                option=input("do you want to enter one more record : y/n : ")
                if option.lower()=='n':
                    break
def ratio():
    while True:
                print("enter 1 for ccvt")
                print("enter 2 for ogi")
                print("enter 3 for iot")
                n=int(input())
                if n==1:
                    mf("ccvt.csv")
                    break
                if n==2:
                    mf("ogi.csv")
                    break
                if n==3:
                    mf("iot.csv")
                    break
                else:
                    print("Invalid choice")
def mf(filename): 
     if os.path.exists(filename):
        with open(filename,'r',newline="") as f:
            c=0
            i=0
            r=csv.reader(f)
            data=list(r)
            data=data[1:]
            for x in data:
                d=x[1]
                if d=='male':
                    c=c+1
                elif d=='female':
                    i=i+1
                else:
                     print("not defined")
                a=i+c     # a is the total sum of male and female
            print("ratio of male is:",c/a)
            print("ratio of female is:",i/a)
     else:
        print("First Enter some data than check records !")
def diversity():
    while True:
                print("enter 1 for ccvt")
                print("enter 2 for ogi")
                print("enter 3 for iot")
                n=int(input())
                if n==1:
                    region("ccvt.csv")
                    break
                if n==2:
                    region("ogi.csv")
                    break
                if n==3:
                    region("iot.csv")
                    break
                else:
                    print("Invalid choice")
def region(filename):
     if os.path.exists(filename):
        with open(filename,'r',newline="") as f:
            r=csv.reader(f)
            data=list(r)
            d={}
            data=data[1:]
            print(data)
            for x in data:
                value=x[6].lower()
                d[value]=d.get(value,0)+1
            print("diversity ratio is:",sum(d.values())/len(d.values()))
     else:
        print("Enter record first Than check the records !")
def show():
    
        while True:
            print("enter 1 for ccvt")
            print("enter 2 for ogi")
            print("enter 3 for iot")
            print("enter 4 for exit")
            n=int(input())
            if n==1:
                showrecord("ccvt.csv")
            elif n==2:
                showrecord("ogi.csv")
            elif n==3:
                showrecord("iot.csv")
            elif n==4:
                print("Exiting ... Show record")
                break
            else:
                print("invalid choice:")
            
        
def showrecord(filename):
     if os.path.exists(filename):
        with open(filename,'r',newline="") as f:
            r=csv.reader(f)
            data=list(r)
            for row in data:
                for col in row:
                    print(col,end=' ')
                print()
     else:
        print("Enter records first than check data !")
def clear():
    os.system('cls')
while True:
    print("enter 1 to add record")
    print("enter 2 to show record")
    print("enter 3 to get male/female ratio")
    print("enter 4 to get diversity region ratio")
    print("enter 5 to exit")
    ch=int(input())
    if ch==1:
        clear()
        add_record()
    elif ch==2:
        clear()
        show()

    elif ch==3:
        clear()
        ratio()
    elif ch==4:
        clear()
        diversity()
    elif ch==5:
        print("exiting ! ... Thank you for using our application")
        break
    else:
        print("invalid choice")

