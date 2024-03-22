from tkinter import *

def sucess():
    
    suc = Tk()
    suc.configure(bg="lightsteelblue")
    suc.geometry("320x240")
    suc.title("Sucess")
   
    Label(suc, text="Your sign up was sucessful\nThank you! ",bg="lightsteelblue",font=("catboo",10)).place(x=60,y=100)
    suc.mainloop()





