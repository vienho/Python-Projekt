#Skriven av Vien Ho

import sys #För användning av sys.exit(0)

##En funktion som:
##Läsa in text.txt, kontrollera att text.txt finns, annars stängs programmet.
##Returnera en bok_lista som innehåller flera objekter till klassen Bok.
##Varje objekt(Bok) innehåller: titel, författare, status vilka fick från i text.txt
def läsa_in_böcker():
    try:
        text_fil = open("text.txt", "r", encoding="UTF-8") #För användning av åäö
    except FileNotFoundError:#Kontrollera att input filen existerar
        print("Text_filet existerar inte! Programmet stängs av!")
        sys.exit(0) #För att stänga av om textfilet inte existerar, 0 argument är default
    bok_lista = []
    for en_rad in text_fil:#Läsa in och skapa en lista av innehållet
        steg_1 = en_rad.strip("\n")
        steg_2 = steg_1.split(",") #Skapa en lista med längden 3
        bok_lista.append(Bok(steg_2[0], steg_2[1], steg_2[2]))
    return bok_lista


class Bok:
    def __init__(self, titel, författare, status):
        self.titel = titel.lstrip(" ")#Ta bort mellanslag till vänster
        self.författare = författare.lstrip(" ")
        self.status = status.lstrip(" ")
    def __str__(self):#För att kunna "print()" ett helt objekt
        return self.titel + ", " + self.författare + ", " + self.status + "\n"
##----------------------------------------------------------------------------------------------------    




class Bibliotek: 
    def __init__(self, bok_lista):
        self.bok_lista = bok_lista
#----------------------------------------------------------------------------------------------------
    def menu(self):
        if len(self.bok_lista) == 0:
            print("Det finns inga böcker i biblitoteket, programmet avslutas!")
            sys.exit(0)
        print("Välkommen till biblioteksprogrammet!")

        while True:
            val=input("""    T söka på Titel.
    F söka på Författare.
    L Låna bok.
    Å Återlämna bok.
    N lägga in Ny bok.
    B ta Bort bok.
    A lista Alla böcker.
    S Sluta.
    
Vad vill du göra?: """)
            try:
                if val == "T" or val == "t":
                    titel = input("Vilken titel söker du efter?: ")
                    biblan.söka_titel(titel)
                elif val == "F" or val == "f":
                    författare = input("Vilken författare söker du efter?: ")
                    biblan.söka_författare(författare)

                elif val == "L" or val == "l":
                    titel = input("Ange titeln på den bok du vill låna: ")
                    biblan.låna(titel)
                elif val == "Å" or val == "å":
                    titel = input("Ange titeln på den bok du vill återlämna: ")
                    biblan.lämna(titel)

                elif val == "N" or val == "n":
                    titel = input("Ange titeln på boken du vill lägga till: ")
                    författare = input("Ange författaren på boken du vill lägga till: ")
                    biblan.skapa_ny_bok(titel, författare)
                elif val == "B" or val == "b":
                    titel = input("Ange titeln på boken du vill ta bort: ")
                    författare = input("Ange författaren på boken du vill ta bort: ")
                    biblan.radera_bok(titel, författare)        

                elif val == "A" or val == "a":
                    biblan.lista_böcker()
                elif val == "S" or val == "s":
                    biblan.spara()
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Fel val, försöka igen!")
#----------------------------------------------------------------------------------------------------
##Metoden kombinerar med metod bok_info som hämtar en boks info
##Iterera genom bok_lista för att söka en bok med samma titel som input argument
##Räkna antal böcker som hittat med en räknare, lagras bokens info i en ny lista: bok_hittas
##Om räknare == 0, hittade 0
##Om r == 1, hittade 1, skriv ut bok_info som lagras i bok_hittas
##Om r > 1, hittade fler än 1, skriv ut bok_info som lagras i bok_hittas            
    def söka_titel(self, titel):
        räknare = 0
        bok_hittas = []
        for boken in self.bok_lista:
            if boken.titel == titel:
                räknare +=1
                bok_hittas.append(Bibliotek.bok_info(boken))
                                
        if räknare == 0:
            print("Titeln hittas INTE!")
        elif räknare == 1:
            print("Hittade " + str(räknare) + " bok")
            print(bok_hittas[0])
        else:
            print("Hittade " + str(räknare) + " böcker")
            for i in range(len(bok_hittas)):
                print(bok_hittas[i])

    def bok_info(self):
        return "Titel: {}. Författare: {}. Status: {}".format(self.titel, self.författare, self.status)   

##Exakt som sök_titel, men med författare som argument istället
    def söka_författare(self, författare):
        räknare = 0
        bok_hittas = []
        for boken in self.bok_lista:
            if boken.författare == författare:
                räknare +=1
                bok_hittas.append(Bibliotek.bok_info(boken))
                
        if räknare == 0:
            print("Förfataren hittas INTE!")
        elif räknare == 1:
            print("Hittade " + str(räknare) + " bok")
            print(bok_hittas[0])
        else:
            print("Hittade " + str(räknare) + " böcker")
            for i in range(len(bok_hittas)):
                print(bok_hittas[i])                
#----------------------------------------------------------------------------------------------------              
#Kontrollera bokens titel och status:
#Om boken är ledigt -> ändra statusen till lånad -> ökar räknare
#Vid slutet av iterationen om räknare == 0, dvs inga ändring -> Boken är inte ledigt
    def låna(self, titel):        
        räknare = 0
        for boken in self.bok_lista:
            if boken.titel == titel and boken.status == "ledigt":
                boken.status = "lånad"
                print("Boken är lånad.")
                räknare+=1                
                break
        if räknare == 0:
            print("Boken är inte ledig.")
#Fungerar på samma sätt som ovan, men kontrollera att status == "lånad" istället.                    
    def lämna(self, titel):
        räknare = 0
        for boken in self.bok_lista:
            if boken.titel == titel and boken.status == "lånad":
                boken.status = "ledigt"            
                print("Boken har lämnats")
                räknare+=1
                break
        if räknare == 0:
            print("Boken måste lånas för att kunna lämnas.")
            
#---------------------------------------------------------------------------------------------------- 
#Lägga till en bok(titel,författare,"ledigt")
    def skapa_ny_bok(self, titel, författare):
        self.bok_lista.append(Bok(titel, författare, "ledigt"))

#Kontrollera att det är samma titel och förfatare som finns i self.bok_lista
    def radera_bok(self, titel, författare):
        räknare = 0
        for boken in self.bok_lista:
            if boken.titel == titel and boken.författare == författare:
                self.bok_lista.remove(boken)
                print("Boken har tagits bort.")
                räknare +=1
                break
        if räknare == 0:
            print("Boken hittas inte.")
#---------------------------------------------------------------------------------------------------- 
    def ge_titel(self):
        return self.titel
#Skapade en ge_titel metod för att returnera titel, som använde i nedan metod för att sortera efter titel            
    def lista_böcker(self):
        self.bok_lista.sort(key = Bibliotek.ge_titel)
        for boken in self.bok_lista:
            print("Titel: " + boken.titel + ". Författare: " + boken.författare + ". Status: " + boken.status)        
#---------------------------------------------------------------------------------------------------- 
    def spara(self):
        fil = open("text.txt", "w", encoding="UTF-8")
        for boken in self.bok_lista:
          fil.write(str(boken))
        fil.close
        
    
#Öppna text_filet, läsa, skicka till class Bok() för att skapa böcker. Returnera en bok_lista av objekter (böcker)            
bok_lista = läsa_in_böcker()
biblan = Bibliotek(bok_lista)
biblan.menu()





