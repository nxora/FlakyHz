from tkinter import *
from tkinter import messagebox
import os
zx = 108224724029
i = []
wn= Tk()
wn.title("Account App")
wn.geometry("500x500")
wn.config(bg="white")
wn.resizable(False,False)
L = Label(wn,text="WELCOME TO ACCOUNT APP",width=50
          ,fg="black",bg="sky blue",font=("arial",15,"bold"))
L.pack()

class Login:
    def __init__(self):
        self.t = wn

    def log(self):
        global e4
        global b
        global ba
        global e
        global e2
        self.w =Tk()
        self.w.config(bg="grey")
        self.w.geometry("700x500")
        self.w.title("Login Page")
        self.w.resizable(False,False)
        f = Label(self.w, text="PROFILE", fg="blue", font=("arial",20,"bold"),width=15)
        f.pack(side="top")
        frame1 = Frame(self.w, width=300)
        frame1.propagate(False)
        frame1.config(highlightthickness=3
                      ,highlightbackground="black",highlightcolor="black",bg="white")
        frame1.place(x=10,y=50)
        l = Label(frame1,text="Enter First Name",font=("arial",15))
        l.grid(row=0,column=0)
        e = Entry(frame1,font=("arial",15))
        e.grid(row=0,column=1)
        e.config(highlightthickness=3, highlightbackground="black",
                    highlightcolor="black")
        o= Button(frame1, text="", activebackground="white",
                   border=0, cursor="hand2", font=("arial", 20, "bold"), activeforeground="white")
        o.grid(row=0, column=2)
        fram = Frame(self.w, width=300)
        fram.propagate(False)
        fram.config(highlightthickness=3, highlightbackground="black",
                    highlightcolor="black")
        fram.place(x=10,y=110)
        l2 = Label(fram,text="Enter Last Name",font=("arial",15))
        l2.grid(row=0,column=0)
        e2 = Entry(fram,font=("arial",15))
        e2.grid(row=0,column=1)
        e2.config(highlightthickness=3, highlightbackground="black",
                    highlightcolor="black",bg="white")
        t= Button(fram, text="", activebackground="white",
                    border=0,font=("arial",20,"bold"), activeforeground="white")
        t.grid(row=0, column=2)
        frame = Frame(self.w, width=300)
        frame.propagate(False)
        frame.config(highlightthickness=3, highlightbackground="black", highlightcolor="black", bg="white")
        frame.place(x=10,y=170)
        l3 = Label(frame,text="Enter Password",font=("arial",15))
        l3.grid(row=2,column=0)
        self.e3 = Entry(frame, show="*", font=("arial", 15))
        self.e3.grid(row=2,column=1)
        b = Button(frame,text="👀",command=m.show,activebackground="grey",
                   font=("arial",20,"bold"),border=0,cursor="hand2",activeforeground="white")
        b.grid(row=2,column=2)
        ram = Frame(self.w, width=300)
        ram.propagate(False)
        ram.config(highlightthickness=3, highlightbackground="black", highlightcolor="black", bg="white")
        ram.place(x=10, y=230)
        l3 = Label(ram, text="Confirm Password", font=("arial", 15))
        l3.grid(row=3, column=0)
        self.e = Entry(ram, show="*", font=("arial", 15))
        self.e.grid(row=3, column=1)
        self.rame = Frame(self.w)
        self.rame.propagate(False)
        self.rame.config(highlightthickness=3
                          , highlightbackground="black", highlightcolor="black", bg="white")
        self.rame.place(x=10,y=290)
        lb = Label(self.rame,text="Enter Email", font=("arial", 15))
        lb.grid(row=0,column=0)
        e4 = Entry(self.rame, font=("arial",15))
        e4.grid(row=0, column=1)
        e4.config(highlightthickness=3,highlightbackground="black",width=40,highlightcolor="black",bg="white")
        ta = Button(self.rame, text="", activebackground="white",
                   border=0, font=("arial", 20, "bold"), activeforeground="white")
        ta.grid(row=0, column=2)
        ba = Button(ram, text="👀", command=m.sh, activebackground="grey",
                    font=("arial", 20), border=0,
                   cursor="hand2", activeforeground="white")
        ba.grid(row=3, column=2)
        ban = Button(self.w,text="Log-in",fg="blue",font=("arial",15,"bold"),width=10,height=2,
                     activebackground="white",cursor="hand2",command=m.com,activeforeground="blue",border=10)
        ban.place(x=170,y=390)
        bn = Button(self.w, text="Back", fg="blue", font=("arial", 15, "bold"), width=10, height=2,
                     activebackground="white", cursor="hand2", activeforeground="blue", border=10,command=m.bo)
        bn.place(x=10,y=390)
    def com(self):
        if e.get() and e2.get() and self.e.get() and self.e3.get() and e4.get():
            self.e3.config(show="*")
            self.e.config(show="*")
            with open("log",'w') as f:
                f.write(f"{e.get()} {e2.get()}\n"
                        f"{self.e3.get()}\n"
                        f"{e4.get()}")
            with open("log",'r') as f:
                qm=f.read()
            with open("create", 'r') as f:
                m=f.read()
            if self.e3.get() and self.e.get():
                if self.e3.get() == self.e.get():
                    pass
                else:
                    messagebox.showerror("Confirm", "Confirm Password!")
            if not self.e3.get() and self.e.get():
                messagebox.showerror("Password", "Enter Password!")
            elif qm==m:
                messagebox.showinfo("Welcome",f"Welcome {e.get()} {e2.get()}\n{e4.get()}\n"
                                              f"You can now select the MENU page")
                self.w.destroy()
            elif not qm==m:
                messagebox.showerror("Profile not found","PLEASE CONFIRM YOUR PROFILE CORRECT OR\n CREATE A NEW ACCOUNT BEFORE LOGGING IN")
                self.w.destroy()
        else:
            messagebox.showerror("Error", "Fill in all required question!")
            self.w.destroy()

    def bo(self):
        self.w.destroy()

    def sh(self):
        if self.e.get():
            self.e.config(show="")
            ba.config(text="Hide",command=m.hd)
        else:
            self.e.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def hd(self):
        if self.e.get():
            self.e.config(show="*")
            ba.config(text="👀",command=m.sh)
        else:
            self.e.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def show(self):
        if self.e3.get():
            self.e3.config(show="")
            b.config(text="Hide",command=m.hide)
        else:
            self.e3.config(highlightthickness=3,highlightbackground="black",highlightcolor="black")

    def hide(self):
        if self.e3.get():
            self.e3.config(show="*")
            b.config(text="👀",command=m.show)
        else:
            self.e3.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def create(self):
        global tr
        global tr2
        global Fa
        self.cr = Tk()
        self.cr.geometry("450x300")
        self.cr.resizable(False, False)
        Fa=Frame(self.cr,width=450,height=300)
        Fa.pack(side="left")
        l = Label(Fa,text="Create an account",width=19,font=("arial", 15))
        l.place(x=40,y=0)
        fm = Frame(Fa, highlightthickness=3, highlightbackground="black", highlightcolor="black", width=300)
        fm.place(x=0, y=40)
        lab = Label(fm,text="Enter First Name",font=("arial", 15))
        lab.grid(row=0,column=0)
        tr = Entry(fm,font=("arial", 15),width=20)
        tr.grid(row=0,column=1)
        ft= Frame(Fa,highlightthickness=3,highlightbackground="black",highlightcolor="black",width=300)
        ft.propagate(False)
        ft.place(x=0,y=80)
        La = Label(ft,text="Enter Last Name",font=("arial", 15))
        La.grid(row=0,column=0)
        tr2 = Entry(ft,font=("arial", 15),width=20)
        tr2.grid(row=0,column=1)
        Button(Fa,text="Next",font=("arial",15,"bold"),command=m.nx,activebackground="white",cursor="hand2",fg="white",bg="blue",width="15").place(x=80,y=170)

    def s(self):
        if t1.get():
            t1.config(show="")
            bp.config(text="Hide",command=m.h)
        else:
            t1.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def h(self):
        if t1.get():
            t1.config(show="*")
            bp.config(text="👀",command=m.s)
        else:
            t1.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def nx(self):
        global t1
        global t2
        global bp
        global bl
        if tr.get() and tr2.get():
            global F
            F=Frame(Fa,width=450,height=290)
            F.pack(side="left")
            l = Label(F, text="Create an account", width=19, font=("arial", 15))
            l.place(x=40, y=0)
            fm = Frame(F, highlightthickness=3, highlightbackground="black", highlightcolor="black", width=300)
            fm.place(x=0,y=40)
            lab = Label(fm, text="Enter Password", font=("arial", 15))
            lab.grid(row=0, column=0)
            t1 = Entry(fm,show="*" ,font=("arial", 15), width=20)
            t1.grid(row=0, column=1)
            bp = Button(fm, text="👀", command=m.s, activebackground="grey",
                        font=("arial", 20), border=0,
                        cursor="hand2", activeforeground="white")
            bp.grid(row=0, column=2)
            ft = Frame(F, highlightthickness=3, highlightbackground="black", highlightcolor="black", width=300)
            ft.propagate(False)
            ft.place(x=0, y=120)
            La = Label(ft, text="Confirm Password", font=("arial", 15))
            La.grid(row=0, column=0)
            t2 = Entry(ft,show="*" , font=("arial", 15), width=20)
            t2.grid(row=0, column=1)
            bl = Button(ft, text="👀", command=m.to, activebackground="grey",
                        font=("arial", 20), border=0,
                        cursor="hand2", activeforeground="white")
            bl.grid(row=0, column=2)
            Button(F, text="Next", font=("arial", 15, "bold"), command=m.check1, activebackground="white",
                   cursor="hand2", fg="white",bg="blue", width="15").place(x=80,y=190)
        elif tr.get() and tr2.get():
            tr.config(show=" ") and tr2.config(show=" ")
            self.cr.destroy()
            messagebox.showerror("Empty spaces", "FILL IN ALL THE REQUESTED QUESTIONS PLEASE")
        else:
            self.cr.destroy()
            messagebox.showerror("Empty spaces", "FILL IN ALL THE REQUESTED QUESTIONS PLEASE")
    def to(self):
        if t2.get():
            t2.config(show="")
            bl.config(text="Hide",command=m.at)
        else:
            t2.config(highlightthickness=3, highlightbackground="black", highlightcolor="black")

    def check1(self):
        global g1
        if t1.get() and t2.get():
            if t1.get()==t2.get():
                Fi = Frame(F, width=450, height=220)
                Fi.pack(side="left")
                fm = Frame(Fi, highlightthickness=3, highlightbackground="black", highlightcolor="black", width=300)
                fm.place(x=0, y=40)
                g = Label(fm, text="Enter Email",font=("arial", 15))
                g.grid(row=0, column=0)
                g1 = Entry(fm,font=("arial", 15),width=50)
                g1.grid(row=0, column=1)
                ch = Checkbutton(Fi,text="Male",font=("arial", 10))
                ch.place(x=80,y=130)
                ch1 = Checkbutton(Fi, text="Female", font=("arial", 10))
                ch1.place(x=140,y=130)
                Button(Fi, text="Submit", font=("arial", 15, "bold"), activebackground="white",
                       cursor="hand2",fg="white", bg="blue", width="15",command=m.sub).place(x=140,y=170)
            else:
                messagebox.showerror("Confirm Password","Please Confirm your password")
                self.cr.destroy()
        else:
            self.cr.destroy()
            messagebox.showerror("Empty spaces", "PLEASE CONFIRM ENTERED PASSWORD")

    def at(self):
        if t2.get():
            t2.config(show="*")
            bl.config(text="👀",command=m.to)

    def sign(self):
        global f
        f = Frame(fa, bg="grey", width=500, height=500)
        f.pack(side="left")
        Label(f, text="Sign Up", fg="white", font=("arial", 20, "bold"), bg="grey").place(x=30, y=10)
        bt = Button(f,bg="grey", text="➖ Log in",activebackground="grey",activeforeground="white",
                    foreground="blue", cursor="hand2", border=0, font=("arial", 20, "bold"),
                    command=m.log)
        bt.place(x=0, y=50)
        bt1 = Button(f,bg="grey",text="➖ Create new account",activebackground="grey",
                     activeforeground="white", cursor="hand2", border=0, foreground="blue",
                     font=("arial", 20, "bold"),command=m.create)
        bt1.place(x=0, y=110)
        bat1 = Button(f, bg="grey", text="➖ Back", activebackground="grey",
                     activeforeground="white", cursor="hand2", border=0, foreground="blue",
                     font=("arial", 20, "bold"),command=m.d)
        bat1.place(x=0, y=170)

    def sub(self):
        if g1.get():
            messagebox.showinfo("Welcome", f"Welcome {tr.get()} {tr2.get()}\n{g1.get()}\n"
                                           f"Now Log in your profile to the Log in page to activate your account.")
            t1.config(show="")
            with open("create", 'w') as f:
                f.write(f"{tr.get()} {tr2.get()}\n"
                        f"{t1.get()}\n"
                        f"{g1.get()}")
            self.cr.destroy()
        else:
            messagebox.showerror("Empty spaces", "Enter an email address")

    def d(self):
        f.destroy()
        fa.config( width=230, height=500)

    def home(self):
        global fa
        global bm
        self.t.config(bg="white")
        self.t.geometry("500x500")
        fa = Frame(self.t, bg="grey", width=230, height=500)
        fa.pack(side="left")
        bm= Button(fa,text="➖ Sign Up",border=0,cursor="hand2",fg="blue",bg="grey",activebackground="grey",activeforeground="white",font=("arial", 20, "bold"),command=m.sign)
        bm.place(x=0, y=40)
        bd = Button(fa, text="➖ Menu", border=0,command=m.menu, cursor="hand2", fg="blue", bg="grey", activebackground="grey",
                    activeforeground="white", font=("arial", 20, "bold"))
        bd.place(x=0, y=110)
        bnd = Button(fa, text="➖ Help", border=0, cursor="hand2", fg="blue", bg="grey",
                    activebackground="grey",
                    activeforeground="white",command=m.help, font=("arial", 20, "bold"))
        bnd.place(x=0, y=180)

    def help(self):
        global vc
        vc= Frame(fa, bg="grey", width=500, height=500)
        fa.config(width=500,height=500)
        vc.place(x=0, y=0)
        fo=Label(vc,bg="white",width=60,fg="blue", height=20,highlightthickness=3,highlightbackground="blue",text="Please read all required information\n"
                                                                                    "to help you Sign Up.\n"
                                                                                    "\nAlso open the Sign Up page and create an account.\n"
                                                                                    "\nIf you create an account,Please Log in your exact account \n"
                                                                                    "profile to activate your Account app.\n"
                                                                                    "\nIf you Log in correctly, you can now activate the menu page\n"
                                                                                    "whenever you want but if you Log out,you would have to\n log in your account\n"
                                                                                    "\nIf you forget your account profile, you can\n either remember it or create a new account\n"
                                                                                    "\nPress the Escape button to quickly exit this app",font=("arial", 13, "bold"))
        fo.place(x=-50, y=0)
        M=Button(vc, fg="blue", text="➖ Back", font=("arial", 15, "bold"),
               cursor="hand2",command=m.vca, border=0, bg="grey", activebackground="white", activeforeground="grey")
        M.place(x=0,y=420)

    def vca(self):
        vc.destroy()
        fa.config(width=230, height=500)

    def menu(self):
        global N
        global fg
        global non
        try:
            if open("log"):
                N = Frame(fa, bg="grey", width=500, height=500)
                N.pack(side="left")
                T = Frame(N, bg="white", width=230, height=70, highlightbackground="black", highlightcolor="black",
                          highlightthickness=3)
                T.place(x=260, y=10)
                BAL = Label(T, text="👤", fg="blue", bg="white", font=("arial", 35, "bold"))
                BAL.place(x=0, y=0)
                with open("log", 'r') as f:
                    mo = f.read()
                BL = Label(T, text=f"{mo}", font=("arial", 10, "bold"))
                BL.place(x=50, y=5)
                x = Frame(N,bg="white",highlightthickness=3,highlightbackground="blue",height=469,width=150)
                x.place(x=0,y=0)
                x2 = Frame(N, bg="white", highlightthickness=3, highlightbackground="blue", height=290, width=320)
                x2.place(x=160, y=100)
                try:
                    with open("deposit", 'r') as f:
                        non= f.read()
                    with open("dep", 'r') as f:
                        nn=f.read()
                except FileNotFoundError:
                   messagebox.showerror("Balance", "Your balance is N0.00")

                fg= Label(x2,fg="blue",bg="white",textvariable=StringVar(value=f"Balance: {0}.00"),font=("arial", 15))
                fg.place(x=0,y=0)
                v = Label(x,fg="white",text="Menu",bg="blue",font=("arial", 20, "bold"),width=12)
                v.place(x=-30,y=0)
                xm1 = Button(x, fg="blue", text="➖ Back", command=m.bk, font=("arial", 15, "bold"),
                            cursor="hand2", border=0, bg="white", activebackground="white", activeforeground="grey")
                xm1.place(x=0, y=40)
                xm=Button(x,fg="blue",text="➖ Log out",command=m.logout,font=("arial", 15, "bold"),cursor="hand2",border=0,bg="white",activebackground="white",activeforeground="grey")
                xm.place(x=0,y=80)
                xm2=Button(x,fg="blue",text="➖ Deposit",command=m.deposit,font=("arial", 15, "bold"),cursor="hand2",border=0,bg="white",activebackground="white",activeforeground="grey")
                xm2.place(x=0, y=120)
                xm3 = Button(x, fg="blue", text="➖ Withdraw",command=m.withdraw, font=("arial", 15, "bold"), cursor="hand2", border=0,
                             bg="white", activebackground="white", activeforeground="grey")
                xm3.place(x=0, y=160)
                xm4 = Button(x, fg="blue", text="➖ Check\nAccount no", font=("arial", 15, "bold"), cursor="hand2", border=0,
                             bg="white",command=m.no,activebackground="white", activeforeground="grey")
                xm4.place(x=0, y=200)
                xm5 = Button(x, fg="blue",text="➖ Check\n"
                                                "  Balance",command=m.bill, font=("arial", 15, "bold"), cursor="hand2", border=0,
                             bg="white", activebackground="white", activeforeground="grey")
                xm5.place(x=0, y=260)
                xm6 = Button(x, fg="blue", text="➖ Transfer",command=m.transfer, font=("arial", 15, "bold"), cursor="hand2", border=0,
                             bg="white", activebackground="white", activeforeground="grey")
                xm6.place(x=0, y=320)

            else:
                messagebox.showinfo("Sign Up", "Please Sign Up first")
        except FileNotFoundError:
            messagebox.showerror("Error", "Please sign up first")

    def bk(self):
        N.destroy()
        fa.config(width=230, height=500)

    def logout(self):
        os.remove("log")
        N.destroy()
        fa.config(width=230, height=500)

    def deposit(self):
        global dsm
        if messagebox.askyesno("Deposit","Do want to deposit money to your account?"):
            self.p=Tk()
            self.p.title("Deposit")
            self.p.geometry("400x120")
            Label(self.p,text="Enter Deposit Amount",font=("arial",10,"bold")).grid(row=0,column=0)
            dsm=Entry(self.p,font=("arial",15))
            dsm.grid(row=0,column=1)
            vx=Button(self.p,text="Deposit",command=m.dep,font=("arial",15,"bold"),cursor="hand2",fg="white",bg="grey",activebackground="white",activeforeground="grey")
            vx.grid(row=1,column=0,columnspan=2)

    def dep(self):
        try:
            if int(dsm.get()):
                i.append(dsm.get())
                for it in i:
                    fg.config(textvariable=StringVar(value=f"Balance: {it}.00"),font=("arial", 15, "bold"))
                messagebox.showinfo("Deposit", f"Deposit '{dsm.get()}' Successfully")
                self.p.destroy()
        except ValueError:
            Label(self.p,text="Numbers only please",width=20,fg="red",font=("arial",10,"bold")).grid(row=2,column=0)

    def no(self):
        messagebox.showinfo("Your Account Number",f'Your Account Number is {zx}')

    def bill(self):
        with open("dep", 'r') as f:
            nin = f.read()
        messagebox.showinfo("Your Account balance", f'Your Account balance is currently: N{nin}.00')

    def transfer(self):
        global tran
        global nome
        global ome
        self.pt = Tk()
        self.pt.title("Transfer")
        self.pt.geometry("400x250")
        self.pt.resizable(False, False)
        fbm = Frame(self.pt, width=40, height=15,highlightthickness=3,highlightbackground="black")
        fbm.place(x=0, y=0)
        tat = Label(fbm,font=("arial",10,"bold"),text="Enter an account number to transfer money")
        tat.grid(row=0,column=0)
        tran= Entry(fbm,font=("arial",15,"bold"),highlightthickness=3,highlightbackground="black")
        tran.grid(row=1,column=0)
        fam = Frame(self.pt,width=40,height=15)
        fam.place(x=0,y=70)
        name = Label(fam,font=("arial",10,"bold"),text="Enter an account name")
        name.grid(row=0,column=0)
        nome = Entry(fam,font=("arial",15,"bold"),highlightbackground="black",highlightthickness=3)
        nome.grid(row=0,column=1)
        fame = Frame(self.pt,width=40,height=15)
        fame.place(x=0,y=130)
        ame = Label(fame, font=("arial", 10, "bold"), text="Enter transfer amount")
        ame.grid(row=0, column=0)
        ome = Entry(fame, font=("arial", 15, "bold"), highlightbackground="black", highlightthickness=3)
        ome.grid(row=0, column=1)
        nub= Button(self.pt,bg="blue",command=m.trans,fg="white",font=("arial",15,"bold"),width=15,text="Transfer",cursor="hand2",activebackground="white",activeforeground="grey")
        nub.pack(side="bottom")

    def withdraw(self):
        global Ep
        self.pat = Tk()
        self.pat.title("Withdraw")
        self.pat.geometry("400x100")
        Label(self.pat,text="Enter withdraw amount",font=("arial",10,"bold")).grid(row=0,column=0)
        Ep=Entry(self.pat,font=("arial",15),highlightthickness=3,highlightbackground="black")
        Ep.grid(row=0,column=1)
        Bot = Button(self.pat,text="Withdraw",command=m.will,font=("arial",15,"bold"),fg="white",bg="blue")
        Bot.grid(row=1,columnspan=2,column=0)

    def will(self):
        try:
            if int(Ep.get()):
                if int(Ep.get()) <= i[0]:
                    bank = i[0] - Ep.get()
                    messagebox.showinfo("Withdraw", f"{Ep.get()} has been withdrawn from your account")
                    fg.config(textvariable=StringVar(value=f"Balance: {bank}.00"), font=("arial", 15, "bold"))
                    self.pat.destroy()
                else:
                    messagebox.showinfo("Insufficient fund","You don't have enough funds to withdraw")
                    self.pat.destroy()
        except ValueError:
            Label(self.pat,text="Numbers only please",width=20,fg="red",font=("arial",10,"bold")).grid(row=2,column=0)

    def trans(self):
        if tran.get() and nome.get() and ome.get():
            try:
                if int(tran.get()) :
                    if messagebox.askyesno:
                        messagebox.showinfo("Transfer",f'N{ome.get()} has been successfully transferred to {nome.get()} account')
                        self.pt.destroy()
                    else:
                        pass
                if not int(ome.get()):
                    Label(self.pt, text="Please enter only number in both the\n account number and amount",
                          fg="red").pack(side="bottom")
            except ValueError:
                Label(self.pt,text="Please enter only number in both the\n account number and amount",fg="red").pack(side="bottom")
        else:
            messagebox.showerror("???","Please fill in out required question")
            self.pt.destroy()

def bind(event):
    wn.destroy()

m = Login()
m.home()
wn.bind("<Escape>",bind)

wn.mainloop()