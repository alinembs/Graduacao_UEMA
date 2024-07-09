#include <Arduino.h>
#include "Line_Follower.h"

void setup()
{
  Serial.begin(115200);
  inicializar_motor(ENA, IN1, IN2, CHA, frequency, resolution);
  delay(500);
  inicializar_motor(ENB, IN3, IN4, CHB, frequency, resolution);
  delay(500);
  init_infrared_sensor();

}

void loop()
{
seguidor_de_linha();
}
