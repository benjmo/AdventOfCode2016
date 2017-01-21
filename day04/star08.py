#!/usr/bin/python3

import re
import collections
import string

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   realSectorSum = 0

   for line in lines:
      letters = re.search('^[A-Za-z\-]+', line).group(0).replace('-', '')
      letterCount = [0] * 26
      for letter in letters:
         index = ord(letter) - ord('a')
         letterCount[index] += 1

#      print(letters)
      sectorID = int(re.search('[0-9]+', line).group(0))

      checksum = re.search('\[[a-z]+\]', line).group(0).replace('[', '').replace(']', '')
      charCounter = dict(collections.Counter(letters))
      sortedChars = sorted(charCounter.items(), key=lambda x: (-x[1],x[0]))
      testChecksum = ""

      for char, count in sortedChars:
         if (len(testChecksum) == 5):
            break
         testChecksum += char

#      print(testChecksum)
      if (testChecksum == checksum):
         realSectorSum += sectorID
         shift = sectorID % 26
         decryptedName = ""
         for char in letters:
            decryptedName += chr(((ord(char) - ord('a')) + (sectorID % 26)) % 26 + ord('a'))
         if ("northpole" in decryptedName):
            # kind of hacky here, we omitted dashes so spaces aren't visible anymore
            # but in the end all we're looking for is a number
            print(sectorID)
            exit()

   print(realSectorSum)


#      getChecksum(letterCount)

if __name__ == '__main__':
   main()