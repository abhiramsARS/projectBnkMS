import tkinter as tk    #importing module

#====================================================================================================================
def closeWindow():
    root.destroy()

#====================================================================================================================    
def accountLogin():
    
    def checkNopen():
        acno=tb1.get()
        if acno == '12345':
            accountWindow(acno)
        else:
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1400x500')    # setting size of window
            root.configure(bg='#fae1e1')
            root.title("NOT FOUND") #adding Title to a program
            
            label1=tk.Label(root,text="Account Unable to find",font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
            label1.pack()

            button3 = tk.Button(root,text='Okay',font=('Ariel',16),width='20',bg='White',command=main)
            button3.pack(pady=20)

        
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1400x500')    # setting size of window
    root.configure(bg='#b3fff5')
    root.title("ACCOUNT Log-in") #adding Title to a program
    label1=tk.Label(root,text="Account Log-in",font=('Times New Roman',36),bg='#b3fff5') # defining Label
    label1.pack(padx=20,pady=40)   #calling label Wihout padding

    tb1=tk.Entry(root,width='40',font=('Ariel',24))
    tb1.pack(padx=20)
       
    button1 = tk.Button(root,text='Login',font=('Ariel',16),width='20',bg='White',command=checkNopen)
    button1.pack(pady=20)

    button2 = tk.Button(root,text='back',font=('Ariel',16),width='20',bg='red',command=main)
    button2.pack(pady=20)

    root.mainloop()
#--------------------------------------------------------------------------------------------------------------------    
def accountWindow(acno):
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1400x500')    # setting size of window
    root.configure(bg='#b3fff5')
    root.title("ACCOUNT :"+acno) #adding Title to a program

    label1=tk.Label(root,text="ACCOUNT :"+acno,font=('Times New Roman',36),bg='#b3fff5') # defining Label
    label1.pack(padx=20,pady=40)

    button1 = tk.Button(root,text='Withdraw',font=('Ariel',16),width='20',bg='White',)
    button2 = tk.Button(root,text='Deposit',font=('Ariel',16),width='20',bg='White',)
    button3 = tk.Button(root,text='Check Balance',font=('Ariel',16),width='20',bg='White',)
    button4 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='red',command=main)

    button1.pack(pady=5)          
    button2.pack(pady=5)           
    button3.pack(pady=5)
    button4.pack(pady=5)

    root.mainloop()
    
#====================================================================================================================  
def adminWindow():
    closeWindow()
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1400x500')    # setting size of window
    root.configure(bg='#b3fff5')
    root.title("ADMINISTRATOR") #adding Title to a program

    label1=tk.Label(root,text="ADMINISTRATOR",font=('Times New Roman',36),bg='#b3fff5') # defining Label
    label1.pack(padx=20,pady=40)

    button1 = tk.Button(root,text='Find Account',font=('Ariel',16),width='20',bg='White')
    button2 = tk.Button(root,text='View Account Holder',font=('Ariel',16),width='20',bg='White')
    button3 = tk.Button(root,text='Edit Account',font=('Ariel',16),width='20',bg='White',)
    button4 = tk.Button(root,text='Back',font=('Ariel',16),width='20',bg='red',command=main)

    button1.pack(pady=5)          
    button2.pack(pady=5)           
    button3.pack(pady=5)
    button4.pack(pady=5)

    root.mainloop()
#--------------------------------------------------------------------------------------------------------------------  
def adminAuthentication():
    
    closeWindow()
    
    def checkNopen():
        acno=tb1.get()
        if acno == 'administrator':
            adminWindow()
        else:
            closeWindow()
            global root
            root = tk.Tk()  # Creating a window with vatiable name root
            root.geometry('1400x500')    # setting size of window
            root.configure(bg='#fae1e1')
            root.title("Invalied Password") #adding Title to a program
            
            label1=tk.Label(root,text="Invalied Password",font=('Times New Roman',36),fg='red',bg='#fae1e1') # defining Label
            label1.pack()

            button3 = tk.Button(root,text='Okay',font=('Ariel',16),width='20',bg='White',command=main)
            button3.pack(pady=20)

    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1400x500')    # setting size of window
    root.configure(bg='#b3fff5')
    root.title("ADMINISTRATOR AUTHENTICATE") #adding Title to a program

    label1=tk.Label(root,text="ADMINISTRATOR AUTHENTICATION",font=('Times New Roman',36),bg='#b3fff5') # defining Label
    label1.pack(padx=20,pady=40)
    
    tb1= tk.Entry(root,width='40',font=('Ariel',24), show='*')
    tb1.pack(padx=20,pady=20)
    
    button1 = tk.Button(root,text='Login',font=('Ariel',16),width='20',bg='White',command=checkNopen)
    button2 = tk.Button(root,text='Exit',font=('Ariel',16),width='20',bg='red',command=main)
    
    button1.pack(pady=20)
    button2.pack(pady=20)

    root.mainloop()
#====================================================================================================================
def main():
    try:
        closeWindow()

    except:
        pass
    
    global root
    root = tk.Tk()  # Creating a window with vatiable name root
    root.geometry('1400x500')    # setting size of window
    root.configure(bg='#b3fff5')
    root.title("Bank") #adding Title to a program

    label1=tk.Label(root,text="Bank Management System",font=('Times New Roman',36),bg='#b3fff5') # defining Label
    label1.pack(padx=20,pady=40)   #calling label Wihout padding

    button1 = tk.Button(root,text='Account Log-in',font=('Ariel',16),width='20',bg='White',command=accountLogin)
    button2 = tk.Button(root,text='Administrator',font=('Ariel',16),width='20',bg='White',command=adminAuthentication)
    button3 = tk.Button(root,text='Exit',font=('Ariel',16),width='20',bg='red',command=root.destroy)
    
    button1.pack(pady=20)          
    button2.pack(pady=20)           
    button3.pack(pady=20)

    root.mainloop() # Calling Window to pop-up
    
#===================================================================================================================

main()

