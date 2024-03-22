from tkinter import *
from sucess import*

def signup():
    global root2
    root2 = Tk()
    root2.configure(bg="lavender")
    root2.geometry("700x600")
    root2.title("Sign up")
    
    Label(root2, text="Signup Here",bg="lavender",fg="coral",font=("Peanut Butter",40)).place(x=280,y=20)
    
    Label(root2, text="First Name :",bg="lavender",fg="deeppink",font=("kathak",20)).place(x=120,y=100)
    Entry(root2, text="First name :",bg="linen",font=("Peanut Butter",25)).place(x=310,y=100)

    Label(root2, text="Last Name :",bg="lavender",fg="deeppink",font=("kathak",20)).place(x=120,y=200)
    Entry(root2, text="Last name :",bg="linen",font=("Peanut Butter",25)).place(x=310,y=200)

    Label(root2, text="Create Password :",bg="lavender",fg="deeppink",font=("kathak",20)).place(x=80,y=300)
    Entry(root2, text="Create Password :",bg="linen",show="*",font=("Peanut Butter",25)).place(x=310,y=300)

    Label(root2, text="Confirm Password :",bg="lavender",fg="deeppink",font=("kathak",20)).place(x=70,y=400)
    Entry(root2, text="Confirm Password :",bg="linen",show="*",font=("Peanut Butter",25)).place(x=310,y=400)

    Button(root2, text=" Submit ",bg="limegreen",fg="white",font=("a Abrasion",15),padx=10, pady=5,command=lambda:[root2.withdraw(),sucess()]).place(x=360,y=500)
    root2.mainloop()



