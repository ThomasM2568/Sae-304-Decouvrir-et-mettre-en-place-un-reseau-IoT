import mcpi.minecraft as minecraft
import random
mc = minecraft.Minecraft.create()
#--------------------------------
#On recupere l'identifiant en jeu du joueur avec l'id donné en argument
#et on retourne sa position
def player_getPos(id_player):
    '''Permet de recuperer les coordonnees du joueur via son nom'''
    pos= mc.entity.getPos(id_player)
    return pos
#--------------------------------
#On récupère l'identifiant du deuxième joueur et on active
#le saut automatique à tous les joueurs
def getPlayerId():
    liste=[]
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        liste.append(entityId)
        mc.entity.setting("autojump",True)
    return liste[1]
#--------------------------------
#On récupère l'id du joueur n°1 qui est celui-qui cherche le diamant
def getMyId():
    liste=[]
    entityIds = mc.getPlayerEntityIds()
    for entityId in entityIds:
        liste.append(entityId)
    return liste[0]
#--------------------------------
#On récupère l'identifiant du joueur grâce à son nom
def getPlayerIdByName(name):
    entityId = mc.getPlayerEntityId(name)
    return entityId
#--------------------------------
def BP_cobweb(player) :
    '''Malus cage de toiles d'araignées. Création d'une cage autour de son adversaire.'''

    pos=player_getPos(player)

    #On place des toiles d'araignées autour du joueur
    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(-1,4):
        #La boucle Y gère la hauteur du bloc
        for Y in range(-2,4):
            #La boucle X gère la coordonnée X du bloc
            for X in range(-3,2):
                try:
                    #On recupere le type de bloc sur la position sur laquelle on creuse
                    blockType = mc.getBlock(pos.x+X,pos.y+Y,pos.z-Z)
                    
                    #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                    #Sinon on peut le retirer en le remplacant par des toiles d'araignées
                    if(blockType!=57):
                        mc.setBlock((pos.x+X),(pos.y+Y),(pos.z-Z,30))
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")

#--------------------------------                   
def BP_gravel(player) :
    '''Malus chute de gravier. Création de blocs de gravier au dessus de son adversaire.'''

    pos=player_getPos(player)

    #On place des blocs de gravier au dessus du joueur adverse
    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(0,3):
        #La boucle Y gère la hauteur du bloc
        for Y in range(3,6):
            #La boucle X gère la coordonnée X du bloc
            for X in range(-2,1):
                try:
                    #On recupere le type de bloc sur la position sur laquelle on creuse
                    blockType = mc.getBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-Z)
                    
                    #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                    #Sinon on peut le retirer en le remplacant par du gravier
                    if(blockType!=57):
                        mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-Z,13)
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")




def BP_lava(player) :
    '''Malus mur de lave. Création d’un mur de lave autour de son adversaire.'''

    pos=player_getPos(player)

    #On place des blocs de lave au dessus du joueur
    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(0,3):
        #La boucle Y gère la hauteur du bloc
        for Y in range(6,9):
            #La boucle X gère la coordonnée X du bloc
            for X in range(-2,1):
                #On recupere le type de bloc sur la position sur laquelle on creuse
                try:
                    blockType = mc.getBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-Z)
                
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de la lave
                
                    if(blockType!=57):
                        mc.setBlock(round(pos.x)+X,round(pos.y)+Y,round(pos.z)-Z,10)
                         
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")




#--------------------------------

def BP_fence(player) :
    '''Malus champs de clôture. Creation de bloc autour de son adversaire.'''

    pos=player_getPos(player)

    #On place des blocs de cloture (FENCE) autour du joueur
    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(-1,4):
        #La boucle Y gère la hauteur du bloc
        for Y in range(-2,4):
            #La boucle X gère la coordonnée X du bloc
            for X in range(-3,2):
                    
                try:
                    #On recupere le type de bloc sur la position sur laquelle on creuse
                    blockType = mc.getBlock(pos.x+X,pos.y+Y,pos.z-Z)
                        
                    #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                    #Sinon on peut le retirer en le remplacant par des barrières
                    print(blockType!=57)
                    if(blockType!=57):
                        mc.setBlock(pos.x+X,pos.y+Y,pos.z-Z,85)
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")
    
    #Pour que le joueur ne soit pas coincé dans des blocs, on remplace
    #les deux blocs au centre de la cage par de l'air
    try:
        blockType = mc.getBlock(pos.x-1,pos.y+1,pos.z)
        if(blockType!=57):
            mc.setBlock(pos.x-1,pos.y+1,pos.z-1,0)
    except ValueError:
        mc.postToChat("Float error, no bonus/malus used")
      
    try:
        blockType = mc.getBlock(pos.x-1,pos.y+0,pos.z-1)
        if(blockType!=57):
            mc.setBlock(pos.x-1,pos.y+0,pos.z-1,0)
    except ValueError:
            mc.postToChat("Float error, no bonus/malus used")
   
#--------------------------------

def BP_dig(player) :
    '''Super pourvoir pour creuser sous son avatar.'''

    pos=player_getPos(player)

    #On place des blocs d'air (AIR) autour du joueur pour simuler le fait qu'il
    #creuse les blocs autour de lui

    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(0,3):
        #La boucle Y gère la hauteur du bloc
        for Y in range(-1,6):
            #La boucle X gère la coordonnée X du bloc
            for X in range(-2,1):
                try:
                    #On recupere le type de bloc sur la position sur laquelle on creuse
                    blockType = mc.getBlock(pos.x+X,pos.y+Y,pos.z-Z)
                    
                    #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                    #Sinon on peut le retirer en le remplacant par de l'air
                    if(blockType!=57):
                        mc.setBlock(pos.x+X,pos.y+Y,pos.z-Z,0)
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")

#--------------------------------

def BP_elevator(player) :
    '''Super pouvoir pour faire un ascenseur d’eau. Creation d une fontaine pour recuperer.'''

    pos=player_getPos(player)

    #On place des blocs d'eau (WATER_STATIONARY) au dessus du joueur
    #sur 5 blocs de haut

    for Z in range(0,3):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for Y in range(1,9):
            for X in range(-2,1):
                try:
                    #On recupere le type de bloc sur la position sur laquelle on creuse
                    blockType = mc.getBlock(int(round(pos.x))+X,int(round(pos.y))+Y,int(round(pos.z))-Z)
                    
                    #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                    #Sinon on peut le retirer en le remplacant par de l'air
                    if(blockType!=57):
                        mc.setBlock(round(int(pos.x))+X,round(int(pos.y))+Y,round(int(pos.z))-Z,8)
                except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")

#--------------------------------

def BP_stairs2(player) :
    '''Bonus escalier. Création d’un escalier devant son personnage'''

    pos=player_getPos(player)
    
    #On fait une boucle qui permet de placer un escalier devant le joueur en mettant
    #un bloc à la fin de l'escalier
    for i in range(0,6):
        try:
            blockType = mc.getBlock(round(pos.x)+i,round(pos.y)+i-1,round(pos.z))
                
            if(blockType!=57 and i!=5):
                mc.setBlock(round(pos.x)+i,round(pos.y)+i-1,round(pos.z),67,0)
            elif(blockType!=57 and i==5):
                mc.setBlock(round(pos.x)+i,round(pos.y)+i-2,round(pos.z),4)
        except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")

    #Cette boucle fait le même escalier mais dans l'autre sens
    #Il se mettra à côté de l'escalier précédent, en hauteur.
    for j in range(0,7):
        try:
            blockType = mc.getBlock(round(pos.x)+j-1,round(pos.y)+j-1,round(pos.z))
                   
            if(blockType!=57 and j==0):
                mc.setBlock(round(pos.x)+5-j,round(pos.y)+j-2+5,round(pos.z)-1,4)
            elif(blockType!=57):
                mc.setBlock(round(pos.x)+5-j,round(pos.y)+j+3,round(pos.z)-1,67,1)
        except ValueError:
                    mc.postToChat("Float error, no bonus/malus used")
#--------------------------------            

def BP_superPouvoir(player) :
    '''Bonus quand on se trouve sur un bloc de diamant'''

    pos=player_getPos(player)

    #On place des blocs d'obsidienne sous le joueur et autour
    #permettant de faire une muraille près du joueur pour le protéger
    #la premiere boucle permet de gerer la coordonnée Z du bloc
    for Z in range(1,4):
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for X in range(-1,2):
            for Y in [0,4]:
                
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(int(pos.x)+X,int(pos.y)-1+Y,int(pos.z)-Z+1)
                            
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(int(pos.x)+X,int(pos.y)-1+Y,int(pos.z)-Z+1,49)

                
                
                    
    for Z in [1,3,1,3]:
        #On creuse a gauche du joueur, sous le joueur, et a sa droite
        #devant lui, sur sa position et derriere lui, on utilise deux boucles
        #supplementaires pour gerer les positions
        for X in [-1,1,-1,1]:
            for Y in range(0,3):
                
                #On recupere le type de bloc sur la position sur laquelle on creuse
                blockType = mc.getBlock(int(pos.x)+X,int(pos.y)+Y,int(pos.z)-Z+1)
                        
                #Si le bloc en question est un bloc de diamant,on ne doit pas le supprimer
                #Sinon on peut le retirer en le remplacant par de l'air
                if(blockType!=57):
                    mc.setBlock(int(pos.x)+X,int(pos.y)+Y,int(pos.z)-Z+1,49)

