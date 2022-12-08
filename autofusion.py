def autofusion(liste:list[int])->list[int]:
    "prend une liste en entree la divise en deux et tri les differentes parties de la liste"
    debut=0
    milieu=len(liste)//2  #ici on a définit le début et la fin de la liste 
    while debut<milieu and milieu <len(liste): #ici on dit tant que debut est plus petit que milieu et milieu plus petit que la longueur de la liste 
        if liste[debut]<liste[milieu]:
            debut=debut+1 
        else: 
            tmp=liste[debut]
            liste[debut]=liste[milieu]
            liste[milieu]=tmp
            debut=debut+1 
        if debut==milieu:
            milieu=milieu+1
        return liste
        
