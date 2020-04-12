from tkinter import *
import random
t=Tk()
t.title("Wybierz przycisk")
t.geometry("300x600")
def wstaw_przyciski():
        ile_przycisków=20
        global przyciski
        przyciski = []
        dobry = random.randint (0,ile_przycisków-1)
        for i in range(ile_przycisków):
               if i == dobry:
                   przyciski.append(Button(t,text="nacisk 100 niutonów", command=trafiony))
               else:
                   przyciski.append(Button(t,text="nacisk 100 niutonów", command=pudło))
        for i in przyciski:
                   i.pack(fill=BOTH, expand=YES)
def trafiony():
        for i in przyciski:
                i.destroy()
        global etykieta
        etykieta = Label(t,text = "Easy wygrałeś 100000000 !!! dolków")
        etykieta.pack(fill=BOTH, expand=YES)
        t.after(5000, restart)
def restart():
        etykieta.destroy()
        wstaw_przyciski()
def pudło():
        for i in przyciski:
                i.destroy()
        global etykieta
        etykieta = Label(t, text = "Bomba")
        etykieta.pack(fill=BOTH, expand=YES)
        t.after(500, restart)
wstaw_przyciski()



