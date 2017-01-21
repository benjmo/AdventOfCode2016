#!/usr/bin/python3

import hashlib
import re

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   freqCounts = [{}, {}, {}, {}, {}, {}, {}, {}]
   for line in lines:
      for i in range(0, 8):
         if (line[i] in freqCounts[i]):
            freqCounts[i][line[i]] += 1
         else:
            freqCounts[i][line[i]] = 1

   message = ""
   for freqCount in freqCounts:
      sortedFreqCount = sorted(freqCount.items(), key=lambda x: x[1])
      message += sortedFreqCount[0][0]

   print(message)




if __name__ == '__main__':
   main()