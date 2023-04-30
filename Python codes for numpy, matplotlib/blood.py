import numpy as np

fname = "blood.txt"
dtype = np.dtype([("gender", "|S1"), ("bps", "f8"), ("bpd", "f8")])

def parse_bp(s):
    try:
        return float(s)
    except ValueError:
        return -99

def reformat_lines(fi):
    for line in fi:
        print(type(line))
        line = line.replace("/", " ")
        yield line

with open(fname) as fi:
    gender, bps, bpd = np.loadtxt(reformat_lines(fi), dtype, skiprows = 9,
                                  usecols= (1,7,8), converters={7:parse_bp, 8:parse_bp},
                                  unpack = True)

print(gender, bps, bpd)
