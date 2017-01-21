#!/usr/bin/python3

# Your puzzle input is ojvtpuvg.

import hashlib
import re

def main():
   i = 0
   doorID = "ojvtpuvg"
   password = ""
   while True:
      hashObject = hashlib.md5()
      hashObject.update((doorID + str(i)).encode('utf-8'))
      if (re.search(r'^00000', hashObject.hexdigest())):
         password += hashObject.hexdigest()[5]
         if (len(password) == 8):
            break
         print(hashObject.hexdigest() + " " + str(i))
      i += 1

   print(password)




if __name__ == '__main__':
   main()