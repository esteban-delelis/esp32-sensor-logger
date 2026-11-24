#include <WiFi.h>
#include <WiFiUdp.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"
#include "secrets.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();
WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  if (!sht31.begin(0x44)) {
    Serial.println("SHT31 introuvable");
    while (true) delay(1000);
  }
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());
}

void loop() {
  float t = sht31.readTemperature();
  float h = sht31.readHumidity();
  if (!isnan(t) && !isnan(h)) {
    char msg[64];
    snprintf(msg, sizeof(msg), "%lu,%.2f,%.2f", millis(), t, h);
    udp.beginPacket(PC_IP, PC_PORT);
    udp.print(msg);
    udp.endPacket();
    Serial.println(msg);
  }
  delay(1000);
}