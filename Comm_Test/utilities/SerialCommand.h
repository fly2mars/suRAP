/**
 * SerialCommand - A Wiring/Arduino library to tokenize and parse commands
 * received over a serial port.
 * 
 * Copyright (C) 2012 Stefan Rado
 * Copyright (C) 2011 Steven Cogswell <steven.cogswell@gmail.com>
 *                    http://husks.wordpress.com
 * 
 * Version 20120522
 * 
 * This library is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this library.  If not, see <http://www.gnu.org/licenses/>.
 */
#ifndef SerialCommand_h
#define SerialCommand_h

#if defined(WIRING) && WIRING >= 100
  #include <Wiring.h>
#elif defined(ARDUINO) && ARDUINO >= 100
  #include <Arduino.h>
#else
  #include <WProgram.h>
#endif
#include <string.h>

#include "utilities.h"
// Size of the input buffer in bytes (maximum length of one command plus arguments)
#define SERIALCOMMAND_BUFFER 128
// Maximum length of a command excluding the terminating null
#define SERIALCOMMAND_MAXCOMMANDLENGTH 8

// Uncomment the next line to run the library in debug mode (verbose messages)
// #define SERIALCOMMAND_DEBUG


class SerialCommand {
  public:
    SerialCommand();      // Constructor
    void addCommand(const char *command, void(*function)());  // Add a command to the processing dictionary.
    void setDefaultHandler(void (*function)(const char *));   // A handler to call when no valid command received.

    void readSerial();    // Main entry point.
    void clearBuffer();   // Clears the input buffer.
    char *next();         // Returns pointer to next token found in command buffer (for getting arguments to commands	).
    void unnext();        // undo the last call of next

	bool getParamInt(int16_t &param);
	bool getParamString(char* &param);
	bool getParamFloat(float &param);

	bool getNamedParamInt(const char* name,    int16_t &param, bool &paramSet);
	bool getNamedParamString(const char* name, char* &param,   bool &paramSet);
	bool getNamedParamFloat(const char* name,  float &param,   bool &paramSet);

	void computeChecksum(char *str, uint8_t &checksum);
	bool endOfParams();
	void useChecksum(bool really);
	bool isChecksum() { return checksum; };

	uint8_t getErrorCode() { return errorCode;};

	enum errorCode { NO_ERROR = 0, CHECKSUM_EXPECTED = 1, CHECKSUM_WRONG = 2 };
  private:
	bool getNamedParam(const char* name,    char* &paramValue);

    // Command/handler dictionary
    struct SerialCommandCallback {
      char command[SERIALCOMMAND_MAXCOMMANDLENGTH + 1];
      void (*function)();
    };                                    // Data structure to hold Command/Handler function key-value pairs
    SerialCommandCallback *commandList;   // Actual definition for command/handler array
    byte commandCount;

    // Pointer to the default handler function
    void (*defaultHandler)(const char *);

    char delim[2]; // null-terminated list of character to be used as delimeters for tokenizing (default " ")
    char term;     // Character that signals end of command (default '\n')

    char buffer[SERIALCOMMAND_BUFFER + 1]; // Buffer of stored characters while waiting for terminator character
    byte bufPos;                        // Current position in the buffer
    char *last;                         // State variable used by strtok_r during processing
    char *savelast;                         // State variable used by strtok_r during processing
	
	bool withChecksum;
	uint8_t checksum;
	uint8_t errorCode;
};

#endif //SerialCommand_h
