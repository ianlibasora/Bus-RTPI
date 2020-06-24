#!/usr/bin/env python3

# https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=2727&format=json

from sys import argv
import requests
import re

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

   web = requests.get(f"https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid={stop}&format=json")
   if web.status_code == 200:
      data = web.json()
      print(data)
   else:
      print(f"Web error occured: code {web.status_code}")

if __name__ == "__main__":
   main()
