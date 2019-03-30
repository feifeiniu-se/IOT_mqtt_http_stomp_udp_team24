#define led_dpin 11
#define buzzer_dpin 12
#define dht_dpin 13
#define light_apin A0
#define rotation_apin A5

//智能家居系统
//温湿度传感器检测温度和湿度，光线传感器检测光强，旋钮传感器用于设置光照强度的阈值
//当温度高于25或者湿度低于15时，蜂鸣器响
//当光线传感器值大于旋钮值（亮度低于设定值）时，LED灯亮
//MQTT -> 温度
//STOMP -> 湿度
//HTTP -> 光强
//UDP -> 旋钮

byte bGlobalErr;
byte dht_dat[5];
int light = 0;
int rotation = 0;
int humdity = 0;
int temperature = 0;
int buzzerState = 0;//0为关，1为开
int ledState = 0;//0为关，1为开
void setup() {
  InitDHT();//初始化DHT
  Init();//初始化其他传感器
  Serial.begin(9600);
  delay(300);
  delay(700);
}

void loop() {
  ReadDHT();
  switch (bGlobalErr) {
    case 0:
      humdity = dht_dat[0];
      temperature = dht_dat[2];
      if (humdity < 15 || temperature > 25) {
        digitalWrite(buzzer_dpin, LOW);
        buzzerState = 1;//蜂鸣器响，状态值为1
      }
      else {
        digitalWrite(buzzer_dpin, HIGH);
        buzzerState = 0;//蜂鸣器关，状态值为0
      }
      break;
    case 1:
      Serial.println("Error 1: DHT start condition 1 not met.");
      break;
    case 2:
      Serial.println("Error 2: DHT start condition 2 not met.");
      break;
    case 3:
      Serial.println("Error 3: DHT checksum error.");
      break;
    default:
      Serial.println("Error: Unrecognized code encountered.");
      break;
  }

  light = Read_light();
  rotation = Read_rotation();
  if (light > rotation) {
    digitalWrite(led_dpin, HIGH);
    ledState = 1;
  }
  else {
    digitalWrite(led_dpin, LOW);
    ledState = 0;
  }

  //输出结果
  Serial.print("light ");
  Serial.print(light);
  Serial.print(" ");
  Serial.print("rotation ");
  Serial.print(rotation);
  Serial.print(" ");
  Serial.print("ledState ");
  Serial.print(ledState);
  Serial.print(" ");
  Serial.print("humdity ");
  Serial.print(humdity, DEC);
  Serial.print(" ");
  Serial.print("temperature ");
  Serial.print(temperature, DEC);
  Serial.print(" ");
  Serial.print("buzzer ");
  Serial.print(buzzerState, DEC);  
  Serial.println(" ");

  delay(800);
  delay(1000);
}

//初始化DHT
void InitDHT() {//初始化DHT
  pinMode(dht_dpin, OUTPUT);
  digitalWrite(dht_dpin, HIGH);
}
//初始化其他传感器
void Init() {//初始化LED，Buzzer
  pinMode(led_dpin, OUTPUT);
  digitalWrite(led_dpin, LOW);
  pinMode(buzzer_dpin, OUTPUT);
  digitalWrite(buzzer_dpin, HIGH);
}

void ReadDHT() {
  bGlobalErr = 0;
  byte dht_in;
  byte i;
  digitalWrite(dht_dpin, LOW);
  delay(20);
  digitalWrite(dht_dpin, HIGH);
  delayMicroseconds(40);
  pinMode(dht_dpin, INPUT);
  //delayMicroseconds(40);
  dht_in = digitalRead(dht_dpin);

  if (dht_in) {
    bGlobalErr = 1;
    return;
  }
  delayMicroseconds(80);
  dht_in = digitalRead(dht_dpin);

  if (!dht_in) {
    bGlobalErr = 2;
    return;
  }
  delayMicroseconds(80);
  for (i = 0; i < 5; i++)
    dht_dat[i] = read_dht_dat();
  pinMode(dht_dpin, OUTPUT);
  digitalWrite(dht_dpin, HIGH);
  byte dht_check_sum =
    dht_dat[0] + dht_dat[1] + dht_dat[2] + dht_dat[3];
  if (dht_dat[4] != dht_check_sum)
  {
    bGlobalErr = 3;
  }
};

byte read_dht_dat() {
  byte i = 0;
  byte result = 0;
  for (i = 0; i < 8; i++) {
    while (digitalRead(dht_dpin) == LOW);
    delayMicroseconds(30);
    if (digitalRead(dht_dpin) == HIGH)
      result |= (1 << (7 - i));
    while (digitalRead(dht_dpin) == HIGH);
  }
  return result;
}
int Read_light() {
  int lightValue = analogRead(A0);
  return lightValue;
}
int Read_rotation() {
  int rotationValue = analogRead(A5);
  return rotationValue;
}
