#!/usr/bin/python

import os
from mymd5calc import md5 
from shutil import copy
from shutil import copy2 
from shutil import copytree 

#def copy_and_log(source, dest):
  #copy2(sourceContent, destContent) 
  #print "Copied (non-exist): {} to {}" \
        #.format(source, dest) # for testing
  
#TODO Make the method return a tuple with the whole time it consumed
#     and also the time it spent actually copying files. 
#     This way the overhead time and the actual copying time can be
#     displayed at the end.
def move(source, dest, doMd5s):
  """
  A recursive function used to handle a "move" action copying the content from
  the source to the dest directory.
  Checks if the MD5s of two files are different only if doMd5s is True (this
  should be done only for overwrite content and not for accumulate content).
  """

  # TODO Redefining it in every method call! Define it once somewhere.
  # Must add a dot (.) before checking for these extensions at the end.
  rarelyModifiedExtensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', \
                              '.tif', '.tiff', \
                              '.avi', '.mkv', '.3gp', '.mpg', '.mpeg', \
                              '.mov', '.wmv', '.swf', '.flv', \
                              '.mp3', '.mp4', '.m4a', '.wma', '.aac', \
                              '.ogg', '.wav', '.flac', \
                              '.pdf', '.swp')
  maxFileSizeForMd5 = 6 * 2 ** 20 # Six MiB. TODO Smarter! 

  #print "Processing outgoing directory: " + source + " ..."
  sourceContent = os.listdir(source)
  destContent = os.listdir(dest)

  for content in sourceContent:
    sourceContent = os.path.join(source, content)
    destContent = os.path.join(dest, content)
    if os.path.isfile(sourceContent):
      sourceContentSize = os.path.getsize(sourceContent)
      #print "Working on file: {} (size: {}B) (max size: {}B" \
      #      .format(content, sourceContentSize, maxFileSizeForMd5)
      if not os.path.exists(destContent):
        copy2(sourceContent, destContent) 
        print " Copied (non-exist) {} to {}".format(sourceContent, destContent)
      elif content.lower().endswith(rarelyModifiedExtensions):
        print " Skipped (rarely modified file type): {}".format(sourceContent)
        continue
      elif sourceContentSize != os.path.getsize(destContent):
        copy2(sourceContent, destContent) 
        print " Copied (size diff) {} to {}".format(sourceContent, destContent)
      elif doMd5s and sourceContentSize <= maxFileSizeForMd5:
        print " Calculating MD5 hash for file: " + content
        sourceMd5 = md5(sourceContent)
        destMd5 = md5(destContent)
        if sourceMd5 != destMd5:
          copy2(sourceContent, destContent) 
          print " Copied (MD5 diff) {} to {}".format(sourceContent, destContent)

        # If copy() is used instead of copy2(), the real 
        # modification/access times can be seen.
    elif os.path.isdir(sourceContent):
      if not os.path.exists(destContent):
        copytree(sourceContent, destContent)
      else:
        move(sourceContent, destContent, doMd5s)
