import random
from tkinter import messagebox

import pyttsx3
from PIL import Image
from customtkinter import *

wn= CTk()
wn.title("Chat Bot")
wn.attributes('-fullscreen', True)

r = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

d = {
        "hello":"Hi there!",
        "how are you":"i'm fine, thanks for asking",
        "good":"Okay",
        "hi":"Hello",
        "what is your name":"My name is Chat bot",
        "hey":"Whats up",
        "bye":"goodbye",
        "goodbye":"goodbye",
        "sure":"alright",
        "okay":"how was your day",
        "fine":"that's good, do you want to tell me about it",
        "no":"okay then what would you like to talk about",
        "it was fine":"okay",
        "yes": "okay",
        "how are you doing": "i will be fine if you continue chatting  with me",
        "you are mad":"no i'm not",
        "nothing":"alright",
        "what do you like to do":"i was programmed to chat and entertain you\n, so if i am to say what i like\n it will be learning from you",
        "are you stupid":"no i'm not",
        "yes you are": "no i'm not",
        "you are stupid": "no, you are stupid for assuming that",
        "how old are you": "i'm one year old",
        "good morning":"Good morning",
        "good night":"Good night",
        "yeah":"okay",
        "":"say something"
    }

def chats():
    CTkLabel(master=scroll, width=500, height=30, text=e.get(), font=("arial", 25, 'bold'), fg_color='blue',
             corner_radius=36).pack()
    if e.get().lower() in d:
        CTkButton(master=scroll,image=I,text=d[e.get()],width=500,height=30,font=("arial",25,'bold'),fg_color='purple',corner_radius=36).pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.say(d[e.get()])
        engine.runAndWait()
    else:
        CTkLabel(master=scroll, text="Sorry i don't understand how to respond this to statement\n"
                                     "Please help me learn by typing my response to your statement\n"
                                     "Now", font=("arial", 25, 'bold'), fg_color='purple',
                 corner_radius=36).pack()
        wr()

def wr():
    global eg,mg
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.say(
        "Sorry i don't understand how to respond to this statement. Please help me learn by typing my response to your statement, inside"
        "the yellow box that says help in responses")
    engine.runAndWait()
    eg = CTkEntry(master=scroll, corner_radius=36, border_color='yellow', placeholder_text='help in responses.....',
                 placeholder_text_color="white", font=('arial', 30), width=700, height=40)
    eg.pack()
    mg = CTkButton(master=scroll, text='send', command=se, corner_radius=36, fg_color='transparent', text_color='yellow',
                  width=70, cursor='hand2', font=('arial', 30, 'bold'), border_width=3, border_color='yellow')
    mg.pack()
    e.configure(state=DISABLED)
    m.configure(state=DISABLED)

def se():
    d[e.get()]=eg.get()
    r.append('2')
    t()
    eg.destroy()
    mg.destroy()
    e.configure(state=NORMAL)
    m.configure(state=NORMAL)

def t():
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Thanks for teaching me on how to respond  to this statement, I am learning well from well")
    dn=CTkButton(master=scroll, text="Thanks for teaching me on how to\n respond to this statement", font=("arial", 25, 'bold'), fg_color='purple',
             corner_radius=36)
    dn.pack()
    fm=CTkButton(master=scroll,
             text="I will learn a lot from you",
             font=("arial", 25, 'bold'), fg_color='purple',
             corner_radius=36)
    fm.pack()

def send(event=None):
    chats()

I = CTkImage(light_image=Image.open("969b91de-0c8e-4323-89f4-069d0c37946a-2.jpg")
             ,dark_image=Image.open("969b91de-0c8e-4323-89f4-069d0c37946a-2.jpg"),size=(70,70))
In = CTkImage(light_image=Image.open("969b91de-0c8e-4323-89f4-069d0c37946a-2.jpg"),dark_image=Image.open("969b91de-0c8e-4323-89f4-069d0c37946a-2.jpg"),size=(100,100))

def s():
    set_appearance_mode('dark')
    switch.configure(text='Light Mode',text_color='white',command=sw)
    e.configure(placeholder_text_color="white")
def sw():
    set_appearance_mode('light')
    switch.configure(text='Dark Mode',text_color='black',command=s)
    e.configure(placeholder_text_color="black")

def bkk():
    bf.destroy()

def talk():
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',200)
    engine.say("Hey there!, I am here to learn from you ,so please help me if i don't have responses to your statement ")
    engine.runAndWait()

def setting():
    global switch,bf,f,com
    bf = CTkFrame(master=wn,corner_radius=16,width=340,height=670)
    bf.grid(row=0,column=0,padx=20,pady=30)
    CTkLabel(master=bf,text='⚙ Setting',font=('arial',30)).place(x=30,y=10)
    switch=CTkSwitch(master=bf,text='Light Mode',text_color='white',fg_color='white',command=sw,font=('Arial',20),border_color='blue',border_width=3)
    switch.place(x=30,y=90)
    CTkButton(master=bf,text='Change text font',border_width=1,border_color='blue',command=ch.fontt,font=("arial",20,'bold'), corner_radius=36).place(x=30,y=160)
    erase = CTkButton(master=bf,font=('arial',20,'bold'),border_width=1,border_color='blue',text='Erase ChatBot memory',cursor='hand2', corner_radius=36)
    erase.place(x=30,y=230)
    CTkButton(master=bf,text='Change Font color',border_width=1,border_color='blue',command=ch.f_color,font=('arial',20,'bold'), corner_radius=36).place(x=30,y=300)
    bk = CTkButton(master=bf, command=bkk, text='Back', corner_radius=36, font=('arial', 20, 'bold'))
    bk.place(x=30, y=600)

class S_ch:
    def f_color(self):
        global fc
        fc=CTkFrame(master=wn,corner_radius=16,width=450,height=670)
        fc.grid(row=0,column=0,pady=20)
        i = IntVar()
        CTkLabel(master=fc,text="Change Font-color",font=("arial",40,'bold')).grid(row=0,column=0)
        CTkRadioButton(master=fc,text="White",command=ch.white,font=("arial",20),variable=i,value=1).grid(row=1,column=0,pady=10)
        CTkRadioButton(master=fc, text="Blue",command=ch.blue, font=("arial", 20),variable=i,value=2).grid(row=2, column=0, pady=10)
        CTkRadioButton(master=fc, text="Yellow",command=ch.yellow, font=("arial", 20),variable=i,value=3).grid(row=3, column=0, pady=10)
        CTkRadioButton(master=fc, text="Black",command=ch.black, font=("arial", 20), variable=i, value=4).grid(row=4, column=0,pady=10)
        CTkRadioButton(master=fc, text="Green",command=ch.green, font=("arial", 20), variable=i, value=5).grid(row=5, column=0,pady=10)
        CTkRadioButton(master=fc, text="Red",command=ch.red, font=("arial", 20), variable=i, value=6).grid(row=6, column=0,pady=10)
        CTkRadioButton(master=fc, text="Pink",command=ch.pink, font=("arial", 20), variable=i, value=7).grid(row=7, column=0,pady=10)
        CTkRadioButton(master=fc, text="Purple",command=ch.purple, font=("arial", 20), variable=i, value=8).grid(row=8, column=0,pady=10)
        CTkRadioButton(master=fc, text="Grey",command=ch.grey, font=("arial", 20), variable=i, value=9).grid(row=9, column=0,pady=10)
        CTkRadioButton(master=fc, text="Brown",command=ch.brown, font=("arial", 20), variable=i, value=10).grid(row=10, column=0,pady=10)
        CTkRadioButton(master=fc, text="Light Blue",command=ch.light_blue, font=("arial", 20), variable=i, value=11).grid(row=11, column=0,pady=10)
        CTkRadioButton(master=fc, text="Light Green",command=ch.light_green, font=("arial", 20), variable=i, value=12).grid(row=12, column=0,pady=10)
        CTkRadioButton(master=fc, text="Sky blue",command=ch.sky_blue, font=("arial", 20), variable=i, value=13).grid(row=13, column=0,pady=10)
        CTkButton(master=fc,command=ch.fbkk,text='Back',border_color='blue',cursor='hand2',corner_radius=36,border_width=1,font=('arial',20)).grid(row=14, column=0,padx=10,pady=10)

    def fbkk(self):
        fc.destroy()

    def blue(self):
        e.configure(placeholder_text_color='blue',text_color='blue')

    def white(self):
        e.configure(placeholder_text_color='white',text_color='white')

    def yellow(self):
        e.configure(placeholder_text_color='yellow',text_color='yellow')

    def green(self):
        e.configure(placeholder_text_color='green', text_color='green')

    def black(self):
        e.configure(placeholder_text_color='black', text_color='black')

    def red(self):
        e.configure(placeholder_text_color='red', text_color='red')

    def pink(self):
        e.configure(placeholder_text_color='pink', text_color='pink')

    def purple(self):
        e.configure(placeholder_text_color='purple', text_color='purple')

    def grey(self):
        e.configure(placeholder_text_color='grey', text_color='grey')

    def brown(self):
        e.configure(placeholder_text_color='brown', text_color='brown')

    def light_blue(self):
        e.configure(placeholder_text_color='light blue', text_color='light blue')

    def light_green(self):
        e.configure(placeholder_text_color='light green', text_color='light green')

    def sky_blue(self):
        e.configure(placeholder_text_color='sky blue', text_color='sky blue')

    def fontt(self):
        global ftt
        ftt = CTkFrame(master=wn, corner_radius=16, width=450, height=670)
        ftt.grid(row=0, column=0, pady=20)
        ii = IntVar()
        CTkLabel(master=ftt,text='Change font text',font=("arial",40,'bold')).grid(row=0,column=0)
        CTkRadioButton(master=ftt,command=ch.arial,text='Arial',value=1,variable=ii,font=('arial',20)).grid(row=1,column=0,pady=10)
        CTkRadioButton(master=ftt,command=ch.arial_black,text='Arial black', value=2, variable=ii, font=('arial', 20)).grid(row=2, column=0,pady=10)
        CTkRadioButton(master=ftt,command=ch.alg, text='Algerian', value=3, variable=ii, font=('arial', 20)).grid(row=3, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Bauhaus 93',command=ch.b3, value=4, variable=ii, font=('arial', 20)).grid(row=4, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Britannic Bold',command=ch.b, value=5, variable=ii, font=('arial', 20)).grid(row=5, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Calibri',command=ch.ca, value=6, variable=ii, font=('arial', 20)).grid(row=6, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Cooper Black',command=ch.ca, value=7, variable=ii, font=('arial', 20)).grid(row=7, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Elephant',command=ch.e, value=8, variable=ii, font=('arial', 20)).grid(row=8, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Impact',command=ch.im, value=9, variable=ii, font=('arial', 20)).grid(row=9, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Lucida Console',command=ch.lu, value=10, variable=ii, font=('arial', 20)).grid(row=10, column=0,pady=10)
        CTkRadioButton(master=ftt, text='Stencil',command=ch.sc, value=11, variable=ii, font=('arial', 20)).grid(row=11,column=0,pady=10)
        CTkRadioButton(master=ftt, text='Wide Latin',command=ch.wi, value=12, variable=ii, font=('arial', 20)).grid(row=12, column=0, pady=10)
        CTkRadioButton(master=ftt, text='Yu Gothic',command=ch.yo, value=13, variable=ii, font=('arial', 20)).grid(row=13, column=0, pady=10)
        CTkButton(master=ftt,command=ch.bbb, text='Back',fg_color='blue',corner_radius=36, font=('arial', 20)).grid(row=14, column=0, pady=10)

    def bbb(self):
        ftt.destroy()

    def arial(self):
        e.configure(font=("arial",30))

    def arial_black(self):
        e.configure(font=('arial black',30))

    def alg(self):
        e.configure(font=('Algerian',30))

    def b(self):
        e.configure(font=('Britannic Bold',30))

    def b3(self):
        e.configure(font=('Bauhaus 93',30))

    def ca(self):
        e.configure(font=('Calibri',30))

    def ca2(self):
        e.configure(font=('Cooper Black',30))

    def e(self):
        e.configure(font=('Elephant',30))

    def im(self):
        e.configure(font=('Impact',30))

    def lu(self):
        e.configure(font=('Lucida Console',30))

    def yo(self):
        e.configure(font=('Yu Gothic',30))

    def sc(self):
        e.configure(font=('Stencil',30))

    def wi(self):
        e.configure(font=('Wide Latin',30))

    def eraser(self):
        pass

ch = S_ch()

def bgk():
    fg.destroy()

def game():
    global fg
    fg = CTkFrame(master=wn,corner_radius=16,width=340,height=670)
    fg.grid(row=0,column=0,padx=20,pady=30)
    gl=CTkLabel(master=fg,cursor='hand2',text='Games with ChatBot ',font=('arial',30,'bold'))
    gl.grid(row=0,column=0,padx=20,pady=20)
    g1 = CTkButton(master=fg,cursor='hand2',command=g.rpc,border_color='blue',border_width=2,text='Rock,Paper,\nScissors',font=('arial',30,'bold'),corner_radius=36)
    g1.grid(row=1,column=0,padx=20,pady=20)
    g2 = CTkButton(master=fg,text='Riddle game',command=gg.riddle,border_color='blue',border_width=2,cursor='hand2', font=('arial', 30, 'bold'), corner_radius=36)
    g2.grid(row=2,column=0,padx=20,pady=20)
    g3 = CTkButton(master=fg, text='Tic Tac Toc',command=T.start,border_color='blue',border_width=2,cursor='hand2', font=('arial', 30, 'bold'),corner_radius=36)
    g3.grid(row=3,column=0,padx=20,pady=20)
    g4 = CTkButton(master=fg,text='Number guessing',border_color='blue',border_width=2,cursor='hand2', font=('arial', 30, 'bold'),corner_radius=36)
    g4.grid(row=4,column=0,padx=20,pady=20)
    g5 = CTkButton(master=fg,text='Ludo Game',border_color='blue',border_width=2,cursor='hand2', font=('arial', 30, 'bold'),corner_radius=36)
    g5.grid(row=5,column=0,padx=20,pady=20)
    # g6 = CTkButton(master=fg,text='Ludo Game',border_color='blue',border_width=2,cursor='hand2', font=('arial', 30, 'bold'),corner_radius=36)
    # g6.grid(row=6,column=0,padx=20,pady=20)
    g7 = CTkButton(master=fg, text='Back',cursor='hand2',fg_color='blue',command=bgk, font=('arial', 30, 'bold'), corner_radius=36,border_color='white',border_width=2)
    g7.grid(row=7,column=0,padx=20,pady=60)


class Game:
    def __init__(self):
        self.ys =[]
        self.ais = []

    def rpc(self):
        global ys,ais,yfr,cfr
        self.f = CTkFrame(master=wn, corner_radius=16, width=975, height=700, border_color='blue', border_width=2)
        self.f.grid(row=0, column=2, padx=0, pady=30)
        self.f2 = CTkFrame(master=wn,corner_radius=16,width=340,height=670,border_color='blue',border_width=2)
        self.f2.grid(row=0,column=0,padx=20,pady=30)
        CTkLabel(master=self.f2,text='Score Board',font=('arial',30,'bold')).place(x=10,y=10)
        self.fr = CTkFrame(master=self.f2,width=250,height=500,border_width=2,border_color='blue',corner_radius=36)
        self.fr.place(x=20,y=50)
        CTkLabel(master=self.fr,text='',image=I).place(x=10,y=15)
        CTkLabel(master=self.fr, text='You',font=('arial',50,'bold')).place(x=150, y=20)
        ys = CTkLabel(master=self.fr,text=f"{len(self.ys)}",font=('arial',20,'bold'))
        ys.place(x=200,y=100)
        ais = CTkLabel(master=self.fr,text=f"{len(self.ais)}",font=('arial',20,'bold'))
        ais.place(x=30,y=100)
        cfr = CTkFrame(master=self.fr,border_width=2,border_color="blue",fg_color='transparent',width=35,height=330,corner_radius=36)
        cfr.place(x=22,y=130)
        yfr = CTkFrame(master=self.fr, border_width=2, border_color="blue", fg_color='transparent', width=35, height=330,corner_radius=36)
        yfr.place(x=192,y=130)
        CTkButton(master=self.f2,text='Back',fg_color='blue',command=g.rbk,border_width=2,border_color='white',font=("arial",30,'bold'),corner_radius=36).place(x=20,y=600)
        CTkLabel(master=self.f,text='Rock,Paper, Scissor',font=('arial',30,'bold')).place(x=370,y=10)
        self.ff1 = CTkFrame(master=self.f,width=800,height=300,border_color='blue',border_width=2,corner_radius=36)
        self.ff1.place(x=90,y=70)
        self.fff= CTkLabel(master=self.f,text='',font=('arial',30,'bold'))
        self.fff.place(x=400,y=400)
        CTkButton(master=self.ff1, text='Reset', fg_color='blue', command=g.r, border_width=2, border_color='white',height=70,
                  font=("arial", 30, 'bold'), corner_radius=36).place(x=320, y=210)
        ai = CTkLabel(master=self.ff1,image=In,text='')
        ai.place(x=40,y=5)
        self.aim = CTkLabel(master=self.ff1,text='',font=('arial',50,'bold'))
        self.aim.place(x=40,y=130)
        Y = CTkLabel(master=self.ff1,text='You',font=('arial',50,'bold'))
        Y.place(x=600,y=5)
        self.em= CTkLabel(master=self.ff1,text='',font=('arial',50,'bold'))
        self.em.place(x=600,y=130)
        rock=CTkButton(master=self.f,text='Rock👊🏿👊🏿',command=g.rocky,font=('arial',30,'bold'),width=290,border_color='white',height=70,corner_radius=36,border_width=2,fg_color='blue',cursor='hand2')
        rock.place(x=50,y=530)
        pap = CTkButton(master=self.f, text='Paper📰📰',command=g.papy, font=('arial', 30, 'bold'), width=290, border_color='white',height=70, corner_radius=36, border_width=2, fg_color='blue', cursor='hand2')
        pap.place(x=350, y=530)
        scis = CTkButton(master=self.f, text='Scissors✂️',command=g.scicy, font=('arial', 30, 'bold'), width=250, border_color='white',
                         height=70, corner_radius=36, border_width=2, fg_color='blue', cursor='hand2')
        scis.place(x=650, y=530)

    def rbk(self):
        self.f2.destroy()
        self.f.destroy()
        self.ys.clear()
        self.ais.clear()

    def r(self):
        self.aim.configure(text='')
        self.em.configure(text='')
        self.fff.configure(text='')
    def rocky(self):
        self.em.configure(text='Rock\n👊🏿👊🏿')
        gam = ["rock","scissor","paper"]
        games = random.choice(gam)
        if games == "rock":
            self.aim.configure(text='Rock\n👊🏿👊🏿')
            self.fff.configure(text='No winner')
        elif games == "scissor":
            self.aim.configure(text="Scissor\n✂️")
            self.fff.configure(text='You won')
            self.ys.append('1')
            ys.configure(text=len(self.ys))
            if len(self.ys) == 1:
                CTkLabel(master=yfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ys) == 2:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ys) == 3:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ys) == 4:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ys) == 5:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ys) == 6:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ys) == 7:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ys) == 8:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ys) == 9:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ys) == 10:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ys) == 11:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ys) == 12:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ys) == 13:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ys) == 14:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ys) == 15:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ys) == 16:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ys) == 17:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You won the game','Congratulations ,You won the game')
                g.rbk()
        elif games == "paper":
            self.aim.configure(text='Paper\n📰📰')
            self.fff.configure(text='You lose')
            self.ais.append('1')
            ais.configure(text=len(self.ais))
            if len(self.ais) == 1:
                CTkLabel(master=cfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ais) == 2:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ais) == 3:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ais) == 4:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ais) == 5:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ais) == 6:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ais) == 7:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ais) == 8:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ais) == 9:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ais) == 10:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ais) == 11:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ais) == 12:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ais) == 13:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ais) == 14:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ais) == 15:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ais) == 16:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ais) == 17:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You lose the game','Sorry, You lose the game to the chatbox')
                g.rbk()
        else:
            self.aim.configure(text='Rock\n👊🏿👊🏿')
            self.fff.configure(text='No winner')

    def papy(self):
        self.em.configure(text='Paper\n📰📰')
        gam = ["rock","paper","scissor"]
        games = random.choice(gam)
        if games == "rock":
            self.aim.configure(text='Rock\n👊🏿👊🏿')
            self.fff.configure(text='You won')
            self.ys.append('1')
            ys.configure(text=len(self.ys))
            if len(self.ys) == 1:
                CTkLabel(master=yfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ys) == 2:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ys) == 3:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ys) == 4:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ys) == 5:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ys) == 6:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ys) == 7:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ys) == 8:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ys) == 9:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ys) == 10:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ys) == 11:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ys) == 12:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ys) == 13:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ys) == 14:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ys) == 15:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ys) == 16:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ys) == 17:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You won the game','Congratulations ,You won the game')
                g.rbk()

        elif games == "paper":
            self.aim.configure(text='Paper\n📰📰')
            self.fff.configure(text='No winner')
        elif games == "scissor":
            self.aim.configure(text='Scissor\n✂️')
            self.ais.append('1')
            self.fff.configure(text='You lose')
            ais.configure(text=len(self.ais))
            if len(self.ais) == 1:
                CTkLabel(master=cfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ais) == 2:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ais) == 3:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ais) == 4:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ais) == 5:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ais) == 6:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ais) == 7:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ais) == 8:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ais) == 9:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ais) == 10:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ais) == 11:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ais) == 12:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ais) == 13:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ais) == 14:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ais) == 15:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ais) == 16:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ais) == 17:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You lose the game','Sorry ,you lost the game to the chatbot ')
                g.rbk()

        else:
            self.aim.configure(text='Paper\n📰📰')
            self.fff.configure(text='No winner')

    def scicy(self):
        self.em.configure(text='Scissor\n✂️')
        gam = ["rock","paper","scissor"]
        games = random.choice(gam)
        if games == "rock":
            self.aim.configure(text="Rock\n👊🏿👊🏿")
            self.fff.configure(text='You lose')
            self.ais.append('1')
            ais.configure(text=len(self.ais))
            if len(self.ais) == 1:
                CTkLabel(master=cfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ais) == 2:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ais) == 3:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ais) == 4:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ais) == 5:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ais) == 6:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ais) == 7:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ais) == 8:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ais) == 9:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ais) == 10:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ais) == 11:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ais) == 12:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ais) == 13:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ais) == 14:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ais) == 15:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ais) == 16:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ais) == 17:
                CTkLabel(master=cfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You lose the game','Sorry,You lost the game to the chatbot')
                g.rbk()
        elif games == "paper":
            self.aim.configure(text="Paper\n📰📰")
            self.fff.configure(text='You won')
            self.ys.append('1')
            ys.configure(text=len(self.ys))
            if len(self.ys) == 1:
                CTkLabel(master=yfr,text='',fg_color='white',width=30,height=2,corner_radius=36).place(x=3,y=310)
            elif len(self.ys) == 2:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=290)
            elif len(self.ys) == 3:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=270)
            elif len(self.ys) == 4:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=250)
            elif len(self.ys) == 5:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=230)
            elif len(self.ys) == 6:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=210)
            elif len(self.ys) == 7:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=190)
            elif len(self.ys) == 8:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=170)
            elif len(self.ys) == 9:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=150)
            elif len(self.ys) == 10:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=130)
            elif len(self.ys) == 11:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=110)
            elif len(self.ys) == 12:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=90)
            elif len(self.ys) == 13:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=70)
            elif len(self.ys) == 14:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=50)
            elif len(self.ys) == 15:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=30)
            elif len(self.ys) == 16:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=10)
            elif len(self.ys) == 17:
                CTkLabel(master=yfr, text='', fg_color='white', width=30, height=2, corner_radius=36).place(x=3, y=-10)
                messagebox.showinfo('You won the game','Congratulations, you won?')
                g.rbk()
        elif games == "scissor":
            self.aim.configure(text="Scissor\n✂️")
            self.fff.configure(text='No winner')
        else:
            self.aim.configure(text="Scissor\n✂️")
            self.fff.configure(text='No winner')

g = Game()

class Game2:
    def riddle(self):
        self.y =[]
        self.g = CTkFrame(master=wn, corner_radius=16, width=975, height=700, border_color='blue', border_width=2)
        self.g.grid(row=0, column=2, padx=0, pady=30)
        self.ge = CTkFrame(master=wn, corner_radius=16, width=340, height=670, border_color='blue', border_width=2)
        self.ge.grid(row=0, column=0, padx=20, pady=30)
        self.scor=CTkLabel(master=self.ge,text=f'Score: {len(self.y)}',font=('arial',40,'bold'))
        self.scor.place(x=20,y=20)
        self.fr = CTkFrame(master=self.ge, border_width=2, border_color="blue", fg_color='transparent', width=35,
                       height=330, corner_radius=36)
        self.fr.place(x=22, y=170)
        self.fr2 = CTkFrame(master=self.ge, border_width=2, border_color="blue", fg_color='transparent', width=35,
                       height=330, corner_radius=36)
        self.fr2.place(x=150, y=170)
        self.fr3 = CTkFrame(master=self.ge, border_width=2, border_color="blue", fg_color='transparent', width=35,
                      height=330, corner_radius=36)
        self.fr3.place(x=270, y=170)
        self.ff1 = CTkFrame(master=self.g, width=800, height=300, border_color='blue', border_width=2, corner_radius=36)
        self.ff1.place(x=90, y=70)
        CTkButton(master=self.ge, text='Back',cursor='hand2', fg_color='blue', command=gg.rbk, border_width=2, border_color='white',
                  font=("arial", 30, 'bold'), corner_radius=36).place(x=20, y=600)
        self.l = CTkLabel(master=self.ff1, text='', width=30, height=2, corner_radius=36,font=("arial",30,'bold'))
        self.l.place(x=100, y=30)
        self.b = CTkButton(master=self.g,text="",cursor='hand2',font=("arial",30,'bold'),height=70,width=350,fg_color='blue',border_width=2,corner_radius=36,border_color='white')
        self.b.place(x=70,y=450)
        self.b2 = CTkButton(master=self.g, text="",cursor='hand2', font=("arial", 30, 'bold'), height=70, width=350, fg_color='blue',
                           border_width=2, corner_radius=36, border_color='white')
        self.b2.place(x=500, y=450)
        self.b3 = CTkButton(master=self.g, text="",cursor='hand2', font=("arial", 30, 'bold'), height=70, width=350, fg_color='blue',
                           border_width=2, corner_radius=36, border_color='white')
        self.b3.place(x=70, y=550)
        self.b4 = CTkButton(master=self.g, text="",cursor='hand2', font=("arial", 30, 'bold'), height=70, width=350, fg_color='blue',
                            border_width=2, corner_radius=36, border_color='white')
        self.b4.place(x=500, y=550)
        CTkLabel(master=self.g, text='Riddle Game', font=('arial', 30, 'bold')).place(x=370, y=10)
        gg.question()

    def rbk(self):
        self.g.destroy()
        self.ge.destroy()

    def question(self):
        que = [
            "I am something, I kiss my mother before I die.What am I ?",
            "A fiance name for an hair dresser is it ?",
            "The word M.O.M is also known to be ?",
            "I am something, People hate me but their clap for me. What am I ?",
            "I am something, Wherever the wind blows ,I flow. What am I ?",
            "a","b","c","d","e","f","g","h","i","j","k","l"
            ,"r","s","t","u","v","w","x","y","z"
        ]
        question = random.choice(que)
        if question == "I am something, I kiss my mother before I die.What am I ?":
            self.l.configure(text='I am something, I kiss my mother before \nI die.What am I ?')
            self.b.configure(text='Brush',command=gg.wrong)
            self.b2.configure(text='Match stick',command=gg.answer)
            self.b3.configure(text='Match box',command=gg.wrong)
            self.b4.configure(text='Polish',command=gg.wrong)
        elif question == "A fiance name for an hair dresser is it ?":
            self.l.configure(text='A fiance name for an hair dresser is it ?')
            self.b.configure(text='Tailor',command=gg.wrong)
            self.b2.configure(text='Block Layer',command=gg.wrong)
            self.b3.configure(text='Hair Stylist',command=gg.answer)
            self.b4.configure(text='All of the them',command=gg.wrong)
        elif question == "The word M.O.M is also known to be ?":
            self.l.configure(text='The word M.O.M is also known to be ?')
            self.b.configure(text='My own mom',command=gg.wrong)
            self.b4.configure(text='Made of money',command=gg.answer)
            self.b2.configure(text='Milk or malt',command=gg.wrong)
            self.b3.configure(text='M.O.M',command=gg.wrong)
        elif question == "I am something, People hate me but their clap for me. What am I ?":
            self.l.configure(text='I am something, People hate me but their\n clap for me. What am I ?')
            self.b.configure(text='Rat',command=gg.wrong)
            self.b2.configure(text='Mosquito',command=gg.answer)
            self.b3.configure(text='Mot',command=gg.wrong)
            self.b4.configure(text='Bug',command=gg.wrong)
        elif question == "I am something, Wherever the wind blows ,I flow. What am I ?":
            self.l.configure(text='I am something, Wherever the wind blows\n ,I flow. What am I ?')
            self.b.configure(text='Wind',command=gg.wrong)
            self.b2.configure(text='Water',command=gg.wrong)
            self.b3.configure(text='Grass',command=gg.answer)
            self.b4.configure(text='Gun',command=gg.wrong)
        elif question == "a":
            self.l.configure(text="I am something, If you cut me ,you will\nI will make you cry. What am I ?")
            self.b.configure(text="Apple",command=gg.wrong)
            self.b2.configure(text='Cane',command=gg.wrong)
            self.b3.configure(text='Onion',command=gg.answer)
            self.b4.configure(text='Pepper',command=gg.wrong)
        elif question == "b":
            self.l.configure(text="I am something, You will like my first name\nbut will hate my second name. What am I ? ")
            self.b.configure(text="Water-Melon",command=gg.wrong)
            self.b2.configure(text='Salt-Pepper',command=gg.wrong)
            self.b3.configure(text='Sugar-Cane',command=gg.answer)
            self.b4.configure(text='Pepper-Soup',command=gg.wrong)
        elif question == "c":
            self.l.configure(text="What has keys but can't open locks ")
            self.b.configure(text="Piano",command=gg.answer)
            self.b2.configure(text='Key',command=gg.wrong)
            self.b3.configure(text='Music keys',command=gg.wrong)
            self.b4.configure(text='Padlock',command=gg.wrong)
        elif question == "d":
            self.l.configure(text="What has a head and a tail but no body")
            self.b.configure(text="Pen",command=gg.wrong)
            self.b2.configure(text='Coin',command=gg.answer)
            self.b3.configure(text='Pencil',command=gg.wrong)
            self.b4.configure(text='Box',command=gg.wrong)
        elif question == "e":
            self.l.configure(text="I am something, I can never be used unless\nI am broken. What am I ?")
            self.b.configure(text="Glass",command=gg.wrong)
            self.b2.configure(text='Box',command=gg.wrong)
            self.b3.configure(text='Screen',command=gg.wrong)
            self.b4.configure(text='Egg',command=gg.answer)
        elif question == "f":
            self.l.configure(text="I am something, You can catch me but can't\nthrow me away. What am I ?")
            self.b.configure(text="Disc",command=gg.wrong)
            self.b2.configure(text='Water',command=gg.wrong)
            self.b3.configure(text='Cold',command=gg.answer)
            self.b4.configure(text='Mosquito',command=gg.wrong)
        elif question == "g":
            self.l.configure(text="What part of the room do we mainly think alot?")
            self.b.configure(text="Room",command=gg.wrong)
            self.b2.configure(text='Class-room',command=gg.wrong)
            self.b3.configure(text='All of them',command=gg.wrong)
            self.b4.configure(text='Toilet',command=gg.answer)
        elif question == "h":
            self.l.configure(text="A School is a place to ?")
            self.b.configure(text="Think",command=gg.wrong)
            self.b2.configure(text='Learn',command=gg.wrong)
            self.b3.configure(text='Make friends',command=gg.wrong)
            self.b4.configure(text='All of them',command=gg.answer)
        elif question == "i":
            self.l.configure(text="I am something. I can be broke but can never\nbe regain. What am I ?")
            self.b.configure(text="All of them",command=gg.wrong)
            self.b2.configure(text='Hand',command=gg.wrong)
            self.b3.configure(text='Glass',command=gg.wrong)
            self.b4.configure(text='Trust',command=gg.answer)
        elif question == "j":
            self.l.configure(text="What has a foot on each side but no legs")
            self.b.configure(text="Ruler",command=gg.answer)
            self.b2.configure(text='Bottle-cover',command=gg.wrong)
            self.b3.configure(text='Pen',command=gg.wrong)
            self.b4.configure(text='Eraser',command=gg.wrong)
        elif question == "k":
            self.l.configure(text="If a boy can be called 'Bro'.\n What can a girl be called ?")
            self.b.configure(text="Bro",command=gg.wrong)
            self.b2.configure(text='Guy',command=gg.wrong)
            self.b3.configure(text='Girl',command=gg.wrong)
            self.b4.configure(text='None of them',command=gg.answer)
        elif question == "r":
            self.l.configure(text="What can go and down but can't move ?")
            self.b.configure(text="None of them",command=gg.wrong)
            self.b2.configure(text='Stairs',command=gg.answer)
            self.b3.configure(text='Car',command=gg.wrong)
            self.b4.configure(text='Electricity',command=gg.wrong)
        elif question == "s":
            self.l.configure(text="I am something. You have to turn my head before\nI can work. What am I ?")
            self.b.configure(text="Tap",command=gg.answer)
            self.b2.configure(text='Pot',command=gg.wrong)
            self.b3.configure(text='Bottle',command=gg.wrong)
            self.b4.configure(text='Cover',command=gg.wrong)
        elif question == "t":
            self.l.configure(text="I am something. I have black and\nwhite written all over me. What am I ?")
            self.b.configure(text="Newspaper",command=gg.answer)
            self.b2.configure(text='Story book',command=gg.wrong)
            self.b3.configure(text='Book',command=gg.wrong)
            self.b4.configure(text='Note',command=gg.wrong)
        elif question == "u":
            self.l.configure(text="I am something. I can be measured but\ncan't be seen. What am I ?")
            self.b.configure(text="All of them",command=gg.wrong)
            self.b2.configure(text='Water',command=gg.wrong)
            self.b3.configure(text='Circle',command=gg.wrong)
            self.b4.configure(text='Time',command=gg.answer)
        elif question == "v":
            self.l.configure(text="I am something. I have three brother but\nwe have never met. What am I?")
            self.b.configure(text="None of them",command=gg.wrong)
            self.b2.configure(text='Clock',command=gg.wrong)
            self.b3.configure(text='Three magnet',command=gg.wrong)
            self.b4.configure(text='Ceiling Fan',command=gg.answer)
        elif question == "w":
            self.l.configure(text="I am something. I have a neck but no\nhead. What am I ?")
            self.b.configure(text="Cup",command=gg.wrong)
            self.b2.configure(text='Spoon',command=gg.wrong)
            self.b3.configure(text='kettle',command=gg.wrong)
            self.b4.configure(text='Bottle',command=gg.answer)
        elif question == "x":
            self.l.configure(text="I am something. I can only increase and\n never decrease. What am I ?")
            self.b.configure(text="Wifi",command=gg.wrong)
            self.b2.configure(text='Age',command=gg.answer)
            self.b3.configure(text='Data',command=gg.wrong)
            self.b4.configure(text='Electricity',command=gg.wrong)
        elif question == "y":
            self.l.configure(text="What is already come back but never return")
            self.b.configure(text="Peace",command=gg.wrong)
            self.b2.configure(text='Plane',command=gg.wrong)
            self.b3.configure(text='Tomorrow',command=gg.answer)
            self.b4.configure(text='Car',command=gg.wrong)
        elif question == "z":
            self.l.configure(text="I am something. I have a mouth both\nI can't eat. What am I ?")
            self.b.configure(text="River",command=gg.answer)
            self.b2.configure(text='Cow',command=gg.wrong)
            self.b3.configure(text='Rat',command=gg.wrong)
            self.b4.configure(text='Stream',command=gg.wrong)
        # else:
        #     messagebox.showerror("Error","Something went wrong")
        #     gg.rbk()

    def answer(self):
        global c1,c2,c3,s1,s2,s3
        self.y.append("1")
        messagebox.showinfo("Correct","Correct answer!!!!")
        self.scor.configure(text=f"Score: {len(self.y)}")
        gg.question()
        if len(self.y) == 1:
            c1 = CTkLabel(master=self.fr, text='', fg_color='white', width=25, height=2, corner_radius=10)
            c1.place(x=5, y=310)
        elif len(self.y) == 2:
            c1.configure(height=30)
            c1.place(x=5, y=295)
        elif len(self.y) == 3:
            c1.configure(height=48)
            c1.place(x=5, y=278)
        elif len(self.y) == 4:
            c1.configure(height=66)
            c1.place(x=5, y=260)
        elif len(self.y) == 5:
            c1.configure(height=80)
            c1.place(x=5, y=246)
        elif len(self.y) == 6:
            c1.configure(height=108)
            c1.place(x=5, y=215)
        elif len(self.y) == 7:
           c1.configure(height=144)
           c1.place(x=5, y=180)
        elif len(self.y) == 8:
            c1.configure(height=174)
            c1.place(x=5, y=150)
        elif len(self.y) == 9:
           c1.configure(height=194)
           c1.place(x=5, y=129)
        elif len(self.y) == 10:
            c1.configure(height=214)
            c1.place(x=5, y=110)
        elif len(self.y) == 11:
            c1.configure(height=310)
            c1.place(x=5, y=13)
        elif len(self.y) == 12:
            s1 = CTkLabel(master=self.ge, text='⭐', text_color='yellow', fg_color='transparent', font=("arial", 45))
            s1.place(x=15, y=100)
        elif len(self.y) == 13:
            c2 = CTkLabel(master=self.fr2, text='', fg_color='white', width=25, height=2, corner_radius=10)
            c2.place(x=5, y=310)
        elif len(self.y) == 14:
            c2.configure(height=30)
            c2.place(x=5, y=295)
        elif len(self.y) == 15:
            c2.configure(height=48)
            c2.place(x=5, y=278)
        elif len(self.y) == 16:
            c2.configure(height=66)
            c2.place(x=5, y=260)
        elif len(self.y) == 17:
            c2.configure(height=80)
            c2.place(x=5, y=246)
        elif len(self.y) == 18:
            c2.configure(height=108)
            c2.place(x=5, y=215)
        elif len(self.y) == 19:
            c2.configure(height=144)
            c2.place(x=5, y=180)
        elif len(self.y) == 20:
            c2.configure(height=174)
            c2.place(x=5, y=150)
        elif len(self.y) == 21:
            c2.configure(height=194)
            c2.place(x=5, y=129)
        elif len(self.y) == 22:
            c2.configure(height=214)
            c2.place(x=5, y=110)
        elif len(self.y) == 23:
            c2.configure(height=310)
            c2.place(x=5, y=13)
        elif len(self.y) == 24:
            s2 = CTkLabel(master=self.ge, text='⭐', text_color='yellow', fg_color='transparent', font=("arial", 45))
            s2.place(x=140, y=100)
        elif len(self.y) == 25:
            c3 = CTkLabel(master=self.fr3, text='', fg_color='white', width=25, height=2, corner_radius=10)
            c3.place(x=5, y=310)
        elif len(self.y) == 26:
            c3.configure(height=30)
            c3.place(x=5, y=295)
        elif len(self.y) == 27:
            c3.configure(height=48)
            c3.place(x=5, y=278)
        elif len(self.y) == 28:
            c3.configure(height=66)
            c3.place(x=5, y=260)
        elif len(self.y) == 29:
            c3.configure(height=80)
            c3.place(x=5, y=246)
        elif len(self.y) == 30:
            c3.configure(height=108)
            c3.place(x=5, y=215)
        elif len(self.y) == 31:
            c3.configure(height=144)
            c3.place(x=5, y=180)
        elif len(self.y) == 32:
            c3.configure(height=174)
            c3.place(x=5, y=150)
        elif len(self.y) == 33:
            c3.configure(height=194)
            c3.place(x=5, y=129)
        elif len(self.y) == 34:
            c3.configure(height=214)
            c3.place(x=5, y=110)
        elif len(self.y) == 35:
            c3.configure(height=310)
            c3.place(x=5, y=13)
        elif len(self.y) == 36:
            s3 = CTkLabel(master=self.ge, text='⭐', text_color='yellow', fg_color='transparent', font=("arial", 45))
            s3.place(x=250, y=100)
            if messagebox.askyesno("CONGRATULATIONS!!!!!","You won the riddle game\nDo you would to play again"):
                gg.rbk()
            else:
                pass

    def wrong(self):
        messagebox.showinfo("Incorrect!!!!", "Incorrect answer!!!!.\n For any incorrect answer ,you would have to play again.")
        self.y.clear()
        self.scor.configure(text=f"Score: {len(self.y)}")
        if c1:
            c1.destroy()
            if len(self.y)== 12:
                s1.destroy()
        elif c2:
            c1.destroy()
            c2.destroy()
            if len(self.y)==24:
                s1.destroy()
                s2.destroy()
        elif c3:
            c1.destroy()
            c2.destroy()
            c3.destroy()
            if len(self.y)==36:
                s1.destroy()
                s2.destroy()
                s3.destroy()
        else:
            pass

gg=Game2()

class TTT:
    def __init__(self):
        pass
    def start(self):
        self.g = CTkFrame(master=wn, corner_radius=16, width=975, height=700, border_color='blue', border_width=2)
        self.g.grid(row=0, column=2, padx=0, pady=30)
        self.ge = CTkFrame(master=wn, corner_radius=16, width=340, height=670, border_color='blue', border_width=2)
        self.ge.grid(row=0, column=0, padx=20, pady=30)

T= TTT()

def hep():
    global hp
    hp = CTkFrame(master=wn,corner_radius=16,width=340,height=670)
    hp.grid(row=0,column=0,padx=20,pady=20)
    CTkLabel(master=hp,text='Help',font=('arial',35,'bold')).place(x=30,y=0)
    info=CTkButton(master=hp,text='Chat box Info',command=about,font=('arial',30,'bold'),border_width=2,cursor='hand2',corner_radius=36,fg_color='blue')
    info.place(x=30,y=80)
    bout = CTkButton(master=hp, text='About',command=about1,font=('arial', 30, 'bold'), border_width=2, cursor='hand2',
                     corner_radius=36, fg_color='blue')
    bout.place(x=30,y=160)
    hb=CTkButton(master=hp,text='Back',command=help_back,font=('arial',30,'bold'),border_width=2,cursor='hand2',corner_radius=36,fg_color='blue')
    hb.place(x=30,y=240)
    CTkLabel(master=hp,image=I,text='',font=("arial",50)).place(x=250,y=0)

def help_back():
    hp.destroy()

def start_chat():
    CTkButton(master=scroll, width=500, height=30, text="hey",image=I, font=("arial", 25, 'bold'), fg_color='purple',
             corner_radius=36).pack()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 120)
    engine.say('hey')
    engine.runAndWait()

def about():
    global abot
    abot = CTkFrame(master=wn,corner_radius=16,width=340,height=670)
    abot.grid(row=0,column=0,padx=20,pady=20)
    CTkLabel(master=abot,text='ChatBox Info',font=('arial',25,'bold')).place(x=30,y=0)
    hs = CTkFrame(master=abot,width=250,height=500,corner_radius=16)
    hs.place(x=10,y=50)
    CTkLabel(master=hs,image=I,text='').grid(row=0,column=0,padx=10,pady=10)
    CTkLabel(master=hs,text="Chat Bot\n"
                            "is a basic application, created\n"
                            "to learn from you ,if it doesn't\n"
                            "know how to reply you statements\n"
                            ",it will ask you for the response\n"
                            "statement it's ment to respond on.\n"
                            "\nThis ChatBot app has a gaming\nfeature,"
                            "It has different selection of\ngame you"
                            "and the chatbox is built to play\ngames with you.\n"
                            "\n If the ChatBot ask a response on your,\n"
                            "statement from you,\n"
                            "it means that the ChatBot want to\n learn the correct"
                            "response statement to use\n in replying you\n"
                            "\nAnd also if the chatbot is\n"
                            "speaking, please wait for\n"
                            "it to finish talking before\n"
                            "you do anything else. ",font=("arial",15,'bold')).grid(row=1,column=0)
    bvk = CTkButton(master=abot,command=about_back,text='Back',font=('arial',30,'bold'),fg_color='blue',border_color='blue',border_width=1,cursor='hand2',corner_radius=36)
    bvk.place(x=30,y=600)

def about1():
    global abot1
    abot1 = CTkFrame(master=wn, corner_radius=16, width=340, height=670)
    abot1.grid(row=0, column=0, padx=20, pady=20)
    CTkLabel(master=abot1, text='About', font=('arial', 25, 'bold')).place(x=30, y=0)
    hs1 = CTkFrame(master=abot1, width=250, height=500, corner_radius=16)
    hs1.place(x=10, y=50)
    CTkLabel(master=hs1, image=I, text='').grid(row=0, column=0, padx=10, pady=10)
    CTkLabel(master=hs1, text="This ChatBot app is mainly built to\n"
                              "entertain the user of the application\n"
                              "It is design to adapt to your statements\n"
                              "\nThis ChatBot app has a gaming\nfeature,"
                            "It has different selection of\ngame you"
                            "and the chatbot is built to play\ngames with you.\n"
                            "\n If the ChatBot ask a response on your,\n"
                            "statement from you,\n"
                            "it means that the ChatBot want to\n learn the correct"
                            "response statement to use\n in replying you",font=("arial",15,'bold')).grid(row=1,column=0)
    bvk1 = CTkButton(master=abot1, command=about1_back, text='Back', font=('arial', 30, 'bold'), fg_color='blue',
                    border_color='blue', border_width=1, cursor='hand2', corner_radius=36)
    bvk1.place(x=30, y=600)

def about1_back():
    abot1.destroy()

def about_back():
    abot.destroy()

def rate_kn():
    global rate
    rate = CTkFrame(master=wn, corner_radius=16, width=340, height=670)
    rate.grid(row=0, column=0, padx=20, pady=20)
    CTkLabel(master=rate,text='ChatBot Knowledge rate',font=('arial',25,'bold')).place(x=30, y=0)
    CTkLabel(master=rate,text="",image=In).place(x=50, y=40)
    CTkLabel(master=rate,text=f"\nThe Chat Bot rate of \nknowledge is currently at {len(r)}%\n"
                              f"\nBut if the ChatBot learns more\n from you ,its Knowledge rate\n"
                              f"will increase ",font=('arial',20,'bold')).place(x=10, y=200)
    brk = CTkButton(master=rate,command=r_bk,text='Back',font=('arial',30,'bold'),fg_color='transparent',border_color='blue',border_width=1,cursor='hand2',corner_radius=36)
    brk.place(x=30, y=600)

def r_bk():
    rate.destroy()

frame = CTkScrollableFrame(master=wn,corner_radius=16,width=310,height=670,border_color='blue',border_width=2,scrollbar_button_color='blue',scrollbar_button_hover_color='blue')
frame.grid(row=0,column=0,padx=20,pady=30)
CTkLabel(master=frame,text='Menu',font=('arial',35),corner_radius=36,text_color='white').grid(row=0,column=0)
bh=CTkButton(master=frame,command=start_chat,text='🤖 Start Chatting',fg_color='blue',corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh.grid(row=1,column=0,pady=40)
bh1=CTkButton(master=frame,text='🎮 Play Game',command=game,fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh1.grid(row=2,column=0,pady=40)
bh2=CTkButton(master=frame,text='Knowledge rate',command=rate_kn,fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh2.grid(row=3,column=0,pady=40)
bh3=CTkButton(master=frame,text='Calculator',fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh3.grid(row=4,column=0,pady=40)
bh4=CTkButton(master=frame,text='⚙ Setting',command=setting,fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh4.grid(row=5,column=0,pady=40)
bh5=CTkButton(master=frame,text='❔ Help',command=hep,fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh5.grid(row=6,column=0,pady=40)
bh6 =CTkButton(master=frame,text='Exit',command=wn.destroy,fg_color='blue',width=300,corner_radius=16,font=('arial',35),border_width=1,cursor='hand2')
bh6.grid(row=7,column=0,pady=40)

but = CTkButton(master=wn,text='Exit',fg_color='blue',command=wn.destroy,font=('arial',20),width=200,corner_radius=16,border_width=1)
but.place(x=1100,y=0)

frame2 = CTkFrame(master=wn,corner_radius=16,width=975,height=700,border_color='blue',border_width=2)
frame2.grid(row=0,column=2,padx=0,pady=30)
e = CTkEntry(master=frame2,corner_radius=36,border_color='blue',placeholder_text='Enter message.....',placeholder_text_color='white',font=('arial',30),width=830,height=70)
e.place(x=70,y=600)
m=CTkButton(master=e,text='✔',command=send,corner_radius=36,fg_color='blue',text_color='white',width=30,cursor='hand2',font=('arial',40,'bold'),border_width=3,border_color='blue')
m.place(x=730,y=9)

scroll = CTkScrollableFrame(master=frame2,corner_radius=36,scrollbar_button_color='blue',scrollbar_button_hover_color='blue',border_color='blue',border_width=2,width=800,height=400)
scroll.place(x=50,y=70)
l = CTkLabel(master=frame2,text='Chatting with my AI bot',height=50,fg_color='blue',font=('arial',20,'bold'),corner_radius=36,width=800)
l.place(x=75,y=10)
sound= CTkRadioButton(master=frame2,cursor='hand2',command=talk,text='🔊',fg_color='blue',font=('arial',25),width=20,corner_radius=16)
sound.place(x=910,y=100)

l1 = CTkLabel(master=frame2,image=I,corner_radius=16,text='')
l1.place(x=900,y=10)

wn.mainloop()