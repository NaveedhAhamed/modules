import my_mod

courses= 'English','maths','history','comscience'
index=my_mod.find_index(courses,'maths')
print(index)

import my_mod as mm

courses= 'English','maths','history','comscience'
index=mm.find_index(courses,'maths')
print(index)

from my_mod import find_index
index=mm.find_index(courses,'maths')
print(index)

import sys
print(sys.path)

import random
courses= 'English','maths','history','comscience'
randomcourse=random.choice(courses)
print(randomcourse)

import math
courses= 'English','maths','history','comscience'
rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendar

today=datetime.date.today()
print(today)

print(calendar.isleap(2020))


import os
print(os.getcwd())
print(os.__file__)