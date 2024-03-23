const int led_num = 13;

void setup(){
  pinMode(led_num, OUTPUT);
}

void loop(){
  digitalWrite(led_num, HIGH);
  delay(1000);

  digitalWrite(led_num, LOW);
  delay(1000);
}


