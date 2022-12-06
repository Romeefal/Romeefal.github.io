# Algorithmique et Programmation  Master Droit & Informatique  UPEC
#Romee Falempin 2022

#malheureusement malgré la consigne je ne peux pas programmer et executer via python3 mes fonctions python car depuis le debut d'année j'essaie de reparer le probleme suivant sur mon ordinateur:mes fichiers.py ne s'enregistrent pas sur le bon dossier de l'ordinateur. Dit dossier que je ne retrouve pas. 
#Ainsi quand je suis sur le terminal ou python3 j'ai le message d'erreur suivant "un tel dossier n'existe pas". Encore a ce jour le probleme persiste (je ne sais pas si j'ai le droit d'utiliser des terminaux sur internet alors malheureusement pour repondre au projet je ne peux que retranscrire mes fonctions et mes commentaires mais pas l'execution de mes fonction comme ça ne fonctionne pas)


#Ceci est l'exercice 1. 

#dans cet exercice on cherche a definir une fonction qui calcule e l’arrondi au décime supérieur d’un nombre à virgule.
#ce qui donne la fonction suivante : 

def arrondi_decime(x:float) -> float: #ici on definit la fonction 
   """prend un nombre decimal et l'arrondi a la decimale pres"""
x=0
n=x+0.1 #ici je demande a ma fonction de rajouter une decimale de 0.1 afin d'arrondir a la prochaine decimale pour  toute entree x. Cette nouvelle entree s'apelle alors N
print (n) #ici je demande a ma fonction d'afficher le resultat 
    #a titre informatif il existe une fonction  dans python qui calcule l'arrondi decimale d'un nombre. Mais c'est une fonction prepromgramme donc j'imagine que ce n'est pas ce qui est demande ici
    #cette fonction est la fonction round()
    #exemple suivant x = round(5.76543, 2)
    #print(x)

#Ceci est l'exercice 2. 

#Ici l'on souhaite une fonction prenant en entrée une distance (un nombre entier, en km) et renvoyant le prix (en €) d’un trajet. 
def prixkm(distance:int)->float:
    """prend une distance en km et renvoie le prix en euros"""
distance=0
i=len(distance)
for i in range (0,16): #a partir de cette ligne je demande a la fonction de renvoyer selon la place de i dans la fonction (le kilometrage) le prix correspondant. Donc je prend bien un "int"en entree pour renvoyer un "float" en sortie
    print (0.7781+distance*0.1944)
    for i in range (16,32):
        print(0.2503+distance*0.2165)
        for i in range (33,64):
            print(2.0706+distance*0.1597)
        for i in range(65,109):
            print(2.8891+distance*0.1489)
            for i in range(110,149):
                print (4.0864+distance*0.1425)
                for i in range(150,199):
                    print(8.0871+distance*0.1193)
                    for i in range(200,300):
                        print(7.7577+distance*0.1209)
                        for i in range(301,499):
                            print(13.6514+distance*0.1030)
                            for i in range (500,799):
                                print(18.4449+distance*0.0921)
                                if i>800:
                                    print(32.2041+distance*0.0755)
                                print (i) 

#ceci est l'exercice 3 

#au sein de cette fonction l'on souhaite obtenir le prix en premiere classe 
#au sein de cette fonction il suffit normalement d'appeler la fonction que nous avons déjà definis avec prixkm et de le multiplier par 1.5
def prixkm1ere(x:float)->float:
    """prend le prix de la seconde classe et affiche le prix de la premiere classe en faisant fois 1.5"""
    m=prixkm*1.5
    print(m)

#ceci est l'exercice 4 

#au sein de cette fonction l'on cherche a afficher les prix plafond des TER intercites. 
def prix_speciaux_max(entree:float)->any:
    """prend le bareme kilometrique et le multiplie par 2.1"""
    entree=0
    i=len(entree)
    for i in entree : #a partitr de cette ligne je demande a la fonction que pour toutes les variables de entree denomee ici i 
        i[entree]=entree*2.1 #ces variables soient multipliées par 2.1 
        return i[entree] #alors il ne restera plus qu'a entre le bareme kilometrique et la fonction renverra ce bareme multiplié par 2.1 


#Ceci est l'exercice 5

#ici nous cherchons a construire une fonction prenant en entree deux noms de gare devant se trouver dans un fichier externe 
#selon si les gares existent alors devra s'afficher : leurs noms, la distance entre les deux gares et les différents prix possibles devront s'afficher 
#si les deux gares n'existent pas un message d'erreur devra s'afficher 
#par ailleurs si il y a une erreur dans la distance entre les gares "-1" devra s'afficher. 

def lesdeuxgares(gare1:str,gare2:str)->str: 
    """prend en entree deux gares et selon si elles existent dans la liste affiche en sorties certaines indications """
    a = open(distance.csv, mode = "r")
    l = a.readline()
    i=0  #i est une variable qui va se deplacer dans la chaine de chaque ligne et elle commence à l'indicateur 0 de l'index. Donc elle commence au debut du fichier csv
    for i in l[a]: #ici j'indique que pour chacune des variable de l[a] c'est a dire, pour i sur la lecture de chaque ligne du fichier csv
        if i in l[a]:#si i est bien sur la lecture de chaque ligne du fichier csv
            print ("la distance entre la gare",i,"et") #a continuer de refchir dessus 
    
#reflechis concretement tu lis une ligne sur chaque ligne tu as 2 variable une str , une int(ou float) il faut que en premier lieux la fonction reconnaise ligne par ligne si une gare existe 
#ensuite la fonction est plus complexe car on souhaite afficher la distance entre les 2 gares et selon la distance le prix qui correspond 
#pour le prix on peut eventuellement appeler une fonction deja faite 
