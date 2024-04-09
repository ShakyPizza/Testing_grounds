/*
* LAB: 3
* Name: ESP32 String + Variable Serial Print
* Author: Khaled Magdy
* For More Info Visit: www.DeepBlueMbedded.com
*/
 
int Counter = 0;
 
void setup()
{
  Serial.begin(115200);
}
 
void loop()
{
  Serial.print("Counter Value = ");
  Serial.println(Counter++);
  delay(1000);
}