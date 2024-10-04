from matplotlib import pyplot as plt

# Input Reading

# When Vce = 0 V
vbe_x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
ib_vce_0_y = [0, 0, 0, 0, 0, 0, 35, 95, 155]

plt.plot(vbe_x, ib_vce_0_y, marker = "o", label = "Vce = 0 V")

# When Vce = 2 V
ib_vce_2_y = [0, 0, 0, 0, 0, 5, 20, 65, 115]

plt.plot(vbe_x, ib_vce_2_y, marker = "o", label = "Vce = 2 V")

plt.xlabel("Base-Emitter Voltage")
plt.ylabel("Base Current")
plt.title("Base-Emitter Voltage v/s Base Current")
plt.legend()
plt.show()