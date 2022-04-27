import numpy as np
import matplotlib.pyplot as plt

data_array = np.loadtxt ("data.txt")

fig, ax = plt.subplots (figsize = (16, 10), dpi = 400)

ax.plot ([i/10 for i in range (869)], data_array, marker = 'o', color = 'r', label = "Voltage to time on a graph", markevery = 10)
ax.grid(which = 'major', linestyle = '-', linewidth = 0.5)
ax.grid(which = 'minor', linestyle = '--', linewidth = 0.25)

ax.set_title ("Process of charging and discharging a capacitor in RC-circuit")
plt.xlabel ("Time, sec")
plt.ylabel ("Voltage, volts")

time_charge = data_array.argmax()/10
time_discharge = 869/10 - time_charge

box_style = dict (facecolor = 'wheat', alpha = 1)
plt.text (40, 1, "Charging time = {}\nDischarging time = {}".format (time_charge, time_discharge), {'size':20}, bbox = box_style)

print (time_charge, time_discharge)

ax.set_ylim (0, 3.5)
ax.set_xlim (xmin = 0)

#list = ax.get_xticks()/10

# list = [list[i]/10 for i in list]

plt.minorticks_on()
plt.legend()

fig.savefig ("test.svg")
fig.savefig ("test.png")
plt.show()
