#!/usr/bin/env python3

from sys import argv
import requests

def mkdct():
   try:
      with open("stops.txt", "r") as fd:
         full = fd.readlines()
         dct = {}
         for line in full:
            k, v = line.strip().split(",")
            dct[k], dct[v] = v, v
   except FileNotFoundError:
      print(" --- Error. No stops.txt file found --- ")
      return {}
   return dct

def main():
   arg = argv[1:]
   dct = mkdct()
   if len(arg) == 0:
      stop = "6030"
   elif arg[0] in dct:
      stop = dct[arg[0]]
   else:
      stop = arg[0]

   print(stop)

if __name__ == "__main__":
   main()
