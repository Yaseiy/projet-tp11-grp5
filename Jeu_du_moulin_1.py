def cree_plateau(variante) :
    variante = str(variante)
    grille = []
    if variante == '3' :
        for i in range(3):
                ligne = []
                for j in range(3):
                    ligne.append(0)
                grille.append(ligne)
                
    elif variante == '6' :
        for i in range(5):
                ligne = []
                for j in range(3):
                    ligne.append(0)
                grille.append(ligne)
        grille[2].append(0)
        
    elif variante == '9' or variante ==  '12' or variante == 'Lasker':
        for i in range(7):
                ligne = []
                for j in range(3):
                    ligne.append(0)
                grille.append(ligne)
        for i in range (3):
            grille[3].append(0)
            
    else :
        print('erreur')

    return grille, variante
#----------------------------------------------------------
def phase_1(plateau, jetons) :
    joueur1 = jetons
    joueur2 = jetons
    tour_j1 = True
    
    while joueur1 > 0 or joueur2 > 0 :
        x = int(input("x"))
        y = int(input("y"))
        if case_libre(plateau,x,y) :
            place_jeton(plateau, tour_j1, x, y)
        else :
            while not(case_libre(plateau, x, y)) :
                x = int(input("x"))
                y = int(input("y"))
                
                
        if tour_j1 == True :
            tour_j1 = False
        elif tour_j1 == False :
            tour_j1 == True
        print(plateau)
 
    return plateau

       
        
    
    

def case_libre(plateau, x, y) :
    if plateau[x][y] == 0 :
        return True
    else :
        return False
    
def place_jeton(plateau, j1, x, y) :
    if case_libre(plateau, x, y) :
        if j1 == True :
            plateau[x][y] = 1
        else :
            plateau[x][y] = 2
        return plateau
    else :
        return False
             
        

        
plto, var = cree_plateau('3')
phase_1(plto, 3)