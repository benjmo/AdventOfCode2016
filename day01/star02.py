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
   visited = {}
   visited[0] = []
   visited[0].append(0)

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
         for i in range(y + 1, y + steps + 1):
            # x must be visited here
            if (i in visited[x]):
               print("Visited twice: " + str(x) + " " + str(i))
            else:
               visited[x].append(i)
         y += steps
      elif (facing == EAST):
         for i in range(x + 1, x + steps + 1):
            if (i not in visited):
               visited[i] = []
               visited[i].append(y)
            elif (y in visited[i]):
               print("Visited twice: " + str(i) + " " + str(y))
            else:
               visited[i].append(y)
         x += steps
      elif (facing == SOUTH):
         for i in range(y - 1, y - steps - 1, -1):
            # x must be visited here
            if (i in visited[x]):
               print("Visited twice: " + str(x) + " " + str(i))
            else:
               visited[x].append(i)
         y -= steps 
      elif (facing == WEST):
         for i in range(x - 1, x - steps - 1, -1):
            if (i not in visited):
               visited[i] = []
               visited[i].append(y)
            elif (y in visited[i]):
               print("Visited twice: " + str(i) + " " + str(y))
            else:
               visited[i].append(y)         
         x -= steps

   print(str(x) + " " + str(y))
   print(abs(x) + abs(y))



if __name__ == "__main__":
    main()