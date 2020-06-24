#!/usr/bin/env python3

"""Dublin Bus rtpi script"""

from sys import argv
import requests

def mkdct():
   dct = {}
   try:
      with open("stops.txt", "r") as fd:
         full = fd.readlines()
         for line in full:
            k, v = line.strip().split(",")
            dct[k], dct[v] = v, v
   except FileNotFoundError:
      print(" --- Error. No stops.txt file found --- ")
      # Insert here backup dictionaries if no file found
      dct = {
         "home": "6030", "drimnagh": "2727", "nangor": "6243",
         "kylemore": "1981", "dcu": "37", "tcd": "4522",
         "castello": "2102", "aston": "326"
      }
   return dct

def main():
   arg = argv[1:]
   dct = mkdct()
   if len(arg) == 0:
      # Default stop id when no code is provided
      stop = "6030"
   elif arg[0].lower() in dct:
      stop = dct[arg[0].lower()]
   else:
      stop = arg[0].lower()

   web = requests.get(f"https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid={stop}&format=json")
   if web.status_code == 200:
      data = web.json()
      results = data["results"]
      for x in results:
         print(" ------------------------------ ")
         print(f"{x['route']}, {x['destination']}, {'Dublin Bus' if x['operator'] == 'bac' else 'Go Ahead'}")
         print(f"Due: {x['duetime']} mins\n" if x['duetime'] != "Due" else f"Due: Now\n")
         print(f"Arrival time: {x['arrivaldatetime'][-8:]}")
         print(f"Scheduled arrival: {x['scheduledarrivaldatetime'][-8:]}")
         print("Additional information: N/A" if x['additionalinformation'] == "" else f"Additional information: {x['additionalinformation']}")
         print(" ------------------------------ \n")
   else:
      print(f"Web error occured: code {web.status_code}")

if __name__ == "__main__":
   main()
