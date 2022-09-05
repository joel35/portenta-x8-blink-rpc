#include <RPC.h>
#include <SerialRPC.h>

int DELAY_LEN = 1000;
int COUNT = 0;
int LED_STATE = HIGH;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  Serial.println("Blink test on M4");

  RPC.bind("count", []{ return COUNT; });
  RPC.bind("led", []{ return LED_STATE; });
  
  Serial.println("Starting");

}

void loop() {
  toggleLED();
  countUp();
  delay(DELAY_LEN);
}

void toggleLED() {
  LED_STATE = (LED_STATE==HIGH)? LOW:HIGH;
  digitalWrite(LED_BUILTIN, LED_STATE);
}

void countUp() {
  COUNT++;
}
