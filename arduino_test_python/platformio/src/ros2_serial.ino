#include <SoftwareSerial.h>

uint8_t send_data[8];
uint8_t receive_data[8];

void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop(){
  for(uint8_t i=0; i<sizeof(send_data); i++){
    send_data[i] = i;
  }

  Serial.write(send_data, sizeof(send_data));

  if((uint8_t)Serial.available() >= sizeof(receive_data)){
    Serial.readBytes(receive_data, sizeof(receive_data));
 
    for(uint8_t i=0; i<sizeof(receive_data); i++){
      if(receive_data[i] == 1){
        //Serial.println(receive_data[i]);
        digitalWrite(13, HIGH);
        delay(1000);
      }else{
        digitalWrite(13, LOW);
      }
    }
  }
  delay(100);
}


