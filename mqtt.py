#Créer le 27/12/20022
import paho.mqtt.client as mqtt
from testpouvoirs import *

# Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.
def on_connect(client, userdata, flags, rc):
    '''' Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.'''
    print("Connected with result code "+str(rc))

    # Souscrire avec la fonction on_connect() veut dire que si on perd la connexion
    # alors une reconnection après la souscription sera renouvelle.
    client.subscribe("gant1/#")

# Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.
def on_message(client, userdata, msg):
    '''Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.'''

    print(msg.topic+" "+str(msg.payload))
    print(str(msg.payload))
    #Traitements des messages reçus dans les differents topics 
    #Cela va permettre lactivation des differents pouvoirs 

    if (str(msg.topic) == "gant1/index"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_index")
            BP_gravel(getPlayerId())
    elif (msg.topic == "gant1/majeur"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_majeur")
            BP_lava(getPlayerId())
    elif (msg.topic == "gant1/annulaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_annulaire")
            BP_fence(getPlayerId())
    elif (msg.topic == "gant1/auriculaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_auriculaire")
            BP_elevator(getMyId())
    
    #-----
    #        
    #-----
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
            BP_stairs(getPlayerId())
    elif (msg.topic == "gant2/auriculaire"):
        if (str(msg.payload) == "b'1'" or str(msg.payload) == "b'0'"):
            print("BP_auriculaire")
            BP_elevator(getMyId())


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Connexion au serveur MQTT
client.connect("192.168.1.112", 1883, 60) 




client.loop_forever()
