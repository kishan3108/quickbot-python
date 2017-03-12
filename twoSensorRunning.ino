#include<Servo.h>
Servo rightServo;
Servo leftServo;
const int pingleft = 4;
const int pingright = 5;

void setup() {
  leftServo.attach(7);
  rightServo.attach(6);

  Serial.begin(9600);
}

void loop() {
  long left = read_left();
  long right = read_right();
  Serial.println(left);
  Serial.println(right);

  if (left > 15 && right > 15) {
    straight();
    Serial.println("straight");
  }
  if (left <= 15 && left >= 5 && right > 15) {
    left_turn();
    Serial.println("left");
  }
  if (left > 15 && right <= 15 && right >= 5) {
    right_turn();
    Serial.println("right");
  }
  if (left < 4 || right < 4) {

    leftServo.write(-180);
    rightServo.write(90);
    Serial.println("Stop");
    delay(150);

  }
}

long read_left() {
  long duration_left, cm;
  pinMode(pingleft, OUTPUT);
  digitalWrite(pingleft, LOW);
  delayMicroseconds(2);
  digitalWrite(pingleft, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingleft, LOW);

  pinMode(pingleft, LOW);
  duration_left = pulseIn(pingleft, HIGH);

  cm = microsecondsToCentimeters(duration_left);
  return cm;
  delay(100);
}

long read_right() {
  long duration_right, cm;
  pinMode(pingright, OUTPUT);
  digitalWrite(pingright, LOW);
  delayMicroseconds(2);
  digitalWrite(pingright, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingright, LOW);

  pinMode(pingright, LOW);
  duration_right = pulseIn(pingright, HIGH);

  cm = microsecondsToCentimeters(duration_right);
  return cm;
  delay(100);
}
long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}
void straight() {
  leftServo.write(180);
  rightServo.write(-180);
  noTone(8); 

}
void left_turn() {
  leftServo.write(90);
  rightServo.write(-180);
  tone(8,500);
}
void right_turn() {
  leftServo.write(180);
  rightServo.write(90);
tone(8,1000);
}

