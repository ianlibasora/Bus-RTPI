# Dublin Public Transport RTPI Library & Script

Dublin Bus, Go Ahead Bus and Luas RTPI library and script in Python. Requires the Python requests module for http requests. Runs in the terminal environment, compatible with both Windows and Linux.

## How it works
- When user calls the "rtpi.py" command, the user supplies the stop code or name as an argument. If a name is supplied, the name would be checked against the users' favourites dictionary within the script. If nothing is found, an error is returned.
- A similar process ocuuers when dealing with luas stops.
- Note: stop codes are only available for bus stops.

## Attribution
- Bus [API][1] and data from [SmartDublin Dublinked][1], [data.gov.ie][2], [National Transport Authority][3], Creative Commons Attribution 4.0 [(CC BY 4.0)][4]
- Luas [stop data][6] from [Transport Infrastructure Ireland][5], Creative Commons Attribution 4.0 [(CC BY 4.0)][4]
- Luas [API][7] from [Transport Infrastructure Ireland][5], [data.gov.ie][8], Creative Commons Attribution 4.0 [(CC BY 4.0)][4]

-----------------------------------

Last updated: 12.Jul.2020, Python 3.8.2

By Joseph Libasora

[1]: <https://data.smartdublin.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail>
[2]: <https://data.gov.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail>
[3]: <https://data.gov.ie/organization/national-transport-authority>
[4]: <https://creativecommons.org/licenses/by/4.0/>
[5]: <https://data.tii.ie/#luas>
[6]: <https://data.tii.ie/Datasets/Luas/StopLocations/index.html>
[7]: <http://luasforecasts.rpa.ie/analysis/view.aspx>
[8]: <https://data.gov.ie/dataset/luas-forecasting-api>
