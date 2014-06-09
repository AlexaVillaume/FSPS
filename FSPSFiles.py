import os

'''
Read an FSPS spec file
'''
class specmodel(object):
    def __init__(self, attr, wave, flux):
        self.agegyr = round(10**attr[0] / 1e9, 3)
        self.mass   = attr[1]
        self.lbol   = attr[2]
        self.sfr    = attr[3]
        self.wave   = wave
        self.flux   = flux

class readspec(object):
    def __init__(self, fname):
        self.data = open(fname, "r")
        # Burn header
        while True:
            line = self.data.readline()
            if line[0] != '#':
                break
        cols = line.split()
        self.tstep = float(cols[0])
        self.sdim = float(cols[1])

        # Get wavelength
        line = self.data.readline()
        cols = line.split()
        self.wave = map(lambda col: float(col)*1e-4, cols)

    def next(self):
        line = self.data.readline()
        if line == "":
            self.data.close()
            raise StopIteration()

        cols = line.split()
        attr = map(lambda col: float(col), cols)

        line = self.data.readline()
        cols = line.split()
        flux = map(lambda col: float(col), cols)

        return specmodel(attr, self.wave, flux)

    def __iter__(self):
        return self

'''
For FSPS .mags and .cmd files
'''
class readmags:
    def __init__(self, fname):
        self.data = open(fname, 'r')
        # Read header to find the columns in the file
        while True:
            line = self.data.readline()
            line = line.lstrip()
            if line[0] == '#':
                header = line.replace('#', '')
                header = header.replace('mags', '')
                header =  header.split()
                break
        self.header = header

    def next(self):
        line = self.data.readline()
        if line == "":
            self.data.close()
            raise StopIteration()

        # Read in and assign the  attributes of the models
        cols = line.split()
        for i, name in enumerate(self.header):
            self.__dict__[name] = float(cols[i])

        # Update the attributes with filter names and values
        with open('/Users/alexawork/FSPS_python/filters.txt', 'r') as names:
            for i, _filter in enumerate(names):
                _filter = _filter.rstrip()
                self.__dict__.update({_filter:float(cols[i + len(self.header)])})

        return self.__dict__.copy()

    def __iter__(self):
        return self

