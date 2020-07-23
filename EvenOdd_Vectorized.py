"""
from datetime import datetime
starttime = datetime.now()
###
print("Even Numbers:")
for number in range(101):
	if number % 2 == 0:
		print(number)

print("Odd Numbers:")
for number in range(101):
	if number % 2 != 0:
		print(number)

###
endtime = datetime.now()
print(endtime-starttime)
# 0:00:00.022590
"""
import numpy as np
from datetime import datetime
starttime = datetime.now()
###

number = np.arange(start=1,stop=100)
print("Even Numbers:", number[(number % 2 == 0)])
print("Odd Numbers:", number[(number % 2 != 0)])

###
endtime = datetime.now()
print(endtime-starttime)
# 0:00:00.1203

