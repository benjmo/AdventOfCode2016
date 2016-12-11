#!/usr/bin/python3

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   triCount = 0
   for line in lines:
      sides = line.split()
      sides = list(map(int, sides))

      if (sides[0] + sides[1] > sides[2] and
          sides[0] + sides[2] > sides[1] and 
          sides[1] + sides[2] > sides[0]):
         triCount += 1

   print(triCount)

if __name__ == '__main__':
   main()