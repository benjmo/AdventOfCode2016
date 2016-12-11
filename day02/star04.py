#!/usr/bin/python3

import re

KEY_A = 10
KEY_B = 11
KEY_C = 12
KEY_D = 15

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   digits = ''
   currDigit = 5

   for line in lines:
      for char in line:
         if (char == 'U' and currDigit not in [1, 2, 4, 5, 9]):
            if (currDigit == 3):
               currDigit -= 2
            else:
               currDigit -= 4
         elif (char == 'D' and currDigit not in [5, 9, KEY_A, KEY_C, KEY_D]):
            if (currDigit == 1):
               currDigit += 2
            else:
               currDigit += 4
         elif (char == 'L' and currDigit not in [1, 2, 5, KEY_A, KEY_D]):
            currDigit -= 1
         elif (char == 'R' and currDigit not in [1, 4, 9, KEY_C, KEY_D]):
            currDigit += 1

      currChar = currDigit
      if (currDigit == KEY_A):
         currChar = 'A'
      elif (currDigit == KEY_B):
         currChar = 'B'
      elif (currDigit == KEY_C):
         currChar = 'C'
      elif (currDigit == KEY_D):
         currChar = 'D'
      digits = digits + str(currChar)

   print(digits)

if __name__ == "__main__":
   main()