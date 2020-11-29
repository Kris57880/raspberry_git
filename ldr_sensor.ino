int CDSPin = 0; // 光敏電阻接在A0接腳
int CDSVal = 0; // 設定初始光敏電阻值為0
int SoilPin = 1;
int SoilVal = 0;
void setup() {
  Serial.begin(9600);
}

void loop() { 
  delay(15000);
  CDSVal = analogRead(CDSPin);
  SoilVal = analogRead(SoilPin);
  Serial.println(CDSVal);
  Serial.println(SoilVal);
  delay(15000); //每30s讀取一次       
}
