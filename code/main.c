#include <Servo.h>
Servo myservo;
int pos = 0;
const int trig_pin = 3;
const int echo_pin = 4;
const int trig_pi = 5;
const int echo_pi = 6;
const int buzzer=11;
void setup()
{
    Serial.begin(9600);
    pinMode(buzzer,OUTPUT);
    pinMode (trig_pin, OUTPUT);
    pinMode (echo_pin, INPUT);
    pinMode (trig_pi, OUTPUT);
    pinMode (echo_pi, INPUT);
    myservo.attach(9);
    delay(3000);
}
void loop()
{
    float duration, distance,duration_us,distance_cm;
    for (pos = 0; pos <= 180; pos +=5) {
        myservo.write(pos);
        digitalWrite(trig_pin, LOW);
        delayMicroseconds(2);
        digitalWrite(trig_pin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trig_pin, LOW);
        duration = pulseIn(echo_pin, HIGH);
        distance= duration*0.034/2;
        digitalWrite(trig_pi, LOW);
        delayMicroseconds(2);
        digitalWrite(trig_pi, HIGH);
        delayMicroseconds(10);
        digitalWrite(trig_pi, LOW);
        duration_us = pulseIn(echo_pi, HIGH);
        distance_cm= duration_us*0.034/2;
        delay(100);
        while(distance>30 && distance_cm<30){
            tone(buzzer,50);
            delay(50);
            noTone(buzzer);
            digitalWrite(trig_pin, LOW);
            delayMicroseconds(2);
            digitalWrite(trig_pin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig_pin, LOW);
            duration = pulseIn(echo_pin, HIGH);
            distance= duration*0.034/2;
            digitalWrite(trig_pi, LOW);
            delayMicroseconds(2);
            digitalWrite(trig_pi, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig_pi, LOW);
            duration_us = pulseIn(echo_pi, HIGH);
            distance_cm= duration_us*0.034/2;
            delay(10);
        }
    }
    for (pos = 180; pos >= 0; pos -= 5) {
        myservo.write(pos);
        digitalWrite(trig_pin, LOW);
        delayMicroseconds(2);
        digitalWrite(trig_pin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trig_pin, LOW);
        duration = pulseIn(echo_pin, HIGH);
        distance= duration*0.034/2;
        digitalWrite(trig_pi, LOW);
        delayMicroseconds(2);
        digitalWrite(trig_pi, HIGH);
        delayMicroseconds(10);
        digitalWrite(trig_pi, LOW);
        duration_us = pulseIn(echo_pi, HIGH);
        distance_cm= duration_us*0.034/2;
        delay(100);
        while(distance>30 && distance_cm<30){
            tone(buzzer,50);
            delay(50);
            noTone(buzzer);
            digitalWrite(trig_pin, LOW);
            delayMicroseconds(2);
            digitalWrite(trig_pin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig_pin, LOW);
            duration = pulseIn(echo_pin, HIGH);
            distance= duration*0.034/2;
            digitalWrite(trig_pi, LOW);
            delayMicroseconds(2);
            digitalWrite(trig_pi, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig_pi, LOW);
            duration_us = pulseIn(echo_pi, HIGH);
            distance_cm= duration_us*0.034/2;
            delay(10);
        }
    }
}
