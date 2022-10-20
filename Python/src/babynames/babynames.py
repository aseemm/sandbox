#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def get_year(filename):
  match = re.search(r'\d+', filename)
  if match:
    year = match.group()

  return year

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  return_list = []
  names_dict = {}
  
  # extract year
  year = get_year(filename)
  return_list.append(year)

  # extract name, count information
  f = open(filename, 'r')
  text = f.read()
  f.close()

  match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  for item in match:
    names_dict[item[1]] = item[0]
    names_dict[item[2]] = item[0]    

  for k, v in names_dict.items():
    return_list.append(k + ' ' + v)

  return sorted(return_list)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names_list = extract_names(filename)
    if summary:
      year = get_year(filename)
      summary_filename = 'baby' + year + '_summary.txt'
      print("Writing summary to ", summary_filename, '...')
      
      f = open(summary_filename, 'w')
      f.write(str(names_list))
      f.close()

      # read file check
      g = open(summary_filename, 'r')
      text = g.read();
      print(text)
      g.close()      
    else:
      print(names_list)
      
if __name__ == '__main__':
  main()
