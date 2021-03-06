#include "core.h"
#include <sstream>
#include <string>

ErrorCodeType glbError = ErrorCodeType::ABSOLUTELY_NO_ERROR;

void resetError() {
	glbError = ErrorCodeType::ABSOLUTELY_NO_ERROR;
}

ErrorCodeType getLastError() {
	return glbError;
}

void setError(ErrorCodeType err) {
	// set error only if error has been reset upfront
	if (glbError == ErrorCodeType::ABSOLUTELY_NO_ERROR)
		glbError = err;
}

bool isError() {
	return glbError != ErrorCodeType::ABSOLUTELY_NO_ERROR;
}


std::string getErrorMessage(ErrorCodeType err) {
	std::ostringstream msg;
	switch (err) {
	case ABSOLUTELY_NO_ERROR: msg << "no error";break;

	// hostCommunication
	case CHECKSUM_EXPECTED: 			msg << "checksum expected";break;
	case CHECKSUM_WRONG: 				msg << "checksum wrong";break;
	case PARAM_WRONG: 					msg << "parameter wrong";break;
	case PARAM_NUMBER_WRONG: 			msg << "number of parameter wrong";break;
	case UNRECOGNIZED_CMD: 				msg << "unknown command";break;

	// encoder
	case ENCODER_CONNECTION_FAILED: 	msg << "Encoder connection failed";break;
	case ENCODER_CALL_FAILED: 			msg << "Rotary Encoder Call failed";break;
	case ENCODER_CHECK_FAILED: 			msg << "Rotary Encoder Check failed";break;

	// servos
	case HERKULEX_COMMUNICATION_FAILED: msg << "HerkuleX communication failed";break;
	case HERKULEX_STATUS_FAILED: 		msg << "HerkuleX status could not be retrieved";break;

	// Cortex Controller
	case CORTEX_CONNECTION_FAILED: 		msg << "cortex connection failed";break;
	case CORTEX_COM_FAILED: 			msg << CORTEX_COMMAND_SERIAL_PORT << " connection failed";break;
	case CORTEX_LOG_COM_FAILED: 		msg << CORTEX_LOGGER_SERIAL_PORT << " connection failed (logger)";break;
	case CORTEX_NO_RESPONSE: 			msg << "no response from cortex";break;
	case CORTEX_POWER_ON_WITHOUT_SETUP: msg << "cannot power on without being setup";break;
	case CORTEX_SETUP_MISSING: 			msg << "call setup upfront";break;

	// configuration errors
	case MISCONFIG_NO_STEPPERS: 		msg << "misconfiguration: no steppers";break;
	case MISCONFIG_NO_ENCODERS: 		msg << "misconfiguration: no encoders";break;
	case MISCONFIG_STEPPER: 			msg << "misconfiguration: no servo";break;
	case MISCONFIG_TOO_MANY_SERVOS: 	msg << "misconfiguration: too many servos";break;
	case MISCONFIG_TOO_MANY_ENCODERS: 	msg << "misconfiguration: too many encoders";break;
	case MISCONFIG_TOO_MANY_STEPPERS: 	msg << "misconfiguration: too many steppers";break;

	// Webserver
	case WEBSERVER_TIMEOUT: 			msg << "no response from webserver (timeout)";break;

	case UNKNOWN_ERROR: 				msg << "mysterious error";break;

	default:
		msg << "unknown error message";
	}
	msg << " (" << (int)err << ")";

	return msg.str();
}

std::string getLastErrorMessage() {
	if (isError())
		return getErrorMessage(getLastError());
	return "";
}
