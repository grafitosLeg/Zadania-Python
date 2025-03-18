import random
gramy = "tak"
podane = []
wylosowane = []
while gramy == "tak":
    for i in range (6):
        podane.append(int(input("Podaj liczbę numer  "+str(i+1) +":  ")))
        wylosowane.append(random.randint(1,50))
    trafione = 0
    for z in podane:
            for j in wylosowane:
                   if z == j :
                       trafione = trafione + 1
    print ("Twój wynik to:  "+str (trafione))
    print ("Wylosowane liczby:  ")
    for i in wylosowane:
            print (i)
    podane.clear()
    wylosowane.clear()
    gramy = input ("Czy chcesz zagrać ponownie?  (tak/nie)  ")
                          
        
   
