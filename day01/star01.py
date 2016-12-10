#!/usr/bin/python3

import re

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

ANTI_CLOCKWISE = -1
CLOCKWISE = 1


def main():
   x = 0
   y = 0
   facing = NORTH

   with open("./input.txt", 'r') as file:
      data = file.read()

   data = data.replace('\n', '')
   data = data.replace(' ', '')

   moves = data.split(',')

   for move in moves:
      if (move[0] == 'L'):
         facing += ANTI_CLOCKWISE
      elif (move[0] == 'R'):
         facing += CLOCKWISE

      if (facing > WEST):
         facing = NORTH
      elif (facing < NORTH):
         facing = WEST

      steps = re.sub(r'[^0-9]', '', move)
      steps = int(steps)

      if (facing == NORTH):
         y += steps
      elif (facing == EAST):
         x += steps
      elif (facing == SOUTH):
         y -= steps 
      elif (facing == WEST):
         x -= steps

   print(str(x) + " " + str(y))
   print(abs(x) + abs(y))



if __name__ == "__main__":
    main()