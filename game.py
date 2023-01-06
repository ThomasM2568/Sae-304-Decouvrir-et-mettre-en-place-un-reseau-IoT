#Créer le 27/12/20022
import paho.mqtt.client as mqtt
from powers import *
import time



# Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.
def on_connect(client, userdata, flags, rc):
    '''' Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.'''
    print("Connected with result code "+str(rc))

    # Souscrire avec la fonction on_connect() veut dire que si on perd la connexion
    # alors une reconnection après la souscription sera renouvelle.
    # On se connecte donc aux topics des deux gants ci-dessous.
    client.subscribe("gant1/#")
    client.subscribe("gant2/#")

# Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.
def on_message(client, userdata, msg):
    '''Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.'''
    
    print(msg.topic+" "+str(msg.payload))
    print(str(msg.payload))
    #Traitements des messages reçus dans les differents topics 
    #Cela va permettre lactivation des differents pouvoirs 

    #Pour les deux parties ci-dessous, on va regarder dans quel topic
    #est posté le message. On regarde ensuite si les messages postés
    #sont bien ceux que nous avions prévu. Dans ce cas, on active les
    #fonctions associées à chaque bouton.
    #---------------#
    # Partie Gant 1 #
    #---------------#
    if (str(msg.topic) == "gant1/index"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_index")
            BP_gravel(getMyId())
    elif (msg.topic == "gant1/majeur"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            try:
                print("BP_majeur")
                BP_lava(getMyId())
            except:
                print("tototototototot")
    elif (msg.topic == "gant1/annulaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_annulaire")
            BP_fence(getMyId())
    elif (msg.topic == "gant1/auriculaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_auriculaire")
            BP_elevator(getPlayerId())
    
    
    #---------------#
    # Partie Gant 2 #
    #---------------#
    elif (str(msg.topic) == "gant2/index"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_index")
            BP_cobweb(getPlayerId())
    elif (msg.topic == "gant2/majeur"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_majeur")
            BP_dig(getMyId())
    elif (msg.topic == "gant2/annulaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_annulaire")
            BP_stairs2(getMyId())
    elif (msg.topic == "gant2/auriculaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_auriculaire")
            BP_elevator(getMyId())

#Cette fonction permet de récupérer l'identifiant d'un joueur lorsqu'il est seul
#à jouer, cette fonction nous a été utile pour les tests mais n'est plus utilisée.
def player_getPos():
    '''Permet de recuperer les coordonnees du joueur'''
    #On recupere l'identifiant en jeu du joueur player
    #par la suite, on fera pos.x, pos.y et pos.z pour récupérer
    #les trois coordonnées. On retourne ensuite ces données.
    pos= mc.player.getPos()
    mc.entity.setting("autojump",True)
    return pos

#Cette fonction permet de placer aléatoirement le bloc de diamant sur
#la carte en positionnant le bloc entre -100 et 100 sur les axes X et Y
#et on le positionne ensuite entre 20 et -40 blocs de hauteur
def setDiamond():

    
    mc.postToChat("Welcome to the game !")
    time.sleep(2)
    mc.postToChat("The rules are simple:")
    time.sleep(2)
    mc.postToChat("- The goal is to find a diamond block")
    time.sleep(1)
    mc.postToChat("before your opponent")
    time.sleep(2)
    mc.postToChat("- You have access to super powers and")
    time.sleep(1)
    mc.postToChat("malus that you can apply malus to")
    time.sleep(1)
    mc.postToChat("your opponent")
    time.sleep(1)
    mc.postToChat("Malus can be activated every 30s.")
    time.sleep(3)
    mc.postToChat("During the game, you have to find")
    time.sleep(1)
    mc.postToChat("the diamond block and")
    time.sleep(1)
    mc.postToChat("only at this place a mega power")
    time.sleep(1)
    mc.postToChat("will be activated.")
    time.sleep(3)
    mc.postToChat("Good Luck !")
    
    
    

    
    #mc.postToChat("Welcome to the game. The rules are simple. The goal is to find the diamond before your adversary. You have access to super powers and penalties to inflict on your opponent. Malus can only be activated every 10 seconds.You have access to super powers and penalties to inflict on your opponent. To win the game, you must find and break the diamond and only at this place the mega power will be active.")
     
    x=random.randint(-100,100)
    z=random.randint(-100,100)
    y=random.randint(-40,20)
    
    #On place le bloc de diamant aux coordonnées aléatoires
    #Le code du bloc de diamant est 57
    mc.setBlock(x,y,z,57)
    #On sauvegarde les coordonnées du diamant dans une liste et on les affiche dans le tchat du jeu.
    diamond=[x,y,z]
    mc.postToChat ("x="+str(diamond[0]) +  "y="+str(diamond[1]) + "z="+str(diamond[2]))
    #On appelle la fonction posDiamond qui permet de donner la distance du joueur attaquant
    #par rapport au diamant.
    print(posDiamond(diamond))


    
    #On retourne la liste diamond pour pouvoir la récupérer par la suite
    return diamond

#La fonctionDiamond permet de donner la distance du joueur attaquant par rapport
#au diamant(type liste) que l'on donne en argument à cette fonction.

def posDiamond(diamond):
    #On récupère les coordonnées du joueur qui attaque et on affiche sa distance par rapport au
    #diamant sur les axes X et Z uniquement et on les affiche dans le tchat.
    pos=player_getPos()
    try:
        mc.postToChat("Distance au diamant "+str(round(pos.x)-diamond[0])+" "+str(round(pos.z)-diamond[2]))
    except:
        print("Error")
    #Si le joueur se trouve à moins de 15 blocs du diamant, on lui
    #indique s'il est proche ou non en hauteur
    if(pos.x-15<=diamond[0]<=pos.x+15 and pos.z-15<=diamond[2]<=pos.z+15):
        print(pos.y-10<=diamond[1])
        print(diamond[1]<=pos.x+10)
        if(pos.y-10<=diamond[1]<=pos.x+10):
            mc.postToChat("[HAUTEUR] chaud")
            
        elif (pos.y-20<=diamond[1]<=pos.y+20):
            mc.postToChat("[HAUTEUR] tiede")
        else:
            mc.postToChat("[HAUTEUR] froid")
        


#On préparezzzzzz le connexion au serveur MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Connexion au serveur MQTT
client.connect("192.168.1.118", 1883, 60)

#On place le diamant sur la carte
liste=setDiamond()

blockType = mc.getBlock(liste[0],liste[1],liste[2])

#Cette variable va permettre de stopper la boucle qui fait tourner le jeu
end=False

#Démarre la boucle de connexion
client.loop_start()
#on laisse le temps à la connexion de se faire
time.sleep(4)

#Tant que la partie n'est pas finie, une boucle while
#va régulièrement afficher la distance du joueur par rapport au diamant
#Si le joueur attaquant casse le bloc de diamant, alors la partie est finie
#On regarde régulièrement si le bloc de diamant est toujours là.
#Si la partie dure plus de 7min, elle est également finie, mais personne ne gagne.
t_end = time.time() + 60 * 7
while end==False or time.time() < t_end:
    posDiamond(liste)
    #On récupère la position du diamant et son type de bloc
 
    posJoueur=mc.player.getTilePos()
    print(posJoueur.x)
    print(type(blockType ))
    print(blockType)
    print("condition ->"+str(posJoueur.x==liste[0] and posJoueur.z==liste[2] and posJoueur.y==liste[1]+1))
    if(posJoueur.x==liste[0] and posJoueur.z==liste[2] and posJoueur.y==liste[1]+1):

        BP_superPouvoir(getMyId())
    time.sleep(10)
    

    #Si le bloc aux coordonnées du bloc de diamant n'est plus un diamant, alors
    #la partie est finie
    if(blockType!=57):
        end==True
        mc.postToChat("[JEU] Partie finie")
                
#Arrête la boucle de connexion
client.loop_stop()




