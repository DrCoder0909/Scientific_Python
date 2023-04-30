import numpy as np
fname = "students.txt"
dtype1 = np.dtype([("gender" , "|S1"), ("height" , "f8")])
a = np.loadtxt(fname, dtype = dtype1 , skiprows = 9 , usecols = (1,3))
print(a)
m = a["gender"] == b'M'
print(m)
print(a["height"][m])
m_av = a["height"][m].mean()
f_av = a["height"][~m].mean()
print("Male Average: {:.2f} m , Female Average: {:2f} m".format(m_av,f_av))


def parse_weight(s):
    try:
        return float(s)
    except ValueError:
        return -99

dtype2 = np.dtype([("gender", "|S1"), ("weight", "f8")])
b = np.loadtxt(fname, dtype = dtype2 , skiprows = 9, usecols=(1,4),
               converters = {4: parse_weight})

mv = b["weight"]>0
m_wav = b["weight"][mv & m].mean()
f_wav = b["weight"][mv & ~m].mean()
print("Male Average: {:.2f} kg, "
       "Female average : {:.2f} kg".format(m_wav, f_wav))

dtype3 = np.dtype([("gender" , "|S1"), ("bps", "f8"), ("bpd", "f8")])

def parse_bp(s):
    try:
        return float(s)
    except ValueError:
        return -99

def reformat_lines(fi):
    for line in fi:
        line = line.replace("/", " ")
        yield line

with open(fname) as fi:
    gender , bps, bpd = np.loadtxt(reformat_lines(fi), dtype3 , skiprows = 9,
                                   usecols = (1,7,8), converters ={7: parse_bp, 8:parse_bp},
                                   unpack = True)

print(bps, bpd)
