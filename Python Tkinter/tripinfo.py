import tkinter as tk


global sri
global ram
global sriram

def budget():
    global sriram
    if(ram=="1"):
        root9 = tk.Tk()
        root9.configure(bg="greenyellow")
        root9.geometry("500x250")
        root9.title("Budget")
        label1=tk.Label(root9,text="No of passenger : {}".format(sriram),font=("Broadway",20),bg="greenyellow").place(x=100,y=50)
        label2=tk.Label(root9,text="Estimated Budget : ₹{}".format(int(sriram)*1000,),bg="greenyellow",font=("Broadway",20)).place(x=100,y=100)

    else:
        root10 = tk.Tk()
        root10.configure(bg="greenyellow")
        root10.geometry("500x250")
        root10.title("Budget")
        label1=tk.Label(root10,text="No of passengers : {}".format(sriram),font=("Broadway",20),bg="greenyellow").place(x=100,y=50)
        label2=tk.Label(root10,text="Estimated Budget : ₹{}".format(int(sriram)*2000),font=("Broadway",20),bg="greenyellow").place(x=100,y=100)

def plans1():
    global sri
    global ram
    global sriram
    f=open("user_data.txt","r")
    f.read()
    if(sri=="kodaikannal" and ram=='1'):
        root5=tk.Tk()
        root5.configure(bg="whitesmoke")
        root5.title("plan page")
        root5.geometry("500x500")
        tk.Label(root5, text="YOUR BEST PLAN",bg="whitesmoke",font=("arial",15)).place(x=0,y=5)
        tk.Label(root5, text="Day:1",bg="whitesmoke",font="arial").place(x=10,y=30)
        tk.Label(root5, text="1.Kodai lake \n 2.Cycling \n 3.Boating \n 4.Green valley view",bg="whitesmoke").place(x=20,y=50)
        tk.Button(root5,text="Calculate Budget",bg="limegreen",fg="white",font=("a Abrasion",15),command=budget).place(x=220,y=250)
        
    elif(sri=="kodaikannal" and ram=='2'):
        root6=tk.Tk()
        root6.configure(bg="whitesmoke")
        root6.title("plan page")
        root6.geometry("500x500")
        tk.Label(root6, text="YOUR BEST PLAN",bg="whitesmoke",font=("arial",15)).place(x=0,y=5)
        tk.Label(root6, text="Day:1",bg="whitesmoke",font="arial").place(x=10,y=30)
        tk.Label(root6, text="1.Kodai lake \n 2.Cycling \n 3.Boating \n 4.Green valley view",bg="whitesmoke").place(x=20,y=50)
        tk.Label(root6, text="Day 2 :",bg="whitesmoke",font="arial").place(x=10,y=150)
        tk.Label(root6, text="1.Coaker’s walk \n 2.500 year Tree \n 3.Pillar Rocks \n 4.Guna Cave",bg="whitesmoke").place(x=20,y=170)
        tk.Button(root6,text="Calculate Budget",bg="limegreen",fg="white",font=("a Abrasion",15),command=budget).place(x=220,y=250)
        
    elif(sri=="chennai" and ram=='1'):
        root7=tk.Tk()
        root7.configure(bg="whitesmoke")
        root7.title("plan page")
        root7.geometry("500x500")
        tk.Label(root7, text="YOUR BEST PLAN",bg="whitesmoke",font=("arial",15)).place(x=0,y=5)
        tk.Label(root7, text="Day:1",bg="whitesmoke",font="arial").place(x=10,y=30)
        tk.Label(root7, text="1.Government museum \n 2.National arts gallery \n 3.Marina beach \n 4.MGR Memorial",bg="whitesmoke").place(x=20,y=50)
        tk.Button(root7,text="Calculate Budget",bg="limegreen",fg="white",font=("a Abrasion",15),command=budget).place(x=220,y=190)
        
    elif(sri=="chennai" and ram=='2'):
        root8=tk.Tk()
        root8.configure(bg="whitesmoke")
        root8.title("plan page")
        root8.geometry("500x500")
        tk.Label(root8, text="YOUR BEST PLAN",bg="whitesmoke",font=("arial",15)).place(x=0,y=5)
        tk.Label(root8, text="Day:1",bg="whitesmoke",font="arial").place(x=10,y=30)
        tk.Label(root8, text="1.Government museum \n 2.National arts gallery \n 3.Marina beach \n 4.MGR Memorial",bg="whitesmoke").place(x=20,y=50)
        tk.Label(root8, text="Day 2 :",bg="whitesmoke",font="arial").place(x=10,y=150)
        tk.Label(root8, text="1.Kapaliswarar temple \n 2.Birla planaerium \n 3.Snake park \n 4.Elliot park",bg="whitesmoke").place(x=20,y=170)
        tk.Button(root8,text="Calculate Budget",bg="limegreen",fg="white",font=("a Abrasion",15),command=budget).place(x=220,y=250)

def saveinfo():
    global ram
    global e1
    global e2
    global e3
    global sriram
    global sri
    sri=str(e1.get())
    ram=str(e2.get())
    sriram=str(e3.get())
    with open("user_data.txt", "w") as file:
        file.write(f"Location: {sri}\n")
        file.write(f"Days: {ram}\n")
        file.write(f"Passengers: {sriram}\n")
    
    plans1()

def tripinfo():
    
    root3 = tk.Tk()
    root3.configure(bg="floralwhite")
    root3.geometry("700x500")
    root3.title("Trip Information")
    
    l1 = tk.Label(root3, text="Enter Information",bg="floralwhite",fg="coral",font=("Peanut Butter",40))
    l1.pack()
    
    global e1
    l2 = tk.Label(root3, text="Location :",bg="floralwhite",fg="#A673BD",font=("kathak",20))
    l2.pack()
    e1 = tk.Entry(root3, text="Location :",bg="linen",font=("Peanut Butter",25))
    e1.pack()
    
    global e2
    l3 = tk.Label(root3, text="Days :",bg="floralwhite",fg="#A673BD",font=("kathak",20))
    l3.pack()
    e2 = tk.Entry(root3, text="Days :",bg="linen",font=("Peanut Butter",25))
    e2.pack()

    global e3
    l4 = tk.Label(root3, text="Number of Persons :",bg="floralwhite",fg="#A673BD",font=("kathak",20))
    l4.pack()
    e3 = tk.Entry(root3, text="Number of Persons :",bg="linen",font=("Peanut Butter",25))
    e3.pack()
   
    b1 = tk.Button(root3, text=" Submit ",bg="limegreen",fg="white",font=("a Abrasion",15),command=saveinfo)
    b1.pack()
    
    root3.mainloop()


    


