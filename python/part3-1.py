## Using random, datetime, and collections give me a useful code that solve a problem.

# Here's a python code that selects a random date in the current year:

from datetime import date
import random

start_dt = date.today().replace(day=1, month=1).toordinal() # Assigns the first day of the current year and creates a new date object with the same year and month with the day set to 1. 
# toordinal(): converts the date object into its proper proleptic Gregorian ordinal.
end_dt = date.today().toordinal() # Assigns the ordinal converted number to end_dt.
random_day = date.fromordinal(random.randint(start_dt, end_dt)) # random_day var is now assigned a new date object and a randomly generated ordinal number.
print(random_day)



