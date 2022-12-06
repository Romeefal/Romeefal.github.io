def trifusion (liste:list[int])->list[int]:
    gauche=[]
    droite=[]
    milieu=len(liste)//2
    if milieu==0:
     return liste
     for i in range (0,milieu):
      gauche=gauche+[liste[i]]
    for i in range (milieu,len(liste)):
        droite=droite+[liste[i]]
    gauche=trifusion(gauche)
    droite=trifusion (droite)
    return fusion (gauche,droite)
