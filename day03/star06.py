#!/usr/bin/python3

def main():
   with open('./input.txt', 'r') as file:
      lines = file.readlines()

   triCount = 0
   for i in range(0, len(lines), 3):
      l0 = list(map(int, lines[i].split()))
      l1 = list(map(int, lines[i + 1].split()))
      l2 = list(map(int, lines[i + 2].split()))

      for j in range(0, 3):
         if (l0[j] + l1[j] > l2[j] and
             l0[j] + l2[j] > l1[j] and
             l1[j] + l2[j] > l0[j]):
            triCount += 1

   print(triCount)

if __name__ == '__main__':
   main()