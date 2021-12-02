# time_calc
A simple CLI python application to date and time calculations


### technologies used:
* python
* argparser
* datetime
* datetime utils

### Structure
The project is structured in
* a main file __tcalc.py__ : responsible for parsing arguments and function calls
* a functions file __lib/timecalc.py__ : contains all the functions responsible for calculations

### usage:
1. tcalc -d <date1> [date2]
  
  to calculate the difference between two dates in years, months and days - DATE FORMAT dd/mm/yyyy
  second date optional, if not present date2 = present day (datetime.today())
  
  2. tcalc -t <time1> [time2] 
  
  to calculate the difference between two periods of time - TIME FORMAT hh:mm:ss
  second time optional, if not present time2 = present hour (datetime.now())
  
  3. tcalc --day <date>
  
  show the weekday for the date]
  
### instalation
  1. clone it
  2. chmod +x tcalc.py
  3. run it
 


