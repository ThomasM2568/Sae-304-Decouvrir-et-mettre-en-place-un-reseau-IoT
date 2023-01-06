int led = 2;
int bouton = 14;
volatile int state = LOW;
int EtatBouton;

void ICACHE_RAM_ATTR blink()
{
  state = !state;
  Serial.println("Je suis la fonction callback");


}

;void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(bouton, INPUT_PULLUP);
}

void loop()
{
  //EtatBouton = digitalRead(pin2);
  //Serial.println(EtatBouton);
  attachInterrupt(bouton, blink, RISING);
  digitalWrite(led, state);

}
