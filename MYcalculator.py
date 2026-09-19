#functions for calculator
# numbers
def click(num):
    result = text.get()
    text.delete(0,'end')
    text.insert(0,str(result)+str(num))

# operators
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

# Equal
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

# clear

def clear():
     text.delete(0,'end')

# GUI for calculator
import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk 

#window creation
root=tk.Tk()
root.geometry("500x500")
root.title("CALCULATOR")

text= tk.Entry(width=70,borderwidth=5,) # for creating text box
text.place(x=0,y=0)


# Buttons from 1-0
b1=tk.Button(text="1", width= 12,command=lambda:click(1))
b1.place(x=0,y=80)

b2=tk.Button(text="2",width= 12,command=lambda:click(2))
b2.place(x=0,y=180)

b3=tk.Button(text="3",width= 12,command=lambda:click(3))
b3.place(x=0,y=280)

b4=tk.Button(text="4",width= 12,command=lambda:click(4))
b4.place(x=100,y=80)

b5=tk.Button(text="5",width= 12,command=lambda:click(5))
b5.place(x=100,y=180)

b6=tk.Button(text="6",width= 12,command=lambda:click(6))
b6.place(x=100,y=280)

b7=tk.Button(text="7",width= 12,command=lambda:click(7))
b7.place(x=200,y=80)

b8=tk.Button(text="8",width= 12,command=lambda:click(8))
b8.place(x=200,y=180)

b9=tk.Button(text="9",width= 12,command=lambda:click(9))
b9.place(x=200,y=280)

b0=tk.Button(text="0",width= 12,command=lambda:click(0))
b0.place(x=0,y=380)

#clear and equal button
b_remove=tk.Button(text="clear",width= 12,command=clear)
b_remove.place(x=100,y=380)

b_equal=tk.Button(text="=", width= 12,command=equal)
b_equal.place(x=200,y=380)

# operator buttons
b_add=tk.Button(text="+", width= 10,command=add)
b_add.place(x=300,y=80)

b_minus=tk.Button(text="-",width= 10,command=minus)
b_minus.place(x=300,y=180)

b_multiply=tk.Button(text="*", width= 10,command=multiply)
b_multiply.place(x=300,y=280)

b_divide=tk.Button(text="/",width= 10,command=divide)
b_divide.place(x=300,y=380)


root.mainloop()



