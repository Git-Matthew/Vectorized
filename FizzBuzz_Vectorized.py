"""
from datetime import datetime
starttime = datetime.now()
###
print("FIZZ BUZZ:")
for number in range(101):
	if (number % 3 == 0) & (number % 5 == 0):
		print(number)

print("FIZZ:")
for number in range(101):
	if number % 3 == 0:
		print(number)

print("BUZZ:")
for number in range(101):
	if number % 5 == 0:
		print(number)

###
endtime = datetime.now()
print(endtime-starttime)
# 0:00:00.026590
"""
import numpy as np
from datetime import datetime
starttime = datetime.now()
###

number = np.arange(start=1,stop=100)
print("FIZZ BUZZ:", number[((number % 3 == 0) & (number % 5 == 0))])
print("FIZZ:", number[(number % 3 == 0)])
print("BUZZ:", number[(number % 5 == 0)])

###
endtime = datetime.now()
print(endtime-starttime)
# 0:00:00.000985

