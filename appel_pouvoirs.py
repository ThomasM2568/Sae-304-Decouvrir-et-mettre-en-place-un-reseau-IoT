# Créé par Thomas Mirbey, le 27/12/2022 en Python 3.7

#--------------------------------

"""
Liste des superpouvoirs :

Super pourvoir pour creuser sous son avatar ( afin de récupérer le diamant s’il est
enterré)
 Super pouvoir pour faire un ascenseur d’eau. Création d’une fontaine pour récupérer
le diamant s’il est en hauteur.
 Méga pouvoir lorsque l’avatar est sur le diamant.
Liste des malus :
 Malus mur de lave. Création d’un mur de lave autour de son adversaire. FAIT
 Malus champs de clôture. Création de bloc autour de son adversaire."""

#--------------------------------

def player_getPos(name):
    '''Permet de recuperer les coordonnees du joueur via son nom'''
    #On recupere l'identifiant en jeu du joueur "martinohanlon"
    #dans une variable de type ...
    entityId = mc.getPlayerEntityId("martinohanlon")

    #Recupere les coordonnees du joueur avec l'identifiant entityId
    #son la forme ...
    playerPos= mc.entity.getPos(entityId)
    return playerPos

#--------------------------------

def BP_lava() :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    pos=player_getPos("martinhanlon")
    """Il faut voir de quel format est la variable playerPos pour pouvoir
    l utiliser dans la ligne en dessous, en attendant, utilisation de
    coordonnees temporaires"""

    #On place des blocs de lave (LAVA_STATIONARY)autour du joueur
    #la premiere boucle permet de gerer la hauteur du bloc
    for j in range(0,3):
        #la deuxieme boucle permet de gerer le x et le y du bloc
        for i in [-1,1]:
            #Placement sur l'axe X
            mc.setBlock(round(x+i),round(y),round(z+j),block.LAVA_STATIONARY.id)
            #Placement sur l'axe Y
            mc.setBlock(round(x),round(y+i),round(z+j),block.LAVA_STATIONARY.id)

#--------------------------------

def BP_fence() :
    '''Malus champs de clôture. Création de bloc autour de son adversaire.'''

    pos=player_getPos("martinhanlon")
    """Il faut voir de quel format est la variable playerPos pour pouvoir
    l utiliser dans la ligne en dessous, en attendant, utilisation de
    coordonnees temporaires"""

    #On place des blocs de cloture (FENCE) autour du joueur
    #la premiere boucle permet de gerer la hauteur du bloc
    for j in range(0,3):
        #la deuxieme boucle permet de gerer le x et le y du bloc
        for i in [-1,1]:
            #Placement sur l'axe X
            mc.setBlock(round(x+i),round(y),round(z+j),block.FENCE.id)
            #Placement sur l'axe Y
            mc.setBlock(round(x),round(y+i),round(z+j),block.FENCE.id)

#--------------------------------


def BP_dig() :
    '''Super pourvoir pour creuser sous son avatar.'''

    pos=player_getPos("martinhanlon")

    #On place des blocs d'air (AIR) autour du joueur pour simuler le fait qu'il
    #creuse les blocs autour de lui

    #On creuse sur 3 blocs de hauteur
    for hauteur in range(1,4):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(-1,1):
            for X in range(-1,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(x+X),round(y+Y),round(z-hauteur))
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!="DIAMOND_BLOCK"):
                    mc.setBlock(round(x+X),round(y+Y),round(z-hauteur),block.AIR.id)

#--------------------------------

def BP_elevator() :
    '''Super pouvoir pour faire un ascenseur d’eau. Création d’une fontaine pour récupérer.'''

    pos=player_getPos("martinhanlon")

    #On place des blocs d'eau (WATER_STATIONARY) au dessus du joueur
    #sur 5 blocs de haut

    for HAUTEUR in range(1,6):
            mc.setBlock(round(x),round(y),round(z+HAUTEUR),block.WATER_STATIONARY.id)

#--------------------------------