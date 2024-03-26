#coding: latin-1
def menage_tuple(tuple_ref,tuple_):
    """ accepte un tuple reference et un tuple � ranger
    Par exemple pour cr�er ["JJ+","99-77","33"]
    avec en r�ference le tuple de toutes les paires
    et en deuxi�me argument le tupple
    ["AA","KK","QQ","JJ","99","88","77","33"]
"""
    # V�rifications
    # 1/ le tuple r�f�rence contient des �l�ments diff�rents
    A=[x for x in tuple_ref if tuple_ref.count(x)>1]

    
    if len(A)==0:
        # Le tuple reference est correct
        # 2/ Le Tuple B est une correction du
        # tuple_ en gardant les �l�ments appartenants au premier
        # rang�s dans le bon ordre
        
        B=[x for x in tuple_ref if x in tuple_]
        
        i=0
        sortie=[]
        while i<len(B):
            rang=tuple_ref.index(B[i])
            sortie.append(B[i])
            j=0
            
            while i+j<len(B) and tuple_ref[rang]==B[i+j]:
                
                j+=1
                rang+=1
            sortie.append(B[i+j-1])
            i=i+j
         #sortie contient un nombre paire de valeurs, si une paire est constitu�e
         #de deux �l�ment diff�rent on remplace par xx-yy sinon on oublie
         #le deuxi�me �l�m�nt
        i=0
        lasortie=[]
        while i<len(sortie):
            if sortie[i]==sortie[i+1]:
                lasortie.append(sortie[i])
            else:
                lasortie.append(sortie[i]+"-"+sortie[i+1])
            i+=2
         
         
            
        return lasortie
    else:
        
        print ("Erreur (fonction menage_tuple) : \n Le tuple r�f�rence contient au moins un doublon")
        return 
    
def analyse_main(m):
    """ Re�oit une chaine de 5 valeurs tri�es et renvoie
    un dictionnaire
    """
    valeurs = list("A K Q J T 9 8 7 6 5 4 3 2".split(" "))
    dic={}
    for i in (1,2,3,4) :
        dic[i]=[x for x in valeurs if i==m.count(x)]
    return dic
    
        
        