import numpy as np

from scipy.constants import physical_constants

def make_record(k,v):
    """
    return the record for this cosntant from the key and value of its entry in the physical_constants
    dictionary
    """

    name = k
    val, units, abs_unc = v
    rel_unc = abs_unc/ abs(val)*1.e6
    return name, val,units, abs_unc, rel_unc

dtype= [("name", "S50"),("val", "f8"),("units","S20"),
        ("abs_unc", "f8"), ("rel_unc", "f8")]
constants = np.array([make_record(k,v) for k , v in physical_constants.items()],
                     dtype = dtype)

constants.sort(order ="rel_unc")

for rec in constants[-10:]:
    print("{:.0f} ppm:{:s}={:g}{:s}".format(rec["rel_unc"], rec["name"].decode(), rec["val"],
          rec["units"].decode()))
