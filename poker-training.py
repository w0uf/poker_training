#!/usr/local/bin/python
# coding: latin-1
#version 1.0.2

from tkinter import *
from poker import *
from xml.dom import minidom
import tkinter.filedialog
from tkinter import messagebox
import webbrowser 
        
joueur="" #nom du  du joueur en cours
jxml="" #URl du fichier xml du joueur en cours
eventails={} # tous les eventails du joueur en cours
questions=0
reponses=0

class Application(Tk):
    
    def __init__(self,parent):
        Tk.__init__(self,parent)       
        self.initialize()
        
    def initialize(self):
        global joueur,jxml,eventails,questions,reponses
        self.erreur_html=""
        
        self.grid()
        self.zone1 = Frame(self,borderwidth=2,relief=GROOVE)#eventail
        self.zone2 = Frame(self,borderwidth=2,relief=GROOVE)#parametre
        self.zone3 = Frame(self,borderwidth=2,relief=GROOVE) #comparer
        self.zone4 = Frame(self,borderwidth=2,relief=GROOVE) #associer
        self.zone5=  Frame(self,borderwidth=2,relief=GROOVE) #go
        #self.zone1bis = Frame(self,borderwidth=2,relief=GROOVE) #eventail visuel
        self.zonecouleur=Frame(self,borderwidth=2,relief=GROOVE)
       
        """ zone 1 ----------------------------------------------- eventail"""
        
        
        self.zone1.grid(column=0,row=0,sticky='EW')
        self.entry = Entry(self.zone1)
        self.entry.grid(column=0,row=0,  sticky='EW')
       
        self.entry.focus_set()
        self.entry.selection_range(0, END)
        self.bind("<Return>", self.OnPressEnter)
        
        self.button1 = Button(self.zone1,text=u"Texte",command=self.OnButton1Click)
        self.button1.grid(column=2,row=0)
        
        
        
        self.button2 = Button(self.zone1,text=u"Detail",command=self.OnButton2Click)
        self.button2.grid(column=3,row=0)
        
        self.buttonvisuel= Button(self.zone1, text=u"Visuel", command=self.visuel)
        self.buttonvisuel.grid(column=4,row=0)
        
        self.labelVariable=StringVar()
        self.label = Label(self.zone1,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue",wraplength=800,  justify=LEFT)
        
        self.label2 = Label(self.zone1,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue",wraplength=800,  justify=LEFT)
        
        self.label.grid(column=0,row=2,columnspan=500,sticky='EW')
        self.grid_columnconfigure(0,weight=1)
        
        
        
        
        
        """ zone 2 ----------------------------------------------- parametres"""
        self.labelz2=Label(self.zone2,text="JOUEUR :")
        self.NJ=StringVar()
        if joueur=="": #Variable globale
            self.NJ.set("Aucun")
        self.labelz3=Label(self.zone2,textvariable=self.NJ)
        self.labelz2.grid(column=0, row=0)
        self.labelz3.grid(column=1, row=0)
        self.bouton_charge_joueur=Button(self.zone2,text="Charger",command=lambda :self.charger())
        self.bouton_charge_joueur.grid(column=3, row=0)
        self.bouton_New_joueur=Button(self.zone2,text="New",command=lambda :self.new_joueur())
        self.bouton_New_joueur.grid(column=4, row=0)
        self.labelz4=Label(self.zone2,text="Hero :")
        self.labelz4.grid(column=0, row=2)
        self.labelz5=Label(self.zone2,text="Vilain :")
        self.labelz5.grid(column=0, row=3)
        self.travail={}
        self.bouton_travail={}
        i=1
        for p in positions:
            
            self.travail[p]=IntVar()
            self.bouton_travail[p]=Checkbutton(self.zone2,variable=self.travail[p], text=str(p) )
            self.bouton_travail[p].grid(row=2, column=i)
            
            i+=1
     
            
        self.opposants={}
        self.bouton_opposant={}
        i=1
        for p in positions:
            
            self.opposants[p]=IntVar()
            self.bouton_opposant[p]=Checkbutton(self.zone2,variable=self.opposants[p], text=str(p) )
            self.bouton_opposant[p].grid(row=3, column=i)
     
            i+=1
        
      
        for i in positions:
            self.travail[i].set(1)
            self.opposants[i].set(1)    
        
        
        self.w=Scale(self.zone2,from_=0, to=100, label=" Eventail des cartes privatives pour les exercices: (en %)", orient=HORIZONTAL, length=500)
        self.w.grid(column=0, row=5, columnspan=600) 
        self.w.set(50) 
        
        self.agr=Scale(self.zone2,from_=0, to=100, label=" Agressivité de la table (en %)", orient=HORIZONTAL, length=500)
        self.agr.grid(column=0, row=6, columnspan=600) 
        self.agr.set(50)
        
        
        try:
             filename=open('defaut.xml','r')
             docxml = minidom.parse(filename)
             nj=docxml.getElementsByTagName('joueur')[0].attributes["Nom"].value
             reflist=docxml.getElementsByTagName('eventail')
             n=len(reflist)
             
             for i in range(n): 
                 a=(reflist[i].attributes["id"].value)   
                 b=(docxml.getElementsByTagName('eventail')[i].childNodes[0].nodeValue)
                 #print (a,b)
                 eventails[str(a).strip()]=str(b).strip()
             #print (eventails)
             if  len(nj)>0 :
                 #les variables  joueur et eventail sont ok
                 self.NJ.set(nj)
                 jxml="defaut.xml"
                 joueur=nj
             
        except:
            filename=open('defaut.xml','w')
            
            ch='''<?xml version="1.0"?>
<?xml-stylesheet type="application/xml" href="modele_joueur.xsl"?>'''
            filename.write(ch)
            filename.write('\n<joueur Nom= "Defaut">')
           
            for i in range(96):
                filename.write('\n<eventail id="'+str(i+1)+'">')
                filename.write('\n')
                filename.write('\n</eventail>')
                eventails[str(i).strip()]=""
            filename.write('</joueur>') 
                  
            filename.close()
            self.NJ.set("défaut") 
            #print("debug new joueur nom",str(j),"file",file)
            joueur="Defaut"
            jxml='defaut.xml'
                
        
        """ zone 3 -----------------------------------------------comparer"""
        
        self.labelVariable1=StringVar()
        self.label_utg=Label(self.zone3,text="UTG")
        self.label_utg.grid(row=1)
        self.entry_utg=Entry(self.zone3)
        self.entry_utg.grid(column=2,row=1,sticky='EW')
        self.label_utg_r=Label(self.zone3,textvariable=self.labelVariable1)
        self.label_utg_r.grid(row=1,column=3)
        
        self.labelVariable2=StringVar()
        self.label_mp=Label(self.zone3,text="MP")
        self.label_mp.grid(row=2)
        self.entry_mp=Entry(self.zone3)
        self.entry_mp.grid(column=2,row=2,sticky='EW')
        self.label_mp_r=Label(self.zone3,textvariable=self.labelVariable2)
        self.label_mp_r.grid(row=2,column=3)
        
        self.labelVariable3=StringVar()
        self.label_co=Label(self.zone3,text="CO")
        self.label_co.grid(row=3)
        self.entry_co=Entry(self.zone3)
        self.entry_co.grid(column=2,row=3,sticky='EW')
        self.label_co_r=Label(self.zone3,textvariable=self.labelVariable3)
        self.label_co_r.grid(row=3,column=3)
        
        self.labelVariable4=StringVar()
        self.label_bu=Label(self.zone3,text="BU")
        self.label_bu.grid(row=4)
        self.entry_bu=Entry(self.zone3)
        self.entry_bu.grid(column=2,row=4,sticky='EW')
        self.label_bu_r=Label(self.zone3,textvariable=self.labelVariable4)
        self.label_bu_r.grid(row=4,column=3)
        
        self.labelVariable5=StringVar()
        self.label_sb=Label(self.zone3,text="SB")
        self.label_sb.grid(row=5)
        self.entry_sb=Entry(self.zone3)
        self.entry_sb.grid(column=2,row=5,sticky='EW')
        self.label_sb_r=Label(self.zone3,textvariable=self.labelVariable5)
        self.label_sb_r.grid(row=5,column=3)
        
        self.labelVariable6=StringVar()
        self.label_bb=Label(self.zone3,text="BB")
        self.label_bb.grid(row=6)
        self.entry_bb=Entry(self.zone3)
        self.entry_bb.grid(column=2,row=6,sticky='EW')
        self.label_bb_r=Label(self.zone3,textvariable=self.labelVariable6)
        self.label_bb_r.grid(row=6,column=3)
        
        
        self.bouton_calcul=Button(self.zone3,text=u"Calcul",command=lambda : self.OnButton_calcul_Clic())
        self.bouton_calcul.grid(row=7,column=5)
        self.grid_columnconfigure(0,weight=2)
        
        
        
        self.label_flop=Label(self.zone3,text="FLOP :")
        self.label_flop.grid(row=1,column=4,columnspan =4)
        
        self.entry_f1=Entry(self.zone3)
        self.entry_f1.grid(column=4, row=2)
        self.entry_f2=Entry(self.zone3)
        self.entry_f2.grid(column=5, row=2)
        self.entry_f3=Entry(self.zone3)
        self.entry_f3.grid(column=6, row=2)

        self.label_turn=Label(self.zone3,text="TURN :")
        self.label_turn.grid(row=3,column=4,columnspan =4)
        
        self.entry_turn=Entry(self.zone3)
        self.entry_turn.grid(column=5, row=4)
       
        
        self.label_river=Label(self.zone3,text="RIVER :")
        self.label_river.grid(row=5,column=4,columnspan =4)
        self.entry_river=Entry(self.zone3)
        self.entry_river.grid(column=5, row=6)
        
        """zone 4--------------------------------------Associer"""
        
        
        self.labelev=Label(self.zone4,text="Eventail :")
        self.labelev.grid(column=0,row=0)
        self.buttone=Button(self.zone4,text="Aucun", command= lambda : self.initzone1())
        self.buttone.grid(column=1,row=0)     
        self.labelj=Label(self.zone4,text="JOUEUR : ")
        self.labelj.grid(column=2,row=0)
        self.buttonj=Button(self.zone4,text="Aucun", command= lambda : self.parametres())
        self.buttonj.grid(column=3,row=0)
        self.retour=IntVar() # cree une variable entiere pour recevoir la valeur retour
     
        
        self.id1=Radiobutton(self.zone4, text="UTG, Open Raise", variable=self.retour, value=1)
        self.id2=Radiobutton(self.zone4, text="UTG VS 3B MP - CALL", variable=self.retour, value=2)
        self.id3=Radiobutton(self.zone4, text="UTG VS 3B MP - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=3)
        self.id4=Radiobutton(self.zone4, text="UTG VS 3B MP - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=4)
      
        self.id5=Radiobutton(self.zone4, text="UTG VS 3B CO - CALL", variable=self.retour, value=5)
        self.id6=Radiobutton(self.zone4, text="UTG VS 3B CO - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=6)
        self.id7=Radiobutton(self.zone4, text="UTG VS 3B CO - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=7)
        
        self.id8=Radiobutton(self.zone4, text="UTG VS 3B BU - CALL", variable=self.retour, value=8)
        self.id9=Radiobutton(self.zone4, text="UTG VS 3B BU - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=9)
        self.id10=Radiobutton(self.zone4, text="UTG VS 3B BU - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=10)
        
        self.id11=Radiobutton(self.zone4, text="UTG VS 3B SB - CALL", variable=self.retour, value=11)
        self.id12=Radiobutton(self.zone4, text="UTG VS 3B SB - 4Bet Bluf: (Fold sur 5Bet) ", variable=self.retour, value=12)
        self.id13=Radiobutton(self.zone4, text="UTG VS 3B SB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=13)
        
        self.id14=Radiobutton(self.zone4, text="UTG VS 3B BB - CALL", variable=self.retour, value=14)
        self.id15=Radiobutton(self.zone4, text="UTG VS 3B BB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=15)
        self.id16=Radiobutton(self.zone4, text="UTG VS 3B BB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=16)
        
        self.id17=Radiobutton(self.zone4, text="MP, Open Raise", variable=self.retour, value=17)
        self.id18=Radiobutton(self.zone4, text="MP VS Open Raise UTG - CALL", variable=self.retour, value=18)
        self.id19=Radiobutton(self.zone4, text="MP VS Open Raise UTG - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=19)
        self.id20=Radiobutton(self.zone4, text="MP VS Open Raise UTG - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=20)
      
        self.id21=Radiobutton(self.zone4, text="MP VS 3B CO - CALL", variable=self.retour, value=21)
        self.id22=Radiobutton(self.zone4, text="MP VS 3B CO - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=22)
        self.id23=Radiobutton(self.zone4, text="MP VS 3B CO - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=23)
        
        self.id24=Radiobutton(self.zone4, text="MP VS 3B BU - CALL", variable=self.retour, value=24)
        self.id25=Radiobutton(self.zone4, text="MP VS 3B BU - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=25)
        self.id26=Radiobutton(self.zone4, text="MP VS 3B BU - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=26)
        
        self.id27=Radiobutton(self.zone4, text="MP VS 3B SB - CALL", variable=self.retour, value=27)
        self.id28=Radiobutton(self.zone4, text="MP VS 3B SB - 4Bet Bluf: (Fold sur 5Bet) ", variable=self.retour, value=28)
        self.id29=Radiobutton(self.zone4, text="MP VS 3B SB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=29)
        
        self.id30=Radiobutton(self.zone4, text="MP VS 3B BB - CALL", variable=self.retour, value=30)
        self.id31=Radiobutton(self.zone4, text="MP VS 3B BB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=31)
        self.id32=Radiobutton(self.zone4, text="MP VS 3B BB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=32)
        
        self.id33=Radiobutton(self.zone4, text="CO, Open Raise", variable=self.retour, value=33)
        self.id34=Radiobutton(self.zone4, text="CO VS Open Raise UTG - CALL", variable=self.retour, value=34)
        self.id35=Radiobutton(self.zone4, text="CO VS Open Raise UTG - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=35)
        self.id36=Radiobutton(self.zone4, text="CO VS Open Raise UTG - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=36)
      
        self.id37=Radiobutton(self.zone4, text="CO VS Open Raise MP - CALL", variable=self.retour, value=37)
        self.id38=Radiobutton(self.zone4, text="CO VS Open Raise MP - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=38)
        self.id39=Radiobutton(self.zone4, text="CO VS Open Raise MP - 4Bet en Value (Call sur 4Bet) ", variable=self.retour, value=39)
        
        self.id40=Radiobutton(self.zone4, text="CO VS 3B BU - CALL", variable=self.retour, value=40)
        self.id41=Radiobutton(self.zone4, text="CO VS 3B BU - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=41)
        self.id42=Radiobutton(self.zone4, text="CO VS 3B BU - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=42)
        
        self.id43=Radiobutton(self.zone4, text="CO VS 3B SB - CALL", variable=self.retour, value=43)
        self.id44=Radiobutton(self.zone4, text="CO VS 3B SB - 4Bet Bluf: (Fold sur 5Bet) ", variable=self.retour, value=44)
        self.id45=Radiobutton(self.zone4, text="CO VS 3B SB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=45)
        
        self.id46=Radiobutton(self.zone4, text="CO VS 3B BB - CALL", variable=self.retour, value=46)
        self.id47=Radiobutton(self.zone4, text="CO VS 3B BB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=47)
        self.id48=Radiobutton(self.zone4, text="CO VS 3B BB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=48)
        
        self.id49=Radiobutton(self.zone4, text="BU, Open Raise", variable=self.retour, value=49)
        self.id50=Radiobutton(self.zone4, text="BU VS Open Raise UTG", variable=self.retour, value=50)
        self.id51=Radiobutton(self.zone4, text="BU VS Open Raise UTG - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=51)
        self.id52=Radiobutton(self.zone4, text="BU VS Open raise UTG - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=52)
      
        self.id53=Radiobutton(self.zone4, text="BU VS Open Raise MP - CALL", variable=self.retour, value=53)
        self.id54=Radiobutton(self.zone4, text="BU VS Open Raise MP - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=54)
        self.id55=Radiobutton(self.zone4, text="BU VS Open Raise MP - 3Bet en Value (5Bet sur 4Bet)", variable=self.retour, value=55)
        
        self.id56=Radiobutton(self.zone4, text="BU VS Open Raise CO - CALL", variable=self.retour, value=56)
        self.id57=Radiobutton(self.zone4, text="BU VS Open Raise CO - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=57)
        self.id58=Radiobutton(self.zone4, text="BU VS Open Raise CO - 3Bet en Value (5Bet sur 4Bet)", variable=self.retour, value=58)
        
        self.id59=Radiobutton(self.zone4, text="BU VS 3B SB - CALL", variable=self.retour, value=59)
        self.id60=Radiobutton(self.zone4, text="BU VS 3B SB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=60)
        self.id61=Radiobutton(self.zone4, text="BU VS 3B SB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=61)
        
            
        self.id62=Radiobutton(self.zone4, text="BU VS 3B BB - CALL", variable=self.retour, value=62)
        self.id63=Radiobutton(self.zone4, text="BU VS 3B BB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=63)
        self.id64=Radiobutton(self.zone4, text="BU VS 3B BB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=64)
        
        self.id65=Radiobutton(self.zone4, text="SB, Open Raise", variable=self.retour, value=65)
        self.id66=Radiobutton(self.zone4, text="SB VS Open Raise UTG - CALL", variable=self.retour, value=66)
        self.id67=Radiobutton(self.zone4, text="SB VS Open Raise UTG - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=67)
        self.id68=Radiobutton(self.zone4, text="SB VS Open Raise UTG - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=68)
      
        self.id69=Radiobutton(self.zone4, text="SB VS Open Raise MP - CALL", variable=self.retour, value=69)
        self.id70=Radiobutton(self.zone4, text="SB VS Open Raise MP - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=70)
        self.id71=Radiobutton(self.zone4, text="SB VS Open Raise MP - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=71)
        
        self.id72=Radiobutton(self.zone4, text="SB VS Open Raise CO - CALL", variable=self.retour, value=72)
        self.id73=Radiobutton(self.zone4, text="SB VS Open Raise CO - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=73)
        self.id74=Radiobutton(self.zone4, text="SB VS Open Raise CO - 3Bet en Value (5Bet sur 4Bet)  ", variable=self.retour, value=74)
        
        self.id75=Radiobutton(self.zone4, text="SB VS Open Raise BU - CALL", variable=self.retour, value=75)
        self.id76=Radiobutton(self.zone4, text="SB VS Open Raise BU - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=76)
        self.id77=Radiobutton(self.zone4, text="SB VS Open Raise CO - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=77)
        
        self.id78=Radiobutton(self.zone4, text="SB VS 3B BB - CALL", variable=self.retour, value=78)
        self.id79=Radiobutton(self.zone4, text="SB VS 3B BB - 4Bet Bluff (Fold sur 5Bet) ", variable=self.retour, value=79)
        self.id80=Radiobutton(self.zone4, text="SB VS 3B BB - 4Bet en Value (Call sur 5Bet) ", variable=self.retour, value=80)
        
        self.id81=Radiobutton(self.zone4, text="BB, Open Raise", variable=self.retour, value=81)
        self.id82=Radiobutton(self.zone4, text="BB VS Open Raise UTG - CALL", variable=self.retour, value=82)
        self.id83=Radiobutton(self.zone4, text="BB VS Open Raise UTG - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=83)
        self.id84=Radiobutton(self.zone4, text="BB VS Open Raise UTG - 3Bet en Value (5Bet sur 4Bet) ", variable=self.retour, value=84)
      
        self.id85=Radiobutton(self.zone4, text="BB VS Open Raise MP - CALL", variable=self.retour, value=85)
        self.id86=Radiobutton(self.zone4, text="BB VS Open Raise MP - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=86)
        self.id87=Radiobutton(self.zone4, text="BB VS Open Raise MP - 3Bet en Value (Call sur 4Bet) ", variable=self.retour, value=87)
        
        self.id88=Radiobutton(self.zone4, text="BB VS Open Raise CO - CALL", variable=self.retour, value=88)
        self.id89=Radiobutton(self.zone4, text="BB VS Open Raise CO - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=89)
        self.id90=Radiobutton(self.zone4, text="BB VS Open Raise CO - 3Bet en Value (Call sur 4Bet) ", variable=self.retour, value=90)
        
        self.id91=Radiobutton(self.zone4, text="BB VS Open Raise BU - CALL", variable=self.retour, value=91)
        self.id92=Radiobutton(self.zone4, text="BB VS Open Raise BU - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=92)
        self.id93=Radiobutton(self.zone4, text="BB VS Open Raise BU - 3Bet en Value (Call sur 4Bet) ", variable=self.retour, value=93)
        
        self.id94=Radiobutton(self.zone4, text="BB VS Open Raise SB - CALL", variable=self.retour, value=94)
        self.id95=Radiobutton(self.zone4, text="BB VS Open Raise SB - 3Bet Bluff (Fold sur 4Bet) ", variable=self.retour, value=95)
        self.id96=Radiobutton(self.zone4, text="BB VS Open Raise SB - 3Bet en Value (Call sur 4Bet) ", variable=self.retour, value=96)
        
        
        self.id1.grid(column=0,row=1, sticky=W)
        self.id2.grid(column=0,row=2, sticky=W)
        self.id3.grid(column=0,row=3,sticky=W)
        self.id4.grid(column=0,row=4,sticky=W)
        self.id5.grid(column=0,row=5, sticky=W)
        self.id6.grid(column=0,row=6, sticky=W)
        self.id7.grid(column=0,row=7,sticky=W)
        self.id8.grid(column=0,row=8, sticky=W)
        self.id9.grid(column=0,row=9, sticky=W)
        self.id10.grid(column=0,row=10,sticky=W)
        self.id11.grid(column=0,row=11, sticky=W)
        self.id12.grid(column=0,row=12, sticky=W)
        self.id13.grid(column=0,row=13,sticky=W)
        self.id14.grid(column=0,row=14, sticky=W)
        self.id15.grid(column=0,row=15, sticky=W)
        self.id16.grid(column=0,row=16,sticky=W)
        
        self.id17.grid(column=1,row=1, sticky=W)
        self.id18.grid(column=1,row=2, sticky=W)
        self.id19.grid(column=1,row=3,sticky=W)
        self.id20.grid(column=1,row=4,sticky=W)
        self.id21.grid(column=1,row=5, sticky=W)
        self.id22.grid(column=1,row=6, sticky=W)
        self.id23.grid(column=1,row=7,sticky=W)
        self.id24.grid(column=1,row=8, sticky=W)
        self.id25.grid(column=1,row=9, sticky=W)
        self.id26.grid(column=1,row=10,sticky=W)
        self.id27.grid(column=1,row=11, sticky=W)
        self.id28.grid(column=1,row=12, sticky=W)
        self.id29.grid(column=1,row=13,sticky=W)
        self.id30.grid(column=1,row=14, sticky=W)
        self.id31.grid(column=1,row=15, sticky=W)
        self.id32.grid(column=1,row=16,sticky=W)
        
        self.id33.grid(column=2,row=1, sticky=W)
        self.id34.grid(column=2,row=2, sticky=W)
        self.id35.grid(column=2,row=3,sticky=W)
        self.id36.grid(column=2,row=4,sticky=W)
        self.id37.grid(column=2,row=5, sticky=W)
        self.id38.grid(column=2,row=6, sticky=W)
        self.id39.grid(column=2,row=7,sticky=W)
        self.id40.grid(column=2,row=8, sticky=W)
        self.id41.grid(column=2,row=9, sticky=W)
        self.id42.grid(column=2,row=10,sticky=W)
        self.id43.grid(column=2,row=11, sticky=W)
        self.id44.grid(column=2,row=12, sticky=W)
        self.id45.grid(column=2,row=13,sticky=W)
        self.id46.grid(column=2,row=14, sticky=W)
        self.id47.grid(column=2,row=15, sticky=W)
        self.id48.grid(column=2,row=16,sticky=W)
        
        self.separation=Label(self.zone4,text=4*"-------------------------------------------------")
        self.separation.grid(row=17,columnspan=3)
        
        self.id49.grid(column=0,row=18, sticky=W)
        self.id50.grid(column=0,row=19, sticky=W)
        self.id51.grid(column=0,row=20,sticky=W)
        self.id52.grid(column=0,row=21,sticky=W)
        self.id53.grid(column=0,row=22, sticky=W)
        self.id54.grid(column=0,row=23, sticky=W)
        self.id55.grid(column=0,row=24,sticky=W)
        self.id56.grid(column=0,row=25, sticky=W)
        self.id57.grid(column=0,row=26, sticky=W)
        self.id58.grid(column=0,row=27,sticky=W)
        self.id59.grid(column=0,row=28, sticky=W)
        self.id60.grid(column=0,row=29, sticky=W)
        self.id61.grid(column=0,row=30,sticky=W)
        self.id62.grid(column=0,row=31, sticky=W)
        self.id63.grid(column=0,row=32, sticky=W)
        self.id64.grid(column=0,row=33,sticky=W)
        
        self.id65.grid(column=1,row=18, sticky=W)
        self.id66.grid(column=1,row=19, sticky=W)
        self.id67.grid(column=1,row=20,sticky=W)
        self.id68.grid(column=1,row=21,sticky=W)
        self.id69.grid(column=1,row=22, sticky=W)
        self.id70.grid(column=1,row=23, sticky=W)
        self.id71.grid(column=1,row=24,sticky=W)
        self.id72.grid(column=1,row=25, sticky=W)
        self.id73.grid(column=1,row=26, sticky=W)
        self.id74.grid(column=1,row=27,sticky=W)
        self.id75.grid(column=1,row=28, sticky=W)
        self.id76.grid(column=1,row=29, sticky=W)
        self.id77.grid(column=1,row=30,sticky=W)
        self.id78.grid(column=1,row=31, sticky=W)
        self.id79.grid(column=1,row=32, sticky=W)
        self.id80.grid(column=1,row=33,sticky=W)
        
        self.id81.grid(column=2,row=18, sticky=W)
        self.id82.grid(column=2,row=19, sticky=W)
        self.id83.grid(column=2,row=20,sticky=W)
        self.id84.grid(column=2,row=21,sticky=W)
        self.id85.grid(column=2,row=22, sticky=W)
        self.id86.grid(column=2,row=23, sticky=W)
        self.id87.grid(column=2,row=24,sticky=W)
        self.id88.grid(column=2,row=25, sticky=W)
        self.id89.grid(column=2,row=26, sticky=W)
        self.id90.grid(column=2,row=27,sticky=W)
        self.id91.grid(column=2,row=28, sticky=W)
        self.id92.grid(column=2,row=29, sticky=W)
        self.id93.grid(column=2,row=30,sticky=W)
        self.id94.grid(column=2,row=31, sticky=W)
        self.id95.grid(column=2,row=32, sticky=W)
        self.id96.grid(column=2,row=33,sticky=W)
        
        self.enregistrer=Button(self.zone4,text='ENREGISTRER', command= lambda :self.modifierjoueur())
        self.enregistrer.grid(column=0,row=34)
        self.voirB=Button(self.zone4,text='VOIR', command= lambda :self.voir_ev_joueur())
        self.voirB.grid(column=2,row=34)
        """zone5"""
        photo = PhotoImage(file="2c.png")
        self.canvas=Canvas(self.zone5, width=68, height=92, background='white')
        self.canvas.create_image(0,0, image=photo,anchor = NW )
        self.canvas.image=photo
        
        photo2 = PhotoImage(file="2d.png")
        self.canvas2=Canvas(self.zone5, width=68, height=92, background='white')
        self.canvas2.create_image(0,0, image=photo2,anchor = NW )
        self.canvas2.image=photo2
        
        self.canvas.grid(column=1, row=1)
        self.canvas2.grid(column=2, row=1)
       
        self.label_position_z5=Label(self.zone5, text= "Position / VS ")
        self.label_position_z5.grid(column=3, row=1)
        
       
        self.label_score_z5=Label(self.zone5, text="")
        self.label_score_z5.grid(column=1, row=3)
        
        self.foldB=Button(self.zone5, text="FOLD", command=lambda: self.Fold())
        self.callB=Button(self.zone5, text="CALL", command=lambda: self.Call())
        self.raiseB=Button(self.zone5, text="RAISE", command=lambda: self.Raise())
        self.foldB.grid(column=1,row=4)
        self.callB.grid(column=2,row=4)
        self.raiseB.grid(column=3,row=4)
        
        
        
        self.resizable(False,False)
        self.menubar=Menu(self)
        self.menuE=Menu(self.menubar, tearoff=0)
        self.menuE.add_command(label="Etudier...", command=lambda: self.associer(self.entry.get()))
        self.menuE.add_command(label="Nouveau", command=lambda: self.initzone1())
        self.menuE.add_command(label="Comparer", command=lambda: self.comparer())
        self.menuE.add_command(label="Ouvrir...", command=lambda: self.ouvre_eventail())
        self.menuE.add_command(label="Sauvegarder...", command=lambda: self.sauve_eventail(self.entry.get()))
        
        self.menuE.add_command(label="XML" ,command=lambda : self.voir_xml())
        
        self.menubar.add_cascade(label="Eventail",menu=self.menuE)
        
        self.menuT=Menu(self.menubar, tearoff=0)
        self.menuT.add_command(label="Parametres", command=lambda: self.parametres())
        self.menuT.add_command(label="Go!", command=lambda: self.go())
        self.menuT.add_command(label="Reset score", command=lambda: self.init_score())
        self.menuT.add_command(label="Revue d'erreurs", command=lambda: self.mes_erreurs())
        self.menubar.add_cascade(label="training",menu=self.menuT)
        
        
        
        self.menuA=Menu(self.menubar, tearoff=0)
        self.menuA.add_command(label="Sur le Web", command=lambda  :webbrowser.open(u"http://site2wouf.fr/poker-training.php") )
        self.menubar.add_cascade(label="A propos",menu=self.menuA)
        self.config(menu=self.menubar)
        
        
    def OnButton_calcul_Clic(self):
        dico={}
        if len(eventail(self.entry_utg.get()).developpe)>0:
            dico["UTG"]=eventail(self.entry_utg.get()).chaine                
            
        if len(eventail(self.entry_mp.get()).developpe)>0:
            dico["MP"]=eventail(self.entry_mp.get()).chaine   
            
        if len(eventail(self.entry_co.get()).developpe)>0:
            dico["CO"]=eventail(self.entry_co.get()).chaine  
            
        if len(eventail(self.entry_bu.get()).developpe)>0:
            dico["BU"]=eventail(self.entry_bu.get()).chaine   
            
        if len(eventail(self.entry_sb.get()).developpe)>0:
            dico["SB"]=eventail(self.entry_sb.get()).chaine 
            
        if len(eventail(self.entry_bb.get()).developpe)>0:
            dico["BB"]=eventail(self.entry_bb.get()).chaine  

        if self.entry_f1.get() in paquet:
            dico["Flop1"]=self.entry_f1.get()
            
        if self.entry_f2.get() in paquet:
            dico["Flop2"]=self.entry_f2.get()
            
        if self.entry_f3.get() in paquet:
            dico["Flop3"]=self.entry_f3.get()
      
        if self.entry_turn.get() in paquet:
            dico["Turn"]=self.entry_turn.get()
            
        if self.entry_river.get() in paquet:
            dico["River"]=self.entry_river.get()
            
            
         
        resultats={} 
        try: 
            resultats=compare(dico)
        except:
            pass
        
        try:
            if "UTG" in resultats.keys():
                self.labelVariable1.set(str(resultats["UTG"])+"%")
            if "MP" in resultats.keys():
                self.labelVariable2.set(str(resultats["MP"])+"%")
            if "CO" in resultats.keys():
                self.labelVariable3.set(str(resultats["CO"])+"%")
            if "BU" in resultats.keys():
                self.labelVariable4.set(str(resultats["BU"])+"%")
            if "SB" in resultats.keys():
                self.labelVariable5.set(str(resultats["SB"])+"%")
            if "BB" in resultats.keys():
                self.labelVariable6.set(str(resultats["BB"])+"%")
        except:
              pass  
        
       
    def oublie(self):
        self.zone1.grid_forget()
        self.zone2.grid_forget()
        self.zone3.grid_forget()
        self.zone4.grid_forget()
        self.zone5.grid_forget()
        self.label.grid_forget()
        self.label2.grid_forget()
        self.zonecouleur.grid_forget()
        
    def initzone1(self):
        self.oublie()
        self.zone1.grid()
        self.label.grid(column=0,row=2,columnspan=500,sticky='EW')
        
    def initzone1bis (self):
        self.oublie()
        self.zone1.grid(column=0,row=2,columnspan=500,sticky='EW')
        
        self.label2.grid(columnspan=10)
        
    def initzone2(self):
        self.oublie()
        self.zone2.grid()
        
    def initzone3(self):
        self.oublie()
        self.zone3.grid()
        
    def initzone4(self):
        self.oublie()
        self.zone4.grid()
        
    def initzone5(self):
        self.oublie()
        self.zone5.grid()
            
    def comparer(self):
        self.oublie()
        self.initzone3()
            
    def ouvre_eventail(self):
        self.initzone1()
        try:
            filename = open(tkinter.filedialog.askopenfilename(),"r")
            
            contenu=filename.read()
            filename.close
            self.entry.delete(0,END)
            self.entry.insert(0,contenu)
            self.labelVariable.set("")
            
        except:
            pass
        
    def sauve_eventail(self,e):
        self.initzone1()
        filename = tkinter.filedialog.asksaveasfile()
        try:   
            filename.write(e)
            filename.close()
        except :
            pass
         
        
    def OnButton1Click(self):
        self.initzone1()
        Q=self.entry.get()
               
        self.labelVariable.set(eventail(Q))
        self.formatechaine(Q)
        
    def OnButton2Click(self):
        self.initzone1()
        Q=self.entry.get()
        
        
        self.labelVariable.set(eventail(Q).developpe)
        self.formatechaine(Q)
        
      
     
    def formatechaine(self,Q):
        contenu= eventail(Q).chaine
        self.entry.delete(0,END)
        self.entry.insert(0,contenu) 
        
         
    def OnPressEnter(self,event):
        self.OnButton1Click()
        


    def parametres(self):
        self.initzone2()
        self.zone2.grid()
        
        
    def charger (self): #charge un joueur
        global joueur,jxml,eventails
        try:
             thefile=tkinter.filedialog.askopenfilename()
             filename2 = open(thefile,"r")  
             #debug:
             docxml = minidom.parse(filename2)
             nj=docxml.getElementsByTagName('joueur')[0].attributes["Nom"].value
             reflist=docxml.getElementsByTagName('eventail')
             n=len(reflist)
             
             for i in range(n): 
                 a=(reflist[i].attributes["id"].value)   
                 b=(docxml.getElementsByTagName('eventail')[i].childNodes[0].nodeValue)
                 #print (a,b)
                 eventails[str(a).strip()]=str(b).strip()
             #print (eventails)
             if  len(nj)>0 :
                 #les variables  joueur et eventail sont ok
                 self.NJ.set(nj)
                 jxml=thefile
                 joueur=nj
                
             
            
             
             webbrowser.open(thefile)
             #webbrowser.open(urllib.request.pathname2url(filename2))
        except:
            pass
    def voir_xml(self):
        try:
            webbrowser.open(jxml)
        except:
            pass
        
                
    def new_joueur(self):
            global joueur,jxml, eventails
            try:
                filename = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".xml")
                file=filename.name
                j=filename.name.split("/")[-1]
                j=j.split(".")[0]
                if filename.name[-4:]!=".xml":
                    filename=filename.name+".xmll"
                    file=str(filename)
                    filename=open(filename,"w")
                ch='''<?xml version="1.0"?>
<?xml-stylesheet type="application/xml" href="modele_joueur.xsl"?>'''
                filename.write(ch)
                filename.write('\n<joueur Nom="'+str(j)+'">')
               
                for i in range(96):
                    filename.write('\n<eventail id="'+str(i+1)+'"> </eventail>')
                    eventails[str(i).strip()]=""
                filename.write('</joueur>') 
                      
                filename.close()
                self.NJ.set(str(j)) 
                #print("debug new joueur nom",str(j),"file",file)
                joueur=str(j)
                jxml=file
            except:
                pass
       
        
    def associer(self,un_eventail):
        self.initzone4()
        b=self.entry.get()
        if b=="":
            b="Aucun"
        self.buttone.config(text=b)
        self.buttone.grid()
        #print("Debug---ASSOCIER----",self.NJ.get(),joueur,jxml)
        self.buttonj.config(text=self.NJ.get())  
        self.buttonj.grid()    
    
    def voir_ev_joueur(self):
        try:
            ancien_eventail=eventails[str(self.retour.get())] #dans le dictionnaire eventails les clefs sont des strings
        except:
            ancien_eventail=""
        self.entry.delete(0,END)
        self.entry.insert(0,ancien_eventail)
        self.visuel()
        
    def modifierjoueur(self):
        global eventails
        """print("debug- modifierjoueur",self.retour.get(),joueur,jxml, self.entry.get())
        "self.retour.get(),joueur,jxml contiennent respectivement le joueur, le xml, l id de l eventail a modifier et l eventail
        print(eventails)
        eventails est un dictionnaire qui contient tous les eventails du joueur en cours"""
        #print (joueur)
        nouvel_eventail=self.entry.get()
        #print("debug",eventails)
        if joueur=="":
            messagebox.showerror ("Erreur","Pas de joueur en cours")
        else:
            
            try:
                ancien_eventail=eventails[str(self.retour.get())] #dans le dictionnaire eventails les clefs sont des strings
            except:
                ancien_eventail=""
                
            #print (ancien_eventail,"--->",nouvel_eventail)
            if ancien_eventail==nouvel_eventail:
                messagebox.showerror ("Erreur","Eventails identiques")
                a=False
            elif nouvel_eventail=="":
                a=messagebox.askokcancel("Alerte !", "Suppression de l'eventail "+str(ancien_eventail)+"?")
            else:
                a=messagebox.askokcancel("Confirmation", "Ancien :"+str(ancien_eventail)+"\nNouveau :"+str(nouvel_eventail))
            if a:
                xmldoc=minidom.parse(jxml)
                listeventail=xmldoc.getElementsByTagName("eventail")
                for e in listeventail:
                   
                    i=e.getAttribute("id")
                    
                    if int(i)==self.retour.get():
                        e.firstChild.replaceWholeText(nouvel_eventail.strip()+" ")
                        eventails[str(i)]=nouvel_eventail
                # print(xmldoc.toxml())       
                n=open(jxml,"w")
                n.write(xmldoc.toxml())
                n.close()
             
    def go(self):
        travaillons=[x for x in positions if self.travail[x].get()]
        adversaires=[x for x in positions if self.opposants[x].get()]
        k=str(max(1,self.w.get())) # pour eviter un eventail vide
        petitpaquet=(eventail(k+"%").developpe)
        self.reponse={}
        self.erreur={"Call":"Mauvais call","Raise":"Mauvais Raise","Fold":"Mauvais Fold"}
        try:
            eventails_position= list(x for x in positions if eventails[str(positions.index(x)*16+1)]!="")
        except:
            eventails_position=()
            
        lescore=str(reponses)+"/"+str(questions)
        self.label_score_z5.config(text=lescore)
              

                
                
        
        agr=self.agr.get() #agressivité entre 0 et 100
        
        """
        eventails
        travaillons
        adversaires
        petitpaquet
        eventails_position
        sont ils acceptables pour une session d'entrainement ?
        
        
        
        """
        #print(eventails)
        alert_message=""
        if joueur=="":
            alert_message=u"Pas de joueur en mémoire !"
        elif len(list(u for u in travaillons if u not in eventails_position))>0:
            alert_message=u"Vous n'avez pas défini d'éventail pour les position(s) : "+ ",".join(u for u in travaillons if u not in eventails_position)
        elif len(travaillons)==0:
            alert_message=u"Pas de position de travail définie dans les paramètres"
        elif len(adversaires)==0:
            alert_message=u"Vous n'avez pas défini au moins un adversaire potentiel"
        elif len(adversaires)==1 and len(travaillons)==1 and adversaires[0]==travaillons[0]:
            alert_message=u"Le seul adversaire disponible ne peut être à la même position que vous !"
        if alert_message!="":
              messagebox.showerror("Erreur",alert_message)
              return
        
        #print("les eventails",eventails.keys())
        #print (eventails_position)
        a=choice(petitpaquet)
        self.a=a
        photo = PhotoImage(file=a[:2]+".png")
        
        self.canvas.create_image(0,0, image=photo,anchor = NW )
        self.canvas.image=photo
        photo2 = PhotoImage(file=a[2:]+".png")
        
        self.canvas2.create_image(0,0, image=photo2,anchor = NW )
        self.canvas2.image=photo2
        
        #print (travaillons,adversaires)
        
        pos=choice(travaillons)
        posx=positions.index(pos)
        adv=choice(list(a for a in adversaires if a!=pos))
        advx=positions.index(adv)
        
        #print(pos,posx,"VS",adv,advx)
        self.enonce=""
        if posx<advx :#hors position, OR ,  defense sur 3B ,ou defense sur 5B
            action=0
            
            # id openraise :positions.index(p)*16+1
            #print (eventail(eventails[str(posx*16+1)]).developpe)
            if self.mde(a,posx*16+1) and agr+randint(0,200)>150:
                action=1 #parfois on sera en défense 1 fois sur 4 en table passive 3 fois sur 4 en table agressive 
                #print(premier)
                #print('debug--->OR puis 4B?')
                #print(adv,posx*16+1+3*advx )
                u=id_ev(posx,advx,1) #u et u+1 sont les id des eventails de 4bet
                if (self.mde(a,u) or self.mde(a,u+1)) and agr+randint(0,200)>150:
                   # il est possible qu'on ait fait un 3 Bet
                   action=2
                                     
                    
            if action==0:
                
                
                self.reponse["Call"]= False
                
                
                self.reponse["Raise"]=self.mde(a,posx*16+1)
                
                
                self.reponse["Fold"]= not self.reponse["Raise"]
                
                
                
                self.erreur["Call"]="Limper en premier n'a pas beaucoup de sens ! \n"+self.bonnereponse()
                
                chaine =str(a)+" n'est pas dans votre éventail d'ouverture "+str(pos)+ "!"
                chaine+='\n'+eventails[str(posx*16+1)]
                chaine+="\n En cas d'erreur, vous pouvez corriger et reprendre ce training ! \n"+self.bonnereponse()
                self.erreur["Raise"]=chaine
                
                chaine =str(a)+" est dans votre éventail d'ouverture "+str(pos)+ "!"
                chaine+='\n'+eventails[str(posx*16+1)]
                chaine+="\n En cas d'erreur, vous pouvez corriger et reprendre ce training ! \n"+self.bonnereponse()
                self.erreur["Fold"]=chaine
                
                
                
                self.enonce="Vous êtes "+str(pos)+" et premier de parole. Que faites-vous ?"
                
            elif action==1:
                
                self.reponse["Call"]= self.mde(a,id_ev(posx,advx,0))    
               
                self.reponse["Raise"]=self.mde(a,id_ev(posx,advx,1)) or self.mde(a,id_ev(posx,advx,2))
                self.reponse["Fold"]= not (self.reponse["Raise"] or self.reponse["Call"])
                
               
                if self.estvide(13*posx+3*advx-1):
                    chaine="Vous n'avez pas d'éventail de Call en tant que "+str(pos)
                    chaine += " \n contre un 3B de "+ str(adv) +". Si c'est une omission vous pouvez corriger avant "
                    chaine += " \n de reprendre l'entainement ! \n"
                    chaine += self.bonnereponse()
                else:
                    chaine =" Non ! "+ str(a)+" n'est pas dans votre éventail pour suivre ce 3B."
                    chaine += '\n'+eventails[str(id_ev(posx,advx,0))]
                    chaine += "\n"+self.bonnereponse()
                    
                self.erreur["Call"]=chaine         
                
                if self.estvide(id_ev(posx,advx,1)) and self.estvide(id_ev(posx,advx,2)):
                    chaine="Vous n'avez pas d'éventail de 4Bet en tant que "+str(pos)       
                    chaine += "\n contre  un 3B de " +str(adv)
                    chaine +=" \n Il doit s'agir d'une omission !!!"
                    chaine += "\n"+self.bonnereponse()
                    
                else:
                    """ il faut considérer l eventail  de 4B total (bluf+ value)"""
                    e_1=eventail(eventails[str(id_ev(posx,advx,1))])
                    e_2=eventail(eventails[str(id_ev(posx,advx,2))])  
                    chaine_debug=e_1.chaine+","+e_2.chaine
                    #print (eventail(chaine_debug).chaine)  
                    chaine="Votre éventail de 4B total (En Bluff et en value) dans cette position est \n"   
                    chaine +=     eventail(chaine_debug).chaine
                    chaine += "\n C'est bien sur modifiable !"
                    chaine += "\n"+self.bonnereponse()
                self.erreur["Raise"]=chaine    
                    
                self.erreur["Fold"]="D'après votre plan de jeu, il ne faut pas être aussi frileux ! \n"+self.bonnereponse()                  
                                    #print("4b?")
                self.enonce="Vous êtes "+str(pos)+" et vous avez logiquement ouvert le pot."
                self.enonce+="\n Mais vous êtes confronté à un 3B de "+str(adv)+"."
                self.enonce+="\n Que faites-vous ?"
                
            elif action==2:
                self.reponse["Call"]= self.mde(a,id_ev(posx,advx,0))
                self.reponse["Raise"]= self.mde(a,id_ev(posx,advx,2))
                self.reponse["Fold"]= not (self.reponse["Call"] or self.reponse["Raise"])
                chaine="Votre range de 4Bet de Value est "
                if self.estvide(id_ev(posx,advx,2)):
                	chaine+="Vide !"
                else:
                	chaine += "\n"+ eventails[str(id_ev(posx,advx,2))]
                chaine += "\n"+self.bonnereponse()
                self.erreur["Call"]=chaine
                self.erreur["Raise"]=chaine
                self.erreur["Fold"]=chaine
                
                self.enonce="Vous êtes "+str(pos)+" et vous avez logiquement ouvert le pot."
                self.enonce+="\n Mais vous avez été confronté à un 3B de "+str(adv)+"."
                self.enonce+="\n 3Bet que vous avez relancé conformément à votre range."
                self.enonce+="\n Mais étiez vous en Bluf ou en Value ? "
                self.enonce+="\n Que faites-vous sur le 5Bet de "+str(adv)+"???" 
        
        else: #en position #défense sur OR ou  défense sur 4Bet
            
                #sur open raise  ou 3Bet de adv
                action=0 #defense sur OR
                if (self.mde(a,id_ev(posx,advx,1))  or self.mde(a,id_ev(posx,advx,2))) and agr+randint(0,200)>150: # 16p+1+3*(p-a-1)=19p-3a-2 or
                    #possibilité que ce soit un 4 Bet
                    action =1 #defence sur 4Bet
            
                if action==0:
                    self.reponse["Call"]= self.mde(a,id_ev(posx,advx,0))
                    self.reponse["Raise"]=self.mde(a,id_ev(posx,advx,1)) or self.mde(a,id_ev(posx,advx,2))
                    self.reponse["Fold"]= not self.reponse["Raise"] and not self.reponse["Call"]
                
                    self.enonce=str(adv)+" vient de faire un Open Raise. Vous êtes "+str(pos)+". Comment réagissez-vous ?"
                    if self.estvide(id_ev(posx,advx,0)):
                        chaine="Vous n'avez pas défini d'éventail de Call sur un Open Raise de "+str(adv)
                    else:
                    	chaine=str(a)+" n'est pas dans votre range de Call : \n"
                    	chaine += eventails[str(id_ev(posx,advx,0))]
                    chaine+="\n"+self.bonnereponse()
                    self.erreur["Call"]=chaine
                    
                    if self.estvide(id_ev(posx,advx,1)) and self.estvide(id_ev(posx,advx,2)):
                        chaine="Vous n'avez pas d'éventail de 3Bet en tant que "+str(pos)       
                        chaine += "\n contre  un 3B de " +str(adv)
                        chaine +=" \n Il doit s'agir d'une omission !!!"
                        chaine += "\n"+self.bonnereponse()
                    else:
                        """ il faut considérer l eventail  de 3B total (bluf+ value)"""
                        e_1=eventail(eventails[str(id_ev(posx,advx,1))])
                        e_2=eventail(eventails[str(id_ev(posx,advx,2))])  
                        chaine_debug=e_1.chaine+","+e_2.chaine
                        #print (eventail(chaine_debug).chaine)  
                        chaine="Votre éventail de 3B total (En Bluff et en value) dans cette position est \n"   
                        chaine +=     eventail(chaine_debug).chaine
                        chaine += "\n  Vous pouvez le corriger si nécessaire !"
                        chaine += "\n"+self.bonnereponse()
                    self.erreur["Raise"]=chaine 
                    self.erreur["Fold"]="Un fold est trop timoré ici ! \n"+self.bonnereponse()
                    
                else:
                    self.reponse["Call"]=False
                    self.reponse["Raise"]=self.mde(a,id_ev(posx,advx,2))
                    self.reponse["Fold"]=not self.reponse["Raise"]
                    self.erreur["Call"]="Un call est exclu ici !"+self.bonnereponse()
                    chaine="Votre plan de jeu ici est de finir all in avec \n"
                    chaine += eventails[str(id_ev(posx,advx,2))]
                    chaine += "\n"+self.bonnereponse()
                    
                    self.enonce="Conformément à votre plan de jeu vous avez réagi activement à l' Open Raise de "+str(adv)+ "par un 3Bet.\n Mais celui-ci ne se laisse pas faire !"
                    self.enonce+="\n Comment réagissez-vous à son 4Bet ? Vous êtes en position "+str(pos)
                    
                            
                     
             
                     
                     
                    
            
            
             
            
            
            
            
            
        self.label_position_z5.config(text=self.enonce)
        self.zone5.grid(column=0,row=0,sticky='EW')
        self.initzone5()
        
        self.canvas.grid()
        
    def Fold(self):
         global questions,reponses
         questions+=1
       
         if self.reponse["Fold"]:
            reponses+=1
         else:
            messagebox.showerror ("Erreur",self.erreur["Fold"])
            self.erreur_html +="<h1>Question "+str(questions)+"</h1>"
            self.erreur_html +='<p><img src="'+self.a[:2]+'.png"/><img src="'+self.a[2:]+'.png"/></p>'
            self.erreur_html += "<h2>Enoncé :</h2><p>"+self.enonce+'</p>'
            self.erreur_html += "<h2> Vous avez cliqué sur Fold !</h2>"
            self.erreur_html += '<p>'+self.erreur["Fold"]+'</p>'
            
         self.go()
    
    def Call(self):
        global questions,reponses
        questions+=1
        
        if self.reponse["Call"]:
            reponses+=1
        else:
            messagebox.showerror ("Erreur",self.erreur["Call"])
            self.erreur_html +="<h1>Question "+str(questions)+"</h1>"
            self.erreur_html +='<p><img src="'+self.a[:2]+'.png"/><img src="'+self.a[2:]+'.png"/></p>'
            self.erreur_html += "<h2>Enoncé :</h2><p>"+self.enonce+'</p>'
            self.erreur_html += "<h2> Vous avez  cliqué sur Call !</h2>"
            self.erreur_html += '<p>'+self.erreur["Call"]+'</p>'
            
        self.go()
    
    def Raise(self):
        global questions,reponses
        questions+=1
        
        if self.reponse["Raise"]:
            reponses+=1
        else:
            messagebox.showerror ("Erreur",self.erreur["Raise"])
            self.erreur_html +="<h1>Question "+str(questions)+"</h1>"
            self.erreur_html +='<p><img src="'+self.a[:2]+'.png"/><img src="'+self.a[2:]+'.png"/></p>'
            self.erreur_html += '<h2>Enoncé :</h2><p>'+self.enonce+'</p>'
            self.erreur_html += "<h2> Vous avez cliqué sur Raise !</h2>"
            self.erreur_html += '<p>'+self.erreur["Raise"]+'</p>'
        self.go()
    
    def mde(self,m,i):#mde pour main dans eventail
        """ reçoit une main et un entier 
        retourne True si la main est dans l'eventail eventails[str(i)] et False sinon"""
        try:
         if m in eventail(eventails[str(i)]).developpe:
             return True
         else:
             return False
        except:
            return False
        
    def bonnereponse(self):
        bonnerep=list(r for r in self.reponse.keys() if self.reponse[r])
        if len(bonnerep)==1:
            chaine="La réponse attendue était "+ str(bonnerep[0])
        else :
            chaine="Les deux autres réponses étaient meilleures !"   
        return chaine
    
    def estvide(self,i):   
        """ reçoit un id et renvoie true si l eventail d id i est vide"""
        
        return len(eventails[str(i)])==0
    
    def visuel(self):
        self.initzone1bis()
        self.bv=[]
        for i in range(169):
            self.bv.append(Button(self.label2,text=textbutton(i),width=4,pady=3,command=lambda x=i: self.clic(x)))
            self.bv[i].grid(column=i//13,row=i%13)
        self.flush=IntVar()
            
        self.gestioncouleur=Checkbutton(self.label2, text="gestion des couleurs" ,variable=self.flush)
        self.gestioncouleur.grid(column=0,row=14,columnspan=60)
        #On recupère le contenu de entry (detail)
        mains= (eventail(self.entry.get()).developpe)
        #on compte dans un dictionnaire:
        #initialisation du dic
        dicomain={}
        for i in range( 169):
            dicomain[textbutton(i)]=0
            
        
        
        for m in mains:
            if m[0]==m[2]:
                dicomain[m[0]+m[2]]+=1
            elif m[1]==m[3]:
                dicomain[m[0]+m[2]+"s"]+=1
            else:
                dicomain[m[0]+m[2]+"o"]+=1
                
        for i in range(169):
            if dicomain[textbutton(i)]==4 and textbutton(i)[-1]=="s":
                self.bv[i].configure(background='red')
            elif dicomain[textbutton(i)]==12 and textbutton(i)[-1]=="o":
                self.bv[i].configure(background='red')
            elif dicomain[textbutton(i)]==6 and textbutton(i)[0]==textbutton(i)[1]:
                self.bv[i].configure(background='red')
            elif dicomain[textbutton(i)]>0:
                self.bv[i].configure(background='orange')
            else :
                self.bv[i].configure(background='white')
                
            #on parcourt les boutons et on change les couleurs
            
            
            
    def clic(self,a):
        """ gestion des couleurs """
        edepart=eventail(self.entry.get()).developpe
        self.e=eventail(textbutton(a)).developpe
        #self.e main cliquée
        
        
        if self.flush.get():
           """gestion des couleurs"""
           self.zone1.grid_forget()
           self.zonecouleur=Frame(self,borderwidth=2,relief=GROOVE)
           photoG=[]
           photoD=[]
           canvasD=[]
           canvasG=[]
           maincouleur=[]
           self.selectioncouleur=[]
           
           for i in range(len(self.e)):
               self.selectioncouleur.append(IntVar())
               photoG.append(PhotoImage(file=self.e[i][:2]+".png"))
               photoD.append(PhotoImage(file=self.e[i][2:]+".png"))
               maincouleur.append(Checkbutton(self.zonecouleur,variable=self.selectioncouleur[i], text="Selection?"))
               if self.e[i][:2]+self.e[i][2:] in edepart:
                   self.selectioncouleur[i].set(1)
           for i in range(len(self.e)):   
               canvasG.append(Canvas(self.zonecouleur, width=68, height=92, background='white'))
               canvasD.append(Canvas(self.zonecouleur, width=68, height=92, background='white'))
               
               col=0
               li=0
           for i in range(len(self.e)):    
               canvasG[i].create_image(0,0, image=photoG[i],anchor = NW )
               canvasD[i].create_image(0,0, image=photoD[i],anchor = NW )
               canvasG[i].grid(column=col, row=li)
               canvasD[i].grid(column=col+1, row=li)
               maincouleur[i].grid(column=col+2, row=li)
               
               col+=3
               if col>12:
                    col=0
                    li=li+1
               canvasD[i].image=photoD[i]
               canvasG[i].image=photoG[i]
               
           bu=Button(self.zonecouleur,text="OK", command=lambda  : self.traiter_couleur())
           bu.grid(column=0, row=li+1)
           self.zonecouleur.grid(column=0,row=0,sticky='EW')    
           
        else:
           "ajouter ou soustraire la main"
           
           #print(edepart)
           #print(e)
           if set(self.e).issubset(edepart):
               #print("soustraire")
               newe=list(set(edepart)-set(self.e))
               newe=",".join(newe)
               #print (newe)
               
               self.entry.delete(0,END)
               self.entry.insert(0,eventail(newe).chaine) 
             
               self.bv[a].configure(background='white')
           else :
               newe=list(set(edepart)|set(self.e))
               newe=",".join(newe)
               #print (newe)
               
               self.entry.delete(0,END)
               self.entry.insert(0,eventail(newe).chaine) 
             
               self.bv[a].configure(background='red')
               
    def traiter_couleur(self):
        
        
        ancien=set(eventail(self.entry.get()).developpe)
        for i in range (len(self.selectioncouleur)):
            if self.selectioncouleur[i].get():
                ancien.add(self.e[i])
            else:
                try:
                    ancien.remove(self.e[i])
                except:
                    pass
        nouveau=",".join(list(ancien))
        self.entry.delete(0,END)
        self.entry.insert(0,eventail(nouveau).chaine)
        self.zonecouleur.grid_forget()       
        self.visuel()
        
    def init_score(self):
        global questions,reponses
        questions=0
        reponses=0
        result = messagebox.askquestion("Attention!", "Le fichier html d'analyse des erreurs va être initialisé. \n Voulez-vous l'afficher avant de perdre les données ?", icon='warning')
       
        if result=="yes":
            webbrowser.open("last_errors_from_wouf_poker.html")
        self.erreur_html=""
            
        lescore=str(reponses)+"/"+str(questions)
        self.label_score_z5.config(text=lescore)

    def mes_erreurs(self):
        parse='<?xml version="1.0"?><html>'
        if questions==0:
            intro="Pas encore de session d'exercices !"
        else:
            score=int(reponses*100/questions)
            intro="{0} question(s) et {1} réponse(s) correcte(s) soit un score de {2}%.".format(questions,reponses,score)
            
        parse+='''
        <head>
        <title>Erreurs : Analyse</title>
        </head>
        <body>
        <h1 style="text-align:center; color:red">ANALYSES DES ERREURS</h1>
        <h2 style="text-align:center; color:green">{00}</h2>
        <hr/>
        
        '''.format(intro)
        parse+=self.erreur_html+"</body></html>"
        # pourquoi pas ajouter vos CSS ?
        parse=minidom.parseString(parse)
        n=open("last_errors_from_wouf_poker.html","w")
        n.write(parse.toprettyxml())
        n.close()
        webbrowser.open("last_errors_from_wouf_poker.html")
        
        
              
        
        
def id_ev(j,v,n):                
           """ Renvoie l id de l eventail joueur j contre vilain
           n=0 ---> Call
           n=1 ---> Bet Bluff
           n=2 ---> Value Bet
           """
           if j<v : # 
               return 16*j+3*v+n-1
           else:
               return 16*j+3*v+n+2
               
                    
    
def textbutton(i): # pour l'affichage visuel de l'éventail
    x=i//13
    y=i%13
    if x>y :
        return valeurs[y]+valeurs[x]+"s"
    elif x<y:
        return valeurs[x]+valeurs[y]+"o"
    else :
        return 2*valeurs[x]
     
       
if __name__ == "__main__":
    app = Application(None)
    app.title('Poker Training')       
    app.mainloop()    
