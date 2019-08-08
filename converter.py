from tkinter import *

def mcal():
	var2 = var1.get()
	var3 = var2 * 3.785
	e2.insert(0, var3)

a = Tk()
a.title("Converter")
var1 = IntVar()
n = "arial",14,"bold"
Label(a,text = "Gallons", padx = 25, font=(n)).grid(row=0,sticky=W)
e1 = Entry(a, width=25 , textvariable=var1)
e1.grid(row=0,column=1)
Label(a,text="Litres", padx=25, font=(n)).grid(row=1,sticky=W)
e2 = Entry(a, width=25)
e2.grid(row=1,column=1)
Button(a,text="calculate", font=(n), command = mcal).grid(row=2,column=1)

a.mainloop()