#Créer le 27/12/20022
import paho.mqtt.client as mqtt


# Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.
def on_connect(client, userdata, flags, rc):
    '''' Cette fonction va permettre de recevoir un reponse CONNACK lorsque le client se connecte au serveur.'''
    print("Connected with result code "+str(rc))

    # Souscrire avec la fonction on_connect() veut dire que si on perd la connexion
    # alors une reconnection après la souscription sera renouvelle.
    client.subscribe("gant1/index")
    client.subscribe("gant1/majeur")
    client.subscribe("gant1/annulaire")
    client.subscribe("gant1/auriculaire")

# Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.
def on_message(client, userdata, msg):
    '''Permet de creer un CALLBACK lorsque lon va recevoir un message publie sur le serveur.'''
    print(msg.topic+" "+str(msg.payload))
    
    #Traitements des messages reçus dans les differents topics 
    #Cela va permettre lactivation des differents pouvoirs 
    if msg.topic == "gant1/index":
        if str(msg.payload) == 1:
            BP_index()
    elif msg.topic == "gant1/majeur":
        if str(msg.payload) == 1:
            BP_majeur()
    elif msg.topic == "gant1/annulaire":        
        if str(msg.payload) == 1:
            BP_annulaire()
    elif msg.topic == "gant1/auriculaire":        
        if str(msg.payload) == 1:
            BP_auriculaire()
    else:
        return ("Erreur")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Connexion au serveur MQTT
client.connect("localhost", 1883, 60) 




client.loop_forever()
