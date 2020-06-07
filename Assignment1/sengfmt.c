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

/*
 * File: sengfmt.c
 * Student Name  Parm Johal:
 * Student Number: V00787710
 * SENG 265 - Assignment 1
 */

 #include <stdio.h>
 #include <string.h>
 #include <stdlib.h>

 /* Defined in spec for input */
 #define MAX_IN_LINES 300
 #define MAX_IN_CHARS 132

 /* Global Variables */
 char output[MAX_IN_LINES * MAX_IN_CHARS];
 char processed[MAX_IN_CHARS];  /* Our formatted string. */
 int line_size = 0;             /* Keeps track of the size of the line we've processed. */

 /* Program options. These are flagged within the input file with ?fmt, ?wdth, ?mrgn */
 int fmt = 0;    /* Off by default. */
 int mrgn = 0;   /* Off by default. */
 int pgwdth = 0; /* Off by default. Turns on fmt if set. */

 int detect_control_sequence (char* line) {
   /* We need to make a copy of the string so strtok does not clobber. */
   char test[MAX_IN_CHARS];
   strncpy (test, line, MAX_IN_CHARS);
   /* Tokenize the string. */
   strtok (test, " \n");
   /* Detect a control sequence */
   if ( !strncmp(test, "?fmt", MAX_IN_CHARS) ) {
     char* opt = strtok (NULL, " \n");
     if ( !strncmp(opt, "on", 3) ) {
       fmt = 1;
     }
     else {
       fmt = 0;
     }
     return 1;
   }
   if ( !strncmp(test, "?mrgn", MAX_IN_CHARS) ) {
     int opt = atoi( strtok (NULL, " \n") );
     mrgn = opt;
     return 1;
   }
   if ( !strncmp(test, "?wdth", MAX_IN_CHARS) ) {
     int opt = atoi( strtok (NULL, " \n") );
     pgwdth = opt;
     fmt = 1;
     return 1;
   }
   return 0;
 }

 void process_line (char* line) {
   /* Function variables. (None for now! TODO: When we get malloc we should put processed here.) */

   /* Split the list into tokens */
   char* word = strtok (line, " \n"); /* Word is our current token. */

   /* For each word, check if we need a new line, set margins, cat it. */
   while (word) {
     /* Do we need a new line? */
     if (line_size + strlen (word) >= pgwdth) { /* mrgn is always specified if fmt is. */
       strncat (processed, "\n", 1);
       line_size = 0;
       /* Check if we need to set margins. */
       if (mrgn) {
         /* Create as many margin spaces as we need. */
         while (line_size < mrgn) {
           strncat (processed, " ", 1);
           line_size++;
         }
       }
     }
     /* Otherwise, add a space. */
     else if (line_size >= mrgn+1) {
       line_size++;
       strncat (processed, " ", 1);
     }
     line_size += strlen (word);
     strncat (processed, word, MAX_IN_CHARS);
     word = strtok (NULL, " \n");
   }

   return;
 }

 int main (int argc, char** args) {
   /* Function variables. */
   FILE* file;
   char line[MAX_IN_CHARS];

   /* Read the file, return an error if it's not valid. */
   file = fopen (args[1], "r");
   if (file == NULL) {
     return -1;
   }

   /* Read through each line, stop at the end. */
   while ( fgets (line, MAX_IN_CHARS, file) ) {
     /* Check for control sequences. */
     if ( detect_control_sequence (line) ) {
       continue;
     }

     /* Edge case for the first line of the output. This can go somewhere better. */
     if (mrgn) {
       /* Create as many margin spaces as we need. */
       while (line_size < mrgn) {
         strncat (processed, " ", 1);
         line_size++; /* Make sure we adjust the line size. */
       }
     }
     /* Process, or don't process, the line based on the control sequences. */
     if (fmt && !strncmp (line, "\n", 1) ) {
       strncat (output, "\n\n", MAX_IN_CHARS);
       line_size = 0;
     }
     if (fmt) {
       process_line (line); /* We could just use a malloc heap here and assign it, but we can't. */
       strncat (output, processed, MAX_IN_CHARS);
       strncpy (processed, "", MAX_IN_CHARS);
     }
     else {
       strncat (output, line, MAX_IN_CHARS);
     }
   }

   /* Zastre's output tests files all have a \n at the end if they are formatted. */
   if (fmt) {
     strncat (output, "\n", MAX_IN_CHARS);
   }

   printf("%s", output);

   /* Return Successfully. */
   return 0;
 }
