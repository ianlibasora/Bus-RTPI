#!/usr/bin/env python3

"""
Dublin Public Transport Script

Dublin Bus, Go Ahead Bus and Luas RTPI script in Python.
Requires the Python requests module for http requests.
Runs in the terminal environment, compatible with both Windows and Linux.
"""

from sys import argv
import requests
from re import findall

def bsdct():
   # User bus favourites dictionary, insert here stop favourites
   dct = {
      "home": "6030", "drimnagh": "2cat7", "nangor": "6243", "mcd": "1981", 
      "dcu": "37", "tcd": "4522", "castello": "2102", "aston": "326"
   }
   return dct

def hlp():
   print("   -----   Dublin RTPI Script   -----   \n")
   print("Dublin public transport RTPI script in Python. Requires the Python requests module for http requests. Runs in the terminal environment, compatible with both Windows and Linux.")
   print("\n# How it works")
   print("- When user calls the 'rtpi.py' command, the user supplies the stop code or name as an argument. If a name is supplied, name is checked against users' favourites dictionary within the script. If nothing found, error is returned.")
   print("- Similar process ocuuers when dualing with luas stops.\n- Note: stop codes are only available for bus stops.")
   print("- Details, refer to README\n")
   print("Example: rtpi.py home\n")
   print("Luas stops:")
   dct = ldct()
   for k in dct.keys():
      print(f"   {k}")
   print("\n Last updated: 29.Jun.2020, Python 3.8.2")
   print(" By Joseph Libasora")

def ldct():
   dct = {
      'tallaght': '1', 'hospital': '2', 'cookstown': '3', 'belgard': '4', 'kingswood': '5',
      'red-cow': '6', 'kylemore': '7', 'bluebell': '8', 'blackhorse': '9', 'drimnagh': '10',
      'goldenbridge': '11', 'suir-road': '12', 'rialto': '13', 'fatima': '14', "james": "15",
      'heuston': '16', 'museum': '17', 'smithfield': '18', 'four-courts': '19', 'jervis': '20',
      'abbey-street': '21', 'busaras': '22', 'connolly': '23', "st-stephens-green": '24', 'harcourt': '25',
      'charlemont': '26', 'ranelagh': '27', 'beechwood': '28', 'cowper': '29', 'milltown': '30',
      'windy-arbour': '31', 'dundrum': '32', 'balally': '33', 'kilmacud': '34', 'stillorgan': '35',
      'sandyford': '36', 'central-park': '37', 'glencairn': '38', 'the-gallops': '39', 'leopardstown-valley': '40',
      'ballyogan-wood': '42', 'racecourse': '43', 'carrickmines': '44', 'brennanstown': '45', 'laughanstown': '46',
      'cherrywood': '47', 'brides-glen': '48', 'fettercairn': '49', 'cheeverstown': '50', 'citywest-campus': '51',
      'fortunestown': '52', 'saggart': '53', "georges-dock": '54', 'mayor-square-nci': '55', 'spencer-dock': '56',
      'the-point': '57', 'depot': '58', "broombridge": "71", "cabra": "70", "phibsborough": "69",
      "grangegorman": "68", "broadstone": "67", "dominick": "66", "parnell": "65", "oconnell-upper": "64",
      "oconnell-gpo": "63", "marlborough": "62", "westmoreland": "61", "trinity": "60", "dawson": "59"
   }
   return dct

def bus(stop):
   # Data from SmartDublin Dublinked and National Transport Authority, README for details
   web = requests.get(f"https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid={stop}&format=json")
   if web.status_code == 200:
      data = web.json()
      results = data["results"]
      if len(results) != 0:
         for x in results:
            print(" ------------------------------ ")
            print(f"{x['route']}, {x['destination']}, {'Dublin Bus' if x['operator'] == 'bac' else 'Go Ahead'}")
            print(f"Due: {x['duetime']} mins\n" if x['duetime'] != "Due" else f"Due: Now\n")
            print(f"Arrival time: {x['arrivaldatetime'][-8:]}")
            print(f"Scheduled arrival: {x['scheduledarrivaldatetime'][-8:]}")
            print("Additional information: N/A" if x['additionalinformation'] == "" else f"Additional information: {x['additionalinformation']}")
            print(" ------------------------------ \n")
      else:
         print(f"Bus API error: code {data['errorcode']}, {data['errormessage']}")
   else:
      print(f"Web error: code {web.status_code}")

def luas(stop):
   # Luas data from Trnansport Infrastructure Ireland, README for details
   web = requests.get(f"http://luasforecasts.rpa.ie/analysis/view.aspx?id={stop}")
   if web.status_code == 200:
      data = web.text
      out = findall(r"<td>.*", data)
      results = [x.strip().strip("<td>").strip("</") for x in out]
      if len(results) != 0:
         i = 3
         while i < len(results):
            bound, dest, time, avls = results[i - 3], results[i - 2], results[i - 1].split(":"), results[i].split(":")
            time, avls = int(time[1]), int(avls[1])

            print(" ------------------------------ ")
            print(f"{bound}: {dest}")
            print(f"Scheduled arrival: {time} mins" if 0 < time else "Scheduled arrival: Now")
            print(f"Estimated arrival: {avls} mins" if 0 < avls else "Estimated arrival: Now")
            print(" ------------------------------ \n")
            i += 13
      else:
         print("No Luas results found")
   else:
      print(f"Web error: code {web.status_code}")

def main():
   arg = argv[1:]
   bus_dct, luas_dct = bsdct(), ldct()
   if len(arg) == 0:
      # Default stop id when no code is provided
      stop = "6030"
      bus(stop)
   elif arg[0] == "-help" or arg[0] == "--help":
      hlp()
   elif arg[0].lower() in bus_dct:
      stop = bus_dct[arg[0].lower()]
      bus(stop)
   elif arg[0].lower() in luas_dct:
      stop = luas_dct[arg[0].lower()]
      luas(stop)
   else:
      stop = arg[0].lower()
      bus(stop)

if __name__ == "__main__":
   main()
