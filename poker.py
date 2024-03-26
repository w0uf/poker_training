#coding: latin-1

import poker_fonctions
from random import *
 
# paquet est un tuple qui contient les 52 cartes
valeurs = "A K Q J T 9 8 7 6 5 4 3 2".split(" ")
couleurs = "h d s c".split(" ")
positions= "UTG MP CO BU SB BB".split(" ")

paquet = []

for i in valeurs:
    for j in couleurs:
        paquet.append(i + j)
paquet = tuple(paquet)
# debug print ( paquet)


# deuxcarte est un tuple qui contient toutes les mains de deux cartes
# sans doublons

deuxcartes = []
for i in paquet:
    for j in paquet:
        if (paquet.index(i) < paquet.index(j)):
            deuxcartes.append(i + j)
deuxcartes = tuple(deuxcartes)


#print (deuxcartes)

UTG,MP,CO,BU,SB,BB,Flop1,Flop2,Flop3,Turn, River="UTG","MP","CO","BU","SB","BB","Flop1","Flop2","Flop3","Turn"," River"
# on va dÃ©finir un objet Ã©ventail avec une chaine de caractÃ¨re 
# sÃ©parateur virgule

class eventail():
    developpe = []
    def __init__(self, chaine):
        developpe = []
        chaine="".join(chaine.split()) #(on enlève les espaces)
        elements = chaine.split(",")
        newelements=[]
        options={
                         1:"QQ+",
                         2:"TT+",
                         3:"99+,AKs",
                         4:"99+,AQs+,AKo",
                         5:"88+,AJs+,KQs,AKo",
                         6:"88+,ATs+,KQs,AQo+",
                         7:"88+,ATs+,KTs+,AQo+",
                         8:"88+,ATs+,KTs+,QJs,AJo+",
                         9:"88+,ATs+,KTs+,QJs,AJo+,KQo",
                         10:"77+,A9s+,KTs+,QTs+,AJo+,KQo",
                         11:"77+,A9s+,KTs+,QTs+,ATo+,KQo",
                         12:"77+,A9s+,KTs+,QTs+,JTs,ATo+,KJo+",
                         13:"77+,A8s+,K9s+,QTs+,JTs,ATo+,KJo+,QJo",
                         14:"77+,A7s+,K9s+,QTs+,JTs,ATo+,KJo+,QJo",
                         15:"77+,A7s+,K9s+,QTs+,JTs,ATo+,KTo+,QJo",
                         16:"66+,A7s+,A5s,K9s+,Q9s+,JTs,ATo+,KTo+,QJo",
                         17:"66+,A5s+,K9s+,Q9s+,JTs,ATo+,KTo+,QTo+",
                         18:"66+,A5s+,K9s+,Q9s+,J9s+,A9o+,KTo+,QTo+",
                         19:"66+,A4s+,K9s+,Q9s+,J9s+,T9s,A9o+,KTo+,QTo+",
                         20:"66+,A4s+,K8s+,Q9s+,J9s+,T9s,A9o+,KTo+,QTo+,JTo",
                         21:"66+,A4s+,K7s+,Q9s+,J9s+,T9s,A8o+,KTo+,QTo+,JTo",
                         22:"66+,A3s+,K7s+,Q8s+,J9s+,T9s,A8o+,KTo+,QTo+,JTo",
                         23:"66+,A3s+,K7s+,Q8s+,J9s+,T9s,A8o+,K9o+,QTo+,JTo",
                         24:"66+,A2s+,K6s+,Q8s+,J8s+,T8s+,A8o+,K9o+,QTo+,JTo",
                         25:"66+,A2s+,K6s+,Q8s+,J8s+,T8s+,A7o+,K9o+,QTo+,JTo",
                         26:"55+,A2s+,K6s+,Q8s+,J8s+,T8s+,A7o+,K9o+,Q9o+,JTo",
                         27:"55+,A2s+,K5s+,Q8s+,J8s+,T8s+,98s,A7o+,K9o+,Q9o+,JTo",
                         28:"55+,A2s+,K5s+,Q7s+,J8s+,T8s+,98s,A7o+,K9o+,Q9o+,J9o+",
                         29:"55+,A2s+,K5s+,Q7s+,J8s+,T8s+,98s,A7o+,A5o,K9o+,Q9o+,J9o+",
                         30:"55+,A2s+,K5s+,Q7s+,J8s+,T8s+,98s,A7o+,A5o,K9o+,Q9o+,J9o+,T9o",
                         31:"55+,A2s+,K5s+,Q7s+,J8s+,T8s+,98s,A5o+,K9o+,Q9o+,J9o+,T9o",
                         32:"55+,A2s+,K4s+,Q7s+,J8s+,T8s+,98s,A5o+,K8o+,Q9o+,J9o+,T9o",
                         33:"55+,A2s+,K4s+,Q6s+,J7s+,T7s+,98s,A5o+,K8o+,Q9o+,J9o+,T9o",
                         34:"55+,A2s+,K4s+,Q6s+,J7s+,T7s+,98s,A4o+,K8o+,Q9o+,J9o+,T9o",
                         35:"55+,A2s+,K3s+,Q5s+,J7s+,T7s+,97s+,87s,A4o+,K8o+,Q9o+,J9o+,T9o",
                         36:"55+,A2s+,K3s+,Q5s+,J7s+,T7s+,97s+,87s,A4o+,K7o+,Q9o+,J9o+,T9o",
                         37:"44+,A2s+,K3s+,Q5s+,J7s+,T7s+,97s+,87s,A4o+,K7o+,Q8o+,J9o+,T9o",
                         38:"44+,A2s+,K3s+,Q5s+,J7s+,T7s+,97s+,87s,A3o+,K7o+,Q8o+,J9o+,T9o",
                         39:"44+,A2s+,K2s+,Q5s+,J7s+,T7s+,97s+,87s,A3o+,K7o+,Q8o+,J8o+,T9o",
                         40:"44+,A2s+,K2s+,Q4s+,J7s+,T7s+,97s+,87s,A3o+,K7o+,Q8o+,J8o+,T8o+",
                         41:"44+,A2s+,K2s+,Q4s+,J7s+,T7s+,97s+,87s,A3o+,K7o+,Q8o+,J8o+,T8o+",
                         42:"44+,A2s+,K2s+,Q4s+,J6s+,T7s+,97s+,87s,A3o+,K6o+,Q8o+,J8o+,T8o+",
                         43:"44+,A2s+,K2s+,Q4s+,J6s+,T6s+,97s+,87s,A2o+,K6o+,Q8o+,J8o+,T8o+",
                         44:"44+,A2s+,K2s+,Q4s+,J6s+,T6s+,97s+,87s,A2o+,K6o+,Q8o+,J8o+,T8o+,98o",
                         45:"44+,A2s+,K2s+,Q4s+,J6s+,T6s+,96s+,86s+,76s,A2o+,K6o+,Q8o+,J8o+,T8o+,98o",
                         46:"44+,A2s+,K2s+,Q3s+,J5s+,T6s+,96s+,86s+,76s,A2o+,K5o+,Q8o+,J8o+,T8o+,98o",
                         47:"44+,A2s+,K2s+,Q3s+,J5s+,T6s+,96s+,86s+,76s,A2o+,K5o+,Q7o+,J8o+,T8o+,98o",
                         48:"44+,A2s+,K2s+,Q2s+,J4s+,T6s+,96s+,86s+,76s,A2o+,K5o+,Q7o+,J8o+,T8o+,98o",
                         49:"33+,A2s+,K2s+,Q2s+,J4s+,T6s+,96s+,86s+,76s,65s,A2o+,K5o+,Q7o+,J7o+,T8o+,98o",
                         50:"33+,A2s+,K2s+,Q2s+,J4s+,T6s+,96s+,86s+,76s,65s,A2o+,K5o+,Q7o+,J7o+,T7o+,98o",
                         51:"33+,A2s+,K2s+,Q2s+,J4s+,T6s+,96s+,86s+,76s,65s,A2o+,K4o+,Q7o+,J7o+,T7o+,98o",
                         52:"33+,A2s+,K2s+,Q2s+,J4s+,T5s+,96s+,86s+,75s+,65s,A2o+,K4o+,Q7o+,J7o+,T7o+,98o",
                         53:"33+,A2s+,K2s+,Q2s+,J4s+,T5s+,96s+,86s+,75s+,65s,A2o+,K4o+,Q6o+,J7o+,T7o+,98o",
                         54:"33+,A2s+,K2s+,Q2s+,J3s+,T5s+,95s+,86s+,75s+,65s,A2o+,K4o+,Q6o+,J7o+,T7o+,98o,87o",
                         55:"33+,A2s+,K2s+,Q2s+,J3s+,T5s+,95s+,85s+,75s+,65s,A2o+,K4o+,Q6o+,J7o+,T7o+,97o+,87o",
                         56:"33+,A2s+,K2s+,Q2s+,J3s+,T4s+,95s+,85s+,75s+,65s,A2o+,K4o+,Q6o+,J7o+,T7o+,97o+,87o",
                         57:"33+,A2s+,K2s+,Q2s+,J3s+,T4s+,95s+,85s+,75s+,65s,A2o+,K3o+,Q6o+,J7o+,T7o+,97o+,87o",
                         58:"33+,A2s+,K2s+,Q2s+,J2s+,T4s+,95s+,85s+,75s+,65s,54s,A2o+,K3o+,Q5o+,J7o+,T7o+,97o+,87o",
                         59:"33+,A2s+,K2s+,Q2s+,J2s+,T3s+,95s+,85s+,75s+,64s+,54s,A2o+,K3o+,Q5o+,J7o+,T7o+,97o+,87o",
                         60:"22+,A2s+,K2s+,Q2s+,J2s+,T3s+,95s+,85s+,75s+,64s+,54s,A2o+,K2o+,Q5o+,J7o+,T7o+,97o+,87o",
                         61:"22+,A2s+,K2s+,Q2s+,J2s+,T3s+,95s+,85s+,74s+,64s+,54s,A2o+,K2o+,Q5o+,J7o+,T7o+,97o+,87o,76o",
                         62:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,95s+,85s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J7o+,T7o+,97o+,87o,76o",
                         63:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,95s+,85s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J6o+,T7o+,97o+,87o,76o",
                         64:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,95s+,84s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J6o+,T7o+,97o+,87o,76o",
                         65:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,94s+,84s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J6o+,T7o+,97o+,86o+,76o",
                         66:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,94s+,84s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J6o+,T6o+,97o+,86o+,76o",
                         67:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,94s+,84s+,74s+,64s+,54s,A2o+,K2o+,Q4o+,J6o+,T6o+,96o+,86o+,76o",
                         68:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,93s+,84s+,74s+,64s+,53s+,A2o+,K2o+,Q3o+,J6o+,T6o+,96o+,86o+,76o",
                         69:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,93s+,84s+,74s+,64s+,53s+,A2o+,K2o+,Q3o+,J5o+,T6o+,96o+,86o+,76o",
                         70:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,93s+,84s+,74s+,63s+,53s+,43s,A2o+,K2o+,Q3o+,J5o+,T6o+,96o+,86o+,76o",
                         71:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,84s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q3o+,J5o+,T6o+,96o+,86o+,76o,65o",
                         72:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,84s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q2o+,J5o+,T6o+,96o+,86o+,76o,65o",
                         73:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,84s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q2o+,J4o+,T6o+,96o+,86o+,76o,65o",
                         74:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,83s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q2o+,J4o+,T6o+,96o+,86o+,75o+,65o",
                         75:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,83s+,73s+,63s+,52s+,43s,A2o+,K2o+,Q2o+,J4o+,T6o+,96o+,85o+,75o+,65o",
                         76:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,63s+,52s+,43s,A2o+,K2o+,Q2o+,J4o+,T6o+,96o+,85o+,75o+,65o",
                         77:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,63s+,52s+,43s,A2o+,K2o+,Q2o+,J4o+,T5o+,96o+,85o+,75o+,65o",
                         78:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,63s+,52s+,43s,A2o+,K2o+,Q2o+,J3o+,T5o+,95o+,85o+,75o+,65o",
                         79:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,62s+,52s+,43s,A2o+,K2o+,Q2o+,J3o+,T5o+,95o+,85o+,75o+,65o",
                         80:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,62s+,52s+,43s,A2o+,K2o+,Q2o+,J3o+,T5o+,95o+,85o+,75o+,65o,54o",
                         81:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,62s+,52s+,42s+,A2o+,K2o+,Q2o+,J3o+,T4o+,95o+,85o+,75o+,65o,54o",
                         82:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,62s+,52s+,42s+,A2o+,K2o+,Q2o+,J2o+,T4o+,95o+,85o+,75o+,65o,54o",
                         83:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,A2o+,K2o+,Q2o+,J2o+,T4o+,95o+,85o+,75o+,64o+,54o",
                         84:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,A2o+,K2o+,Q2o+,J2o+,T3o+,95o+,85o+,75o+,64o+,54o",
                         85:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T3o+,95o+,85o+,74o+,64o+,54o",
                         86:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T3o+,95o+,84o+,74o+,64o+,54o",
                         87:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,95o+,84o+,74o+,64o+,54o",
                         88:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,94o+,84o+,74o+,64o+,54o",
                         89:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,94o+,84o+,74o+,64o+,53o+",
                         90:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,93o+,84o+,74o+,64o+,53o+",
                         91:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,93o+,84o+,74o+,63o+,53o+,43o",
                         92:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,84o+,74o+,63o+,53o+,43o",
                         93:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,84o+,73o+,63o+,53o+,43o",
                         94:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,83o+,73o+,63o+,53o+,43o",
                         95:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,83o+,73o+,63o+,52o+,43o",
                         96:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,73o+,63o+,52o+,43o",
                         97:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,73o+,63o+,52o+,42o+",
                         98:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,73o+,62o+,52o+,42o+",
                         99:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,72o+,62o+,52o+,42o+",
                         100:"22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,72o+,62o+,52o+,42o+,32o"
                         
                         
                         
                         
                         
                         
                }
        
        for e in elements:
            if e!="":
                if e[-1]=="%" and int(e[:-1]) in options.keys():
                    
                    newelements+=options[int(e[:-1])].split(",")
                else:
                    newelements+=e.split(",")
        
        
        for e in newelements:
            if (len(e)==0):
                pass
            
                
            elif (len(e) == 1):
                print ("erreur : {0} est ignoré".format(e))
            elif (len(e) == 2):
                # Ils s'agit de deux valeurs ou d'une erreur
                
                if e[0] in valeurs and e[1] in valeurs:
                    # debug on range e[0] et e[1]
                        if valeurs.index(e[0]) > valeurs.index(e[1]):
                            # on  echange
                            e0, e1 = e[1], e[0]
                        else:
                            e0, e1 = e[0], e[1]
                        for jeu in deuxcartes:
                            if  (jeu[0] == e0 and jeu[2] == e1):                                               
                                    developpe.append(jeu)
                elif e[0] in valeurs and e[1]=="*":
                    #joker en deuxiÃ¨me position
                    # print ("debug joker")
                    for jeu in deuxcartes:
                        if jeu[0]==e[0] and valeurs.index(e[0])<valeurs.index(jeu[2]):
                            developpe.append(jeu)
                elif e[1] in valeurs and e[0]=="*":
                    #joker en premiÃ¨re position
                    # print ("debug joker")
                    for jeu in deuxcartes:
                        if jeu[2]==e[1] and valeurs.index(jeu[0])<valeurs.index(e[1]):
                            developpe.append(jeu)
                elif   "r" in e:
                      
                    for jeu in deuxcartes:
                            if  (jeu[0] == e[0] or jeu[0] == e[1] or jeu[2]==e[0] or jeu[2]==e[1]):                                               
                                    developpe.append(jeu)
                                                  
                else :
                    # erreur
                    print ("erreur :{0} est ignore".format(e))
            elif (len(e) == 3):
                # suited ou outsuites ou serie genre AT+ (s,o,+) ou erreur
                if e[0] in valeurs and e[1] in valeurs and e[2] in ("s", "o", "+"):
                    if e[2] == "s":  # suited 
                        for jeu in deuxcartes:
                            if  (jeu[0] == e[0] and jeu[2] == e[1] and jeu[1] == jeu[3]):                                               
                                    developpe.append(jeu)
                        for jeu in deuxcartes:
                            if  (jeu[0] == e[1] and jeu[2] == e[0] and jeu[1] == jeu[3]):                                               
                                    developpe.append(jeu)
                    elif e[2] == "o":  # outsuited
                        if e[0]!=e[1]:
                            for jeu in deuxcartes:
                                if  (jeu[0] == e[0] and jeu[2] == e[1] and jeu[1] != jeu[3]):                                               
                                        developpe.append(jeu)
                        for jeu in deuxcartes:
                            if  (jeu[0] == e[1] and jeu[2] == e[0] and jeu[1] != jeu[3]):                                               
                                    developpe.append(jeu)
                    elif e[2] == "+":  # serie
                        # debug on range e[0] et e[1]
                        if valeurs.index(e[0]) > valeurs.index(e[1]):
                            # on  echange
                            e0, e1 = e[1], e[0]
                        else:
                            e0, e1 = e[0], e[1]
                        # e0 contient la plus grande carte, e1 la plus petite
                        # print (e0, e1)
                        if e0 == e1:
                            # serie de paires
                            for jeu in deuxcartes:
                                if  valeurs.index(jeu[0]) <= valeurs.index(e0) and jeu[0] == jeu[2]:
                                            developpe.append(jeu)
                        else:
                            # non paires 
                            if valeurs.index(e0)+1==valeurs.index(e1): #connecteurs
                                for jeu in deuxcartes:
                                    if valeurs.index(jeu[2])-valeurs.index(jeu[0])==1 and valeurs.index(jeu[2])<=valeurs.index(e1):
                                        developpe.append(jeu)
                            else:
                                for jeu in deuxcartes: #serie genre AT+
                                    if  jeu[0] == e0 and valeurs.index(jeu[2]) <=  valeurs.index(e1) and jeu[0] != jeu[2]:
                                            developpe.append(jeu)
                            
                            
                else :
                    print ("erreur : {0} est ignore. je ne comprends pas {1}".format(e, e[2]))
            elif len(e) == 4 : 
                if (e[3]=="+" and e[0] in valeurs and e[1] in valeurs and e[2] in ["o","s"]) or (e[0] in valeurs and e[1] in couleurs and e[2] in valeurs and e[3] in couleurs)  :
                    
                    if e[2]=="o":
                        #outsuited +
                        if valeurs.index(e[0]) > valeurs.index(e[1]):
                            # on  echange
                            e0, e1 = e[1], e[0]
                        else:
                            e0, e1 = e[0], e[1]
                            #e0 et e1 sont rangÃ©s
                        if e0 == e1:
                            # serie de paires
                            
                            for jeu in deuxcartes:
                                if  valeurs.index(jeu[0]) <= valeurs.index(e0) and jeu[0] == jeu[2] and jeu[1]!=jeu[3]:
                                            developpe.append(jeu)
                                            
                          # non paires 
                        elif valeurs.index(e0)+1==valeurs.index(e1) : #connecteurs outsuited
                                for jeu in deuxcartes:
                                    if valeurs.index(jeu[2])-valeurs.index(jeu[0])==1 and valeurs.index(jeu[2])<=valeurs.index(e1) and jeu[1]!=jeu[3]:
                                        developpe.append(jeu)
                        else:
                                for jeu in deuxcartes: #serie genre AT+
                                    if  jeu[0] == e0 and valeurs.index(jeu[2]) <=  valeurs.index(e1) and jeu[0] != jeu[2] and jeu[1]!=jeu[3]:
                                            developpe.append(jeu)
                        
                        
                    elif e[2]=="s":
                        #suited +
                        if valeurs.index(e[0]) > valeurs.index(e[1]):
                            # on  echange
                            e0, e1 = e[1], e[0]
                        else:
                            e0, e1 = e[0], e[1]
                            #e0 et e1 sont rangÃ©s
                        
                        
                        if e0 == e1:
                            # serie de paires
                            print ("Pas de paire suited",e)
                         # non paires 
                        elif valeurs.index(e0)+1==valeurs.index(e1) : #connecteurs outsuited
                                for jeu in deuxcartes:
                                    if valeurs.index(jeu[2])-valeurs.index(jeu[0])==1 and valeurs.index(jeu[2])<=valeurs.index(e1) and jeu[1]==jeu[3]:
                                        developpe.append(jeu)
                        else:
                                for jeu in deuxcartes: #serie genre AT+
                                    if  jeu[0] == e0 and valeurs.index(jeu[2]) <=  valeurs.index(e1) and jeu[0] != jeu[2] and jeu[1]==jeu[3]:
                                            developpe.append(jeu)
                        
                    
                    elif e[0] in valeurs and e[1] in couleurs and e[2] in valeurs and e[3] in couleurs:
                        
                        if valeurs.index(e[0]) > valeurs.index(e[2]):
                            # on  echange
                            e0, e1, e2,e3 = e[2],e[3], e[0],e[1]
                        else:
                            e0, e1,e2, e3 = e[0], e[1], e[2], e[3]
                            #e0e1e2e3 rangÃ© 
                            
                        if e0==e2 and couleurs.index(e[1]) > couleurs.index(e[3]):
                            #on echange
                            e1,e3=e3,e1
                            
                        #print ("debug",e0,e1,e2,e3)
                        developpe.append(str(e0)+str(e1)+str(e2)+str(e3))
                    else :
                        print("Le troisieme caractere {0} de la chaine {1} me semble incompréhensible".format(e[2],e))
                
                
                else :    
                    print("Les expressions de 4 caractees doivent se terminer par o+ ou s+ et commencer par deux valeurs de cartes ou alors spÃ©cifier les deux couleurs des cartes, ce n'est pas le cas pour", e)
            elif len(e)==5:
                
                # truc genre Ah2h+ ou AT-AK ou connecteurs ou JJ-99
                if e[0] in valeurs and e[1] in couleurs and e[2] in valeurs and e[3]==e[1] and e[4]=="+":
                    if valeurs.index(e[0])<valeurs.index(e[2]):
                        for jeu in deuxcartes:
                            if jeu[0]==e[0] and jeu[1]==e[1] and jeu[3]==e[1] and valeurs.index(jeu[2])<=valeurs.index(e[2]):
                                #print("debug", valeurs.index(jeu[2]),valeurs.index(e[2]))
                                developpe.append(jeu)
                    if valeurs.index(e[0])>valeurs.index(e[2]):
                            for jeu in deuxcartes:
                                if jeu[2]==e[0] and jeu[1]==e[1] and jeu[3]==e[1] and valeurs.index(jeu[0])<=valeurs.index(e[2]):
                                    # print("debug", valeurs.index(jeu[2]),valeurs.index(e[2]))
                                    developpe.append(jeu)
                    else:
                        print("Erreur inconnue")
                elif e[2]=="-" and e[0] in valeurs and e[1] in valeurs and e[3] in valeurs and e[4] in valeurs: 
                    k,l=e.split("-")     
                    # k est-il une paire ?
                    if k[0]==k[1]:
                        #cela a du sens si l est une paire aussi
                        if l[0]==l[1]:
                            if valeurs.index(k[0])<valeurs.index(l[0]):
                                k,l=k[0],l[0]
                            else:
                                l,k=k[0],l[0]
                            
                            for jeu in deuxcartes:
                                if jeu[0]==jeu[2] and valeurs.index(jeu[0])>=valeurs.index(k) and valeurs.index(jeu[0])<=valeurs.index(l):
                                    developpe.append(jeu)
                        else:
                            print("{2} : Erreur {0} est une paire mais pas {1}.".format(k,l,e))
                    
                    elif (valeurs.index(k[0])-valeurs.index(k[1]))**2== (valeurs.index(l[0])-valeurs.index(l[1]))**2:
                        # print("debug : mÃªme diffÃ©rence")
                        # one grapper - two grapper etc....
                        if valeurs.index(k[0])>valeurs.index(k[1]):
                            a,b,diff=k[1],k[0], valeurs.index(k[0])-valeurs.index(k[1])
                        else:
                            b,a,diff=k[1],k[0], valeurs.index(k[1])-valeurs.index(k[0])
                        if valeurs.index(l[0])>valeurs.index(l[1]):
                            c,d,=l[1],l[0]
                        else:
                            d,c=l[1],l[0]
                        if valeurs.index(c)<valeurs.index(a):
                            a,b,c,d=c,d,a,b
                                  
                        #print (a,b,diff,c,d)
                        for jeu in deuxcartes:
                            if valeurs.index(jeu[0])>=valeurs.index(a) and valeurs.index(jeu[2])<=valeurs.index(d) and valeurs.index(jeu[2])-valeurs.index(jeu[0])==diff:
                                developpe.append(jeu)
                    elif k[0] in l or k[1] in l:
                        # k et l ont une carte en commun
                        if k[0] in l:
                            # c'est lui la carte commune
                            a,b=k[0],k[1]
                            if a==l[0]:
                                c=l[1]
                            else:
                                c=l[0]
                        else:
                            a,b=k[1],k[0]
                            if a==l[0]:
                                c=l[1]
                            else:
                                c=l[0]
                        #a,b,c debug
                        if valeurs.index(b)>valeurs.index(c):
                            b,c=c,b
                        #a est la commune, on va de ab Ã  ac
                        for jeu in deuxcartes:
                            if jeu[0]==a and valeurs.index(jeu[2])>=valeurs.index(b) and valeurs.index(jeu[2])<=valeurs.index(c):
                                developpe.append(jeu)
                    else:
                        print("erreur inconnue dans chaine",e)   
                    
                                
                else:
                    print("Erreur inconnue")
            elif len(e)==6:
                print (e,"est incomprehensible")
            elif len(e)==7:
                    
                    if e[0] in valeurs and e[1] in valeurs and e[2] in ("s","o") and e[3]=="-" and e[4] in valeurs and e[5] in valeurs and e[6]==e[2] and e[0]!=e[1] and e[4]!=e[5]:
                        #T7s-T3s ou T7o-T3o ou connecteurs (Ã  n trous) suited ou non
                        k,l=e.split("-")
                        suited=(str(k[2])=="s")
                        k=k[0:2]
                        l=l[0:2]
                        if (valeurs.index(k[0])-valeurs.index(k[1]))**2== (valeurs.index(l[0])-valeurs.index(l[1]))**2:
                            # print("debug : mÃªme diffÃ©rence")
                            # one grapper - two grapper etc....
                            if valeurs.index(k[0])>valeurs.index(k[1]):
                                a,b,diff=k[1],k[0], valeurs.index(k[0])-valeurs.index(k[1])
                            else:
                                b,a,diff=k[1],k[0], valeurs.index(k[1])-valeurs.index(k[0])
                            if valeurs.index(l[0])>valeurs.index(l[1]):
                                c,d,=l[1],l[0]
                            else:
                                d,c=l[1],l[0]
                            if valeurs.index(c)<valeurs.index(a):
                                a,b,c,d=c,d,a,b
                                      
                            #debug print (a,b,diff,c,d)
                            for jeu in deuxcartes:
                                if valeurs.index(jeu[0])>=valeurs.index(a) and valeurs.index(jeu[2])<=valeurs.index(d) and valeurs.index(jeu[2])-valeurs.index(jeu[0])==diff and ((suited and jeu[1]==jeu[3]) or (not suited and jeu[1]!=jeu[3])):
                                    developpe.append(jeu)
                        elif k[0] in l or k[1] in l:
                        # k et l ont une carte en commun
                            if k[0] in l:
                                # c'est lui la carte commune
                                a,b=k[0],k[1]
                                if a==l[0]:
                                    c=l[1]
                                else:
                                    c=l[0]
                            else:
                                a,b=k[1],k[0]
                                if a==l[0]:
                                    c=l[1]
                                else:
                                    c=l[0]
                            #a,b,c debug
                            if valeurs.index(b)>valeurs.index(c):
                                b,c=c,b
                            #a est la commune, on va de ab Ã  ac et suited
                            #print("debug ",a,b,c,suited)
                            for jeu in deuxcartes:
                                if jeu[0]==a and valeurs.index(jeu[2])>=valeurs.index(b) and valeurs.index(jeu[2])<=valeurs.index(c) and ((suited and jeu[1]==jeu[3]) or (not suited and jeu[1]!=jeu[3])):
                                    developpe.append(jeu)
                        pass
                    else:
                        print (e,"est incomprehensible") 
                        
                        
                    
            else :
                print("erreur inconnue")
     
        
        self.developpe=[x for x in deuxcartes if x in developpe]
        # jeu simplifiÃ©
        factorise=[]
        tampon=list(self.developpe)
        #on va vider le tampon en remplissant factorise
        #On essaie d'oublier les couleurs
        
        compte={} #dictionnaire contenant le nombre d'occuarances des différentes mains
        for carte in valeurs:
            compte[carte+carte]=0
            for carte2 in valeurs:
                if carte!=carte2:
                    compte[carte+carte2+"s"]=0
                    compte[carte+carte2+"o"]=0
                        
        for e in tampon:
            if e[0]==e[2]:
                compte[e[0]+e[2]]+=1
            elif e[1]==e[3]:
                compte[e[0]+e[2]+"s"]+=1
            else :
                compte[e[0]+e[2]+"o"]+=1
        #print("debug compte",compte)                   
        #Traitement des paires:
        paires=[c+c for c in valeurs if compte[c+c]==6]
        
       
        #On effaces les paires dans tampon et dans compte
        tampon = [x for x in tampon  if not (x[0]+x[2]) in paires]
        for jeu in paires:
            compte[jeu]=0
        #paire_s contient les paires simplifiés
        purgeAA=poker_fonctions.menage_tuple(["AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22"],paires)
        
        #si un element de purgeAA contient une chaine  de laformre AA-xx on remplace par xx+
        
        for i in range (0,len(purgeAA)):
            if purgeAA[i][0:3]=="AA-":
                purgeAA[i]=purgeAA[i][3:]+"+"
        self.paires_s=purgeAA
        
        #traitement des AS
        #suited
        As_suited=["A"+x+"s" for x in valeurs if x!="A" and compte["A"+x+"s"]==4]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in As_suited or x[1]!=x[3]]
        for jeu in As_suited:
            compte[jeu]=0
        
        self.As_suited=As_suited
        self.As_suited_s=poker_fonctions.menage_tuple(["AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s"],As_suited)
   
      
        #outsuited
        As_outsuited=["A"+x+"o" for x in valeurs if x!="A" and compte["A"+x+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in As_outsuited or x[1]==x[3]]
        for jeu in As_outsuited:
            compte[jeu]=0
            
        self.As_outsuited=As_outsuited
        self.As_outsuited_s=poker_fonctions.menage_tuple(["AKo","AQo","AJo","ATo","A9o","A8o","A7o","A6o","A5o","A4o","A3o","A2o"],As_outsuited)
       
                    
                
        As=[x[:-1] for x in As_suited if x[:-1]+"o" in As_outsuited]+[x for x in As_suited if not x[:-1]+"o" in As_outsuited]+[x for x in As_outsuited if not x[:-1]+"s" in As_suited]
        
        chaineas = poker_fonctions.menage_tuple(["AK","AQ","AJ","AT","A9","A8","A7","A6","A5","A4","A3","A2"],[x for x in As])
        chaineas = chaineas+poker_fonctions.menage_tuple(["AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s"],[x for x in As])
        chaineas =chaineas+ poker_fonctions.menage_tuple(["AKo","AQo","AJo","ATo","A9o","A8o","A7o","A6o","A5o","A4o","A3o","A2o"],[x for x in As])      
        self.As=chaineas
        
        #traitement des Roi
        #suited
        K_suited=["K"+x+"s" for x in valeurs if x!="K" and compte["K"+x+"s"]==4]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in K_suited or x[1]!=x[3]]
        for jeu in K_suited:
            compte[jeu]=0
            
        self.K_suited=K_suited
        self.K_suited_s=poker_fonctions.menage_tuple(["KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s","K4s","K3s","K2s"],K_suited)
   
      
        #outsuited
        K_outsuited=["K"+x+"o" for x in valeurs if x!="K" and compte["K"+x+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in K_outsuited or x[1]==x[3]]
        for jeu in K_outsuited:
            compte[jeu]=0
        self.K_outsuited=K_outsuited
        self.K_outsuited_s=poker_fonctions.menage_tuple(["KQo","KJo","KTo","K9o","K8o","K7o","K6o","K5o","K4o","K3o","K2o"],K_outsuited)
       
                    
                
        K=[x[:-1] for x in K_suited if x[:-1]+"o" in K_outsuited]+[x for x in K_suited if not x[:-1]+"o" in K_outsuited]+[x for x in K_outsuited if not x[:-1]+"s" in K_suited]
        
        chaineK = poker_fonctions.menage_tuple(["KQ","KJ","KT","K9","K8","K7","K6","K5","K4","K3","K2"],[x for x in K])
        chaineK = chaineK+poker_fonctions.menage_tuple(["KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s","K4s","K3s","K2s"],[x for x in K])
        chaineK =chaineK+ poker_fonctions.menage_tuple(["KQo","KJo","KTo","K9o","K8o","K7o","K6o","K5o","K4o","K3o","K2o"],[x for x in K])      
        self.K=chaineK
        
        #traitement des Dames
        #suited
        Q_suited=["Q"+x+"s" for x in valeurs if x!="Q" and compte["Q"+x+"s"]==4]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in Q_suited or x[1]!=x[3]]
        for jeu in Q_suited:
            compte[jeu]=0
            
        self.Q_suited=Q_suited
        self.Q_suited_s=poker_fonctions.menage_tuple(["QJs","QTs","Q9s","Q8s","Q7s","Q6s","Q5s","Q4s","Q3s","Q2s"],Q_suited)
   
      
        #outsuited
        Q_outsuited=["Q"+x+"o" for x in valeurs if x!="Q" and compte["Q"+x+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in Q_outsuited or x[1]==x[3]]
        for jeu in Q_outsuited:
            compte[jeu]=0
        self.Q_outsuited=Q_outsuited
        self.Q_outsuited_s=poker_fonctions.menage_tuple(["QJo","QTo","Q9o","Q8o","Q7o","Q6o","Q5o","Q4o","Q3o","Q2o"],Q_outsuited)
       
                    
                
        Q=[x[:-1] for x in Q_suited if x[:-1]+"o" in Q_outsuited]+[x for x in Q_suited if not x[:-1]+"o" in Q_outsuited]+[x for x in Q_outsuited if not x[:-1]+"s" in Q_suited]
        
        chaineQ = poker_fonctions.menage_tuple(["QJ","QT","Q9","Q8","Q7","Q6","Q5","Q4","Q3","Q2"],[x for x in Q])
        chaineQ = chaineQ+poker_fonctions.menage_tuple(["QJs","QTs","Q9s","Q8s","Q7s","Q6s","Q5s","Q4s","Q3s","Q2s"],[x for x in Q])
        chaineQ =chaineQ+ poker_fonctions.menage_tuple(["QJo","QTo","Q9o","Q8o","Q7o","Q6o","Q5o","Q4o","Q3o","Q2o"],[x for x in Q])      
        self.Q=chaineQ
        
        
        #traitement des Valets
        #suited
        J_suited=["J"+x+"s" for x in valeurs if x!="J" and compte["J"+x+"s"]==4]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in J_suited or x[1]!=x[3]]
        for jeu in J_suited:
            compte[jeu]=0
            
        self.J_suited=J_suited
        self.J_suited_s=poker_fonctions.menage_tuple(["JTs","J9s","J8s","J7s","J6s","J5s","J4s","J3s","J2s"],J_suited)
   
      
        #outsuited
        J_outsuited=["J"+x+"o" for x in valeurs if x!="J" and compte["J"+x+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in J_outsuited or x[1]==x[3]]
        for jeu in J_outsuited:
            compte[jeu]=0
        self.J_outsuited=J_outsuited
        self.J_outsuited_s=poker_fonctions.menage_tuple(["JTo","J9o","J8o","J7o","J6o","J5o","J4o","J3o","J2o"],J_outsuited)
       
                    
                
        J=[x[:-1] for x in J_suited if x[:-1]+"o" in J_outsuited]+[x for x in J_suited if not x[:-1]+"o" in J_outsuited]+[x for x in J_outsuited if not x[:-1]+"s" in J_suited]
        
        chaineJ = poker_fonctions.menage_tuple(["JT","J9","J8","J7","J6","J5","J4","J3","J2"],[x for x in J])
        chaineJ = chaineJ+poker_fonctions.menage_tuple(["JTs","J9s","J8s","J7s","J6s","J5s","J4s","J3s","J2s"],[x for x in J])
        chaineJ =chaineJ+ poker_fonctions.menage_tuple(["JTo","J9o","J8o","J7o","J6o","J5o","J4o","J3o","J2o"],[x for x in J])      
        self.J=chaineJ            
        #print("compte", compte)
        
        #traitement des dix
        #suited
        T_suited=["T"+x+"s" for x in valeurs if x!="T" and compte["T"+x+"s"]==4]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in T_suited or x[1]!=x[3]]
        for jeu in T_suited:
            compte[jeu]=0
            
        self.T_suited=T_suited
        self.T_suited_s=poker_fonctions.menage_tuple(["T9s","T8s","T7s","T6s","T5s","T4s","T3s","T2s"],T_suited)
   
      
        #outsuited
        T_outsuited=["T"+x+"o" for x in valeurs if x!="T" and compte["T"+x+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in T_outsuited or x[1]==x[3]]
        for jeu in T_outsuited:
            compte[jeu]=0
        self.T_outsuited=T_outsuited
        self.T_outsuited_s=poker_fonctions.menage_tuple(["T9o","T8o","T7o","T6o","T5o","T4o","T3o","T2o"],T_outsuited)
       
                    
                
        T=[x[:-1] for x in T_suited if x[:-1]+"o" in T_outsuited]+[x for x in T_suited if not x[:-1]+"o" in T_outsuited]+[x for x in T_outsuited if not x[:-1]+"s" in T_suited]
        
        chaineT = poker_fonctions.menage_tuple(["T9","T8","T7","T6","T5","T4","T3","T2"],[x for x in T])
        chaineT = chaineT+poker_fonctions.menage_tuple(["T9s","T8s","T7s","T6s","T5s","T4s","T3s","T2s"],[x for x in T])
        chaineT =chaineT+ poker_fonctions.menage_tuple(["T9o","T8o","T7o","T6o","T5o","T4o","T3o","T2o"],[x for x in T])      
        self.T=chaineT            
        #print("compte", compte)
       
       #traitement des connecteurs
        #suited
        
        G_suited=[x+y+"s" for x in valeurs for y in valeurs if (valeurs.index(x)+1==valeurs.index(y) and compte[x+y+"s"]==4)]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in G_suited or x[1]!=x[3]]
        for jeu in G_suited:
            compte[jeu]=0
            
        self.G_suited=G_suited
        self.G_suited_s=poker_fonctions.menage_tuple(["98s","87s","76s","65s","54s","43s","32s"],G_suited)
        
         #outsuited
        G_outsuited=[x+y+"o" for x in valeurs for y in valeurs if valeurs.index(x)+1==valeurs.index(y) and compte[x+y+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in G_outsuited or x[1]==x[3]]
        for jeu in G_outsuited:
            compte[jeu]=0
        self.G_outsuited=G_outsuited
        self.G_outsuited_s=poker_fonctions.menage_tuple(["98o","87o","76o","65o","54o","43o","32o"],G_outsuited)
       
                    
                
        G=[x[:-1] for x in G_suited if x[:-1]+"o" in G_outsuited]+[x for x in G_suited if not x[:-1]+"o" in G_outsuited]+[x for x in G_outsuited if not x[:-1]+"s" in G_suited]
        
        chaineG = poker_fonctions.menage_tuple(["98","87","76","65","54","43","32"],[x for x in G])
        chaineG = chaineG+poker_fonctions.menage_tuple(["98s","87s","76s","65s","54s","43s","32s"],[x for x in G])
        chaineG =chaineG+ poker_fonctions.menage_tuple(["98o","87o","76o","65o","54o","43o","32o"],[x for x in G])      
        self.G=chaineG           
        
       #traitement des 1-G --> G1 
        #suited
        
        G1_suited=[x+y+"s" for x in valeurs for y in valeurs if (valeurs.index(x)+2==valeurs.index(y) and compte[x+y+"s"]==4)]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in G1_suited or x[1]!=x[3]]
        for jeu in G1_suited:
            compte[jeu]=0
            
        self.G1_suited=G1_suited
        self.G1_suited_s=poker_fonctions.menage_tuple(["97s","86s","75s","64s","53s","42s"],G1_suited)
        
         #outsuited
        G1_outsuited=[x+y+"o" for x in valeurs for y in valeurs if valeurs.index(x)+2==valeurs.index(y) and compte[x+y+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in G1_outsuited or x[1]==x[3]]
        for jeu in G1_outsuited:
            compte[jeu]=0
        self.G1_outsuited=G1_outsuited
        self.G1_outsuited_s=poker_fonctions.menage_tuple(["97o","86o","75o","64o","53o","42o"],G1_outsuited)
       
                    
                
        G1=[x[:-1] for x in G1_suited if x[:-1]+"o" in G1_outsuited]+[x for x in G1_suited if not x[:-1]+"o" in G1_outsuited]+[x for x in G1_outsuited if not x[:-1]+"s" in G1_suited]
        
        chaineG1 = poker_fonctions.menage_tuple(["97","86","75","64","53","42"],[x for x in G1])
        chaineG1 = chaineG1+poker_fonctions.menage_tuple(["97s","86s","75s","64s","53s","42s"],[x for x in G1])
        chaineG1 =chaineG1+ poker_fonctions.menage_tuple(["97o","86o","75o","64o","53o","42o"],[x for x in G1])      
        self.G1=chaineG1           
        
         #traitement des 2-G --> G2 
        #suited
        
        G2_suited=[x+y+"s" for x in valeurs for y in valeurs if (valeurs.index(x)+3==valeurs.index(y) and compte[x+y+"s"]==4)]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in G2_suited or x[1]!=x[3]]
        for jeu in G2_suited:
            compte[jeu]=0
            
        self.G2_suited=G2_suited
        self.G2_suited_s=poker_fonctions.menage_tuple(["96s","85s","74s","63s","52s"],G2_suited)
        
         #outsuited
        G2_outsuited=[x+y+"o" for x in valeurs for y in valeurs if valeurs.index(x)+3==valeurs.index(y) and compte[x+y+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in G2_outsuited or x[1]==x[3]]
        for jeu in G2_outsuited:
            compte[jeu]=0
        self.G2_outsuited=G2_outsuited
        self.G2_outsuited_s=poker_fonctions.menage_tuple(["96o","85o","74o","63o","52o"],G2_outsuited)
       
                    
                
        G2=[x[:-1] for x in G2_suited if x[:-1]+"o" in G2_outsuited]+[x for x in G2_suited if not x[:-1]+"o" in G2_outsuited]+[x for x in G2_outsuited if not x[:-1]+"s" in G2_suited]
        
        chaineG2 = poker_fonctions.menage_tuple(["96","85","74","63","52"],[x for x in G2])
        chaineG2 = chaineG2+poker_fonctions.menage_tuple(["96s","85s","74s","63s","52s"],[x for x in G2])
        chaineG2 =chaineG2+ poker_fonctions.menage_tuple(["96o","85o","74o","63o","52o"],[x for x in G2])      
        self.G2=chaineG2        
        self.factorise=tuple(factorise)
        
          #traitement des 3-G --> G3 
        #suited
        
        G3_suited=[x+y+"s" for x in valeurs for y in valeurs if (valeurs.index(x)+4==valeurs.index(y) and compte[x+y+"s"]==4)]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"s") in G3_suited or x[1]!=x[3]]
        for jeu in G3_suited:
            compte[jeu]=0
            
        self.G3_suited=G3_suited
        self.G3_suited_s=poker_fonctions.menage_tuple(["95s","84s","73s","62s"],G3_suited)
        
         #outsuited
        G3_outsuited=[x+y+"o" for x in valeurs for y in valeurs if valeurs.index(x)+4==valeurs.index(y) and compte[x+y+"o"]==12]
        
        
        tampon = [x for x in tampon  if not (x[0]+x[2]+"o") in G3_outsuited or x[1]==x[3]]
        for jeu in G3_outsuited:
            compte[jeu]=0
        self.G3_outsuited=G3_outsuited
        self.G3_outsuited_s=poker_fonctions.menage_tuple(["95o","84o","73o","62o"],G3_outsuited)
       
                    
                
        G3=[x[:-1] for x in G3_suited if x[:-1]+"o" in G3_outsuited]+[x for x in G3_suited if not x[:-1]+"o" in G3_outsuited]+[x for x in G3_outsuited if not x[:-1]+"s" in G3_suited]
        
        chaineG3 = poker_fonctions.menage_tuple(["95","84","73","62"],[x for x in G3])
        chaineG3 = chaineG3+poker_fonctions.menage_tuple(["95s","84s","73s","62s"],[x for x in G3])
        chaineG3 =chaineG3+ poker_fonctions.menage_tuple(["95o","84o","73o","62o"],[x for x in G3])      
        self.G3=chaineG3        
        self.factorise=tuple(factorise)
        
        self.paires=tuple(paires)
        
        
        #les mains  qui restent:
        mains_reste_s=[x for x in compte if compte[x]==4 and x[-1]=="s"]
        
        mains_reste_o=[x for x in compte if compte[x]==12 and x[-1]=="o" ]
        tampon = [x for x in tampon if not x[0]+x[2]+"s" in mains_reste_s and not x[0]+x[2]+"o" in mains_reste_o  ]
        mains_reste=[x[:-1] for x in mains_reste_s if x[:-1]+"o" in mains_reste_o]+[x for x in mains_reste_s if not x[:-1]+"o" in mains_reste_o]+[x for x in mains_reste_o if not x[:-1]+"s" in mains_reste_s]+tampon
        self.mains_reste=mains_reste     
        simplifie=",".join(list(self.paires_s))
        simplifie+=","+",".join(list(self.As))
        simplifie+=","+",".join(list(self.K))
        simplifie+=","+",".join(list(self.Q))
        simplifie+=","+",".join(list(self.J))
        simplifie+=","+",".join(list(self.T))
        simplifie+=","+",".join(list(self.G))
        simplifie+=","+",".join(list(self.G1))
        simplifie+=","+",".join(list(self.G2))
        simplifie+=","+",".join(list(self.G3))
        simplifie+=","+",".join(list(self.mains_reste))
        
        simplifie=(simplifie.split(","))
        simplifie=[x for x in simplifie if x!=""]
        #print("debug simplifie de chaine",simplifie)
        
        """ il faut simplifier les chaines qui commencent par:
        AA- AK- AKo- et AKs-"""
        
        for rg in range(len(simplifie)):
            #print(rg,simplifie[rg])
            if simplifie[rg][0:3] in ("AA-","AK-"):
                simplifie[rg]=str(simplifie[rg][3:])+"+"
            if simplifie[rg][0:4] in ("AKo-","AKs-"):
                simplifie[rg]=str(simplifie[rg][4:])+"+"
        #print (simplifie)
                
                
            
            
        simplifie=",".join(simplifie)          
        
        
        
        
        self.chaine=simplifie
        
        
        
        
    def __repr__(self):
        
        chaine= "Cet echantillon contient "+str(len(self.developpe))+" /1326 mains soit {0:.2f}% des mains. \n".format(100* len(self.developpe)/1326.0)
        chaine += "\n  Paires : "+",".join(list(self.paires_s))+"  ("+str(len(self.paires)*6)+" mains soit {0:.2f}% des mains)".format(600* len(self.paires)/1326.0)
        nb=len(self.As_suited)*4+len(self.As_outsuited)*12
        chaine +="\n"
        chaine += "\n  Ax : "+",".join(list(self.As))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format( 100*nb/1326.0)
        nb=len(self.K_suited)*4+len(self.K_outsuited)*12
        chaine += "\n  Kx : "+",".join(list(self.K))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100*nb/1326.0)
        nb=len(self.Q_suited)*4+len(self.Q_outsuited)*12
        chaine += "\n  Qx : "+",".join(list(self.Q))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100* nb/1326.0)
        nb=len(self.J_suited)*4+len(self.J_outsuited)*12
        chaine += "\n  Jx : "+",".join(list(self.J))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format( 100*nb/1326.0)
        nb=len(self.T_suited)*4+len(self.T_outsuited)*12
        chaine += "\n  Tx : "+",".join(list(self.T))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format( 100*nb/1326.0)
        chaine +="\n"
        nb=len(self.G_suited)*4+len(self.G_outsuited)*12
        chaine += "\n\n Sous les Broadways :\n\n  connecteurs : "+",".join(list(self.G))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100* nb/1326.0)
        nb=len(self.G1_suited)*4+len(self.G1_outsuited)*12
        chaine += "\n  1-Gapper : "+",".join(list(self.G1))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100* nb/1326.0)
        nb=len(self.G2_suited)*4+len(self.G2_outsuited)*12
        chaine += "\n  2-Gapper : "+",".join(list(self.G2))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100* nb/1326.0)
        nb=len(self.G3_suited)*4+len(self.G3_outsuited)*12
        chaine += "\n  3-Gapper : "+",".join(list(self.G3))+"  ("+str(nb)+" mains soit {0:.2f}% des mains)".format(100*nb/1326.0)
        chaine += "\n\n  "+",".join(self.mains_reste)
        
        return chaine    

class main5():
    def __init__(self,chaine):
        c = list(x for x in paquet if x in chaine)
        if len(c)!=5:
            self.chaine="".join(c)
            self.valeur="Erreur"
            self.flush=""
            self.commentaire=""
            return
        fl=(c[0][1]+c[1][1]+c[2][1]+c[3][1]+c[4][1] in ("hhhhh","sssss","ccccc","ddddd"))         
        c5=[x[0 ]for x in c]  
        if fl:
            flush= str(c[0][1])
        else:
            flush="rainbow" 
          
        self.flush=flush
        self.chaine="".join(c5)
        # valeur
        self.valeur="?"
        self.commentaire="EC"
        # c5 contient les 5 cartes ordonnés, fl booleen couleur
      
        # quinte flush ?
        if fl and ("".join(c5) in ("AKQJT98765432") or "".join(c5)=="A5432"):
            if "".join(c5)=="A5432":
                self.valeur=9
                self.commentaire="Quinte Flush hauteur 5"
            else:
                self.valeur=valeurs.index(c5[0])
                self.commentaire="Quinte Flush hauteur "+"".join(c5)[0]
            # les valeurs vont de 0 (meilleur) à 9             
         
         
         # carré?
        
        elif poker_fonctions.analyse_main(c5)[4]!=[]:
            
            a="".join(poker_fonctions.analyse_main(c5)[4])
            
            b="".join(poker_fonctions.analyse_main(c5)[1])
            self.valeur=13*valeurs.index(a)+valeurs.index(b)+10
          
            self.commentaire="Carré de "+ a +" avec un  "+b
             
            # Les valeurs des carrés vont de 11 à 177
                
        #full
        
        elif poker_fonctions.analyse_main(c5)[3]!=[] and poker_fonctions.analyse_main(c5)[2]!=[]:
            a="".join(poker_fonctions.analyse_main(c5)[3])
            
            b="".join(poker_fonctions.analyse_main(c5)[2])
                        
            self.commentaire="Full aux "+a +" par les "+b
            self.valeur=13*valeurs.index(a)+valeurs.index(b)+178 
           # full au 2 par les 3 valeur 345
           
        #couleur
        elif self.flush!="rainbow":
            self.commentaire="Couleur hauteur "+c5[0]
            
            self.valeur=valeurs.index(c5[0])*28561+valeurs.index(c5[1])*2197+valeurs.index(c5[2])*169+valeurs.index(c5[3])*13+valeurs.index(c5[4])+346
        #221891  
        
        #quinte 
        elif "".join(c5) in ("AKQJT98765432") or "".join(c5)=="A5432":
            self.valeur=221546 + valeurs.index(c5[1])
            if "".join(c5)=="A5432":
                hauteur=5
                self.valeur=221892+10
            else:
                hauteur=c5[0]
                self.valeur=221892 + valeurs.index(c5[1])
            self.commentaire="Quinte hauteur "+str(hauteur)
        # roue---221902
        
        
        #brelan 
        elif poker_fonctions.analyse_main(c5)[3]!=[]:
            a="".join(poker_fonctions.analyse_main(c5)[3])       
            b=poker_fonctions.analyse_main(c5)[1][0]
            c=poker_fonctions.analyse_main(c5)[1][1]
            self.commentaire="Brelan de "+str(a)+" avec "+str(b)+" et "+str(c)
            self.valeur=169*valeurs.index(a)+13*valeurs.index(b)+valeurs.index(c)+221903
            
            #22243 -----> 224072 
            
        #2 paires
        
        elif len(poker_fonctions.analyse_main(c5)[2])==2:
            a="".join(poker_fonctions.analyse_main(c5)[2][0])
            b="".join(poker_fonctions.analyse_main(c5)[2][1])
            c="".join(poker_fonctions.analyse_main(c5)[1])
            self.commentaire="2 paires "+a+" et "+b+ " (avec un "+c+")"
         
           
            self.valeur=169*valeurs.index(a)+13*valeurs.index(b)+valeurs.index(c)+224073
            # -------- 226098
            
        # 1 paire
        elif len(poker_fonctions.analyse_main(c5)[2])==1:
            a="".join(poker_fonctions.analyse_main(c5)[2])
            b="".join(poker_fonctions.analyse_main(c5)[1][0])
            c="".join(poker_fonctions.analyse_main(c5)[1][1])
            d="".join(poker_fonctions.analyse_main(c5)[1][2])
            self.commentaire="1 paire de "+a+" kicker "+b
            self.valeur=2197*valeurs.index(a)+169*valeurs.index(b)+13*valeurs.index(c)+valeurs.index(b)+226099
            
            #254123 
            
        elif len(poker_fonctions.analyse_main(c5)[1])==5:
            self.commentaire = " hauteur "+c5[0]
            self.valeur=valeurs.index(c5[0])*28561+valeurs.index(c5[1])*2197+valeurs.index(c5[2])*169+valeurs.index(c5[3])*13+valeurs.index(c5[4]) +  254124
       
            
            
            
            
           
            
        else: 
            print("debug...erreur inconnue OBJET main5")
            
              
                        
                        


          
      
            

    def __repr__(self):
        return self.chaine+"("+self.flush+") :"+str(self.valeur)+"    "+self.commentaire










        
            
               
def la_main(p1,p2,c1,c2,c3,c4,c5):
    #prend en paramètres 2 cartes privatives et les 5 cartes du board et renvoie la main de 5 cartes.
    #verifications :
    
    k=[p1,p2,c1,c2,c3,c4,c5]
    if set(k).issubset(set(list(paquet))) and len(set(k))==7:
        sa_valeur=1000000000
        
        #Les 5 cartes sont valides
        for i in range(7):
            for j in range(i):
                Une_main="".join(set(k)-set([k[i],k[j]]))
                if main5(Une_main).valeur<sa_valeur:
                    sa_valeur=main5(Une_main).valeur
                    La_main=Une_main
        
                         
        
        La_main=main5(La_main)
        return(La_main.chaine,La_main.valeur,La_main.commentaire)
    else:
       
        print ("Erreur")
        return 

def compare(dic):
    """reçoit un dictionnaire contenant les eventails des 6 joueurs en commençant par UTG et les 5 cartes du board
    
    format {UTG:eventail,MP:eventail,CO:eventail,BU:eventail,SB:eventail,BB:eventail, Flop1:carte, Flop2, Flop3, Turn, River}
    
    """
    precision=1000
    A=set(x for x in dic.keys())
    joueurs=list(A&set(('UTG','MP','CO','BU','SB','BB')))
    cards=list(A&set(('Flop1','Flop2','Flop3','Turn','River')))
    #print (joueurs, cards)
    for j in joueurs:
        if (type (dic[j]))!=eventail:
            if type(dic[j])==str:
                dic[j]=eventail(dic[j]) #On accepte aussi les chaines dans ce cas on crée l'éventail
    if len(joueurs)>1:        #La liste des joueurs contient au moins deux joueurs avec un éventail
        
        paquet_purge=list(paquet)
        for c in cards:
            if dic[c] not in paquet_purge:
                
                print ("ERREUR ",c,":",dic[c]," est ignoré")
                cards.remove(c)
            else:
                paquet_purge.remove(dic[c])
        
        
                
        gains={X:0 for X in joueurs}
        resultats={X:0 for X in joueurs}
        
        print("Patientez SVP")
        #print (gains)
        for distribution in range(precision):
            
            paq=list(paquet_purge)
            
            #print ("eventail,univers ,distribution, joueur" ,dic[j].developpe,univers,distribution, j)
            jeu7={X:[] for X in joueurs} # on prepare l'espace pour les cartes privatives
            #debug........................................................................................................................................
            
           
          
            
                    
                
            for c in cards:
                for jj in joueurs:
                     jeu7[jj].append(dic[c])
                
                if dic[c] in paq:
                    paq.remove(dic[c])
                     
            
           
              
            for jjj in joueurs:
                
                univers=[x for x in dic[jjj].developpe if x[:2] in paq and x[2:] in paq]
                
                if len(univers)<1:
                    print("ERREUR 101")
                    
                    return
                choix= choice(univers)
                paq.remove(choix[:2])
                paq.remove(choix[2:])
                jeu7[jjj].append(choix[:2])
                jeu7[jjj].append(choix[2:])
                #print ("eventail,univers ,distribution, joueur" ,dic[j].developpe,univers,distribution, j,la_main(*jeu7)[0])
                #print( jeu7)
                #print ("_________________",distribution,j,jeu7)          
                #print("0/",la_main(*jeu7)[0])
                #print("1/",la_main(*jeu7)[1])
                
                #print("2/",la_main(*jeu7)[2])
                #jeu[j]=la_main(*jeu7)[1]
                #G=[x for x in joueurs if jeu[x]==max(jeu.values())]
                
            for c in range(5-len(cards)):
                choix=choice(paq)
                paq.remove(choix)
                for jjjj in joueurs:
                    jeu7[jjjj].append(choix)  
                #print(jeu7)
            
            for j in joueurs:
                #print("debug",jeu7)
                resultats[j]=la_main(*jeu7[j])[1]
            
            #print ("resultats",resultats)
            lesgagnants=[]
            for jjj in joueurs:
                #print (min(resultats.values()))
                if resultats[jjj]==min(resultats.values()):
                    lesgagnants.append(jjj)
            #print (lesgagnants)
                    # les joueurs ont la meilleur main
            for lg in lesgagnants:
                gains[lg]+=(float(len(joueurs))/float(len(lesgagnants)))
        
        for g in gains:
            gains[g]=int(100*gains[g]/(precision*len(gains)))
        return (gains)
        
            
            #print (max(jeu.values()))     
            #
            #print ("G",G)
                 
                 
                 
                        
                  
                 
              
                
        
        
        
        


""""debug        

a = eventail("98+")
print (a.developpe)
print (a.factorise)
print (repr(a))

for i in a.developpe:
    aaaaa=i+"5s6s7s"
    print(repr(main5(aaaaa)))

print(la_main("As","Kd","Jh","Th","Kc","3c","3d"))"""




# compare({UTG:"50%",SB:"50%",Flop1:"Ah"})