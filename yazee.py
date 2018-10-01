#yazee

import random, pickle, sys

#abfrage basisinfos (Spielerzahl, Name)
class Spieler:
    def __init__(self):
        global spielerliste
        spielerliste = dict()
        spieleranzahl = int(input("Wieviele Spieler: "))
        for i in range(spieleranzahl):
            spielerliste[i+1] = input("Bitte Name eingeben: ")

    def spielen(self):
        for i in spielerliste.values():
            print(i + ", du bist dran.")
            i = Werfen()

            #1. wurf
            wurf1 = i.wurf1()
            wahl = input("(w)erfen, (a)nschreiben oder (s)treichen:")
            if wahl == "w":
                ubergabe1 = i.behalten(wurf1)

                #2. wurf
                wurf2 = i.wurf2(ubergabe1)
                wahl = input("(w)erfen, (a)nschreiben oder (s)treichen:")
                if wahl == "w":
                    ubergabe2 = i.behalten(wurf2)

                    #3. wurf
                    wurf3 = i.wurf3(ubergabe2)
                    wahl = input("(a)nschreiben oder (s)treichen:")
                    if wahl == "a":
                        i.schreiben(wurf3)
                    else:
                        i.streichen()

                elif wahl == "a":
                    i.schreiben(wurf2)
                else:
                    i.streichen()

            elif wahl == "a":
                i.schreiben(wurf1)
            else:
                i.streichen()

class Werfen():
    #wurf1, möglichkeit zu schreiben oder streichen
    def wurf1(self):
        wurfliste = []
        for i in range (1,6):
            roll = random.randint(1,6)
            wurfliste.append(roll)
            wurfliste.sort()
        print(wurfliste)
        return wurfliste

    def wurf2(self, wurf):
        self.wurf = wurf
        differenz = 5 - len(self.wurf)
        for i in range (1, differenz + 1):
            roll = random.randint(1,6)
            self.wurf.append(roll)
            self.wurf.sort()
        print(self.wurf)
        return(self.wurf)

    def wurf3(self, wurf):
        self.wurf = wurf
        differenz = 5 - len(self.wurf)
        for i in range (1, differenz + 1):
            roll = random.randint(1,6)
            self.wurf.append(roll)
            self.wurf.sort()
        print(self.wurf)
        return(self.wurf)

    def behalten(self, wurf):
        haltliste = []
        self.wurf = wurf
        alleneu = input("Alle (n)eu oder (e)inzelne?")
        if alleneu == "n":
            t = False
            halteliste = self.wurf
        else:
            t = True

            while t:
                beh = int(input("Behalten:")) - 1
                halten = self.wurf.pop(beh)
                haltliste.append(halten)
                print("KANN GEWORFEN WERDEN: ", self.wurf, "WIRD GEHALTEN: ", haltliste)
                more = input("Noch mehr (j/n)")
                if more == "j" and len (haltliste) > 1:
                    continue
                if more == "n":
                    t = False
        return haltliste

    def schreiben(self, wurf):
        self.wurf = wurf
        z = Pruefung()
        zahlenlist = z.zaehlen(self.wurf)
        z.analyse(zahlenlist)


class Pruefung:
    def zaehlen(self, wurf):
        self.wurf = wurf
        dic_zahlen = dict()
        for item in wurf:
            dic_zahlen[item] = dic_zahlen.get(item, 0) + 1
        print(dic_zahlen)
        zahlen_reverse = []
        for (k,v) in dic_zahlen.items():
            zahlen_reverse.append((v,k))
        print(zahlen_reverse)
        return zahlen_reverse

    def analyse(self, zahlenlist):  #hier muss noch eine lösung gefunden werden
        self.dic_zahlen = zahlenlist  #wie die auswertung der würfe stattfindet
        if len(self.dic_zahlen) == 5:
            print("5")
        elif len(self.dic_zahlen) == 4:
            print("4")
        elif len(self.dic_zahlen) == 3:
            print("3")
        elif len(self.dic_zahlen) == 2:
            print("2")
        else:
            print("1")
#streichen

#schreiben
#hier muss geprüft werden was geworfen wurde und das so geschrieben werden kann

#nächster ist dran

#zusammenzählen

#sieger bestimmen und ausgeben

#alltime highscore in liste

#hauptprogramm starten
random.seed()
s = Spieler()
s.spielen()
