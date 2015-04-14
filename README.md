FSPS
====


### What this is

FSPSFiles contains classes easily reading and working with FSPS output files (.mags, .spec, and .cmd)

### How to the routines 

Put this directory in your Python path and then in any program you can import the program,

'''python
import FSPSFiles
'''

This will allow you to read in the outfiles. For example,

'''python
test = FSPSFiles.readcmd(<fname.cmd>)
'''
