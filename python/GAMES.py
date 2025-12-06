from tkinter import *
import random
from tkinter import messagebox
import os

wn = Tk()
wn.title("Habeeb Games")
wn.resizable(False,False)
wn.geometry("550x520")
frame = Frame(wn,bg="red",height=550,width=250)
frame.pack(side="left")

class RPC:
    def __init__(self):
        self.y = []
        self.c =[]
        self.ty = []
        self.tc = []
        self.pt1 =[]
        self.pt2 =[]
        self.l = Label(wn,bg="light green", text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮", font=("arial", 70, "bold"))
        self.l.pack(side="right")
    def bk(self):
        self.f.destroy()
        frame.config(height=550,width=250)
        self.y.clear()
        self.c.clear()
        self.l = Label(wn, text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮",bg="light green", font=("arial", 70, "bold"))
        self.l.pack(side="right")

    def start(self):
        global l1,b1,l2,fam,b2,b3,la1,la2
        self.f = Frame(frame,bg="red",width=550,height=550)
        self.f.pack()
        self.l.destroy()
        l = Label(self.f,text="Rock,Paper,Scissor",bg="red",fg="light green",font=("elephant",15,"bold"))
        l.place(x=130,y=10)
        fam = Frame(self.f, bg="white", width=400, height=100, highlightthickness=3, highlightbackground="black")
        fam.place(x=100,y=70)
        l1 = Label(fam,fg="red",textvariable=StringVar(value=f"Computer choose:"),font=("arial",15,"bold"))
        l1.place(x=0,y=0)
        l2 = Label(fam,fg="red",textvariable=StringVar(value=f"Player choose:"),font=("arial",15,"bold"))
        l2.place(x=0,y=40)
        Label(self.f, text="Select a character of choice", bg="red", fg="light green", font=("elephant", 15,"bold")).place(x=0,y=35)
        b1=Button(self.f,bg="red",cursor="hand2",fg="light green",command=m.r,font=("arial",15,"bold"),text="➖Rock👊🏿👊🏿")
        b1.place(x=0,y=175)
        b2 = Button(self.f, bg="red",cursor="hand2",command=m.p,fg="light green", font=("arial", 15, "bold"), text="➖Paper📰📰")
        b2.place(x=0,y=230)
        b3 = Button(self.f, bg="red", cursor="hand2",command=m.s, fg="light green", font=("arial", 15, "bold"), text="➖Scissor✂️✂️")
        b3.place(x=0,y=290)
        fa = Frame(self.f,bg="white",width=200,height=90,highlightthickness=3,highlightbackground="black")
        fa.place(x=200,y=420)
        la = Label(fa,text="Scores",fg="red",bg="white", font=("arial", 15, "bold"))
        la.place(x=40,y=0)
        la1 = Label(fa,textvariable=StringVar(value=f"Computer: {len(self.c)}"),fg="red",bg="white", font=("arial",10, "bold"))
        la1.place(x=0,y=30)
        la2 = Label(fa, textvariable=StringVar(value=f"Player: {len(self.y)}"), fg="red", bg="white", font=("arial", 10, "bold"))
        la2.place(x=0, y=49)
        rs = Button(self.f,text="➖Reset",command=m.reset,fg="light green",bg="red",font=("elephant",15,"bold"),cursor="hand2")
        rs.place(x=0,y=400)
        b = Button(self.f,command=m.bk,cursor="hand2",text="➖Back",fg="light green",bg="red",font=("elephant", 20, "bold"))
        b.place(x=0,y=450)

    def r(self):
        global qr
        l2.config(textvariable=StringVar(value="Player choose: Rock👊🏿👊🏿"),fg="blue")
        game = [" Rock👊🏿👊🏿","Paper📰📰","Scissor✂️✂️"]
        gam = random.choice(game)
        if gam == "Scissor✂️✂️":
            l1.config(textvariable=StringVar(value="Computer choose: Scissor✂️✂️"),fg="blue")
            messagebox.showinfo("Winner","You won 😁")
            self.y.append("1")
            la2.config(textvariable=StringVar(value=f"Player: {len(self.y)}"))
            
        elif gam == "Paper📰📰":
            l1.config(textvariable=StringVar(value="Computer choose: Paper📰📰"), fg="blue")
            messagebox.showinfo("You lose", "Computer won the game 😎")
            self.c.append("1")
            la1.config(textvariable=StringVar(value=f"Computer: {len(self.c)}"))
        elif gam == "Rock👊🏿👊🏿":
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("No Winner","No winner")
        else:
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("No Winner", "No winner")

    def p(self):
        l2.config(textvariable=StringVar(value="Player choose: Paper📰📰"),fg="blue")
        game = [" Rock👊🏿👊🏿", "Paper📰📰", "Scissor✂️✂️"]
        gam= random.choice(game)
        if gam == "Rock👊🏿👊🏿":
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("Winner","You won the game")
            self.y.append("1")
            la2.config(textvariable=StringVar(value=f"Player: {len(self.y)}"))
        elif gam == "Scissor✂️✂️":
            l1.config(textvariable=StringVar(value="Computer choose: Scissor✂️✂️"), fg="blue")
            messagebox.showinfo("You lose","Computer won the game")
            self.c.append("1")
            la1.config(textvariable=StringVar(value=f"Computer: {len(self.c)}"))
        elif gam == "Paper📰📰":
            l1.config(textvariable=StringVar(value="Computer choose: Paper📰📰"), fg="blue")
            messagebox.showinfo("No Winner","No winner")
        else:
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("Winner", "You won the game")
            self.y.append("1")
            la2.config(textvariable=StringVar(value=f"Player: {len(self.y)}"))

    def s(self):
        l2.config(textvariable=StringVar(value="Player choose: Scissor✂️✂️"),fg="blue")
        game = [" Rock👊🏿👊🏿", "Paper📰📰", "Scissor✂️✂️"]
        gam = random.choice(game)
        if gam == "Paper📰📰":
            l1.config(textvariable=StringVar(value="Computer choose: Paper📰📰"), fg="blue")
            messagebox.showinfo("Winner", "You won the game")
            self.y.append("1")
            la2.config(textvariable=StringVar(value=f"Player: {len(self.y)}"))
        elif gam == "Rock👊🏿👊🏿":
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("You lose", "Computer won the game")
            self.c.append("1")
            la1.config(textvariable=StringVar(value=f"Computer: {len(self.c)}"))
        elif gam == "Scissor✂️✂️":
            l1.config(textvariable=StringVar(value="Computer choose: Scissor✂️✂️"), fg="blue")
            messagebox.showinfo("No Winner", "No winner")
        else:
            l1.config(textvariable=StringVar(value="Computer choose: Rock👊🏿👊🏿"), fg="blue")
            messagebox.showinfo("You lose", "Computer won the game")
            self.c.append("1")
            la1.config(textvariable=StringVar(value=f"Computer: {len(self.c)}"))

    def reset(self):
        l2.config(fg="red",textvariable=StringVar(value=f"Player choose:"),font=("arial",15,"bold"))
        l1.config(fg="red",textvariable=StringVar(value=f"Computer choose:"),font=("arial",15,"bold"))

    def opt(self):
        global fun
        fun = Frame(frame,width=550,height=550,bg="red")
        fun.pack()
        lm =Label(fun,text="Tic Tac Toc\nSelect whom you are to play Tic Tac Toc with",fg="white",bg="red",font=("elephant",15,"bold"))
        lm.place(x=10,y=10)
        pl = Button(fun,text="👤 VS 👤",font=("elephant",30,"bold"),fg="white",bg="red",command=m.ttt)
        pl.place(x=120,y=100)
        cm = Button(fun, text="👤 VS 💻",command=m.com, font=("elephant", 30, "bold"), fg="white", bg="red")
        cm.place(x=120, y=200)
        bj = Button(fun,text="➖Back",fg="white",bg="red",command=m.bk2,font=("elephant",20,"bold"))
        bj.place(x=0,y=420)
    def bba(self):
        with open("bbc",'w') as f:
            f.write("computer")
        bb.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb2.config(text="⭕",fg="blue",activebackground="light green",activeforeground="red")
        try:
            if open("bbc") and open("bb4") and open("bb8"):
                bb.config(bg="grey")
                bb4.config(bg="grey")
                bb8.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
        except FileNotFoundError:
            pass

    def bb12(self):
        with open("bb1",'w') as f:
            f.write("computer")
        bb1.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb4.config(text="⭕",fg="blue",activebackground="light green",activeforeground="red")

    def bb22(self):
        with open("bb2",'w') as f:
            f.write("computer")
        bb2.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb.config(text="⭕", fg="blue", activebackground="light green", activeforeground="red")
        try:
            if open("bb2") and open("bb5") and open("bb8"):
                bb2.config(bg="red")
                bb5.config(bg="red")
                bb8.config(bg="red")
                messagebox.showinfo("O win", "Computer[O] is the winner")
                self.tc.append("1")
                J.config(textvariable=StringVar(value=f"Computer[⭕]: {len(self.tc)}"))
        except FileNotFoundError:
            pass

    def bb32(self):
        with open("bb3",'w') as f:
            f.write("computer")
        bb3.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb6.config(text="⭕",fg="blue",activebackground="light green",activeforeground="red")
        try:
            if open("bb3") and open("bb4") and open("bb5"):
                bb3.config(bg="grey")
                bb4.config(bg="grey")
                bb5.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
        except FileNotFoundError:
            pass

    def bb52(self):
        with open("bb5", 'w') as f:
            f.write("computer")
        bb5.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb8.config(text="⭕",fg="blue",activebackground="light green",activeforeground="red")
        try:
            if open("bb3") and open("bb4") and open("bb5"):
                bb3.config(bg="grey")
                bb4.config(bg="grey")
                bb5.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
            elif open("bb2") and open("bb5") and open("bb8"):
                bb2.config(bg="red")
                bb5.config(bg="red")
                bb8.config(bg="red")
                messagebox.showinfo("O win", "Computer[O] is the winner")
                self.tc.append("1")
                J.config(textvariable=StringVar(value=f"Computer[⭕]: {len(self.tc)}"))
        except FileNotFoundError:
            pass

    def bb42(self):
        bb4.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb5.config(text="⭕", fg="blue", activebackground="light green", activeforeground="red")
        with open("bb4",'w') as f:
            f.write("computer")
        try:
            if open("bbc") and open("bb4") and open("bb8"):
                bb.config(bg="grey")
                bb4.config(bg="grey")
                bb8.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
            elif open("bb3") and open("bb4") and open("bb5"):
                bb3.config(bg="grey")
                bb4.config(bg="grey")
                bb5.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
        except FileNotFoundError:
            pass
    def bb62(self):
        with open("bb6",'w') as f:
            f.write("computer")
        bb6.config(text="❌",fg="red",activebackground="light green",activeforeground="red")
        bb7.config(text="⭕", fg="blue", activebackground="light green", activeforeground="red")

    def bb72(self):
        with open("bb7",'w') as f:
            f.write("computer")
        bb8.config(text="⭕", fg="blue", activebackground="light green", activeforeground="red")
        bb7.config(text="❌", fg="red", activebackground="light green", activeforeground="red")

    def bb82(self):
        bb8.config(text="❌", fg="red", activebackground="light green", activeforeground="red")
        bb7.config(text="⭕", fg="blue", activebackground="light green", activeforeground="red")
        with open("bb8",'w') as f:
            f.write("computer")
        try:
            if open("bbc") and open("bb4") and open("bb8"):
                bb.config(bg="grey")
                bb4.config(bg="grey")
                bb8.config(bg="grey")
                self.ty.append("1")
                messagebox.showinfo("X win", "Player X is the winner")
                I.config(textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"))
            elif open("bb2") and open("bb5") and open("bb8"):
                bb2.config(bg="red")
                bb5.config(bg="red")
                bb8.config(bg="red")
                messagebox.showinfo("O win", "Computer[O] is the winner")
                self.tc.append("1")
                J.config(textvariable=StringVar(value=f"Computer[⭕]: {len(self.tc)}"))
        except FileNotFoundError:
            pass
    def com(self):
        global fn,bb,bb1,bb2,bb3,bb4,bb5,bb6,bb7,bb8,I,J
        fun.destroy()
        fn = Frame(frame,width=550,height=550,bg="light green")
        fn.pack()
        Label(fn,text="Tic Tac Toc with computer",font=("elephant",20,"bold"),bg="light green",fg="red").place(x=100,y=0)
        Label(fn, text="❌ and ⭕", font=("elephant", 20, "bold"), bg="light green", fg="red").place(x=140, y=50)
        fy = Frame(fn,width=300,height=300,highlightthickness=3,highlightbackground="red")
        fy.place(x=10,y=90)
        fin = Frame(frame, width=150, height=220, highlightbackground="red", highlightthickness=3)
        fin.place(x=400, y=100)
        Label(fin, text="Score", fg="red", font=("arial", 15, "bold")).place(x=30, y=0)
        I = Label(fin,textvariable=StringVar(value=f"Player[❌]: {len(self.ty)}"),fg="red",font=("arial",10,"bold"))
        I.place(x=0, y=30)
        J=Label(fin, textvariable=StringVar(value=f"Computer[⭕]: {len(self.tc)}"), fg="red",
              font=("arial",10, "bold"))
        J.place(x=0, y=60)
        bb = Button(fy, text="",command=m.bba, width=9, height=5,font=("arial",15,"bold"))
        bb.grid(row=0, column=0)
        bb1 = Button(fy, text="",command=m.bb12,width=9, height=5,font=("arial",15,"bold"))
        bb1.grid(row=0, column=1)
        bb2 = Button(fy, text="",command=m.bb22, width=9, height=5,font=("arial",15,"bold"))
        bb2.grid(row=0, column=2)
        bb3 = Button(fy, text="",command=m.bb32, width=9, height=5,font=("arial",15,"bold"))
        bb3.grid(row=1, column=0)
        bb4 = Button(fy, text="",command=m.bb42, width=9, height=5,font=("arial",15,"bold"))
        bb4.grid(row=1, column=1)
        bb5 = Button(fy, text="",command=m.bb52, width=9, height=5,font=("arial",15,"bold"))
        bb5.grid(row=1, column=2)
        bb6 = Button(fy, text="",command=m.bb62, width=9, height=5,font=("arial",15,"bold"))
        bb6.grid(row=2, column=0)
        bb7 = Button(fy, text="", width=9,command=m.bb72, height=5,font=("arial",15,"bold"))
        bb7.grid(row=2, column=1)
        bb8 = Button(fy, text="",command=m.bb82, width=9, height=5,font=("arial",15,"bold"))
        bb8.grid(row=2, column=2)
        k = Button(fn, text="➖Back", fg="red", bg="light green", command=m.bk3, font=("elephant", 20, "bold"))
        k.place(x=400,y=450)
        r = Button(fn,text="Restart",command=m.re2,font=("elephant",20,"bold"),bg="light green",fg="red")
        r.place(x=400,y=370)

    def ttt(self):
        fun.destroy()
        global fo,b,b1,b2,b3,b4,b5,b6,b7,b8
        fo = Frame(frame,width=550,height=550,bg="light green")
        fo.pack()
        La = Label(fo,text="Tic Tac Toc Game",fg="red",bg="light green",font=("elephant",15,"bold"))
        La.place(x=100,y=0)
        Label(fo, text="❌ and ⭕", font=("elephant", 20, "bold"), bg="light green", fg="red").place(x=140, y=30)
        f = Frame(fo,width=300,height=400,highlightbackground="red",highlightcolor="red",highlightthickness=3)
        f.place(x=10,y=70)
        fi = Frame(frame,width=150,height=220,highlightbackground="red",highlightcolor="red",highlightthickness=3)
        fi.place(x=380,y=70)
        Label(fi,text="Score",fg="red",font=("elephant",15,"bold")).place(x=30,y=0)
        Label(fi, textvariable=StringVar(value=f"Player1[❌]: {len(self.pt1)}"), fg="red", font=("arial", 10, "bold")).place(x=0, y=30)
        Label(fi, textvariable=StringVar(value=f"Player2[⭕]: {len(self.pt2)}"), fg="red",
              font=("arial", 10, "bold")).place(x=0, y=60)
        b = Button(f, text="",command=m.bn, width=9,height=5,font=("arial",15,'bold'))
        b.grid(row=0, column=0)
        b1 = Button(f, text="",command=m.bn1, width=9, height=5,font=("arial",15,"bold"))
        b1.grid(row=0, column=1)
        b2 = Button(f, text="",command=m.bn2, width=9,height=5,font=("arial",15,"bold"))
        b2.grid(row=0, column=2)
        b3 = Button(f, text="", width=9,command=m.bn3, height=5,font=("arial",15,"bold"))
        b3.grid(row=1, column=0)
        b4 = Button(f, text="", width=9,command=m.bn4, height=5,font=("arial",15,"bold"))
        b4.grid(row=1, column=1)
        b5 = Button(f, text="", width=9,command=m.bn5, height=5,font=("arial",15,"bold"))
        b5.grid(row=1, column=2)
        b6 = Button(f, text="", width=9, height=5,command=m.bn6,font=("arial",15,"bold"))
        b6.grid(row=2, column=0)
        b7 = Button(f, text="", width=9, height=5,command=m.bn7,font=("arial",15,"bold"))
        b7.grid(row=2, column=1)
        b8 = Button(f, text="", width=9,command=m.bn8, height=5,font=("arial",15,"bold"))
        b8.grid(row=2, column=2)
        re = Button(fo,text="Restart",command=m.restart,font=("elephant",20,"bold"),bg="light green",fg="red")
        re.place(x=400,y=370)
        bot = Button(fo,text="➖Back",fg="red",bg="light green",command=m.bkf,font=("elephant",20,"bold"))
        bot.place(x=400,y=450)

    def bn(self):
        gam = ["❌","⭕"]
        game= random.choice(gam)
        if game == "⭕":
            b.config(text=game,fg="blue",activebackground="light green",activeforeground="white")
        else:
            b.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn1(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b1.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b1.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn2(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b2.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b2.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn3(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b3.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b3.config(text=game, fg="red", activebackground="light green", activeforeground="white")
    def bn4(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b4.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
           b4.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn5(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b5.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b5.config(text=game, fg="red", activebackground="light green", activeforeground="white")
    def bn6(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b6.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b6.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn7(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b7.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b7.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bn8(self):
        gam = ["❌", "⭕"]
        game = random.choice(gam)
        if game == "⭕":
            b8.config(text=game, fg="blue", activebackground="light green", activeforeground="white")
        else:
            b8.config(text=game, fg="red", activebackground="light green", activeforeground="white")

    def bkf(self):
        fo.destroy()
        m.opt()

    def bk3(self):
        fn.destroy()
        m.opt()
        self.ty.clear()
        self.tc.clear()
        try:
            os.remove("bbc")
            os.remove("bb4")
            os.remove("bb8")
        except FileNotFoundError:
            pass
        try:
            os.remove("bbc")
            os.remove("bb1")
            os.remove("bb2")
            os.remove("bb3")
            os.remove("bb4")
            os.remove("bb5")
            os.remove("bb6")
            os.remove("bb7")
            os.remove("bb8")
        except FileNotFoundError:
            pass

    def bk2(self):
        fun.destroy()
        frame.config(height=550, width=250)
        self.l = Label(wn, text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮", bg="light green", font=("arial", 70, "bold"))
        self.l.pack(side="right")

    def restart(self):
        b.config(text="",bg="white")
        b1.config(text="",bg="white")
        b2.config(text="",bg="white")
        b3.config(text="",bg="white")
        b4.config(text="",bg="white")
        b5.config(text="",bg="white")
        b6.config(text="",bg="white")
        b7.config(text="",bg="white")
        b8.config(text="",bg="white")

    def re2(self):
        bb.config(text="",bg="white")
        bb1.config(text="",bg="white")
        bb2.config(text="",bg="white")
        bb3.config(text="",bg="white")
        bb4.config(text="",bg="white")
        bb5.config(text="",bg="white")
        bb6.config(text="",bg="white")
        bb7.config(text="",bg="white")
        bb8.config(text="",bg="white")
        try:
            os.remove("bbc")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb1")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb2")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb3")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb4")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb5")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb6")
        except FileNotFoundError:
            pass
        try:
            os.remove("bb7")
            os.remove("bb8")
        except FileNotFoundError:
            pass

class Quiz(RPC):
    def quiz(self):
        global fot
        fot = Frame(frame,width=600,height=550,bg="light green")
        fot.pack()
        Label(fot, text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮", bg="light green", font=("arial", 70, "bold")).pack(side="right")
        root =  Frame(fot,width=250,height=550,bg="red")
        root.place(x=0,y=0)
        Label(root,text="QUIZ GAME",fg="white",bg="red",font=("arial",15,"bold")).place(x=40,y=0)
        start = Button(root,text="➖START GAME",cursor="hand2",command=q.start,bg="red",fg="light green",font=("elephant",15,"bold"))
        start.place(x=0,y=40)
        score = Button(root,text="➖CHECK SCORE",cursor="hand2", bg="red", fg="light green", font=("elephant", 15, "bold"))
        score.place(x=0, y=130)
        HELP = Button(root,text="➖HELP",command=q.help, bg="red",cursor="hand2", fg="light green", font=("elephant", 15, "bold"))
        HELP.place(x=0, y=230)
        back = Button(root, text="➖BACK",cursor="hand2",command=q.back, bg="red", fg="light green", font=("elephant", 15, "bold"))
        back.place(x=0, y=330)
    def help(self):
        global moot,back
        moot = Frame(frame,width=600,height=550,bg="red")
        moot.place(x=0,y=0)
        Label(moot,bg="white",highlightthickness=3,font=("arial",10,"bold"),highlightbackground="light green",fg="blue",text="\nThis quiz game is easy to play\n"
                                                                                          "To start playing ,you would need pick the correct answer\n"
                                                                                          "to move to the next question\n"
                                                                                          "\nIf all questions are answered correctly \n"
                                                                                          "you would have completed to game.\n"
                                                                                          "If you keep an incorrect answer,"
                                                                                          "\n1 marks will subtracted from your score.",width=50,height=50).place(x=0,y=-150)
        back = Button(frame, text="➖BACK", cursor="hand2", command=q.back21, bg="red", fg="light green",
                      font=("elephant", 15, "bold"))
        back.place(x=0, y=420)
        
    def back21(self):
        moot.destroy()
        back.destroy()
        frame.config(width=250, height=550)
        self.l = Label(wn, text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮", bg="light green", font=("arial", 70, "bold"))
        self.l.pack(side="right")

    def back(self):
        fot.destroy()
        frame.config(width=250, height=550)
        self.l = Label(wn, text="🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮\n🎮🎮🎮🎮", bg="light green", font=("arial", 70, "bold"))
        self.l.pack(side="right")


    def resume(self):
        global Question,ql11,ql22,ql33,ql44,ql55,ql66,ql77,ql88,ql99,ql110,ql111,ql112,ql113,ql114,mano,mno
        if question == "What is the most common name for 'POVERTY' in Nigeria?":
            ql1.destroy()
        elif question == "Who is the current president of Nigeria?":
            ql2.destroy()
        elif question == "Which of the following is not a fruit?":
            ql3.destroy()
        elif question =="What is the capital of France?":
            ql4.destroy()
        elif question == "What is the square root of 625?":
            ql5.destroy()
        elif question =="Which of the following currency is rear to find in Nigeria?":
            ql6.destroy()
        elif question =="A toilet is a place to ?":
            ql7.destroy()
            man.destroy()
        elif question == "A kitchen is for ?":
            ql8.destroy()
        elif question =="What does Tik Tok do to us ?":
            ql9.destroy()
            mn.destroy()
        elif question == "What do human being breath in ?":
            ql10.destroy()
        elif question == "What planet is known to be red ?":
            ql11.destroy()
        elif question == "What is the most commonly and local food in Nigeria?":
            ql12.destroy()
        elif question == "Which of the following is more important ?":
            ql13.destroy()
        elif question == "If a cow drains a farmer of foods and supplies,and a farmer drains milk out of the cow. Who is the one been milked?":
           ql14.destroy()
        elif question == "Who is the creator for the game ?":
            ql15.destroy()
        ques = [
            "What is the most common name for 'POVERTY' in Nigeria?",
            "Who is the current president of Nigeria?",
            "Which of the following is not a fruit?",
            "What is the capital of France?",
            "What is the square root of 625?",
            "Which of the following currency is rear to find in Nigeria?",
            "A toilet is a place to ?",
            "A kitchen is for ?",
            "What does Tik Tok do to us ?",
            "What do human being breath in ?",
            "What planet is known to be red ?",
            "What is the most commonly and local food in Nigeria?",
            "Which of the following is more important ?",
            "If a cow drains a farmer of foods and supplies,and a farmer drains milk out of the cow. Who is the one been milked?",
            "Who is the creator for the game ?"
        ]
        Question = random.choice(ques)
        if Question == "What is the most common name for 'POVERTY' in Nigeria?":
            ql101 = Label(foot,bg="red",text="What is the most common name for \n'POVERTY' in Nigeria?",width=35,height=3,fg="white", font=("arial", 12, "bold"))
            ql101.place(x=0,y=10)
            Button(self.foot1,text="Poor",command=q.wrong,fg="white",cursor="hand2",width=20,bg="red", font=("arial", 15, "bold")).place(x=40,y=70)
            Button(self.foot1,text="Sapa",command=q.sapa,cursor="hand2",activebackground="light green",fg="white",width=20,bg="red",font=("arial", 15, "bold")).place(x=40,y=140)
            Button(self.foot1,text="Poverty",command=q.wrong,cursor="hand2",fg="white",width=20,bg="red", font=("arial", 15, "bold")).place(x=40,y=210)
            Button(self.foot1,text="Broke",command=q.wrong,cursor="hand2",fg="white",width=20,bg="red",font=("arial", 15, "bold")).place(x=40,y=280)
            Button(foot,text="➖Back", bg="red",command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(x=420,y=450)
        elif Question == "Who is the current president of Nigeria?":
            ql22 = Label(foot,text="Who is the current president of Nigeria?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql22.place(x=0,y=10)
            Button(self.foot1, bg="red",command=q.wrong,text="Peter Obi",width=20, fg="white", cursor="hand2", font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Bola Ahmed Tinubu",width=20,command=q.Bola, cursor="hand2", activebackground="light green", fg="white", bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1,command=q.wrong,text="Buhari", cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Habeeb",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "Which of the following is not a fruit?":
            ql33 = Label(foot,text="Which of the following is not a fruit?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql33.place(x=0,y=10)
            Button(self.foot1, text="Grape",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Banana",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Apple",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Maize",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What is the capital of France?":
            ql44 = Label(foot,text="What is the capital of France?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql44.place(x=0,y=10)
            Button(self.foot1, text="America",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Paris",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="London",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Dubai",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What is the square root of 625?":
            ql55 = Label(foot,text="What is the square root of 625?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql55.place(x=0,y=10)
            Button(self.foot1, text="5",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="15",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="25",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "Which of the following currency is\n rear to find in Nigeria?":
            ql66 = Label(foot,text="Which of the following currency is rear to find in Nigeria?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql66.place(x=0,y=10)
            Button(self.foot1, text="N50",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="N20",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="N5",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "A toilet is a place to ?":
            ql77 = Label(foot,text="A toilet is a place for ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql77.place(x=0,y=10)
            Button(self.foot1, text="For Praying",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="For Thinking",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="For releasing physis",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            mano=Button(self.foot1, text="For Thinking and releasing physis", width=38,height=2, activebackground="light green", cursor="hand2", fg="white", bg="red",
                   font=("arial", 8, "bold"),command=q.Bola)
            mano.place(x=35, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "A kitchen is for ?":
            ql88 = Label(foot,text="A kitchen is for ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql88.place(x=0,y=10)
            Button(self.foot1, text="Stealing meat",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Eating",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Cooking",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="For Thinking",
                   cursor="hand2", fg="white",command=q.wrong, width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What does Tik Tok do to us ?":
            ql99 = Label(foot,text="What does Tik Tok do to us ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql99.place(x=0,y=10)
            mno=Button(self.foot1, text="Help us Thinking "
                                    "before we talk",command=q.wrong, fg="white", cursor="hand2", width=38,height=2, bg="red",
                   font=("arial", 8, "bold"))
            mno.place(x=40, y=70)
            Button(self.foot1, text="Help in Posting",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Entertain us",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="All of the above",command=q.sapa, activebackground="light green",
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What do human being breath in ?":
            ql100 = Label(foot,text="What do human being breath in ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql100.place(x=0,y=10)
            Button(self.foot1, text="Water",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Carbon dioxide",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Oxygen",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Poverty",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What planet is known to be red ?":
            ql111 = Label(foot,text="What planet is known to be red ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql111.place(x=0,y=10)
            Button(self.foot1, text="Jupiter",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Venus",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Mars",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Pluto",
                   cursor="hand2", fg="white",command=q.wrong, width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "What is the most commonly and \nlocal food in Nigeria?":
            ql112 = Label(foot,text="What is the most commonly and local food in Nigeria?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql112.place(x=0,y=10)
            Button(self.foot1, text="Beans",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Yam",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Garri",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Rice",command=q.sapa, activebackground="light green",
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "Which of the following is more important ?":
            ql113=Label(foot,text="Which of the following is more important ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql113.place(x=0,y=10)
            Button(self.foot1, text="Electricity",command=q.Bola, activebackground="light green", fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Tik Tok",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Wifi",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Google",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "If a cow drains a farmer of foods and supplies,and a farmer drains milk out of the cow. Who is the one been milked?":
            ql114= Label(foot,width=35,height=3,text="If a cow drains a farmer of foods \nand supplies, and a farmer drains milk out of the\ncow. Who is the one been milked?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql114.place(x=0,y=10)
            Button(self.foot1, text="The Farmer",command=q.wrong, fg="white", cursor="hand2", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="The cow",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Both of them",command=q.Bola,activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None of them",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif Question == "Who is the creator for this game ?":
            ql115=Label(foot,text="Who is the creator for the game ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql115.place(x=0,y=10)
            Button(self.foot1, text="H-storm", command=q.wrong, fg="white", cursor="hand2", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Salam", command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Habeeb", command=q.Bola, activebackground="light green", cursor="hand2",
                   fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Hb", command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
    def start(self):
        global foot,o,lin1,lin2,lin3,S,S2,S3,ql1,ql2,ql3,ql4,ql5,ql6,ql7,ql8,ql9,question,ql10,ql11,ql12,ql13,ql14,mn,man,ql15
        fot.destroy()
        self.qscore = []
        foot = Frame(frame, width=550, height=550, bg="red")
        foot.pack()
        ques =[
            "What is the most common name for 'POVERTY' in Nigeria?",
            "Who is the current president of Nigeria?",
            "Which of the following is not a fruit?",
            "What is the capital of France?",
            "What is the square root of 625?",
            "Which of the following currency is rear to find in Nigeria?",
            "A toilet is a place to ?",
            "A kitchen is for ?",
            "What does Tik Tok do to us ?",
            "What do human being breath in ?",
            "What planet is known to be red ?",
            "What is the most commonly and local food in Nigeria?",
            "Which of the following is more important ?",
            "If a cow drains a farmer of foods and supplies,and a farmer drains milk out of the cow. Who is the one been milked?",
            "Who is the creator for the game ?"
            ]
        question = random.choice(ques)
        self.foot1 = Frame(foot,bg="red",width=300,height=500)
        self.foot1.place(x=0,y=40)
        self.foot2 = Frame(foot,bg="light green",width=150,height=250)
        self.foot2.place(x=380,y=70)
        o=Label(self.foot2,text="Score",fg="red",bg="light green", font=("arial", 20, "bold"))
        o.place(x=0,y=0)
        S= Label(self.foot2,text="⭐" ,font=("arial", 25, "bold"),fg="white",bg="light green")
        S.place(x=0,y=30)
        S2 = Label(self.foot2, text="⭐", font=("arial", 25, "bold"), fg="white", bg="light green")
        S2.place(x=50, y=30)
        S3 = Label(self.foot2, text="⭐", font=("arial", 25, "bold"), fg="white", bg="light green")
        S3.place(x=100, y=30)
        lin1 = Frame(self.foot2,bg="white",highlightthickness=3,highlightbackground="red",width=30,height=150)
        lin1.place(x=10,y=70)
        lin2 = Frame(self.foot2, bg="white", highlightthickness=3, highlightbackground="red", width=30, height=150)
        lin2.place(x=60, y=70)
        lin3 = Frame(self.foot2, bg="white", highlightthickness=3, highlightbackground="red", width=30, height=150)
        lin3.place(x=110, y=70)
        if question == "What is the most common name for 'POVERTY' in Nigeria?":
            ql1 = Label(foot,bg="red",text="What is the most common name for 'POVERTY' in Nigeria?",fg="white", font=("arial", 12, "bold"))
            ql1.place(x=0,y=10)
            Button(self.foot1,text="Poor",command=q.wrong,fg="white",cursor="hand2",width=20,bg="red", font=("arial", 15, "bold")).place(x=40,y=70)
            Button(self.foot1,text="Sapa",command=q.sapa,cursor="hand2",activebackground="light green",fg="white",width=20,bg="red",font=("arial", 15, "bold")).place(x=40,y=140)
            Button(self.foot1,text="Poverty",command=q.wrong,cursor="hand2",fg="white",width=20,bg="red", font=("arial", 15, "bold")).place(x=40,y=210)
            Button(self.foot1,text="Broke",command=q.wrong,cursor="hand2",fg="white",width=20,bg="red",font=("arial", 15, "bold")).place(x=40,y=280)
            Button(foot,text="➖Back", bg="red",command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(x=420,y=450)
        elif question == "Who is the current president of Nigeria?":
            ql2 = Label(foot,text="Who is the current president of Nigeria?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql2.place(x=0,y=10)
            Button(self.foot1, text="Peter Obi",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red", font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Bola Ahmed Tinubu",command=q.Bola, cursor="hand2", activebackground="light green", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Buhari",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Habeeb",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "Which of the following is not a fruit?":
            ql3 = Label(foot,text="Which of the following is not a fruit?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql3.place(x=0,y=10)
            Button(self.foot1, text="Grape",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Banana",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Apple",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Maize",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What is the capital of France?":
            ql4 = Label(foot,text="What is the capital of France?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql4.place(x=0,y=10)
            Button(self.foot1, text="America",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Paris",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="London",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Dubai",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What is the square root of 625?":
            ql5 = Label(foot,text="What is the square root of 625?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql5.place(x=0,y=10)
            Button(self.foot1, text="5",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="15",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="25",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "Which of the following currency is rear to find in Nigeria?":
            ql6 = Label(foot,text="Which of the following currency is rear to find in Nigeria?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql6.place(x=0,y=10)
            Button(self.foot1, text="N50",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="N20",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="N5",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None",command=q.wrong, cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "A toilet is a place to ?":
            ql7 = Label(foot,text="A toilet is a place for ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql7.place(x=0,y=10)
            Button(self.foot1, text="For Praying",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="For Thinking",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="For releasing feces",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            man=Button(self.foot1, text="For Thinking and\n releasing feces", activebackground="light green", cursor="hand2", fg="white", width=22, bg="red",
                   font=("arial", 15, "bold"),command=q.sapa)
            man.place(x=35, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "A kitchen is for ?":
            ql8 = Label(foot,text="A kitchen is for ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql8.place(x=0,y=10)
            Button(self.foot1, text="Stealing meat",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Eating",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Cooking",command=q.Bola, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="For Thinking",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What does Tik Tok do to us ?":
            ql9 = Label(foot,text="What does Tik Tok do to us ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql9.place(x=0,y=10)
            mn=Button(self.foot1, text="Help us Think\n"
                                        "before we talk",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold"))
            mn.place(x=40, y=70)
            Button(self.foot1, text="Help in Posting",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Entertain us",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="All of the above",command=q.Bola, activebackground="light green",
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What do human being breath in ?":
            ql10 = Label(foot,text="What do human being breath in ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql10.place(x=0,y=10)
            Button(self.foot1, text="Water",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Carbon dioxide",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Oxygen",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Poverty",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What planet is known to be red ?":
            ql11 = Label(foot,text="What planet is known to be red ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql11.place(x=0,y=10)
            Button(self.foot1, text="Jupiter",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Venus",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Mars",command=q.sapa, activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Pluto",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "What is the most commonly and local food in Nigeria?":
            ql12 = Label(foot,text="What is the most commonly and local food in Nigeria?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql12.place(x=0,y=10)
            Button(self.foot1, text="Beans",command=q.wrong, fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Yam",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Garri",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Rice",command=q.Bola, activebackground="light green",
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "Which of the following is more important ?":
            ql13=Label(foot,text="Which of the following is more important ?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql13.place(x=0,y=10)
            Button(self.foot1, text="Electricity",command=q.Bola, activebackground="light green", fg="white", cursor="hand2", width=20, bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Tik Tok",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Wifi",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Google",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "If a cow drains a farmer of foods and supplies,and a farmer drains milk out of the cow. Who is the one been milked?":
            ql14= Label(foot,text="If a cow drains a farmer of foods \nand supplies, and a farmer drains milk out of the \ncow. Who is the one been milked?",bg="red",fg="white", font=("arial", 12, "bold"))
            ql14.place(x=0,y=10)
            Button(self.foot1, text="The Farmer",command=q.wrong, fg="white", cursor="hand2", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="The cow",command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Both of them",command=q.sapa,activebackground="light green", cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="None of them",command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        elif question == "Who is the creator for this game ?":
            ql15=Label(foot,text="Who is the creator for the game ?",width=35,height=3,bg="red",fg="white", font=("arial", 12, "bold"))
            ql15.place(x=0,y=10)
            Button(self.foot1, text="H-storm", command=q.wrong, fg="white", cursor="hand2", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(
                x=40, y=70)
            Button(self.foot1, text="Salam", command=q.wrong, cursor="hand2", fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=140)
            Button(self.foot1, text="Habeeb", command=q.Bola, activebackground="light green", cursor="hand2",
                   fg="white", width=20,
                   bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=210)
            Button(self.foot1, text="Hb", command=q.wrong,
                   cursor="hand2", fg="white", width=20, bg="red",
                   font=("arial", 15, "bold")).place(x=40, y=280)
            Button(foot, text="➖Back", bg="red", command=q.qbk, fg="light green", font=("elephant", 15, "bold")).place(
                x=420, y=450)
        else:
            messagebox.showerror("Error", "Something went wrong.Please try again later...")
            q.qbk()

    def sapa(self):
        messagebox.showinfo("Correct","Correct!!!")
        self.qscore.append("1")
        o.config(text=f"Score: {len(self.qscore)}")
        if len(self.qscore) == 1:
            Frame(lin1,width=40,height=25,bg="red").place(x=0,y=120)
            q.resume()
        elif len(self.qscore) == 2:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 3:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 4:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 5:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 6:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 7:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 8:
            S.config(fg="red")
            q.resume()
        elif len(self.qscore) == 9:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=120)
            q.resume()
        elif len(self.qscore) == 10:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 11:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 12:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 13:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 14:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 15:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 16:
            S2.config(fg="red")
            q.resume()
        elif len(self.qscore) == 17:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=120)
            q.resume()
        elif len(self.qscore) == 18:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 19:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 20:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 21:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 22:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 23:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 24:
            S3.config(fg="yellow")
            S.config(fg="yellow")
            S2.config(fg="yellow")
            messagebox.showinfo("You won ⭐⭐⭐","Congratulations ,You won the quiz game")
            if messagebox.askyesno("Congratulations ⭐⭐⭐", "Would you like to play the quiz game again"):
                self.qscore.clear()
                q.resume()
                o.config(text=f"Score: {len(self.qscore)}")
                q.qbk()
            else:
                pass
        elif mano:
            mano.destroy()
        else:
            messagebox.showerror("Error", "Something went wrong.Please try again later...")
            q.bk()

    def Bola(self):
        messagebox.showinfo("Correct", "Correct!!!")
        self.qscore.append("1")
        o.config(text=f"Score: {len(self.qscore)}")
        if len(self.qscore) == 1:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=120)
            q.resume()
        elif len(self.qscore) == 2:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 3:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 4:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 5:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 6:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 7:
            Frame(lin1, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 8:
            S.config(fg="red")
            q.resume()
        elif len(self.qscore) == 9:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=120)
            q.resume()
        elif len(self.qscore) == 10:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 11:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 12:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 13:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 14:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 15:
            Frame(lin2, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 16:
            S2.config(fg="red")
            q.resume()
        elif len(self.qscore) == 17:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=120)
            q.resume()
        elif len(self.qscore) == 18:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=100)
            q.resume()
        elif len(self.qscore) == 19:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=80)
            q.resume()
        elif len(self.qscore) == 20:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=60)
            q.resume()
        elif len(self.qscore) == 21:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=40)
            q.resume()
        elif len(self.qscore) == 22:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=20)
            q.resume()
        elif len(self.qscore) == 23:
            Frame(lin3, width=40, height=25, bg="red").place(x=0, y=0)
            q.resume()
        elif len(self.qscore) == 24:
            S3.config(fg="yellow")
            S.config(fg="yellow")
            S2.config(fg="yellow")
            messagebox.showinfo("You won ⭐⭐⭐", "Congratulations ,You won the quiz game")
            if messagebox.askyesno("Congratulations⭐⭐⭐", "Would you like to play the quiz game again"):
                self.qscore.clear()
                q.resume()
                o.config(text=f"Score: {len(self.qscore)}")
                q.qbk()
            else:
                pass
        elif mano:
            mano.destroy()
        else:
            messagebox.showerror("Error", "Something went wrong.Please try again later...")
            q.qbk()
    def wrong(self):
        messagebox.showinfo("Incorrect Answer!!!!!!!!","Your answer was Incorrect.....")
        o.config(text=f"Score: {len(self.qscore)}")
        q.resume()

    def qbk(self):
        foot.destroy()
        q.quiz()

m = RPC()
q=Quiz()

def esc(event):
    wn.destroy()

Label(frame,fg="light green",font=("arial black",20,"bold"),text="Games",bg="red",width=13).place(x=0,y=0)
bt=Button(frame,text="➖Rock,Paper\n,Scissors",cursor="hand2",activebackground="grey",command=m.start,bg="red",activeforeground="white",font=("elephant",15,"bold"),fg="light green")
bt.place(x=0,y=50)
bt1=Button(frame,text="➖Tic Tac Toc",command=m.opt,cursor="hand2",height=2,activebackground="grey",bg="red",activeforeground="white",font=("elephant",15,"bold"),fg="light green")
bt1.place(x=0,y=130)
bt2=Button(frame,text="➖Quiz Game",command=q.quiz,cursor="hand2",height=2,activebackground="grey",bg="red",activeforeground="white",font=("elephant",15,"bold"),fg="light green")
bt2.place(x=0,y=210)

wn.bind("<Escape>",esc)

wn.mainloop()