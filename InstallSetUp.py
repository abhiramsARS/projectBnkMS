print("""If any Error occur before printing \"All Modules Found\",
          You Need to install Some Packages,
          for that you are advised to use the below mentioned commands in your Command promt at
          the location of python\n
              \" python -m pip install  tk\"
              \" python -m pip install  mysql-connector\"
              \" python -m pip install  cryptography\"
              \" python -m pip install  tabulate\"
          """)

import tkinter as tk    #importing module
import mysql.connector
import pickle
from cryptography.fernet import Fernet
from tabulate import tabulate

try:
    pwd=input("Enter Database Password :")
    db=mysql.connector.connect(host="localhost",user="root",passwd=pwd)
    csr=db.cursor()

except:
    print("Setup Error")
    exit()
    
print("="*100+"\n  All Modules Found   \n"+"="*100)

ent=input("Press Enter to - Start Database setup")
csr.execute("Create Database bankms")
csr.execute("use bankms")
print("Database Created")

csr.execute("""create table account(ac_no varchar(9) not null primary key,ac_holder varchar(20) not null,ph_no int not null,
ac_balance int,ac_status varchar(2) not null,ac_date date);""")
print("Table-1 Created")

csr.execute("""create table transaction(trans_id varchar(8) not null primary key,trns_date date not null,
trans_ac varchar(9) not null,bnf_ac varchar(9) not null,trans_method varchar(10) not null,amount integer not null ,
trans_type varchar(2) not null);""")
print("Table-2 Created")

csr.execute("""insert into account values("BAC-00001","Test",1234567890,0,'O',curdate());""")
csr.execute("""insert into transaction values("2420001",curdate(),"BAC-00001","BAC-00001","deposit",0,"c"); """)
db.commit()

print("Traial Data Added")

csr.execute("Select * from Account")
for i in csr:
    dra=i
csr.execute("Select * from Transaction")
for i in csr:
    drt=i

print("\nChecking for Data retriving")

if(dra[0]=='BAC-00001' and dra[1]=='Test'and dra[2]==1234567890):
    print("Check-1 : status : SUCESS")
    ts=1
else:
    print("Check-1 : status : Failed")
    ts=0
     
if(drt[0]=='2420001' and drt[2]=='BAC-00001'):
    print("Check-1 : status : SUCESS")
    ts=1
else:
    print("Check-2 : status : Failed")
    ts=0

