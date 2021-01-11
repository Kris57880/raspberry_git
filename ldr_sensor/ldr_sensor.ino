int CDSPin = 0; // 光敏電阻接在A0接腳
int CDSVal = 0; // 設定初始光敏電阻值為0
int SoilPin = 1;
int SoilVal = 0;
void setup() {
  Serial.begin(9600);
  pinMode(DUST_PIN, INPUT);
  starttime = millis(); //get the current time;

}

void loop() { 
  duration = pulseIn(DUST_PIN, LOW);
  lowpulseoccupancy = lowpulseoccupancy + duration;
  now = millis();
  if ((now - starttime) > DUST_SAMPLE_MS) {
        ratio = lowpulseoccupancy / (DUST_SAMPLE_MS * 10.0);  // Integer percentage 0=>100
        concentration = 1.1 * pow(ratio, 3) - 3.8 * pow(ratio, 2) + 520 * ratio + 0.62; // using spec sheet curve

        Console.print(ratio);
        Serial.print(ratio);
        delay(3000);
        CDSVal = analogRead(CDSPin);
        Serial.println(CDSVal);
        delay(3000)
        SoilVal = analogRead(SoilPin);
        Serial.println(SoilVal);
        lowpulseoccupancy = 0;
        starttime = millis();
   }
     
}
