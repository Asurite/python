# READING SECOND CODE
import os # Lets you interact with the OS Python is currently running on.
import re # Lets you check if a set of strings matches it.
import datetime # Supplies classes for manipulating dates and times.
def function_two(directory):

 date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}') #Format the date into a specific format.
 for filename in os.listdir(directory): # Search for the date pattern in the file.
  if os.path.isfile(os.path.join(directory, filename)):
   match = date_pattern.search(filename) # Extracts the date string and convert it to a datetime.
 if match:
   date_str = match.group() # Get the year and month from the date and create a new directory with it.
 file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
 year = str(file_date.year)
 month = file_date.strftime('%B')
 new_directory = os.path.join(directory, year, month) # Creates a new directory.
 os.makedirs(new_directory, exist_ok=True) # Moves the file into the new directory.
 old_path = os.path.join(directory, filename) # Find the files with the pattern that we alrady set.
 new_path = os.path.join(new_directory, filename) # Creates a new directory from the year and month of the date.
 os.rename(old_path, new_path) # Moves the files to the new directory.