import mcpi.minecraft as minecraft
import random
import time
mc = minecraft.Minecraft.create()

def player_getPos():
    '''Permet de recuperer les coordonnees du joueur via son nom'''
    #On recupere l'identifiant en jeu du joueur player
    #dans une variable de type ...
    pos= mc.player.getPos()
    #Recupere les coordonnees du joueur avec l'identifiant entityId
    #son la forme ...
    return pos

def setDiamond():
    x=random.randint(-128,128)
    z=random.randint(-128,128)
    y=random.randint(-40,20)
    mc.setBlock(x,y,z,57)
    diamond=[x,y,z]

    mc.postToChat ("x="+str(diamond[0]) +  "y="+str(diamond[1]) + "z="+str(diamond[2]))
    diamant=posDiamond(diamond)

    return diamond

def posDiamond(diamond):
    done=False
    pos=player_getPos()
    mc.postToChat("Distance au diamant "+str(round(pos.x)-diamond[0])+" "+str(round(pos.z)-diamond[2]))
    if(pos.x-15<=diamond[0]<=pos.x+15 and pos.z-15<=diamond[2]<=pos.z+15):
        if(pos.y-10<=diamond[1]<=pos.x+10):
            mc.postToChat("[HAUTEUR] chaud")
            
        elif (pos.y-20<=diamond[1]<=pos.y+20):
            mc.postToChat("[HAUTEUR] tiede")
        else:
            mc.postToChat("[HAUTEUR] froid")
        

liste=setDiamond()
posDiamond(liste)
blockType = mc.getBlock(liste[0],liste[1],liste[2])

end=False


while end==False:
    
    time.sleep(10)
    posDiamond(liste)
    blockType = mc.getBlock(liste[0],liste[1],liste[2])
    if(blockType!=57):
        end==True
        mc.postToChat("[JEU] Partie finie")
                