### 1. 说明
这是一个在Teensy 3.x上调试HerkuleX电机的测试代码，使用了[dfrobot](https://www.dfrobot.com/wiki/index.php/Herkulex_DRS-0101_SKU:SER0032)的例子和。[BotCortex](https://github.com/jochenalt/Walter/tree/master/code/BotCortex)中的库代码，编译通过，但未上传到Teensy上测试。

### 2. 运行
#### IDE与编译设置
* Arduino 1.8.8 + [Teensyduino](https://www.pjrc.com/teensy/teensyduino.html)
* 设置开发板为Teensy 3.5
* 拷贝代码中[utilities]目录和Libraries中的[Herkulex]目录到Arduino的库目录([Arduino安装目录]/[libraries])

### 3. 代码
按照walter项目中的BotCortex的代码配置，以方便进一步修改和集成。

```
#include <HerkuleX.h>
#include <Arduino.h>
#include "Config.h"
#include <i2c_t3.h>
//#include "Libraries/HerkuleX/HerkuleX.h"

// global variables declared in pins.h
HardwareSerial* cmdSerial = &Serial5;     // UART used to communicate with Cerebellum
HardwareSerial* logger = &Serial4;      // UART used to log
HardwareSerial* servoComm = &Serial1;   // UART used to communicate with the HerkuleX servos
HardwareSerial* printerComm = &Serial6;   // UART used to control the thermal printer

int n=1; //motor ID - verify your ID !!!!
void setup()  
{
  delay(2000);  //a delay to have time for serial monitor opening
  Serial.begin(115200);    // Open serial communications
  Serial.println("Begin");
  Herkulex.beginSerial(servoComm, 115200); //open serial port 1 
  Herkulex.reboot(n); //reboot first motor
  delay(500);   
  Herkulex.initialize(); //initialize motors
  delay(200);  
}

void loop(){
  Serial.println("Move Angle: -100 degrees");
  Herkulex.moveOneAngle(n, -100, 1000, LED_BLUE); //move motor with 300 speed  
  delay(1200);
  Serial.print("Get servo Angle:");
  Serial.println(Herkulex.getAngle(n));
  Serial.println("Move Angle: 100 degrees");
  Herkulex.moveOneAngle(n, 100, 1000, LED_BLUE); //move motor with 300 speed  
  delay(1200);
  Serial.print("Get servo Angle:");
  Serial.println(Herkulex.getAngle(n));
  
}

```

为独立编译，将utilities中的代码作为一个库安装到Arduino目录中。[BotCortex](https://github.com/jochenalt/Walter/tree/master/code/BotCortex)还包含了与上位机通讯时公用的错误定义(core)代码、机构运动控制相关的配置代码(ActuatorProperty)，以及通讯命令定义(CommDef)怠慢，都从公用目录中抽取出来，拷贝utilities中。