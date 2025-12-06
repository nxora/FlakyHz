from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox

wn= Tk()
wn.geometry("590x520")
wn.resizable(False,True)
wn.title("My Savings App")
frame = Frame(wn)
frame.grid(row=0,column=0,padx=10,pady=10)

def add(event=None):
    if name.get() and amount.get() and id.get():
        table.insert('','end',values=[id.get(),name.get().title(),amount.get(),age.get()+"yrs",month.get().title(),year.get()])
    else:
        messagebox.showinfo("Error","Please fill in the empty spaces")

def delete(event=None):
    if table.selection():
        table.delete(table.selection())
    else:
        messagebox.showerror("Error","Please Selection a name to delete")

def clear():
    if name.get() and amount.get() and id.get():
        if messagebox.askyesno:
            table.delete('1.0',END)
    else:
        messagebox.showerror("Error","No table to clear")

lf =LabelFrame(frame,text="Profile info",bg="grey")
lf.grid(row=0,column=0)
n = Label(lf,text="Name",bg="grey",font=("arial",12,"bold"))
n.grid(row=0,column=0)
name = Entry(lf,font=("arial",12))
name.grid(row=1,column=0,padx=10)
a= Label(lf,text='Amount',font=("arial",12,"bold"),bg='grey')
a.grid(row=0,column=1)
amount = Entry(lf,font=("arial",12))
amount.grid(row=1,column=1,pady=10)
amount.insert(0,"N")
i = Label(lf,text='ID',font=( "arial",12,"bold"),bg='grey')
i.grid(row=0,column=2)
id=Entry(lf)
id.grid(row=1,column=2,padx=10)
Label(lf,text='Age',font=("arial",12,'bold'),bg='grey').grid(row=3,column=2)
age = Spinbox(lf,from_=5,to=30)
age.grid(row=4,column=2)
Label(lf,text='Month',font=('arial',12,'bold'),bg="grey").grid(row=3,column=1)
month = Combobox(lf,font='bold',values=['January','February','March','April','May','June','July','August','September','October','November','December'])
month.grid(row=4,column=1)
month.current(0)
Label(lf,text='Year',font=('arial',12,'bold'),bg="grey").grid(row=3,column=0)
year = Combobox(lf,values=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026'],font=("arial",10))
year.current(9)
year.grid(row=4,column=0,pady=10)

lf2= LabelFrame(frame,text='Options')
lf2.grid(row=2,column=0,padx=10,pady=10)
b = Button(lf2,text='Add',command=add,font=('arial',15,'bold'),cursor='hand2',width=12,bg='grey')
b.grid(row=0,column=0,padx=10)
d = Button(lf2,text='Delete',command=delete,font=('arial',15,'bold'),cursor='hand2',width=12,bg='grey')
d.grid(row=0,column=2,padx=10)
c = Button(lf2,text='Clear',command=clear,font=('arial',15,'bold'),cursor='hand2',width=12,bg='grey')
c.grid(row=0,column=1,padx=10,pady=10)

table = Treeview(frame,columns=('id','n','am','age','month','year'),show='headings',cursor='hand2')
table.grid(row=3,column=0,pady=10)
table.column('id',width=50)
table.heading('id',text='ID')
table.column('n',width=150)
table.heading('n',text='Name')
table.column('am',width=90)
table.heading('am',text='Amount')
table.column('age',width=70)
table.heading('age',text='Age')
table.column('month',width=110)
table.heading('month',text='Month')
table.column('year',width=90)
table.heading('year',text='Year')

wn.bind("<Delete>",delete)
wn.bind("<Return>",add)

wn.mainloop()