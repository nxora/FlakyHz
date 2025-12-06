from tkinter import *
from tkinter import ttk

wn = Tk()
wn.geometry("700x360")
frame=Frame(wn)
frame.place(x=50,y=10)

l =LabelFrame(frame,text="Registration Form",bg="grey")
l.grid(row=0,column=0)

i=Label(l,text="First Name",font=("Arial",10,'bold'),bg="grey")
i.grid(row=0,column=0)
Entry(l,font=("arial",12)).grid(row=1,column=0,padx=10)

ii=Label(l,text="Last Name",font=("Arial",10,'bold'),bg="grey")
ii.grid(row=0,column=1)
Entry(l,font=("arial",12)).grid(row=1,column=1,padx=10)

Label(l,text="Middle Name",font=("Arial",10,'bold'),bg="grey").grid(row=0,column=2)
Entry(l,font=("arial",12)).grid(row=1,column=2,padx=10)

Label(l,text="Age",font=("Arial",10,'bold'),bg="grey").grid(row=2,column=0)
s=Spinbox(l,from_=0,to=100,font=("arial",10))
s.grid(row=3,column=0)

y=Label(l,text="Year",font=("Arial",10,'bold'),bg="grey")
y.grid(row=2,column=1)
c2=ttk.Combobox(l,values=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026'],font=("arial",10))
c2.grid(row=3,column=1,pady=10, padx=10)
c2.current(9)


Label(l,text="Month",font=("Arial",10,'bold'),bg="grey").grid(row=2,column=2)
c=ttk.Combobox(l,font=("arial",10),values=['January','February','March','April','May','June','July','August','September','October','November','December'])
c.grid(row=3,column=2,padx=10)
c.current(0)

label1= LabelFrame(frame,bg="grey",text="Security info")
label1.grid(row=1,column=0,pady=10)
iv= Label(label1,text="Enter Password",bg="grey",font=("Arial",10,'bold'))
iv.grid(row=0,column=0,padx=10,)
e= Entry(label1,font=("arial",12),show="*")
e.grid(row=1,column=0,padx=10)
v= Label(label1,text="Confirm Password",bg="grey",font=("Arial",10,'bold'))
v.grid(row=0,column=1)
e2= Entry(label1,font=("arial",12),show="*")
e2.grid(row=1,column=1,pady=10,padx=65)
vi= Label(label1,text="Enter Email",bg="grey",font=("Arial",10,'bold'))
vi.grid(row=2,column=0)
e3= Entry(label1,font=("arial",12),width=30)
e3.grid(row=3,column=0,pady=10,padx=10)
label2 = LabelFrame(frame)
label2.grid(row=2,column=0,pady=10)
check=Button(label2,text="Submit",width=75,bg="grey",font=("arial",10,'bold'))
check.grid(row=0,column=0)

wn.mainloop()