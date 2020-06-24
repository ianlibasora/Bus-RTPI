# Dublin Bus RTPI Script

Dublin bus RTPI script in Python. Required the Python requests module for http requests. Runs in the terminal environment, compatible with both Windows and Linux. Uses external "stops.txt" file to store the users stops. Can still be run without the "stops.txt" file.

## How it works
- When run, user provides bus stop number as an argument. If a "stops.txt" file exists, it will check the file as a dictionary against the provided arguement. Through this, keywords can be used as keys for stop numbers.
- If there is no "stops.txt" file, the user can only provide stop numbers to check bus times

## Attribution
- API and bus data from [SmartDublin Dublinked](https://data.smartdublin.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail) under Creative Commons Attribution [(CC-BY)](http://opendefinition.org/licenses/cc-by/)

-----------------------

Last updated: 24.Jun.2020, Python 3.8.2

By Joseph Libasora
