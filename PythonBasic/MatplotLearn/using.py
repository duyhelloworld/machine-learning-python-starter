# import matplotlib
# print(matplotlib.__doc__)

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 10])
y = np.array([0, 10])

# Draw

# plt.plot(x, y)
# Draw from x1 -> x2 +  y1 -> y2
# plt.plot([1, 3], [8, -10])
# plt.plot(x, y, marker="o") # *, ., x, +, D, s, >, y, 1, l, _
# plt.plot(np.array([1, 2, 4, 6, 10]), "D")


# Marker Beautuful

# plt.plot([1, 4, 2, 4, 8, -3, 10], "o:g")
# marker : line : color
# plt.plot([1, 4, 2, 4, 8, -3, 10], "-.")
# plt.plot([1, 4, 2, 4, 8, -3, 10], c = "r", ls = "dotted")
# plt.plot([1, 4, 2, 4, 8, -3, 10], c = "m", ls = "solid", lw = 20)


# Labels

# xx = [1, 23, 45, 7, 3, 10, 23, 67, 54, 98, 80]
# yy = [4, 12, 67, 0, 10, 9, 29, 67, 44, 81, 10]
# plt.plot(xx, c = "r")
# plt.plot(yy, c = "g")
# plt.xlabel("speed(m/s)")
# plt.ylabel("time(s)")
# plt.title("Data Frame of Speed/Time", loc="right")
# plt.grid(visible=True, axis="both", lw = 1.0, c="gray", ls="dashed")

# Sub-Plot
kg = [100, 140, 178, 200, 270, 410]
year = np.linspace(1950, 2010, endpoint=2010, retstep=10)
plt.plot(kg, year)
# plt.subplot(kg)
plt.show()
