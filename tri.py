def tri (liste:list[int])->list[int]: 
    gauche=[]
    droite=[]
    milieu=len(liste)//2
    for i in range (0,milieu):
      gauche=gauche+[liste[i]]
    for i in range (milieu,len(liste)):
        droite=droite+[liste[i]]
    gauche=triInsertion(gauche)
    droite=triInsertion (droite)
    return fusion (gauche,droite)