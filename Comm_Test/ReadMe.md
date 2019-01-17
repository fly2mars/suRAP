### 1. 说明
这是一个在Teensy 3.x上调试与服务器通讯的测试代码。

### 2. 运行
#### IDE与编译设置
与测试代码[controller test](https://github.com/fly2mars/suRAP/tree/master/Controller_Test)相同
* Arduino 1.8.8 + [Teensyduino](https://www.pjrc.com/teensy/teensyduino.html)
* 设置开发板为Teensy 3.5
* 拷贝代码中[utilities]目录和Libraries中的[Herkulex]目录到Arduino的库目录([Arduino安装目录]/[libraries])

### 3. 代码

#### [Protocal](#)
命令字符串格式：
[CMD name] + [space] + [parameter]
CMD name在CommDef.h中定义，共8种，可根据打印过程和装备的需要对指令进行扩展。
<pre>                                                
	LED_CMD = 0,
	HELP_CMD = 1,
	ECHO_CMD = 2,
	ENABLE_CMD = 3,
	DISABLE_CMD = 4,
	POWER_CMD = 5,
	KNOB_CMD = 6,
	STEP_CMD = 7,
	CHECKSUM_CMD = 8,
	MEM_CMD = 9,
	GET_CMD = 10,
	SET_CMD = 11,
	MOVETO_CMD = 12,
	LOG_CMD = 13,
	INFO_CMD = 14,
	SETUP_CMD = 15,
	PRINT_CMD = 16,
	PRINTLN_CMD = 17
</pre>						
example:
   >* ECHO Hello   
   >* MOVETO 2.20 0.00 2.00 0.00 1.00 1.00 3

#### [WalterServer](#)
在初始化中检测端口（eg.COM3, COM4)，成功后，每10毫秒从动作规划端扫描
```
cortexOk = TrajectoryExecution::getInstance().setup(CortexSampleRate);
```

调用CortexController::.setupCommunication()进行连接测试：

```
bool ok= serialLog.connect(COM4, 115200);
bool ok= serialLog.connect(COM3, 115200);

```

可以先去掉日志发送端口COM4的相关功能（在），只测试命令端口COM3


```
bool CortexController::setupCommunication(){
//注释掉563-568行
   
}
```

#### [Arm Controller](#)


HostCommunication对象中仅保留 cmd_ECHO和cmd_CHECKSUM响应进行测试。

```
#include <HerkuleX.h>
#include <Arduino.h>
#include "Config.h"
#include <i2c_t3.h>
#include "hostCommunication.h"


// global variables declared in pins.h
HardwareSerial* cmdSerial = &Serial5;     // UART used to communicate with Cerebellum
HardwareSerial* logger = &Serial4;      // UART used to log


int n=1; //motor ID - verify your ID !!!!
void setup()  
{
  hostComm.setup();
}

void loop(){
 
  uint32_t now = millis();
  hostComm.loop(now);
}

```
