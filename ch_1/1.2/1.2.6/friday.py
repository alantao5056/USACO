"""
ID: alantao2
LANG: PYTHON3
PROG: friday
"""

fridayInput = open('friday.in', 'r')
fridayOutput = open('friday.out', 'w')

def getMonthDays(year, month):
  months = {
    "1": 31,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
  }

  if(month != 2):
    return months[str(month)]

  if(year % 4 == 0):
    if(year % 100 == 0):
      if(year % 400 == 0):
        return 29
      else:
        return 28
    else:
      return 29
  else:
    return 28
  
days = {
  "1": 0,
  "2": 0,
  "3": 0,
  "4": 0,
  "5": 0,
  "6": 0,
  "0": 0
}

yearsToGo = int(fridayInput.readline())
daysOfPreviousMonths = 0

for year in range(1900, 1900 + yearsToGo):
  for month in range(1, 13):      
    totalDays = daysOfPreviousMonths + 13
    days[str(totalDays % 7)] += 1
    daysOfPreviousMonths += getMonthDays(year, month)

fridayOutput.write(f'{days["6"]} {days["0"]} {days["1"]} {days["2"]} {days["3"]} {days["4"]} {days["5"]}\n')