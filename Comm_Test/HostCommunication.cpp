/*
* HostCommunication.cpp
*
* Created: 26.06.2016 22:16:52
* Author: JochenAlt
*/


#include <I2CPortScanner.h>
#include "HostCommunication.h"
//#include <Controller.h>
//#include <BotMemory.h>
#include <CommDef.h>
#include <utilities.h>
#include <core.h>
//#include "LightsController.h"
//#include "Printer.h"


HostCommunication hostComm;
//extern Controller controller;
//extern BotMemory botMemory;
//
//extern void setCortexBoardLED(bool onOff);
//extern void setLEDPattern();

void replyOk() {
	cmdSerial->println(F(">ok"));
	cmdSerial->print(F(">"));
}

void replyError(int errorCode) {
	int patchedErrorCode = errorCode;
	if (errorCode == PARAM_NUMBER_WRONG) {
		if (hostComm.sCmd.getErrorCode() != 0) {
			patchedErrorCode = hostComm.sCmd.getErrorCode();
		}
	}
	cmdSerial->print(F(">nok("));
	cmdSerial->print(patchedErrorCode);
	cmdSerial->println(")");
	cmdSerial->print(F(">"));
}


void cmd_ECHO() {
  bool paramsOK = true; 
  char* param = 0;
  paramsOK = hostComm.sCmd.getParamString(param) && paramsOK; 
  paramsOK = hostComm.sCmd.endOfParams() && paramsOK;

  
  if (paramsOK) {
    cmdSerial->print(param);

    replyOk();
  }
  else {
    replyError(PARAM_NUMBER_WRONG);
  }
}

// the only command that does not require a checksum
void cmd_CHECKSUM() {
  char* onoff = 0;
  bool paramsOK = hostComm.sCmd.getParamString(onoff);
  // paramsOK = hostComm.sCmd.endOfParams() && paramsOK;

  if (paramsOK) {
    bool valueOK = false;
    if (strncasecmp(onoff, "on", 2) == 0) {
      hostComm.sCmd.useChecksum(true);
      valueOK = true;
    }
    if (strncasecmp(onoff, "off", 3) == 0) {
      hostComm.sCmd.useChecksum(false);
      valueOK = true;
    }
    if (valueOK) {
      replyOk();
    }
    else
      replyError(PARAM_WRONG);
  } else {
      replyError(PARAM_NUMBER_WRONG);
  }
}

// This gets set as the default handler, and gets called when no other command matches.
void cmdUnrecognized(const char *command) {
	cmdSerial->print(command);
	replyError(UNRECOGNIZED_CMD);
}


// default constructor
HostCommunication::HostCommunication()
{
} //HostCommunication



void HostCommunication::setup() {
  
  // Reset with real callback functions defined above
  commDef[2].cmdFunction = cmd_ECHO;
  commDef[8].cmdFunction = cmd_CHECKSUM;
	// Setup callbacks for SerialCommand commands
	for (int i = 0;i<CommDefType::NumberOfCommands;i++) {
		sCmd.addCommand(commDef[i].name, commDef[i].cmdFunction);
	}
	
	sCmd.setDefaultHandler(cmdUnrecognized);   // Handler for command that isn't matched  (says "What?")

	sCmd.useChecksum(false);
}

void HostCommunication::loop(uint32_t now) {
	sCmd.readSerial();     // We don't do much, just process serial commands
}
