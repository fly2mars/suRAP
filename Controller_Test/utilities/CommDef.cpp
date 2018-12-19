#include "CommDef.h"

// functions pointers implementing a command. Used on Cortex' side only. On the webserver, these commands are implemented with empty functions
//
//extern void cmdLED();
//extern void cmdPOWER();
//extern void cmdECHO();
//extern void cmdSETUP();
//extern void cmdMOVETO();
//extern void cmdDISABLE();
//extern void cmdENABLE();
//extern void cmdGET();
//extern void cmdSET();
//extern void cmdSTEP();
//extern void cmdMEM();
//extern void cmdCHECKSUM();
//extern void cmdKNOB();
//extern void cmdLOG();
//extern void cmdHELP();
//extern void cmdINFO();
//extern void cmdCONFIG();
//extern void cmdPRINT();
//extern void cmdPRINTLN();
void cmdHELP() {};
void cmdSTEP() {};
void cmdLED() {};
void cmdPOWER(){};
void cmdECHO(){};
void cmdDISABLE(){};
void cmdSETUP(){};
void cmdENABLE(){};
void cmdGET(){};
void cmdSET(){};
void cmdMOVETO(){};
void cmdMEM(){};
void cmdCHECKSUM(){};
void cmdKNOB(){};
void cmdLOG(){};
void cmdINFO(){};
void cmdCONFIG() {};
void cmdPRINT(){};
void cmdPRINTLN(){};
CommDefType commDef[CommDefType::NumberOfCommands] {
	//cmd ID						Name, 		timeout,	function pointer
	{ CommDefType::LED_CMD,		    "LED",		500, 		cmdLED },
	{ CommDefType::HELP_CMD,	    "HELP", 	500, 		cmdHELP },
	{ CommDefType::ECHO_CMD,	    "ECHO", 	500, 		cmdECHO },
	{ CommDefType::ENABLE_CMD,		"ENABLE", 	500, 		cmdENABLE},
	{ CommDefType::DISABLE_CMD,		"DISABLE", 	200, 		cmdDISABLE },
	{ CommDefType::SETUP_CMD,		"SETUP", 	1500, 		cmdSETUP},
	{ CommDefType::POWER_CMD,		"POWER", 	500, 		cmdPOWER },
	{ CommDefType::KNOB_CMD,		"KNOB", 	200, 		cmdKNOB },
	{ CommDefType::STEP_CMD,		"STEP", 	200, 		cmdSTEP },
	{ CommDefType::CHECKSUM_CMD,	"CHECKSUM", 200, 		cmdCHECKSUM},
	{ CommDefType::MEM_CMD,	        "MEM", 		200, 		cmdMEM},
	{ CommDefType::SET_CMD,	        "SET", 		100, 		cmdSET},
	{ CommDefType::GET_CMD,	        "GET", 		100, 		cmdGET},
	{ CommDefType::MOVETO_CMD,	    "MOVETO", 	75, 		cmdMOVETO},
	{ CommDefType::LOG_CMD,	        "Log", 		200, 		cmdLOG },
	{ CommDefType::INFO_CMD,	    "INFO", 	200, 		cmdINFO },
	{ CommDefType::PRINT_CMD,	    "PRINT", 	1000, 		cmdPRINT},
	{ CommDefType::PRINTLN_CMD,	    "PRINTLN", 	1000, 		cmdPRINTLN}

};

// returns command definition of the passed command
CommDefType* CommDefType::get(CommDefType::CommandType cmd) {
	for (int i = 0;i<NumberOfCommands;i++) {
		if (commDef[i].cmd == cmd)
			return &commDef[i];
	}
	return 0;
}
