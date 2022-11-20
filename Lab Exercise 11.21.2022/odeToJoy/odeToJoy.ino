//Plays a melody
const int buttonPin = 2;
int pbState = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  pbState = digitalRead(buttonPin);
  if (pbState == HIGH){
      //First group of notes
      tone(8, 247, 300);
      delay(500);
      tone(8, 247, 300);
      delay(500);
      tone(8, 262, 300);
      delay(500);
      tone(8, 294, 300);
      delay(500);
      tone(8, 294, 300);
      delay(500);

      //second group of notes
      tone(8, 262, 300);
      delay(500);
      tone(8, 247, 300);
      delay(500);
      tone(8, 220, 300);
      delay(500);
      tone(8, 196, 300);
      delay(500);
      tone(8, 196, 300);
      delay(500);
    
      //third group of notes
      tone(8, 220, 300);
      delay(500);
      tone(8, 247, 300);
      delay(500);
      tone(8, 247, 500);
      delay(650);
      tone(8, 220, 200);
      delay(250);
      tone(8, 220, 200);
      delay(250);
    }
}
