#include "Arduino.h"

// motors 1 settings
int CHA  = 0;
int ENA   = 14; // this pin must be PWM enabled pin if Arduino board is used
int IN1  = 27;
int IN2  = 26;
// motor 2 settings
int IN3 = 25;
int IN4 = 33;
int ENB = 32;// this pin must be PWM enabled pin if Arduino board is used
int CHB = 1;
// 200
int  VELOCIDADE  =  70;
// 30 000
const int frequency = 500; 
const int resolution = 8;

void inicializar_motor(int ENA_pin, int IN1,int IN2, int pwm_channel, int frequency,int resolution)
{

  pinMode(ENA_pin, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  ledcSetup(pwm_channel, frequency, resolution);
  ledcAttachPin(ENA_pin, pwm_channel);
  
}
void Para_Frente(int IN1,int IN2,int IN3,int IN4,int CH1,int CH2,int VELOCIDADE )
{
    //VELOCIDADE
    ledcWrite(CH1, VELOCIDADE); 
    ledcWrite(CH2, VELOCIDADE);  
      
      
     //MOTOR  1
        digitalWrite(IN2, HIGH);
        digitalWrite(IN1, LOW);  
     //MOTOR 2

        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
  
}

void Stop(int IN1,int IN2,int IN3,int IN4)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}

void Para_Tras(int IN1,int IN2,int IN3,int IN4,int CH1,int CH2,int VELOCIDADE )
{

      //VELOCIDADE
      ledcWrite(CH1, VELOCIDADE); 
      ledcWrite(CH2, VELOCIDADE); 
      
  
     //MOTOR  1
        digitalWrite(IN2, LOW);
        digitalWrite(IN1, HIGH);  
     //MOTOR 2

        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
  
}
void Para_Esq(int IN1,int IN2,int IN3,int IN4,int CH1,int CH2,int VELOCIDADE ){

   //VELOCIDADE
      ledcWrite(CH1, VELOCIDADE); 
      ledcWrite(CH2, VELOCIDADE); 
      
  
     //MOTOR  1
        digitalWrite(IN2, HIGH);
        digitalWrite(IN1, LOW);  
     //MOTOR 2

        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);

}

void Para_Dir(int IN1,int IN2,int IN3,int IN4,int CH1,int CH2,int VELOCIDADE)
{

   //VELOCIDADE
      ledcWrite(CH1, VELOCIDADE); 
      ledcWrite(CH2, VELOCIDADE); 
      
  
     //MOTOR  1
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);  
     //MOTOR 2

        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
}
