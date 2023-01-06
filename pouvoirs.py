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
def player_getPos2(id_player):
    '''Permet de recuperer les coordonnees du joueur via son nom'''
    #On recupere l'identifiant en jeu du joueur player
    #dans une variable de type ...
    pos= mc.entity.getPos(id_player)
    #Recupere les coordonnees du joueur avec l'identifiant entityId
    #son la forme ...
    return pos
#--------------------------------
def getPlayerId():
    liste=[]
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        liste.append(entityId)
    return liste[1]
#--------------------------------
def getPlayerIdByName(name):
    entityId = mc.getPlayerEntityId(name)
    return entityId
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
                    
def BP_gravel() :
    '''Super pouvoir pour faire un ascenseur d’eau. Creation d une fontaine pour recuperer.'''

    pos=player_getPos()

    #On place des blocs d'eau (WATER_STATIONARY) au dessus du joueur
    #sur 5 blocs de haut

    for hauteur in range(0,3):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(3,6):
            for X in range(-2,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(round(pos.z)+X,round(pos.y)+Y,round(pos.z)-hauteur)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,13)

#--------------------------------
def BP_cobweb() :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

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
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,30)
                    

def BP_stairs() :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    pos=player_getPos()
    """Il faut voir de quel format est la variable playerPos pour pouvoir
    l utiliser dans la ligne en dessous, en attendant, utilisation de
    coordonnees temporaires"""

    #On place des blocs de cloture (FENCE) autour du joueur
    #la premiere boucle permet de gerer la hauteur du bloc
    for i in range(0,5):
        blockType = mc.getBlock(round(pos.x)+i,round(pos.y)+i-1,round(pos.z))
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
        if(blockType!=57):
            mc.setBlock(round(pos.x)+i,round(pos.y)+i-1,round(pos.z),67)
        

def BP_stairs_facing() :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    #pos = mc.player.getPos()
    mc = minecraft.Minecraft.create()
    playerEntities = mc.getPlayerEntityIds()
    pos=mc.entity.getPos(playerEntities[0])
    #get the direction
    direction = mc.player.getDirection(pos)
    #calc the position of the block in front of the player
    x = round(pos.x + (direction.x * BLOCKDISTANCE))
    y = round(pos.y + (direction.y * BLOCKDISTANCE) + 1)
    z = round(pos.z + (direction.z * BLOCKDISTANCE))
    mc.setBlock(x,y,z,block.DIAMOND_BLOCK)
    time.sleep(0.1)
    mc.setBlock(x,y,z,block.AIR)
        

def BP_cobweb2(player) :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    pos=player_getPos2(player)
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
                    mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-hauteur,30)
BP_cobweb2(89955)