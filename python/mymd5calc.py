#!/usr/bin/python

import hashlib

def md5(filepath):

  """
  A simple function wrapping hashlib's functionality for MD5 calculation for
  fileObjects.
  """

  blockSize = 10 * 2**20 # This should be 10MiB.
  hashlibsMd5Calculator = hashlib.md5()
  fileObject = open(filepath)
  while True:
    block = fileObject.read(blockSize)
    if not block:
      break
    hashlibsMd5Calculator.update(block)

  return hashlibsMd5Calculator.digest()

