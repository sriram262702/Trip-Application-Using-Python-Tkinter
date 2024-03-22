from tkinter import *
from tripinfo import *
from signup import *
from sucess import *


root = Tk()
root.title("Login")
root.configure(bg="whitesmoke")
root.geometry("600x500")
e1 =StringVar()
e2= StringVar()

def login():

    photo=PhotoImage(file="s.png")
    resized_image = photo.subsample(2)
    image_label = Label(image=resized_image)
    image_label.pack()

    Label(root, text="TRIP POLAMAA",bg="whitesmoke",fg="limegreen",font=("vacaciones",40)).place(x=120,y=140)
        
    Label(root, text="User name :",bg="whitesmoke",fg="tomato",font=("Peanut Butter",25)).place(x=50,y=220)
    Entry(root, text="User name :",bg="linen",font=("Peanut Butter",25)).place(x=210,y=220)

    Label(root, text="Password :",bg="whitesmoke",fg="tomato",font=("Peanut Butter",25)).place(x=50,y=280)
    Entry(root, text="Password :",bg="linen",show="*",font=("Peanut Butter",25)).place(x=210,y=280)

    Button(root, text=" Submit ",bg="limegreen",fg="white",font=("a Abrasion",15),padx=10, pady=5,command=lambda:[root.withdraw(),tripinfo()]).place(x=160,y=340)
    Button(root, text=" Signup ",bg="orange",fg="white",font=("a Abrasion",15),padx=10, pady=5,command=lambda:[root.withdraw(),signup()]).place(x=310,y=340)
    root.mainloop()

login()
