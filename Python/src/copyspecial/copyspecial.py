#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

def run_shell_command(cmd):
  print("About to run cmd:", cmd)
  # return
  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  out = process.stdout.read()
  err = process.stderr.read()    
  returncode = process.wait()
  if returncode:
    raise Exception(returncode, err)
  else:
    return (out, err)
          
# Write functions and modify main() to call them
def get_special_files(dir, todir, tozip):
  print(os.getcwd())
  files = os.listdir(dir)
  zip_cmd = 'zip -f ' + tozip
  for file in files:
    match = re.search(r'__\w+__', file)
    if match:
      print(os.path.abspath(file))

      if todir:
        cmd = 'pwd'
        out, err = run_shell_command(cmd)        
        
        cmd = 'ls -ltr ' + os.getcwd() + '/' + dir
        out, err = run_shell_command(cmd)        
        
        cmd = 'cp ' + os.getcwd() + '/' + dir + '/' + file + ' ' + todir
        out, err = run_shell_command(cmd)

      if tozip:
        zip_cmd = zip_cmd + ' ' + file

  if todir:
    cmd = 'ls -ltr ' + todir
    out, err = run_shell_command(cmd)        
    print(out)
    print(err)

  if tozip:
    out, err = run_shell_command(zip_cmd)            
    print(out)
    print(err)          
    
  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # Call your functions
  get_special_files(args[0], todir, tozip)
  
if __name__ == "__main__":
  main()
