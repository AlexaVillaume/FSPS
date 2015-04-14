FSPS
====


### What this is

FSPSFiles contains classes easily reading and working with FSPS output files (.mags, .spec, and .cmd)

### How to the routines 

Put this directory in your Python path and then in any program you can import the program,

```python
import FSPSFiles
```

This will allow you to read in the outfiles. For example,

```python
test = FSPSFiles.readcmd(<fname.cmd>)
test = FSPSFiles.readmags(<fname.mags>)
test = FSPSFiles.readspec(<fname.spec>)
```

Doing this returns class instances of whatever file you're reading in. It's important to note that what is returned from ```python readcmd```, ```python readmags```, and
```python readspec```
