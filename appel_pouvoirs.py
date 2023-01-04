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
import mcpi.minecraft as minecraft
import random
mc = minecraft.Minecraft.create()


#--------------------------------

def player_getPos():
    '''Permet de recuperer les coordonnees du joueur via son nom'''
    #On recupere l'identifiant en jeu du joueur player
    #dans une variable de type ...
    pos= mc.player.getPos()
    #Recupere les coordonnees du joueur avec l'identifiant entityId
    #son la forme ...
    return pos
#--------------------------------

def BP_lava() :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    pos=player_getPos()
    """Il faut voir de quel format est la variable playerPos pour pouvoir
    l utiliser dans la ligne en dessous, en attendant, utilisation de
    coordonnees temporaires"""


    #On place des blocs de lave (LAVA_STATIONARY)autour du joueur
    #la premiere boucle permet de gerer la hauteur du bloc
    for hauteur in range(0,3):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(1,3):
            for X in range(-2,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                
                if(blockType!=57):
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,10)




#--------------------------------

def BP_fence() :
    '''Malus champs de clôture. Creation de bloc autour de son adversaire.'''

    pos=player_getPos()
    """Il faut voir de quel format est la variable playerPos pour pouvoir
    l utiliser dans la ligne en dessous, en attendant, utilisation de
    coordonnees temporaires"""

    #On place des blocs de cloture (FENCE) autour du joueur
    #la premiere boucle permet de gerer la hauteur du bloc
    for hauteur in range(-1,4):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(-2,4):
            for X in range(-3,2):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,85)
         
         
    blockType = mc.getBlock(round(pos.x)-1,round(pos.y)+1,round(pos.z))
    if(blockType!=57):
        mc.setBlock(round(pos.x)-1,round(pos.y)+1,round(pos.z)-1,0)
        
    blockType = mc.getBlock(round(pos.x)-1,round(pos.y)+0,round(pos.z)-1)
    if(blockType!=57):
        mc.setBlock(round(pos.x)-1,round(pos.y)+0,round(pos.z)-1,0) 
   
#--------------------------------

def BP_dig() :
    '''Super pourvoir pour creuser sous son avatar.'''

    pos=player_getPos()

    #On place des blocs d'air (AIR) autour du joueur pour simuler le fait qu'il
    #creuse les blocs autour de lui

    #On creuse sur 3 blocs de hauteur
    for hauteur in range(0,3):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(-1,2):
            for X in range(-2,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,0)
    
    
#--------------------------------

def BP_elevator() :
    '''Super pouvoir pour faire un ascenseur d’eau. Creation d une fontaine pour recuperer.'''

    pos=player_getPos()

    #On place des blocs d'eau (WATER_STATIONARY) au dessus du joueur
    #sur 5 blocs de haut

    for hauteur in range(0,3):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(1,3):
            for X in range(-2,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(pos.z)+X,round(pos.y)+Y,round(pos.z)-hauteur)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,8)

#--------------------------------
def setDiamond():
    x=random.randint(-128,128)
    z=random.randint(-128,128)
    y=random.randint(-40,20)
    mc.setBlock(x,y,z,57)
    mc.postToChat ("x="+str(x) +  "y="+str(y) + "z="+str(z))

test=player_getPos()
setDiamond()