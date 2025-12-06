from tkinter import *
from tkinter import messagebox
# create a window
wn = Tk()
wn.title("Task app")
wn.geometry("500x500")
wn.resizable(False,False)
val =StringVar()
we = []
i=[]
# created a command to view all added task
def view():
    Label(frame, text="", height=2, bg="blue").place(x=0, y=150)
    global l
    fram = Frame(wn, width=300, height=500)
    fram.place(x=200, y=10)
    fram.propagate(False)
    fram.config(highlightthickness=1, highlightbackground="blue")
    Label(fram,text="VIEW TASKS",font=("arial",20,"bold"),fg="blue").pack(side="top")
    l= Listbox(fram,bg="blue",font=("arial",15,"bold"),fg="white",width=25,height=15)
    l.pack(side="top")
    for i in we:
      l.insert(END,i)
    if we:
        Button(fram,text="REMOVE TASK",cursor="hand2",font=("arial",15,"bold")
               ,width=15,fg="red",command=delete).pack(side="top")
    else:
        messagebox.showinfo("Error","No tasks available yet.....")
# create a command to remove a task.
def delete():
    if l.curselection():
        l.delete(l.curselection())
    else:
        messagebox.showinfo("Error","Select a task to delete")
# created a command to clear all tasks add to the list
def clr():
    fram = Frame(wn, width=300, height=500)
    fram.place(x=200, y=10)
    fram.propagate(False)
    fram.config(highlightthickness=1, highlightbackground="blue")
    Label(frame, text="", height=2, bg="blue").place(x=0, y=230)
    if messagebox.askyesno("Confirm","Do you really want to clear all your tasks?"):
       we.clear()
       i.clear()
       messagebox.showinfo("CLEARED","ALL TASK CLEARED SUCCESSFULLY")
    else:
        pass
# created a command to view the statistics of the tasks added
def st():
    fram = Frame(wn, width=300, height=500)
    fram.place(x=200, y=10)
    fram.propagate(False)
    Label(fram, text="STATISTICS TASKS", font=("arial", 20, "bold"), fg="blue").pack(side="top")
    Label(frame, text="", height=2, bg="blue").place(x=0, y=310)
    Label(fram, textvariable=StringVar(value=f"Total tasks: {len(we)-len(i)}\n"
                                             f"Total task added: {len(we)}\n"
                                             f"Task cleared: 0\n"
                                             f"Completed task: {len(i)}\n"
                                             f"Storage Space left: {12- len(we)}"),
          highlightbackground="red",
          fg="blue", font=("arial", 15, "bold"), highlightthickness=3, width=25,
          height=10).pack(side="top")

# created a command to exit the program
def exite(event):
    wn.destroy()
# create a task to submit the task
def sub():
    if entry.get():
        if len(we) == 12:
           messagebox.showinfo("Task app", "Task app storage is full!")
        else:
            entry.get()
            we.append(entry.get())
            messagebox.showinfo("Task added",f"'{entry.get()}'"
                                             f" has been added to your list "
                                             f"successfully".title())
    else:
        messagebox.showerror("Error","No tasks added yet."
                                     " Please add a task first".title())
def su(event):
    if entry.get():
        if len(we) == 12:
            messagebox.showinfo("Task app", "Task app storage is full!")
        else:
            entry.get()
            we.append(entry.get())
            messagebox.showinfo("Task added", f"'{entry.get()}'"
                                              f" has been added to your list "
                                              f"successfully".title())
    else:
        messagebox.showerror("Error", "No tasks added yet."
                                      " Please add a task first".title())
# created a command to add to a task
def add():
    global entry
    Label(frame, text="", height=2, bg="blue").place(x=0, y=70)
    frame3 = Frame(wn, width=300, height=500)
    frame3.place(x=200, y=10)
    frame3.propagate(False)
    frame3.config(highlightthickness=1, highlightbackground="blue")
    label = Label(frame3,font=("arial",20,"bold"),
                  text="ADD TASK",fg="blue")
    label.place(x=10,y=10)
    entry = Entry(frame3)
    entry.place(x=10,y=50)
    entry.config(font=("arial",15,"bold"))
    bu = Button(frame3,bg="grey",text="SUBMIT TASK",fg="red",cursor="hand2",
                font=("arial",15,"bold"),command=sub)
    bu.place(x=10,y=100)
def mark():
    global la
    Label(frame, text="", height=2, bg="blue").place(x=0, y=400)
    fram = Frame(wn, width=300, height=500)
    fram.place(x=200, y=10)
    fram.propagate(False)
    fram.config(highlightthickness=1, highlightbackground="blue")
    Label(fram, text="MARK TASKS",font=("arial",15,"bold"), height=2, fg="blue").pack(side="top")
    la = Listbox(fram,bg="blue",fg="white",font=("arial",15,"bold"),width=40,height=15)
    la.pack()
    for i in we:
        la.insert(la.size(),i)
    bu = Button(fram, bg="grey", text="MARK TASK", fg="red", cursor="hand2",
                font=("arial", 15, "bold"),command=ma)
    bu.pack()
def ma():
    if la.curselection():
        la.delete(la.curselection())
        la.insert(la.size(),la.curselection(),"Completed ✔")
        i.append(la.curselection())
    else:
        messagebox.showinfo("Error", "Select a task to delete")
# create two frame
frame = Frame(wn,width=200,height=500)
frame.pack(side="left")
frame.propagate(False)
frame.config(bg="grey",highlightthickness=1,highlightbackground="blue")
frame2 = Frame(wn,width=300,height=500)
frame2.pack(side="right")
frame2.propagate(False)
frame2.config(highlightthickness=1,highlightbackground="blue")
# create buttons and labels to the first frame
l=lab = Label(frame,text="MENU LIST",width=20,fg="grey",font=("arial",15,"bold"))
l.pack(side="top")
but1 = Button(frame,text="ADD TASK",activebackground="grey",activeforeground="white"
              ,fg="blue",
              font=("arial",15,"bold"),cursor="hand2",bg="grey"
              ,border=0,command=add)
but1.place(x=40,y=70)
but2 = Button(frame,text="VIEW TASK",activebackground="grey",activeforeground="white",
              fg="blue",font=("arial",15,"bold")
              ,bg="grey",border=0,cursor="hand2",command=view)
but2.place(x=40,y=150)
but3 = Button(frame,text="CLEAR TASKS",activebackground="grey",activeforeground="white",
              fg="blue",font=("arial",15,"bold")
              ,bg="grey",border=0,cursor="hand2",command=clr)
but3.place(x=30,y=230)
but4 = Button(frame,text="STATISTICS",activebackground="grey",activeforeground="white",
              fg="blue",font=("arial",15,"bold")
              ,bg="grey",border=0,cursor="hand2",command=st)
but4.place(x=40,y=310)
but5 = Button(frame,text="MARK DONE TASK",activebackground="grey",activeforeground="white",
              fg="blue",font=("arial",15,"bold",)
              ,bg="grey",border=0,cursor="hand2",width=15,command=mark)
but5.place(x=10,y=400)
wn.bind("<Escape>",exite)
wn.bind("<Return>",su)

wn.mainloop()