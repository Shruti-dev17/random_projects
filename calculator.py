
import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk

def click(num):
    result = text.get()
    text.delete(0,'end')
    text.insert(0,str(result)+str(num))

def add():
   n1= text.get()
   global math 
   math= "addition"
   global i
   i= int(n1)
   text.delete(0,'end')
    
def minus():
   n1= text.get()
   global math 
   math= "substraction"
   global i
   i= int(n1)
   text.delete(0,"end")
    
def multiply():
      n1= text.get()
      global math 
      math= "multiplication"
      global i
      i= int(n1)
      text.delete(0,"end")

def divide():
      n1= text.get()
      global math 
      math= "division"
      global i
      i= int(n1)
      text.delete(0,"end")

def equal():
    n2 = text.get()
    text.delete(0,"end")
    if math == "addition":
        text.insert(0, i + int(n2))
    elif math == "substraction":
        text.insert(0,i - int(n2))
    elif math == "multiplication":
            text.insert(0,i * int(n2))
    elif math == "division":
            text.insert(0,i / int(n2))

def clear():
     text.delete(0,'end')

# GUI

root=tk.Tk()
root.geometry("500x550")
root.title("CALCULATOR")
root.configure(bg="#a41ec2")
cus_font_label=tfont.Font(family="Courier",size=25,weight="bold",slant="italic")
cus_font_entry=tfont.Font(family="Courier",size=20,weight="bold",slant="italic")
heading=tk.Label(text="Calculator",font=cus_font_label,bg="#a41ec2",fg="#c9a6f7")
heading.pack()
text= tk.Entry(width=70,borderwidth=5,font=cus_font_entry,bg="#D153FF")
text.pack(ipady=20,padx=10)
text.focus()

b1=tk.Button(text="1",height=4, width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(1))
b1.place(x=10,y=140)

b2=tk.Button(text="2",height=4, width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(2))
b2.place(x=10,y=240)

b3=tk.Button(text="3",height=4, width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(3))
b3.place(x=10,y=340)

b4=tk.Button(text="4", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(4))
b4.place(x=150,y=140)

b5=tk.Button(text="5", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(5))
b5.place(x=150,y=240)

b6=tk.Button(text="6", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(6))
b6.place(x=150,y=340)

b7=tk.Button(text="7", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(7))
b7.place(x=290,y=140)

b8=tk.Button(text="8", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(8))
b8.place(x=290,y=240)

b9=tk.Button(text="9", height=4,width= 12,font=("Times new roman",10,"bold"),bg="#D576F8",command=lambda:click(9))
b9.place(x=290,y=340)

b0=tk.Button(text="0", height=4,width= 12,font=("Times new roman",10,"bold"),bg="plum",command=lambda:click(0))
b0.place(x=10,y=440)

b_remove=tk.Button(text="clear", height=4,font=("Times new roman",10,"bold"),bg="plum",width= 12,command=clear)
b_remove.place(x=150,y=440)

b_equal=tk.Button(text="=",height=4,font=("Times new roman",10,"bold"),bg="plum", width= 12,command=equal)
b_equal.place(x=290,y=440)

b_add=tk.Button(text="+",height=4,font=("Times new roman",10,"bold"),bg="plum", width= 10,command=add)
b_add.place(x=410,y=140)

b_minus=tk.Button(text="-", height=4,font=("Times new roman",10,"bold"),bg="plum",width= 10,command=minus)
b_minus.place(x=410,y=240)

b_multiply=tk.Button(text="*",height=4,font=("Times new roman",10,"bold"),bg="plum", width= 10,command=multiply)
b_multiply.place(x=410,y=340)

b_divide=tk.Button(text="/", height=4,font=("Times new roman",10,"bold"),bg="plum",width= 10,command=divide)
b_divide.place(x=410,y=440)

root.mainloop()



