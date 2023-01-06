#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define LED_PIN         2
#define BOUTON_ANNULAIRE   14
#define BOUTON_AURICULAIRE  12
#define BOUTON_MAJEUR  13
#define BOUTON_INDEX 0

// SSID de la borne linksys, mdp  et adresse IP de notre serveur MQTT
const char* ssid = "binome_2";
const char* password = "tpRT9025";
const char* mqtt_server = "192.168.1.118";


int auriculaire = 0;
int annulaire = 0;
int majeur = 0;
int index_ = 0;
boolean pub = false;


WiFiClient espClient;
PubSubClient client(espClient);
unsigned long start_ = 0;
unsigned long t ;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;
int valeur[10];



void setup_wifi() {

  delay(10);
  // On commance par une connexion au wifi de la borne linksys qui a pour SSID binome_2
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    valeur[i] = (char)payload[i];
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

////////////////////////Call back de de l'auriculaire /////////////////////////////////////////
void ICACHE_RAM_ATTR auriculaireEvent() {
  if(pub == false){
    auriculaire = !auriculaire;
    Serial.println("Bouton auriculaire : Pouvoir active");
    snprintf (msg, MSG_BUFFER_SIZE, "%ld", auriculaire);
    client.publish("gant1/auriculaire" , msg);
    Serial.print("Publish message: ");
    Serial.println(msg);
    pub = true;
    start_  = millis();
  }else{
    start_ = millis();
  }
}
////////////////////////Call back de de l'annulaire/////////////////////////////////////////
void ICACHE_RAM_ATTR annulaireEvent() {
  if(pub == false){
    annulaire = !annulaire;
    Serial.println("Bouton annulaire : Pouvoir active");
    snprintf (msg, MSG_BUFFER_SIZE, "%ld", annulaire);
    client.publish("gant1/annulaire" , msg);
    Serial.print("Publish message: ");
    Serial.println(msg);
    pub = true;
    start_ = millis();
  }else{
    start_ = millis();
  }
}

////////////////////////Call back de du majeur/////////////////////////////////////////
void ICACHE_RAM_ATTR majeurEvent() {
  if(pub == false){
    majeur = !majeur;
    Serial.println("Bouton majeur : Pouvoir active");
    snprintf (msg, MSG_BUFFER_SIZE, "%ld", majeur);
    client.publish("gant1/majeur" , msg);
    Serial.print("Publish message: ");
    Serial.println(msg);
    pub = true;
    start_ = millis();
  }else{
    start_ = millis();
  }
}

////////////////////////Call back de de l'index/////////////////////////////////////////
void ICACHE_RAM_ATTR indexEvent() {
  if(pub == false){
    index_ = !index_;
    Serial.println("Bouton index : Pouvoir active");
    snprintf (msg, MSG_BUFFER_SIZE, "%ld", index_);
    client.publish("gant1/index" , msg);
    Serial.print("Publish message: ");
    Serial.println(msg);
    pub = true;
    start_ = millis();
  }else{
    start_ = millis();
  }
}


/////////////////////////////////////////////////////////////////

void setup() {
  pinMode(LED_PIN, OUTPUT);     //Initialise la LED en tant que OUTPOUT
  
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  //
  pinMode(BOUTON_ANNULAIRE, INPUT_PULLUP);
  pinMode(BOUTON_AURICULAIRE, INPUT_PULLUP);
  pinMode(BOUTON_MAJEUR, INPUT_PULLUP);
  pinMode(BOUTON_INDEX, INPUT_PULLUP);

  // Nous allons définir a chaque bouton une fonction callback qui va être activé par un front montant
  attachInterrupt(BOUTON_ANNULAIRE, annulaireEvent, RISING);
  attachInterrupt(BOUTON_AURICULAIRE, auriculaireEvent, RISING);
  attachInterrupt(BOUTON_MAJEUR, majeurEvent, RISING);
  attachInterrupt(BOUTON_INDEX, indexEvent, RISING);
}




void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

/////////Cette partie est un filtre anti-rebond qui va nous permettre de ne pas activer/////// 
// les rebonds lorsqu'une fonction callback sollicité plusieurs fois en moins de 300ms ////////
  if (pub == true){
    digitalWrite(LED_PIN, LOW);
    
    t = millis() - start_;
    Serial.print("Temps : ");
    Serial.print(t);
    Serial.println(" ms");
    
    if(t < 300){
      Serial.println(" Rebond");
    }else{
      pub = false;
    }
  }else{
    delay(1000);
    digitalWrite(LED_PIN, HIGH);
  }

/////////////////////////////////////////////////////////////////


}
