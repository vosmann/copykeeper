#!/usr/bin/python

import sys
import os
import time
from copykeeperrecursives import move

#print "Name of the operating system dependent \"os\" module imported: " \
#  + os.name
#print "The same, but with finer granularity: " + sys.platform
#print "System-dependent version information:"
#for element in os.uname():
#  print element

beginTime = time.time()

# Parameter handling.

if len(sys.argv) != 6: # Need four directories (two remote, two local)
  print "Wrong number of parameters."
  sys.exit()
# A few constants.
putCmd = "put" 
getCmd = "get"
cmd = sys.argv[1]

if (cmd != putCmd) and (cmd != getCmd):
  print "Wrong command. Expected: \"put\" or \"get\"." 
  sys.exit()

print "...CopyKeeper..."
print "Command (from local perspective): " + cmd

# Have frendlier variable names for important paths.
# "Local" indicates the computer's internal hard drive and "remote" the 
# external storage unit (external hard drive or similar).
overwriteLocal = sys.argv[2]
accumulateLocal = sys.argv[3]
overwriteRemote = sys.argv[4]
accumulateRemote = sys.argv[5]

print "Local directories: "
print " 1. " + overwriteLocal
print " 2. " + accumulateLocal
print "Remote directories: "
print " 3. " + overwriteLocal
print " 4. " + accumulateLocal

dirCounter = 1
for path in sys.argv[2:]:
  if not os.path.exists(path):
    print "The " + str(dirCounter) + ". specified directory doesn't exist."
    sys.exit()
  dirCounter += 1

  
if cmd == putCmd:

  # First store stuff from the "overwrite" directory.
  doMd5s = True
  move(overwriteLocal, overwriteRemote, doMd5s)

  # Then store stuff from the "accumulate" directory.
  # Do the same stuff as with "overwrite" (for the first iteration; maybe add
  # a system that makes sure no multiple copies are put on the external HDD).
  doMd5s = False
  move(accumulateLocal, accumulateRemote, doMd5s)

elif cmd == getCmd:
  # Don't retrieve anything from the "accumulate" dir,
  # but copy everything from "overwrite".
  doMd5s = True
  move(overwriteRemote, overwriteLocal, doMd5s) 

print "\n"
print "EXECUTION TIME: {0:.3f} minutes.".format((time.time() - beginTime) / 60)
