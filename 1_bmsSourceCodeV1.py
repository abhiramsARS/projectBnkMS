# Project : BANK MANAGEMENT SYSTEM [BnkMS]

#####################################################################################################################
import tkinter as tk     #importing TKINTER module for : Creating User friendly Graphical unser interface environment
import mysql.connector     #importing MYSQL module for : Connecting to MySQL database for efficent Data management
import pickle     #importing PIKCLE module for : Reading from binary(.bin) files
from cryptography.fernet import Fernet     #importing CRYPTOGRAPHY module for : Decrypting hashed password 
from tabulate import tabulate     #importing TABULATE module for : Tabular Representation of data

#####################################################################################################################


def closeWindow():
    root.destroy()

#====================================================================================================================

def errorWindow(typ,back=1):
    def back_to():
        if back==1:  # back to Main Window
            main()
        elif back==2:  # back to Admin Window
            adminWindow()
        elif back==3:  # back to account login Window
            accountLogin()
        else:
            main()
        
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('500x500')    # setting size of window
    root.configure(bg='#fae1e1')
    root.title("Error") #adding Title to a program
            
    label1=tk.Label(root,text=typ,font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
    button3 = tk.Button(root,text='okay',font=('Ariel',16),width='20',bg='white',command=back_to)
    
    label1.pack()    
    button3.pack(pady=20)
    
#====================================================================================================================
def importPasswords():
    global pwd_dict    # Password Dictionary
    Tpwd_lst=[]  # Temporary Password List
    with open('datakey.bin','rb') as f1:              # Extracting encryption key
        key=pickle.load(f1)
    cipher = Fernet(key)

    with open('passwords.bin','rb') as f2:            # Extracting Hashed Passwords
        retfiles=pickle.load(f2)   # Retrieved data from Files

    for i in retfiles:                                # Data Decrytion  
        i=cipher.decrypt(i)
        Tpwd_lst.append(i)
        
    pwd_dict={"admin_pwd":Tpwd_lst[0].decode('utf-8') ,"database_pwd":Tpwd_lst[1].decode('utf-8') ,"super_password":Tpwd_lst[2].decode('utf-8') }
    Tpwd_lst.clear()
    
#====================================================================================================================
def dbLogQry(qry):

    f=open("dbLog.txt",'a')
    f.write(qry)
    f.write("\n")
    f.close
    
#====================================================================================================================
def root():
    importPasswords()
    try:
        # Connecting MySQL Server to Python.
        global csr
        global db
        db=mysql.connector.connect(host="localhost",user="root",passwd=pwd_dict['database_pwd'],database='bankms')  # Database Object
        csr=db.cursor() # Cursor Object
        main()
        
    except:
        global root
        root = tk.Tk()  # Creating a window with vatiable name root
        root.geometry('500x500')    # setting size of window
        root.configure(bg='#fae1e1')
        root.title("NOT FOUND") #adding Title to a program
                
        label1=tk.Label(root,text="Database Error",font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
        label1.pack()

        button3 = tk.Button(root,text='okay',font=('Ariel',16),width='20',bg='white',command=closeWindow)
            
        button3.pack(pady=20)
#===================================================================================================================
def main():
    try:
        closeWindow()
    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("Bank") #adding Title to a program

    label1=tk.Label(root,text="Bank Management System",font=('Times New Roman',36),bg='#9b9c98') # defining Label
    button1 = tk.Button(root,text='Account Log-in',font=('Ariel',16),width='20',bg='#9ea9f7',command=accountLogin)
    button2 = tk.Button(root,text='Administrator',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminAuthentication)
    button3 = tk.Button(root,text='Exit',font=('Ariel',16),width='20',bg='red',command=root.destroy)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop() # Calling Window to pop-up
    
#===================================================================================================================

def accountLogin():
    
    def accountDisplay(acdet):
            
            def acCall():
                accountWindow(acdet)  

            closeWindow()
            global root    
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            root.title("Account Brief") #adding Title to a program

            table_lst=(("Account Number",str(acdet[0])),("Account Holder",str(acdet[1])),("Phone Number",str(acdet[2])),
                       ("A/C Balance",str(acdet[3])),("A/C Status",str(acdet[4])),)
            table=tabulate(table_lst,tablefmt="grid")

            label1=tk.Label(root,text=table,font=('Courier new',12),bg='#9b9c98')# defining Label
            button1 = tk.Button(root,text='Open Account',font=('Ariel',16),width='20',bg='white',command=acCall)
            button2 = tk.Button(root,text='Wrong Account',font=('Ariel',16),width='20',bg='white',command=main)
            
            label1.pack(padx=0,pady=0)
            button1.pack(pady=20)
            button2.pack(pady=20)
            
    def checkNopen():
        acno=tb1.get()  # Variable : Account Number
        acs=[]
        q1="select ac_no from account"
        csr.execute(q1)
        dbLogQry(q1)
        for i in csr:
            acs.append(i[0])   
        if 'BAC-'+acno in acs:
            acs.clear()
            q2="select * from account where ac_no=\"bac-"+acno+"\""
            csr.execute(q2)
            dbLogQry(q2)
            for i in csr:
                acdet=i  # Variable : Account Details
            accountDisplay(acdet)           
            
        else:
            
            errorWindow("Account Unable to find")
            
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT Log-in") #adding Title to a program
    label1=tk.Label(root,text="Account Log-in",font=('Times New Roman',36),bg='#9b9c98') # defining Label

    frame=tk.Frame(root)
    label2=tk.Label(frame,text="BAC-",font=('Times New Roman',24),bg='#9b9c98')    
    tb1=tk.Entry(frame,width='40',font=('Ariel',24))  
    button1 = tk.Button(root,text='Login',font=('Ariel',16),width='20',bg='#9ea9f7',command=checkNopen)
    button2 = tk.Button(root,text='back',font=('Ariel',16),width='20',bg='red',command=main)

    label1.pack(padx=20,pady=40)   #calling label Wihout padding
    frame.pack(side=tk.TOP)
    label2.grid(row=0,column=0)
    tb1.grid(row=0,column=1)
    button1.pack(pady=20)  
    button2.pack(pady=20)

    root.mainloop()
#====================================================================================================================   
def accountWindow(acdet):       

    def withdraw():
        acWithdraw(acdet)

    def deposit():
        acDeposit(acdet)
        
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT :"+acdet[0]) #adding Title to a program

    label1=tk.Label(root,text="ACCOUNT :"+acdet[0],font=('Times New Roman',36),bg='#9b9c98') # defining Label
    label1.pack(padx=20,pady=40)

    button1 = tk.Button(root,text='Withdraw',font=('Ariel',16),width='20',bg='#9ea9f7',command=withdraw)
    button2 = tk.Button(root,text='Deposit',font=('Ariel',16),width='20',bg='#9ea9f7',command=deposit)
    button3 = tk.Button(root,text='Check Balance',font=('Ariel',16),width='20',bg='#9ea9f7',)
    button4 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='red',command=main)

    button1.pack(pady=5)          
    button2.pack(pady=5)           
    button3.pack(pady=5)
    button4.pack(pady=5)

    root.mainloop()

#====================================================================================================================   
def acWithdraw(acdet):

    def proceedWithdraw():
        
        def dbOperations():
            mode=tbmode.get() # Variable : transaction Mode
            q0="select max(trans_id) from transaction"
            csr.execute(q0)
            dbLogQry(q0)
            for i in csr:
                atid=int(i[0])+1  # Variable : Allocated Transaction ID
            q1="insert into transaction values (\""+str(atid)+"\",curdate(),\""+acdet[0]+"\",\""+mode+"\","+amt+",\"d\")"
            q2="update account set ac_balance="+str(acdet[3]-int(amt))+" where ac_no=\""+acdet[0]+"\""
            csr.execute(q1)
            csr.execute(q2)
            dbLogQry(q1)
            dbLogQry(q2)
            db.commit()
            q1=q2=0

            q3="select * from transaction where trans_id=\""+str(atid)+"\""
            csr.execute(q3)
            dbLogQry(q3)
            for i in csr :
                trans_data=i # Variable : Transaction Data
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            root.title("Completion Window"+acdet[0]) #adding Title to a program
            
            label1=tk.Label(root,text="Withdraw Sucess Full"+acdet[0],font=('Times New Roman',16),bg='#9b9c98')
            table=tabulate((trans_data,),tablefmt="grid")
            label2=tk.Label(root,text=table,font=('courier new',16),bg='#9b9c98')
            button1 = tk.Button(root,text='okay',font=('Ariel',16),width='20',bg='#9ea9f7',command=backToACwindow)
            
            label1.pack(pady=5)
            label2.pack(pady=5)
            button1.pack(pady=5)
            
        amt=tbamt.get() # Variable : Amount
        if acdet[3]>int(amt):
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            root.title("ACCOUNT WITHDRAW :"+acdet[0]) #adding Title to a program
            
            label1=tk.Label(root,text="CONFIRMATION WINDOW :"+acdet[0],font=('Times New Roman',16),bg='#9b9c98')

            tbmode=tk.Entry(root,width='40',font=('Ariel',24))
            button1 = tk.Button(root,text='Confirm',font=('Ariel',16),width='20',bg='#9ea9f7',command=dbOperations)
            button2 = tk.Button(root,text='Terminate',font=('Ariel',16),width='20',bg='#9ea9f7',command=main)
            
            label1.pack(pady=5)
            tbmode.pack(pady=5)
            button1.pack(pady=5)
            button2.pack(pady=5)
            
        else:
            errorWindow("Insufficent Balance",3)

    def backToACwindow():
        accountWindow(acdet)
        
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT WITHDRAW :"+acdet[0]) #adding Title to a program

    label1=tk.Label(root,text="ACCOUNT WITHDRAW :"+acdet[0],font=('Times New Roman',36),bg='#9b9c98') # defining Label
    label1.pack(padx=20,pady=40)

    label2=tk.Label(root,text="Enter Amount:",font=('Ariel',16),bg='White')
    tbamt=tk.Entry(root,width='40',font=('Ariel',24))
    button1 = tk.Button(root,text='Withdraw',font=('Ariel',16),width='20',bg='#9ea9f7',command=proceedWithdraw)
    button2 = tk.Button(root,text='CANCEL',font=('Ariel',16),width='20',bg='#9ea9f7',command=backToACwindow)

    label2.pack(pady=0)
    tbamt.pack(pady=10)
    button1.pack(pady=5)          
    button2.pack(pady=5)           

    root.mainloop()
#====================================================================================================================   
def acDeposit(acdet):

    def proceedWithdraw():
        
        def dbOperations():
            mode=tbmode.get()
            q0="select max(trans_id) from transaction"
            csr.execute(q0)
            dbLogQry(q0)
            for i in csr:
                atid=int(i[0])+1 # Variable : Allocated Transaction ID
            q1="insert into transaction values (\""+str(atid)+"\",curdate(),\""+acdet[0]+"\",\""+mode+"\","+amt+",\"c\")"
            q2="update account set ac_balance="+str(acdet[3]+int(amt))+" where ac_no=\""+acdet[0]+"\""
            csr.execute(q1)
            csr.execute(q2)
            dbLogQry(q1)
            dbLogQry(q2)
            db.commit()
            q1=q2=0
            q3="select * from transaction where trans_id=\""+str(atid)+"\""
            csr.execute(q3)
            dbLogQry(q3)
            for i in csr :
                trans_data=i    # Variable : Transaction data
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            root.title("Completion Window"+acdet[0]) #adding Title to a program
            
            label1=tk.Label(root,text="Transaction Sucess Full"+acdet[0],font=('Times New Roman',16),bg='#9b9c98')
            table=tabulate((trans_data,),tablefmt="grid")
            label2=tk.Label(root,text=table,font=('courier new',16),bg='#9b9c98')
            button1 = tk.Button(root,text='okay',font=('Ariel',16),width='20',bg='#9ea9f7',command=backToACwindow)
            
            label1.pack(pady=5)
            label2.pack(pady=5)
            button1.pack(pady=5)
            
        amt=tbamt.get() # Variable : Amount
        closeWindow()
        global root
        root = tk.Tk()  # Creating a window with vatiable name root
        root.geometry('1000x600')    # setting size of window
        root.configure(bg='#9b9c98')
        root.title("ACCOUNT DEPOSIT :"+acdet[0]) #adding Title to a program
        
        label1=tk.Label(root,text="CONFIRMATION WINDOW :"+acdet[0],font=('Times New Roman',16),bg='#9b9c98')

        tbmode=tk.Entry(root,width='40',font=('Ariel',24))
        button1 = tk.Button(root,text='Confirm',font=('Ariel',16),width='20',bg='#9ea9f7',command=dbOperations)
        button2 = tk.Button(root,text='Terminate',font=('Ariel',16),width='20',bg='#9ea9f7',command=main)
        
        label1.pack(pady=5)
        tbmode.pack(pady=5)
        button1.pack(pady=5)
        button2.pack(pady=5)

    def backToACwindow():
        accountWindow(acdet)
        
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT DEPOSIT :"+acdet[0]) #adding Title to a program

    label1=tk.Label(root,text="ACCOUNT DEPOSIT :"+acdet[0],font=('Times New Roman',36),bg='#9b9c98') # defining Label
    label1.pack(padx=20,pady=40)

    label2=tk.Label(root,text="Enter Amount:",font=('Ariel',16),bg='White')
    tbamt=tk.Entry(root,width='40',font=('Ariel',24))
    button1 = tk.Button(root,text='Deposit',font=('Ariel',16),width='20',bg='#9ea9f7',command=proceedWithdraw)
    button2 = tk.Button(root,text='CANCEL',font=('Ariel',16),width='20',bg='#9ea9f7',command=backToACwindow)

    label2.pack(pady=0)
    tbamt.pack(pady=10)
    button1.pack(pady=5)          
    button2.pack(pady=5)           

    root.mainloop()    
#====================================================================================================================  
def adminAuthentication():
        
    def checkNopen():
        adpwd=tb1.get()
        if adpwd == pwd_dict['admin_pwd']:
            adminWindow()
        else:
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('500x500')    # setting size of window
            root.configure(bg='#fae1e1')
            root.title("Invalied Password") #adding Title to a program
            
            label1=tk.Label(root,text="Invalied Password",font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
            button3 = tk.Button(root,text='Try Again',font=('Ariel',16),width='20',bg='white',command=adminAuthentication)
            button4 = tk.Button(root,text='Okay',font=('Ariel',16),width='20',bg='white',command=main)
            
            label1.pack()
            button3.pack(pady=20)
            button4.pack(pady=20)
            

    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ADMINISTRATOR AUTHENTICATE") #adding Title to a program

    label1=tk.Label(root,text="ADMINISTRATOR AUTHENTICATION",font=('Times New Roman',36),bg='#9b9c98') # defining Label
    tb1= tk.Entry(root,width='40',font=('Ariel',24), show='*')
    button1 = tk.Button(root,text='Login',font=('Ariel',16),width='20',bg='#9ea9f7',command=checkNopen)
    button2 = tk.Button(root,text='Exit',font=('Ariel',16),width='20',bg='red',command=main)

    label1.pack(padx=20,pady=40)
    tb1.pack(padx=20,pady=20)
    button1.pack(pady=20)
    button2.pack(pady=20)

    root.mainloop()    
#====================================================================================================================
def adminWindow():
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ADMINISTRATOR") #adding Title to a program

    label1=tk.Label(root,text="ADMINISTRATOR",font=('Times New Roman',36),bg='#9b9c98') # defining Label
    button1 = tk.Button(root,text='Find Account',font=('Ariel',16),width='20',bg='#9ea9f7',command=admin_findAccount)
    button2 = tk.Button(root,text='Create Account',font=('Ariel',16),width='20',bg='#9ea9f7',command=admin_CreateAccount)
    button3 = tk.Button(root,text='Edit Account',font=('Ariel',16),width='20',bg='#9ea9f7',)
    button4 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='red',command=main)

    label1.pack(padx=20,pady=40)
    button1.pack(pady=5)          
    button2.pack(pady=5)           
    button3.pack(pady=5)
    button4.pack(pady=5)

    root.mainloop()
#====================================================================================================================
def admin_findAccount():
    
    def db_searchAcNo():
        acno=tb1.get()
        acs, acdet=[],[]
        q1="select ac_no from account"
        csr.execute(q1)
        dbLogQry(q1)
        for i in csr:
            acs.append(i[0])
        q2="select * from account where ac_no=\"bac-"+acno+"\""    
        csr.execute(q2)
        dbLogQry(q2)
        for i in csr:
            acdet=i
        closeWindow()
        global root
        root = tk.Tk()  # Creating a window with vatiable name root
        root.geometry('1000x600')    # setting size of window
        root.configure(bg='#9b9c98')
        root.title("ADMINISTRATOR : Find Account") #adding Title to a program

        table=tabulate((acdet,),headers=["Account Number","Account Holder","Phone Number","A/C Balance","A/C Status","A/C date"],tablefmt="grid")

        label1=tk.Label(root,text="Accounts Found :-",font=('Courier New',10),bg='#9b9c98')# defining Label
        label2=tk.Label(root,text=table,font=('Courier New',10),bg='#9b9c98')# defining Label
        button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)
        
        label1.pack(padx=20,pady=10)
        label2.pack(padx=20,pady=10)
        button1.pack(pady=5)

        root.mainloop()              
        
    def db_searchName():
        achn=(tb1.get()).lower()
        acs,acdet=[],[]
        q1="select ac_holder from account"
        csr.execute(q1)
        dbLogQry(q1)
        for i in csr:
            acs.append(i[0].lower())

        q2="select * from account where ac_holder like \"%"+achn+"%\""
        csr.execute(q2)
        dbLogQry(q2)
        for i in csr:
            acdet.append(i)
        closeWindow()
        global root
        root = tk.Tk()  # Creating a window with vatiable name root
        root.geometry('1000x600')    # setting size of window
        root.configure(bg='#9b9c98')
        root.title("ADMINISTRATOR : Find Account")#adding Title to a program
        
        table=tabulate(acdet,headers=["Account Number","Account Holder","Phone Number","A/C Balance","A/C Status","A/C date"],tablefmt="grid")

        label1=tk.Label(root,text="Accounts Found :-",font=('Courier New',10),bg='#9b9c98')# defining Label    
        label2=tk.Label(root,text=table,font=('Courier New',10),bg='#9b9c98')# defining Label
        button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)

        label1.pack(padx=0,pady=0)
        label2.pack(padx=0,pady=0)
        button1.pack(pady=5)

        root.mainloop()

    def db_searchPhNo():
        acpn=tb1.get()
        try:
            acpn=int(acpn)
        except:
            errorWindow('Invalid Mobile Number Format')   
        acs,acdet=[],[]
        q1="select ph_no from account"
        csr.execute(q1)
        dbLogQry(q1)
        for i in csr:
            acs.append(i[0])

        q2="select * from account where ph_no = "+str(acpn)
        csr.execute(q2)
        dbLogQry(q2)
        for i in csr:
            acdet.append(i)
        closeWindow()
        global root
        root = tk.Tk()  # Creating a window with vatiable name root
        root.geometry('1000x600')    # setting size of window
        root.configure(bg='#9b9c98')

        table=tabulate(acdet,headers=["Account Number","Account Holder","Phone Number","A/C Balance","A/C Status","A/C date"],tablefmt="grid")
        label1=tk.Label(root,text="Accounts Found :-",font=('Courier New',10),bg='#9b9c98')# defining Label    
        label2=tk.Label(root,text=table,font=('Courier New',10),bg='#9b9c98')# defining Label
        button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)

        label1.pack(padx=0,pady=0)
        label2.pack(padx=0,pady=0)
        button1.pack(pady=5)

        root.mainloop()
            

            
    closeWindow()        
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ADMINISTRATOR : Find Account") #adding Title to a program

    label1=tk.Label(root,text="Find Account",font=('Times New Roman',36),bg='#9b9c98') # defining Label
    tb1=tk.Entry(root,width='40',font=('Ariel',24))
    button1 = tk.Button(root,text='Find Account Number',font=('Ariel',16),width='20',bg='#9ea9f7',command=db_searchAcNo)
    button2 = tk.Button(root,text='Find Account Name',font=('Ariel',16),width='20',bg='#9ea9f7',command=db_searchName)
    button3 = tk.Button(root,text='Find Account Phone Number',font=('Ariel',16),width='30',bg='#9ea9f7',command=db_searchPhNo)
    
    label1.pack(padx=20,pady=40)
    tb1.pack(padx=20,pady=20)
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(padx=20,pady=5)
    
    root.mainloop()
#====================================================================================================================
    
def admin_CreateAccount():
    def createAC():
        name=tb1.get()
        phno=tb2.get()
        q1="select max(ac_no) from account"
        csr.execute(q1)
        dbLogQry(q1)
        for i in csr:
            nacno=i[0][4:]
            nacno=int(nacno)+1
            
        phnol=[]
        q2="select ph_no from account"
        csr.execute(q2)
        dbLogQry(q2)
        for i in csr:
            phnol.append(i[0])
            
        try:    
            if int(phno) in phnol:
                errorWindow("Phone Number Already Exist")
                
            elif len(phno)!=10:
                errorWindow("Invalied Phone Number")

            else:
                q='insert into account values(\"BAC-'+str(nacno)+"\",\""+name+"\","+phno+",0,\"O\",curdate())"
                csr.execute(q)
                dbLogQry(q)
                db.commit()
                closeWindow()        
                global root
                root = tk.Tk()  # Creating a window with vatiable name root
                root.geometry('1000x600')    # setting size of window
                root.configure(bg='#9b9c98')
                root.title("ADMINISTRATOR : Account Created") #adding Title to a program

                label1=tk.Label(root,text="Account Created",font=('Times New Roman',36),bg='#9b9c98') # defining Label
                label2=tk.Label(root,text="A/C No. BAC-:"+str(nacno),font=('Times New Roman',36),bg='#9b9c98') # defining Label
                button1 = tk.Button(root,text='Create Account',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)

                label1.pack(padx=20,pady=40)
                label2.pack(padx=20,pady=40)
                button1.pack(pady=5)

        except:
            errorWindow("Cannot add Account",2)

        
        
    closeWindow()        
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ADMINISTRATOR : Create Account") #adding Title to a program

    label0=tk.Label(root,text="Create Account",font=('Times New Roman',36),bg='#9b9c98') # defining Label

    frame=tk.Frame(root)
    label1=tk.Label(frame,text=" Account Holder Name  :",font=('Times New Roman',18),bg='#9b9c98')
    tb1=tk.Entry(frame,width='40',font=('Ariel',18))
    label2=tk.Label(frame,text=" Account Phone Number :",font=('Times New Roman',18),bg='#9b9c98')
    tb2=tk.Entry(frame,width='40',font=('Ariel',18))
    button1 = tk.Button(root,text='Create Account',font=('Ariel',16),width='20',bg='#9ea9f7',command=createAC)
    button2 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)
    
    label0.pack(padx=20,pady=40)

    frame.pack(side=tk.TOP)
    label1.grid(row=0,column=0)
    tb1.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    tb2.grid(row=1,column=1)
    button1.pack(pady=5)
    button2.pack(pady=5)
    
    root.mainloop()
    
#####################################################################################################################
        
root()

#####################################################################################################################

