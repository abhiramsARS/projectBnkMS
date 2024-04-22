# Project-BnkMS

#####################################################################################################################
import tkinter as tk    #importing module
import mysql.connector

#####################################################################################################################


def closeWindow():
    root.destroy()
#====================================================================================================================
def errorWindow(typ):
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('500x500')    # setting size of window
    root.configure(bg='#fae1e1')
    root.title("NOT FOUND") #adding Title to a program
            
    label1=tk.Label(root,text=typ,font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
    button3 = tk.Button(root,text='okay',font=('Ariel',16),width='20',bg='white',command=main)
    
    label1.pack()    
    button3.pack(pady=20)
    
#====================================================================================================================
def root():
    try:
        global csr
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="arsmysql",database='bankms')
        csr=mydb.cursor()
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

            label1=tk.Label(root,text="Account Number -"+str(acdet[0]),font=('Ariel',18),bg='#9b9c98')# defining Label
            label2=tk.Label(root,text="Account Holder -"+str(acdet[1]),font=('Ariel',18),bg='#9b9c98')
            label3=tk.Label(root,text="Phone Number   -"+str(acdet[2]),font=('Ariel',18),bg='#9b9c98')
            label4=tk.Label(root,text="A/C Balance    -"+str(acdet[3]),font=('Ariel',18),bg='#9b9c98')
            label5=tk.Label(root,text="A/C Status     -"+str(acdet[4]),font=('Ariel',18),bg='#9b9c98')
            button1 = tk.Button(root,text='Open Account',font=('Ariel',16),width='20',bg='white',command=acCall)
            button2 = tk.Button(root,text='Wrong Account',font=('Ariel',16),width='20',bg='white',command=main)
            
            label1.pack(padx=0,pady=0)
            label2.pack(padx=0,pady=0)
            label3.pack(padx=0,pady=0)
            label4.pack(padx=0,pady=0)
            label5.pack(padx=0,pady=0)
            button1.pack(pady=20)
            button2.pack(pady=20)
            
    def checkNopen():
        acno=tb1.get()
        acs=[]
        csr.execute("select ac_no from account")
        for i in csr:
            acs.append(i[0])   
        if 'BAC-'+acno in acs:
            csr.execute("select * from account where ac_no=\"bac-"+acno+"\"")
            for i in csr:
                acdet=i
            accountDisplay(acdet)           
            
        else:
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('500x500')    # setting size of window
            root.configure(bg='#fae1e1')
            root.title("NOT FOUND") #adding Title to a program
            
            label1=tk.Label(root,text="Account Unable to find",font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
            button3 = tk.Button(root,text='Try Again',font=('Ariel',16),width='20',bg='white',command=accountLogin)
            button4 = tk.Button(root,text='Okay',font=('Ariel',16),width='20',bg='white',command=main)
                      
            label1.pack()
            button3.pack(pady=20)
            button4.pack(pady=20)
            
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT Log-in") #adding Title to a program
    label1=tk.Label(root,text="Account Log-in",font=('Times New Roman',36),bg='#9b9c98') # defining Label
    label1.pack(padx=20,pady=40)   #calling label Wihout padding

    tb1=tk.Entry(root,width='40',font=('Ariel',24))  
    button1 = tk.Button(root,text='Login',font=('Ariel',16),width='20',bg='#9ea9f7',command=checkNopen)
    button2 = tk.Button(root,text='back',font=('Ariel',16),width='20',bg='red',command=main)

    tb1.pack(padx=20)
    button1.pack(pady=20)  
    button2.pack(pady=20)

    root.mainloop()
#====================================================================================================================   
def accountWindow(acdet):       
    
    closeWindow()
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1000x600')    # setting size of window
    root.configure(bg='#9b9c98')
    root.title("ACCOUNT :"+acdet[0]) #adding Title to a program

    label1=tk.Label(root,text="ACCOUNT :"+acdet[0],font=('Times New Roman',36),bg='#9b9c98') # defining Label
    label1.pack(padx=20,pady=40)

    button1 = tk.Button(root,text='Withdraw',font=('Ariel',16),width='20',bg='#9ea9f7',)
    button2 = tk.Button(root,text='Deposit',font=('Ariel',16),width='20',bg='#9ea9f7',)
    button3 = tk.Button(root,text='Check Balance',font=('Ariel',16),width='20',bg='#9ea9f7',)
    button4 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='red',command=main)

    button1.pack(pady=5)          
    button2.pack(pady=5)           
    button3.pack(pady=5)
    button4.pack(pady=5)

    root.mainloop()
#====================================================================================================================  
def adminAuthentication():
        
    def checkNopen():
        adpwd='administrator' #tb1.get()
        if adpwd == 'administrator':
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
    button2 = tk.Button(root,text='View Account Holder',font=('Ariel',16),width='20',bg='#9ea9f7')
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
        acs=[]
        csr.execute("select ac_no from account")
        for i in csr:
            acs.append(i[0])
        if 'BAC-'+acno in acs:
            csr.execute("select * from account where ac_no=\"bac-"+acno+"\"")
            for i in csr:
                acdet=i
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            root.title("ADMINISTRATOR : Find Account") #adding Title to a program
            label1=tk.Label(root,text="Account Number -"+str(acdet[0]),font=('Ariel',18),bg='#9b9c98')# defining Label
            label2=tk.Label(root,text="Account Holder -"+str(acdet[1]),font=('Ariel',18),bg='#9b9c98')
            label3=tk.Label(root,text="Phone Number   -"+str(acdet[2]),font=('Ariel',18),bg='#9b9c98')
            label4=tk.Label(root,text="A/C Balance    -"+str(acdet[3]),font=('Ariel',18),bg='#9b9c98')
            label5=tk.Label(root,text="A/C Status     -"+str(acdet[4]),font=('Ariel',18),bg='#9b9c98')
            label6=tk.Label(root,text="A/C date       -"+str(acdet[5]),font=('Ariel',18),bg='#9b9c98')
            button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)
            
            label1.pack(padx=20,pady=10)
            label2.pack(padx=20,pady=10)
            label3.pack(padx=20,pady=10)
            label4.pack(padx=20,pady=10)
            label5.pack(padx=20,pady=10)
            label6.pack(padx=20,pady=10)
            button1.pack(pady=5)

            root.mainloop()

        else:
            errorWindow('Account Number Not Found') 
            

            
        
    def db_searchName():
        achn=tb1.get()
        acs,acdet=[],[]
        csr.execute("select ac_holder from account")
        for i in csr:
            acs.append(i[0].lower())
        if achn.lower() in acs:
            csr.execute("select ac_no from account where ac_holder like \"%"+achn+"%\"")
            for i in csr:
                acdet.append(i[0])
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            
            for j in acdet:
                root.title("ADMINISTRATOR : Find Account") #adding Title to a program
                label1=tk.Label(root,text="Account Number -"+str(j),font=('Ariel',18),bg='#9b9c98')# defining Label
                label7=tk.Label(root,text="="*25,font=('Ariel',18),bg='#9b9c98')

                label1.pack(padx=0,pady=0)
                label7.pack(padx=0,pady=0)

            button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)
            button1.pack(pady=5)

            root.mainloop()
            
        else:
            errorWindow('Account Name Not Found')
            
    def db_searchPhNo():
        acpn=tb1.get()
        try:
            acpn=int(acpn)
        except:
            errorWindow('Invalid Mobile Number Format')
        print(acpn)    
        acs,acdet=[],[]
        csr.execute("select ph_no from account")
        for i in csr:
            acs.append(i[0])
        if acpn in acs:
            csr.execute("select ac_no from account where ph_no = "+str(acpn))
            for i in csr:
                acdet.append(i[0])
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1000x600')    # setting size of window
            root.configure(bg='#9b9c98')
            
            for j in acdet:
                root.title("ADMINISTRATOR : Find Account") #adding Title to a program
                label1=tk.Label(root,text="Account Number -"+str(j),font=('Ariel',18),bg='#9b9c98')# defining Label
                label7=tk.Label(root,text="="*25,font=('Ariel',18),bg='#9b9c98')

                label1.pack(padx=0,pady=0)
                label7.pack(padx=0,pady=0)

            button1 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='#9ea9f7',command=adminWindow)
            button1.pack(pady=5)

            root.mainloop()
            
        else:
            errorWindow('Phone Number Not Found')
            
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
    button3 = tk.Button(root,text='Find Account Phone Number',font=('Ariel',16),width='20',bg='#9ea9f7',command=db_searchPhNo)
    
    label1.pack(padx=20,pady=40)
    tb1.pack(padx=20,pady=20)
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(padx=20,pady=5)
    
    root.mainloop()
#####################################################################################################################
        
root()

#####################################################################################################################

