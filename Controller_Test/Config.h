
/*
 * Config.h
 *
 * Configuration of servos, steppers, etc.
 * Author: JochenAlt
 */


#ifndef __ACTUATOR_CONFIG_H_
#define __ACTUATOR_CONFIG_H_

#include "Arduino.h"
#include "Libraries/AMS_AS5048B/ams_as5048b.h"					// library for rotary encoder AMS-5048B
#include "Libraries/sn3218/sn3218.h"							// library for 18-channel PWM controller (panel)

#define MAX_ACTUATORS 7						// total number of actuators
#define MAX_ENCODERS 5						// total number of encoders
#define MAX_STEPPERS 5						// total number of steppers
#define MAX_SERVOS 2						// total number of servos

#define HERKULEX_BAUD_RATE 115200			// baud rate for connection to herkulex servos
#define PRINTER_BAUD_RATE 9600				// baud rate for Adafruit Thermal Printer

#define MOTOR_KNOB_SAMPLE_RATE (56)		// every [ms] the potentiometer is sampled

#define SERVO_SAMPLE_RATE  56				// every [ms] the motors get a new position. 11.2ms is the unit Herkulex servos are working with, sample rate should be a multiple of that
#define SERVO_MOVE_DURATION 12				// herkulex servos have their own PID controller, so we need to add some time to a sample to make the movement smooth.
#define PIBOT_PULSE_WIDTH_US 2				// pulse width of one step which can be recognized by PiBot Driver (I tried this out)

#define I2C_BUS_RATE I2C_RATE_300			// frequency of i2c bus (1MHz KHz)
#define I2C_BUS_TYPE I2C_OP_MODE_ISR		// I2C library is using interrupts
#define ENCODER_FILTER_RESPONSE_TIME 5		// complementary filter of rotary encoder has this response time in [ms]

#define HAND_HERKULEX_MOTOR_ID    0xFD		// this is the HERKULEX_BROADCAST_ID used for all servos
#define GRIPPER_HERKULEX_MOTOR_ID 0xFC		// this ID has been programmed into the gripper servo explicitly

// encoder values have statics, so for calibration we take a some samples and use the average, if all samples are quite close to each other.
#define ENCODER_CHECK_MAX_VARIANCE 0.3	// maximum variance [�] in encoder calibration which is ok
#define ENCODER_CHECK_NO_OF_SAMPLES 5	// so many samples for calibration

// names of LEDs
#define LED_UPDATE_RATE 20

#define LED_SETUP 0
#define LED_HEARTBEAT 1
#define LED_ENABLED 2
#define LED_POWER_ON 3
#define LED_POSE_SAMPLE 4
#define LED_TRAJECTORY_MODE 5
#define LED_AMOK_MODE 6
#define LED_CONTROL_MODE 7
#define LED_UPPERARM 8
#define LED_HIP 9
#define LED_ELBOW 10
#define LED_FOREARM 11
#define LED_HAND 12
#define LED_WRIST 13
#define LED_BROKEN_LIGHT 14
#define LED_FINGER 15

enum ActuatorIdentifier {HIP=0 , UPPERARM=1, FOREARM=2, ELLBOW=3, WRIST=4, HAND=5, GRIPPER=6 };
extern void logActuator(ActuatorIdentifier actuatorNumber);

struct ActuatorSetupData {
	ActuatorIdentifier id;
	void print();
};

struct ServoSetupData {
	ActuatorIdentifier id;
	uint8_t herkulexMotorId;
	bool reverse;
	int16_t minTorque;
	int16_t maxTorque; // actually this is the maximum PWM value of Herkulex servo which is prop. to torque
	int16_t setupSpeed;
	void print();
};

enum WireColor { BLACK, GREEN, BLUE, RED, NON_COLOR };

struct StepperSetupData {
	ActuatorIdentifier id;
	bool direction;			// forward or reverse direction?

	uint8_t enablePIN;		// enabling the stepper driver
	uint8_t directionPIN;	// selecting direction of stepper driver
	uint8_t clockPIN;		// clock of stepper driver

	float degreePerStep;	// typically 1.8 or 0.9� per step
	float amps;				// current of the motor, not in use, for documentation only

	WireColor driverA1;		// not in use, just for documentation, color of stepper PINS
	WireColor driverA2;
	WireColor driverB1;
	WireColor driverB2;


	void print();
};

struct RotaryEncoderSetupData {
	ActuatorIdentifier id;
	uint8_t I2CAddress;
	uint8_t I2CBusNo;

	bool clockwise;
	void print();
};

struct RotaryEncoderConfig {
	ActuatorIdentifier  id;
	// uint8_t setupid;
	float  nullAngle;

	void print();
};

struct ServoConfig {
	ActuatorIdentifier  id;

	float nullAngle;
	float  maxAngle;			// [�]
	float  minAngle;			// [�]

	void print();
};

// contains the speed that is executed with the given number of microsteps (1/1 to 1/16)
#define NUMBER_OF_MICROSTEP_OPTIONS 5 // 2^5 = 16

struct StepperConfig {
	ActuatorIdentifier id;

	float maxAngle;			// [�]
	float minAngle;			// [�]
	float kP;				// PID controller
	float kD;				// PID controller
	float kI;				// PID controller
	float maxAcc;			// maximum acceleration in rpm/s
	float maxSpeed;			// maximum speed in rpm
	int   sampleRate;		// current sample rate of closed-loop

	int   microSteps;						// configured micro steps of Pibot stepper driver (1, 2, 4, 8, or 16)

	void print();
};

enum ActuatorType { SERVO_TYPE, STEPPER_ENCODER_TYPE, NO_ACTUATOR};

class ActuatorConfig {
	public:
	static void setDefaults();
	void print();

	ActuatorType actuatorType;
	ActuatorIdentifier id;
	union ConfigUnion {
		struct {
			ServoConfig servo;
		} servoArm;
		struct {
			RotaryEncoderConfig  encoder;
			StepperConfig stepper;
		} stepperArm;
	} config;
};

// all setup data is stored in a global structure
extern ActuatorSetupData		actuatorSetup[MAX_ACTUATORS];
extern StepperSetupData			stepperSetup[MAX_STEPPERS];
extern ServoSetupData			servoSetup[MAX_SERVOS];
extern RotaryEncoderSetupData	encoderSetup[MAX_ENCODERS];

#endif
