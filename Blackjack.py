import random
import time

class Card:
    def __init__(self, maa, arvo, kortin_arvo):
        self.maa = maa
        self.arvo = arvo
        self.kortin_arvo = kortin_arvo

#Tulostaa sen hetkiset kortit näytölle
def print_kortit(kortit, piilossa):    
    k = ""
    for kortti in kortit:
        k = k + "{}".format(kortti.maa) + kortti.arvo + " "
    if piilossa:
        k += "?".format(kortti.arvo)
    print(k)


def blackjack_peli(pakka):
    pelaajan_kortit = []
    jakajan_kortit = []
 
    pelaajan_summa = 0
    jakajan_summa = 0

    print("Jakaja jakaa sinulle kaksi korttia kuvapuoli ylöspäin ja itselleen kaksi korttia, joista toisen kuvapuoli ylöspäin ja toisen kuvapuoli alaspäin. Sinä ilmoitat, haluatko uuden kortin (Paina H ottaaksesi uuden kortin ja S jos et halua kortteja). Jakaja jakaa, kunnes et halua enää lisää kortteja tai korttiesi summa on yli kaksikymmentäyksi. Tämän jälkeen jakaja ottaa itselleen kortteja, kunnes hänen kätensä on kuusitoista tai enemmän. Jos käden arvo on seitsemäntoista tai enemmän, jakaja ei saa ottaa enempää kortteja. Pelin voittaa se, jolla korttien yhteislukema on suurempi menemättä yli kahtakymmentäyhtä tai on tasan 21. Kuvakorttien arvo on 10. Ässän arvo on 11 niin kauan kunnes korttien yhteislukema menee yli 21, jonka jälkeen sen arvo on yksi.")
    aloitus=input("Paina Enter aloittaaksesi pelin ")
    if aloitus == "":
        while len(pelaajan_kortit) < 2:
            
            #Arpoo alkukortit pelaajalle
            pelaajan_kortti = random.choice(pakka)
            pelaajan_kortit.append(pelaajan_kortti)
            pakka.remove(pelaajan_kortti)
    
            pelaajan_summa += pelaajan_kortti.kortin_arvo

            #Muuttaa toisen ässän numeroksi 1 jos pelaaja sai kaksi ässää
            if len(pelaajan_kortit) == 2:
                if pelaajan_kortit[0].kortin_arvo == 11 and pelaajan_kortit[1].kortin_arvo == 11:
                    pelaajan_kortit[0].kortin_arvo = 1
                    pelaajan_summa -= 10

            #Arpoo jakajalle alkukortit
            jakajan_kortti = random.choice(pakka)
            jakajan_kortit.append(jakajan_kortti)
            pakka.remove(jakajan_kortti)

            jakajan_summa += jakajan_kortti.kortin_arvo

            #Muuttaa toisen ässän numeroksi 1 jos jakaja sai kaksi ässää
            if len(jakajan_kortit) == 2:
                if jakajan_kortit[0].kortin_arvo == 11 and jakajan_kortit[1].kortin_arvo == 11:
                    jakajan_kortit[1].kortin_arvo = 1
                    jakajan_summa -= 10

        
   
    if pelaajan_summa == 21:
        print("SAIT BLACKJACKIN (21)!")
        print("VOITIT!")
        quit()
 
    print("JAKAJAN KORTIT: ")
    print_kortit(jakajan_kortit[:-1], True)
    print("JAKAJAN KORTTIEN SUMMA = ", jakajan_summa - jakajan_kortit[-1].kortin_arvo)

    time.sleep(2)
    print() 

    print("SINUN KORTTISI: ")
    print_kortit(pelaajan_kortit, False)
    print("KORTTIESI SUMMA = ", pelaajan_summa)

    while pelaajan_summa < 21:
        kysy = input("Paina H ottaaksesi uuden kortin tai S jos et halua lisää kortteja: ")

        if len(kysy) != 1 or (kysy.upper() != "H" and kysy.upper() != "S"):
            print("Kokeile uudelleen")

        #Jos pelaaja halusi lisää kortteja lisää yksi kortti pelaajan käteen
        if kysy.upper() == "H":

            pelaajan_kortti = random.choice(pakka)
            pelaajan_kortit.append(pelaajan_kortti)
            pakka.remove(pelaajan_kortti)

            pelaajan_summa += pelaajan_kortti.kortin_arvo
 
            x = 0
            while pelaajan_summa > 21 and x < len(pelaajan_kortit):
                if pelaajan_kortit[x].kortin_arvo == 11:
                    pelaajan_kortit[x].kortin_arvo = 1
                    pelaajan_summa -= 10
                    x += 1
                else:
                    x += 1 
              
            print("JAKAJAN KORTIT: ")
            print_kortit(jakajan_kortit[:-1], True)
            print("JAKAJAN KORTTIEN SUMMA = ", jakajan_summa - jakajan_kortit[-1].kortin_arvo)

            time.sleep(2)
            print()
 
            print("SINUN KORTTISI: ")
            print_kortit(pelaajan_kortit, False)
            print("KORTTIESI SUMMA = ", pelaajan_summa)
             
        if kysy.upper() == "S":
            break
 
 
    print("SINUN KORTTISI: ")
    print_kortit(pelaajan_kortit, False)
    print("KORTTIESI SUMMA = ", pelaajan_summa)
    
    time.sleep(2)

    print("JAKAJAN KORTIT: ")
    print_kortit(jakajan_kortit, False)
    print("JAKAJAN KORTTIEN SUMMA = ", jakajan_summa)
 
    if pelaajan_summa == 21:
        print("SAIT BLACKJACKIN (21)!")
        quit()
 
    if pelaajan_summa > 21:
        print("SAIT YLI 21, JOTEN HÄVISIT")
        quit()

    #Ottaa jakajalle kortteja niin kauan kunnes summa on 17 tai yli
    while jakajan_summa < 17: 
 
        print("JAKAJA OTTAA UUDEN KORTIN...")
 
        jakajan_kortti = random.choice(pakka)
        jakajan_kortit.append(jakajan_kortti)
        pakka.remove(jakajan_kortti)
 
        jakajan_summa += jakajan_kortti.kortin_arvo
 
        x = 0
        while jakajan_summa > 21 and x < len(jakajan_kortit):
            if jakajan_kortit[x].kortin_arvo == 11:
                jakajan_kortit[x].kortin_arvo = 1
                jakajan_summa -= 10
                x += 1
            else:
                x += 1
 
        print("SINUN KORTTISI: ")
        print_kortit(pelaajan_kortit, False)
        print("KORTTIESI SUMMA = ", pelaajan_summa)

        time.sleep(2)
        print()

        print("JAKAJAN KORTIT: ")
        print_kortit(jakajan_kortit, False)
        print("JAKAJAN KORTTIEN SUMMA = ", jakajan_summa)      
 
 
    if jakajan_summa > 21:        
        print("JAKAJA SAI YLI 21, JOTEN VOITIT!") 
        quit()  
 
    if jakajan_summa == 21:
        print("JAKAJA SAI BLACKJACKIN (21), JOTEN HÄVISIT")
        quit()
 
    if jakajan_summa == pelaajan_summa:
        print("TASAPELI")
 
    elif pelaajan_summa > jakajan_summa:
        print("VOITIT!")                 
 
    else:
        print("JAKAJA VOITTI")
           
 
if __name__ == "__main__":
 
    maat = ["Pata", "Hertta", "Risti", "Ruutu"]
 
    maiden_arvot = {"Pata":"♠", "Hertta":"♥", "Risti": "♣", "Ruutu": "♦"}
 
    kortit = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    korttien_arvot = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    pakka = []
 
    for maa in maat:
 
        for kortti in kortit:
 
            pakka.append(Card(maiden_arvot[maa], kortti, korttien_arvot[kortti]))
    
    blackjack_peli(pakka)