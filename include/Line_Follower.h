#include "DC_Motors.h"

// Definição dos pinos dos sensores
#define pin_S1 34
#define pin_S2 35
bool Sensor1 = 0;
bool Sensor2 = 0;
int direcao_anterior = -1;
// Inicializar os pinos dos sensores infravermelhos
void init_infrared_sensor()
{
    // Setamos os pinos dos sensores como entrada
    pinMode(pin_S1, INPUT);
    pinMode(pin_S2, INPUT);
}
int resultado_do_sensor()
{
    Sensor1 = digitalRead(pin_S1);
    Sensor2 = digitalRead(pin_S2);
     if ((Sensor1 == 0) && (Sensor2 == 0))
    {
        // Serial.println("0 e 0");
        return 0;
    }
    if ((Sensor1 == 1) && (Sensor2 == 0))
           
    { 
    //  Serial.println("1 e 0");
     return 2;
    }
    if ((Sensor1 == 0) && (Sensor2 == 1))
    { // Se detectar um lado branco e o outro preto
    //    Serial.println("0 e 1");
     return 3;
    }
    if ((Sensor1 == 1) && (Sensor2 == 1))
    {
        // Serial.println("1 e 1");
     return 1;
    }
}
// funcao para detectar as linhas
void seguidor_de_linha()
{
   int direcao = resultado_do_sensor();
   if (direcao_anterior == -1){
    direcao_anterior = direcao;
   }
   if((direcao == 3 || direcao == 2) && (direcao_anterior != 0))
   {
    Serial.println("Frente");
    Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);

   }

   if(direcao == 1   && direcao_anterior == 3)
   {
    Serial.println("Frente");
    Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
    Para_Dir(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
    Serial.println("Direita");
    direcao_anterior == 3;
   }

     if(direcao == 1   && direcao_anterior == 2)
   {
    Serial.println("Frente");
     Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
     Para_Esq(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
    Serial.println("Esquerda");
    direcao_anterior == 2;
   }
    if(direcao == 0 && direcao_anterior == 3)
   {
    Serial.println("Frente");
     Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
     Para_Esq(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
    Serial.println("Esquerda");
    direcao_anterior == 3;
   }
    if(direcao == 0 && direcao_anterior == 2)
   {
    Serial.println("Frente");
     Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
     Para_Dir(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    delay(1000);
    Serial.println("Direita");
    direcao_anterior == 2;
   }
}

int linhas_detectadas()
{
    // Neste processo armazenamos o valor lido pelo sensor na variável que armazena tais dados.
    Sensor1 = digitalRead(pin_S1);
    Sensor2 = digitalRead(pin_S2);
    // define o retorno
    //  0 - Parado
    //  1 - Frente
    //  2- Esquerda
    //  3 - Direita
    int direcao = 0;
    // Aqui está toda a lógica de comportamento do robô: Para a cor branca atribuímos o valor 0 e, para a cor preta, o valor 1.
    if ((Sensor1 == 0) && (Sensor2 == 0))
    {
        direcao = 0;
        Stop(IN1, IN2, IN3, IN4);
    }
    if((Sensor1 == 1) || (Sensor2 == 1))
    {
direcao = 1; // Se detectar na extremidade das faixas duas cores brancas
        Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);

    }
    if ((Sensor1 == 1) && (Sensor2 == 0))
    { // Se detectar um lado preto e o outro branco
        direcao = 2;
        Para_Esq(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    }
    if ((Sensor1 == 0) && (Sensor2 == 1))
    { // Se detectar um lado branco e o outro preto
        direcao = 3;
        Para_Dir(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    }
    if ((Sensor1 == 1) || (Sensor2 == 1))
    {
        direcao = 1; // Se detectar na extremidade das faixas duas cores brancas
        Para_Frente(IN1, IN2, IN3, IN4, CHA, CHB, VELOCIDADE);
    }
    return direcao;
}
