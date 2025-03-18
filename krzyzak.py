from turtle import*
import math 
bok = 100
def kwadrat ():
    for i in range (4):
        fd (bok)
        left (90)
def plansza ():
    for i in range (3):
        for j in range (3):
               pd ()
               kwadrat ()
               pu ()
               fd (bok)
        bk(3*bok)
        left (90)
        fd (bok)
        right (90)
def krzyżyk (a,b):
        pu ()
        setx (a*bok + bok/2)
        sety (b*bok + bok/2)
        pd ()
        left (45)
        for i in range (4):
               fd (bok/4)
               bk (bok/4)
               left (90)
        right (45)
        pu ()
def kółko (a,b):
        pu ()
        setx (a*bok + bok/2)
        sety (b*bok + bok/2 - 54/math.pi)
        pd ()
        for i in range (36):
               fd (3)
               left (10)
        pu ()
          
        
        
    
        
        
         
               
