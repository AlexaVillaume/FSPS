FSPS Files
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

Doing this returns class instances of whatever file you're reading in. It's important to note that what is returned from ```readcmd```, ```readmags```, and
```readspec``` are distinct objects that have slightly different behaviors. However, all the file classes take in the attributes given in the
headers of the FSPS outfiles and organizes the data such that you can select based on those attributes.

## Examples

### CMD Files
```python
test = FSPSFiles.readcmd(<fname.cmd>)
smc_agb_84 =[]
for model in test:
    if model['phase'] != 6.0:
        if model['age'] == 8.7:
            smc_agb_84.append(model)
```

So as you can see you see you can select on any of the attributes given in the .cmd header. In this case I'm making a phase selection and the
selecting based on age. The ```smc_agb_84``` array now contains the magnitudes for all the filters that FSPS supports. Note that at the end of this
for-loop the file is closed. If you want to do any more selections on it you have to reopen it. If I want to select a certain
filter I can do the follow, 

```python
smc_nod_84_twom_j = map(lambda source: source['twomass_j'] + smc_distmod, smc_nod_84)
```

Which gives me the J-band photometry for all the stars in a population of log age = 8.4 for every phase except 6.

### Mags Files
```python
test = FSPSFiles.readmags(<fname.mags>)

mphot_980 = []
for model in test:
    if model['log(age)'] == 9.80:
        mphot_980.append(ab_fnu(model['irac1']))
        mphot_980.append(ab_fnu(model['irac2']))
        mphot_980.append(ab_fnu(model['irac3']))
        mphot_980.append(ab_fnu(model['irac4']))
        mphot_980.append(ab_fnu(model['mips_24']))
```

Here I'm selecting based on age and filling an array with integrated photometry. Note, the file is closed once the for-loop is over.

### Spec Files

The behavior of ```readspec``` is a bit different but equally straightforward. 

```python
test = FSPSFiles.readspec(<fname.spec>)

for model in test:
    if model.logage == 9.80:
        agb_spec_980 = np.asarray(map(lambda value: value, model.flux))
        swave = np.asarray(model.wave)
    if model.logage == 9.85:
        agb_spec_985 = np.asarray(map(lambda value: value, model.flux))
        swave = np.asarray(model.wave)
```

After I open the file I can loop through the different spectra the file contains and here I'm making selections based on age. Once again, once you
leave the for-loop the file is closed.


