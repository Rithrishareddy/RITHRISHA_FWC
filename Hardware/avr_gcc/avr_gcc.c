// Pin Definitions
const int X = 2;
const int Y = 3;
const int Z = 4;
const int LED = 13;

void setup() {
  pinMode(X, INPUT);
  pinMode(Y, INPUT);
  pinMode(Z, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  int x = digitalRead(X);
  int y = digitalRead(Y);
  int z = digitalRead(Z);

  // Full Expression:
  // f = (x || z) && (y || (z || y)) && (x || (z && (x || y)))
  int part1 = (x || z);
  int part2 = (y || (z || y));
  int part3 = (x || (z && (x || y)));
  int f = part1 && part2 && part3;

  digitalWrite(LED, f);
  delay(100);
}

