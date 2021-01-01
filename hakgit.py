import threading 
from threading import*
import time

dic={}
l=[]
#create
def create():
    print("Enter key value pair \n")
    key,value=map(str,input().split())
    key=int(key)
    print("Enter timeout:")
    timeout=int(input())
    timeout=timeout*60
    if key in dic:
        print("error: this key already exists") 
    else:
        if len(dic)<(1024*1020*1024) and key<=(16*1024*1024):  
            if timeout==0:
                l=[value,timeout]
            else:
                l=[value,time.time()+timeout]
            if len(value)<=32: 
                dic[key]=l
                print(dic)
            else:
                print("Memory limit exceeded!!")
        else:
            print("Invalid key_name! key_name must be alphabet only")

#read
def read():
    print("Enter key to read the pair\n")
    key=int(input())
    if key not in dic:
        print("key does not exist in database")
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                res=str(key)+":"+str(b[0])
                print(res)
            else:
                print("time-to-live of",key,"has expired")
        else:
            res=str(key)+":"+str(b[0])
            print(res)
        
#delete
def delete():
    print("Enter the key to delete\n")
    key=int(input())
    if key not in dic:
        print("Key does not Exist\n")
        
    else:
        del dic[key]
        print(dic)
        print("Successfully deleted\n")

def stack():
    file=open("hak.txt",'w+') 
    strc=str(dic)
    file.write(strc)
    file=open("hak.txt",'r') 
    print(file.read())
    file.close()

print("File based key-value data store\n")
i=1
while(i!=5):

    print("Select the operation you want to do:\n")
    print("\n1. Create \n2. Read \n3. Delete \n4. Exit\n")
    opt=int(input())
    if(opt==1):
        create()
    elif(opt==2):
        read()
    elif(opt==3):
        delete()
    elif (opt==4):
        stack()
        exit(0)
    else:
        print("Invalid Operation enter valid operation\n")
print(dic)
t1=threading.Thread(target=(create or read or delete)) 
t1.start()
time.sleep(1)
t2=threading.Thread(target=(create or read or delete))
t2.start()
time.sleep(1)
