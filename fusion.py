def fusion(list1:list[int],list2:list[int])->list[int]: 

    i1= [0]
    i2= [0] 
    resulat=[]

    while i1 < len(list1) and i2< len(list2):
        if list1[i1]<list2[i2]:
             Resultat =Resultat+[list1[i1]] 
             i1=i1+1 
        else:
            Resultat= Resultat+ [list2[i2]]
            i2=i2+1 
    while i1<len(list1): 
            Resultat=Resultat+[list1[i1]]
            i1=i1+1 
    while i2<len(list2):
            Resultat=Resultat+[list2[i2]]
            i2=i2+1 

    

