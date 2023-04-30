#analyzing data from a stroop effect experiment
import numpy as np

data = np.genfromtxt("color.txt", skip_header = 1,
                      dtype=[("student", "u8"), ("gender", "S1"),
                             ("black", "f8"), ("color" , "f8")],
                      delimiter = ",",
                      missing_values ="X")

nwords = 25
filtered_data = data[np.isfinite(data["black"]) & np.isfinite(data["color"])]
print(filtered_data)
fb = filtered_data["black"][filtered_data["gender"]==b"F"]/nwords
mb = filtered_data["black"][filtered_data["gender"]==b"M"]/nwords
fc = filtered_data["color"][filtered_data["gender"]==b"F"]/nwords
mc = filtered_data["color"][filtered_data["gender"]==b"M"]/nwords

mu_fb , sig_fb = np.mean(fb), np.std(fb)
mu_fc , sig_fc = np.mean(fc), np.std(fc)
mu_mb , sig_mb = np.mean(mb), np.std(mb)
mu_mc , sig_mc = np.mean(mc), np.std(mc)

print("Mean and standard deviation times per word(sec)")
print("gender |  black    |    color    |  difference")
print("    F  | {:4.3f} ({:4.3f}) | {:4.3f}({:4.3f}) | {:4.3f}"
       .format(mu_fb,sig_fb, mu_fc , sig_fc , mu_fc-mu_fb))
print("    M  | {:4.3f}({:4.3f})  | {:4.3f}({:4.3f})  | {:4.3f}"
       .format(mu_mb , sig_mb , mu_mc, sig_mc,  mu_mc-mu_mb))
