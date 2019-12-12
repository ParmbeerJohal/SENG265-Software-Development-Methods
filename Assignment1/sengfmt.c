/*
 * UVic SENG 265, Fall 2018, A#1
 *
 * This will contain a solution to sengfmt. In order to complete the
 * task of formatting a file, it must open and read the file (hint: 
 * using fopen() and fgets() method) and format the text content base on the 
 * commands in the file. The program should output the formated content 
 * to the command line screen by default (hint: using printf() method).
 *
 * Supported commands include:
 * ?width width :  Each line following the command will be formatted such 
 *                 that there is never more than width characters in each line 
 * ?mrgn left   :  Each line following the command will be indented left spaces 
 *                 from the left-hand margin.
 * ?fmt on/off  :  This is used to turn formatting on and off. 
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
#ifdef DEBUG
	printf("%s does nothing right now.\n", argv[0]);
#endif
	exit(0);
}
