/*
 *  scode.h
 *
 */

#include <string>

#ifndef SCODE_H
#define SCODE_H


#define	SCODE_SET_X		1 
#define	SCODE_SET_Y		2
#define	SCODE_SET_ROT	3
#define	SCODE_SET_SPEED 4
#define	SCODE_MOVE_TO	5
#define	SCODE_BITMAP	6
#define	SCODE_DELAY		7
#define	SCODE_NOP		8

#define SEPIA_SETTING_INTENSITY_DELAY_MULTIPLIER 128
#define SEPIA_SETTING_GALVO_TRAVEL_SPEED 129

#define SEPIA_IMAGE 0
#define SEPIA_VECTOR 255

using namespace std;
/*
 *	the header command to start a serie of scodes. there are maximum 256 scodes in one package ( excluding header ).
 */
string scode_header();
/* move to new x location ( the galvo is not actually moved ) */
string scode_set_x(uint16_t x);
/* move to new y location ( the galvo is not actually moved ) */
string scode_set_y(uint16_t y);
/**
 *	steps is spacing between the dots. draw every steps pixel
 *	steps 0 means go as quickly as possible
 */
string scode_move_to(uint16_t steps);
/**
 *	set the speed for lines ( the amount of time the laser rests on a pixel.
 */ 
string scode_set_speed(uint16_t speed);
/**
 *	wait for a certain amount of time
 */
string scode_delay(uint16_t delay);
/**
 *	end a sequence of commands with this Nope command
 */
string scode_nop();
/**
 *	
 */
string sepia_intensity_modifier(uint16_t delay);

#endif

