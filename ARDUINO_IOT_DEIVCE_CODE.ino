#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "2HGFC2F88JH022594";
const char* password = "GVbVe8A5qLeVNtevTP42cB";

const int ledPin = 2;
const int Ldigit = 15;

IPAddress staticIP(192, 168, 0, Ldigit);
IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 240);

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  connectToWiFi();
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    blinkLED();
  }
}

void connectToWiFi() {
  WiFi.config(staticIP, gateway, subnet);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

const int delayed = 1980;

void blinkLED() {
  digitalWrite(ledPin, LOW);
  delay(Ldigit*5);
  digitalWrite(ledPin, HIGH);
  delay(delayed);
}
