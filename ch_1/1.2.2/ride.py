"""
ID: alantao2
LANG: PYTHON3
PROG: ride
"""

def StrToNum (string):
    num = 1
    for letter in string:
        num = num * (ord(letter) - ord('A') + 1) % 47
    return num

rideInput = open('ride.in', 'r')
rideOutput = open('ride.out', 'w')

ride = rideInput.readline().strip()
comet = rideInput.readline().strip()

if(StrToNum(ride) % 47 == StrToNum(comet) % 47):
    rideOutput.write('GO\n')
    rideOutput.close()
else:
    rideOutput.write('STAY\n')
    rideOutput.close()