#coding: latin-1
def menage_tuple(tuple_ref,tuple_):
    """ accepte un tuple reference et un tuple à ranger
    Par exemple pour créer ["JJ+","99-77","33"]
    avec en réference le tuple de toutes les paires
    et en deuxième argument le tupple
    ["AA","KK","QQ","JJ","99","88","77","33"]
"""
    # Vérifications
    # 1/ le tuple référence contient des éléments différents
    A=[x for x in tuple_ref if tuple_ref.count(x)>1]

    
    if len(A)==0:
        # Le tuple reference est correct
        # 2/ Le Tuple B est une correction du
        # tuple_ en gardant les éléments appartenants au premier
        # rangés dans le bon ordre
        
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
         #sortie contient un nombre paire de valeurs, si une paire est constituée
         #de deux élément différent on remplace par xx-yy sinon on oublie
         #le deuxième élémént
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
        
        print ("Erreur (fonction menage_tuple) : \n Le tuple référence contient au moins un doublon")
        return 
    
def analyse_main(m):
    """ Reçoit une chaine de 5 valeurs triées et renvoie
    un dictionnaire
    """
    valeurs = list("A K Q J T 9 8 7 6 5 4 3 2".split(" "))
    dic={}
    for i in (1,2,3,4) :
        dic[i]=[x for x in valeurs if i==m.count(x)]
    return dic
    
        
        