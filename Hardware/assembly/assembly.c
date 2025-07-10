// Pin Definitions
const int P = 2;
const int Q = 3;
const int R = 4;
const int S = 5;
const int LED = 13;

void setup() {
  pinMode(P, INPUT);
  pinMode(Q, INPUT);
  pinMode(R, INPUT);
  pinMode(S, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  int p = digitalRead(P);
  int q = digitalRead(Q);
  int r = digitalRead(R);
  int s = digitalRead(S);

  // Boolean Expression: f = (q && s) || (p && r && s) || (p && q && r)
  int f = (q && s) || (p && r && s) || (p && q && r);

  digitalWrite(LED, f);
  delay(100);
}

