#!/usr/bin/python3

# Your puzzle input is ojvtpuvg.

import hashlib
import re

def main():
   i = 0
   doorID = "ojvtpuvg"
   password = [' '] * 8
   while True:
      hashObject = hashlib.md5()
      hashObject.update((doorID + str(i)).encode('utf-8'))
      if (re.search(r'^00000', hashObject.hexdigest())):
         passIndex = hashObject.hexdigest()[5]
         if (passIndex in "01234567" and password[int(passIndex)] == " "):
            password[int(passIndex)] = hashObject.hexdigest()[6]
         if (not " " in password):
            break
         print(hashObject.hexdigest() + " " + str(i))
         print(password)
      i += 1

   print("".join(password))




if __name__ == '__main__':
   main()