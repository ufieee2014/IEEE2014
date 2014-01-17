/*
 * main.cpp
 *
 * Created: 9/8/2013 8:34:40 PM
 *  Author: Mason
 */ 

#ifndef F_CPU
#define F_CPU 32000000
#endif

#include <avr/io.h>
#include <stdio.h>
#include <util/delay.h>
#include "init.h"
#include "hwlib/motor.h"
#include "hwlib/pid.h"
#include "hwlib/uart.h"	
#include "hwlib/twi.h"
#include "hwlib/mpu6050.h"
#include "hwlib/uart_handler_pointers.h"


int main() {

	init();

	while(1) {
		
		if(uart_get_msg_status()) {
			uart_set_msg_status(false);
			char* message = uart_get_msg();
			// message[0] is the length, message[1] is the type, and message[2] is the first part of the message.
			HandlerPointers[(uint8_t)message[1]]((char*)&message[2], message[0]);
		}
		
		
	}
}
