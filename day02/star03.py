#!/usr/bin/python3

import re

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   digits = ''
   currDigit = 5

   for line in lines:
      for char in line:
         if (char == 'U' and currDigit > 3):
            currDigit -= 3
         elif (char == 'D' and currDigit < 7):
            currDigit += 3
         elif (char == 'L' and currDigit not in [1, 4, 7]):
            currDigit -= 1
         elif (char == 'R' and currDigit not in [3, 6, 9]):
            currDigit += 1
      digits = digits + str(currDigit)

   print(digits)

if __name__ == "__main__":
   main()