
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plot
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class mclass:
 
    def __init__(self, window):
        self.window = window
       ## window = Tk()
       ## window.title('Phénomène de  Runge')
       ## window.resizable(width=True, height=True)
       ## window.geometry('+0+0')
        varTitle = StringVar()
        varTitle.set(" METHODE DE DICHOTOMIE")
        labelTitle = Label(window, textvariable=varTitle, height=2 ,foreground="#FFFFFF",background="#009688")
        labelTitle.grid(row=0, columnspan=3, sticky=S, padx=20)
        
        varA = StringVar()
        varA.set("La fonction f(x):")
        labelA = Label(window, textvariable=varA, height=2)
        labelA.grid(row=3,  pady=10, padx=20)
        varm   = StringVar()
        varm.set("   x**3 + x**2 -3x - 3")
        labelm = Label(window, textvariable=varm, height=2)
        labelm.grid(row=3,column=2 ,sticky=W, pady=10, padx=20)

     
        
        
        varF = StringVar()

        varF.set(" Ecart :")
        labelF = Label(window, textvariable=varF, height=2)
        labelF.grid(row=4)

        idF = StringVar()
        self.boxF = Entry(window, bd=4, width=40, textvariable=idF)
        self.boxF.grid(row=4, column=2, pady=10, padx=10)


        varB = StringVar()
        varB.set("le borne inférieur a :")
        labelB = Label(window, textvariable=varB, height=2)
        labelB.grid(row=6)

        idB = StringVar()
        self.boxB = Entry(window, bd=4, width=40, textvariable=idB)
        self.boxB.grid(row=6, column=2, pady=10, padx=10)

        varN = StringVar()
        varN.set("la borne supérieur b:")
        labelN = Label(window, textvariable=varN, height=2)
        labelN.grid(row=7)

        idN = StringVar()
        self.boxN = Entry(window, bd=4, width=40, textvariable=idN)
        self.boxN.grid(row=7, column=2, pady=10, padx=10)

        self.button1 = Button(window, text=" Afficher courbe des solutions ", foreground="#FFFFFF",background="#009688",width=40, command=self.plot)
        self.button1.grid(row=8, column=2, sticky=E, pady=20, padx=20)
        self.button2 = Button(window, text=" Donner Solution et nbr d'itérations nécessaires",foreground="#FFFFFF", background="#009688",width=40, command=self.calcule)
        self.button2.grid(row=9, column=2, sticky=E, pady=20, padx=20)
    def calc(self):
        e = float(self.boxF.get())
        a = float(self.boxB.get())
        b = float(self.boxN.get())
        f =  lambda x: x**3+x**2-3*x-3

        m=(a+b)/2
        ecart = abs(b-a)
        n=0
        while abs(b-a)>e:
            n+=1
            if f(a)*f(m)<0:
                  b=m
            else:
                a=m
            m=(a+b)/2
        

        return m ,' et le nombre d itération neccessaires est ' , n
        

    def plot(self):
    
        window = Tk()
        window.geometry("600x554")
        e = float(self.boxF.get())
        a = float(self.boxB.get())
        b = float(self.boxN.get())
        f =  lambda x: x**3+x**2-3*x-3
        #F = self.boxF.get().lower().replace(' ', '')

        #f = lambda x: eval(F)
        T=np.linspace(float(self.boxB.get()),float(self.boxN.get()),41)
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=100, height=100, bd= 5)

        self.fr2.grid(row=1,column=1,padx=10,pady=10)

        self.fig = Figure(figsize=(5,5))
        self.a = self.fig.add_subplot(111)
        
        self.a.cla()
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        self.a.plot(T,f(T),color='blue')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        window.mainloop()
    def calcule(self):
        e = float(self.boxF.get())
        a = float(self.boxB.get())
        b = float(self.boxN.get())
        f =  lambda x: x**3+x**2-3*x-3
        window = Tk()
        window.geometry("500x200")
        p=self.calc()
        lb2 = Label(window,text = "le solution ègal  "  + str(p) + "" )
        lb2.place(x=10,y=10)

        window.mainloop()
        
        
    
if __name__ == '__main__':
    window = Tk()
    window.title('Method Newton')
    window.resizable(width=True, height=True)
    window.geometry('+0+0')
    start = mclass(window)
    window.mainloop()
  
