from tkinter import *

def mcal():
	var2 = var1.get()
	var3 = var2 * 3.785
	e2.insert(0, var3)

a = Tk()
a.minsize(500,500)
a.title("Converter")
var1 = IntVar()
n = "arial",14,"bold"
Label(a,text = "Gallons", padx = 25, font=(n),fg='black', bg='SeaGreen1',  pady=10).place(x=100,y=125)
e1 = Entry(a, width=25 , textvariable=var1)
e1.place(x=250,y=125)
Label(a,text="Litres", padx=25, font=(n),fg='black', bg='SeaGreen1', pady=10).place(x=100,y=275)
e2 = Entry(a, width=25)
e2.place(x=250,y=275)
Button(a,text="calculate", font=(n), command = mcal, bg='SeaGreen1', padx=10, pady=10).pack(side=BOTTOM, pady=50)

a.mainloop()