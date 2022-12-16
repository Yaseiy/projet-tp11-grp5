plateau_3 = {0:[0, (1,3,4)], 1:[0, (0,2,4)], 2:[0, (1,4,5)], 3:[0, (0,4,6)], 4:[0, (0,1,2,3,5,6,7,8)], 5:[0, (2,4,8)], 6:[0, (3,4,7)], 7:[0, (4,6,8)], 8:[0, (4,5,7)]}
#-------------------------------------------------------

def case_libre(plateau, case) :
    if plateau[case][0] == 0 :
        return True
    else :
        return False

#-------------------------------------------------------
    
def place_jeton_1(plateau, case) :
    if case_libre(plateau, case) :
        plateau[case][0] = 1
        return plateau
    else :
        return False
#-------------------------------------------------------
    
def place_jeton_2(plateau, case) :
    if case_libre(plateau, case) :
        plateau[case][0] = 2
        return plateau
    else :
        return False
#-------------------------------------------------------

def phase_1_basique(plateau, jetons) :
    joueur1 = jetons
    joueur2 = jetons
    tour_j1 = True
    while joueur1 > 0 or joueur2 > 0:
        case = int(input("case ?"))
        if not(case_libre(plateau, case)) :
            while not(case_libre(plateau, case)) :
                case = int(input("case ?"))
        if tour_j1 == True :
            place_jeton_1(plateau, case)
            joueur1 -= 1
            tour_j1 = False
        else :
            place_jeton_2(plateau, case)
            joueur2 -= 1
            tour_j1 = True    
        print(plateau)
    return plateau

#-----------------------------------------------------------
def detecter_moulin(plateau):
    for i in range len(plateau) :
        for j in range len(plateau[j]
        if plateau[i]
#-----------------------------------------------------------

def deplacer_jeton() :
    pass
#-----------------------------------------------------------
def phase_2() :
    pass

#test---------------------------------------------------------
##phase_1_basique(plateau_3, 3)
detecter_moulin(plateau_3)
