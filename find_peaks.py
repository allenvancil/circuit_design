import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# data = np.loadtxt('data/Capacitor.csv', skiprows=1)
# freq = data[:, 0]
# mag = data[:, 1]

dd = pd.read_csv('data/Capacitor.csv')
dd = pd.DataFrame(dd)
dd = dd[::][50:100]
print(dd)

# freq = dd['Freq.']
# mag = dd['V(out)']

# peaks, _ = find_peaks(mag, height=-100, distance=50)

# topN = 5  # number of peaks to label
# sorted_peaks = peaks[np.argsort(mag[peaks])[-topN:]]

# plt.figure(figsize=(6,10))
# plt.plot(freq, mag, label='FFT')
# plt.scatter(freq[sorted_peaks], mag[sorted_peaks], color='red', marker='x', label='peaks')

# # arranging the text labels on plot and at peaks
# for i in sorted_peaks:
#     plt.text(freq[i], mag[i]+3, f"{freq[i]/1e6:.2f} MHz\n{mag[i]:.1f} dB", ha='center', fontsize=8, rotation=45)

# plt.xscale('log')
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnetude (dB)")
# plt.title("FFT plot of 27 MHz")
# plt.legend()
# plt.grid(True, which="both", ls="--")
# plt.tight_layout()
# plt.show()
