int16_t textArray1[100], textArray2[100], textArray3[100];
float result[5];
unsigned long c = 1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT); //blue potassium
  pinMode(A1, INPUT); //green phophorous
  pinMode(A2, INPUT); //red Nitrogen
}

void loop(){
while(c <= 30){
  // put your main code here, to run repeatedly:
  int ldr1 = analogRead(A0);
  int ldr2 = analogRead(A1);
  int ldr3 = analogRead(A2);
  textArray1[c] = ldr1;
  textArray2[c] = ldr2;
  textArray3[c] = ldr3;
  c += 1;
}
  float avg1 = 0, ans1 = 0;
  for(int i = 0; i <= c - 1; i++){
    ans1 = ans1 + textArray1[i];
  }
  avg1 = ans1 / (c - 1);
  float temp1 = avg1 / 773.0;
  double per1 = (temp1 * 100) ; 
//  double per1 = 78.34; 
   Serial.println(per1);
   result[0] = per1;
//---------------------------------------------------------------------------------
  
  float avg2 = 0, ans2 = 0;
  for(int i = 0; i <= c - 1; i++){
    ans2 = ans2 + textArray2[i];
  }
  avg2 = ans2 / (c - 1);
  float per2 = (avg2 / 487.0) *100;
  //double per2 = (temp2 * 100) ;
  //double per2 = 30.48; 
   Serial.println(per2);
   result[1] = per2;

//-------------------------------------------------------------------------
  float avg3 = 0, ans3 = 0;
  for(int i = 0; i <= c - 1; i++){
    ans3 = ans3 + textArray3[i];
  }
  avg3 = ans3 / (c - 1);
  float temp3 = avg3 / 373.0;
  double per3 = (temp3 * 100) ;
  //double per3 = 15.36;
   Serial.println(per3);

   result[2] = per3;

//    Serial.println(result);
//for(int i = 0; i < 3; i++){
//  Serial.println(result[i]);
//  Serial.println(" ");
//}
//-------------------------------------------------------------------------------

   delay(100000);
}
