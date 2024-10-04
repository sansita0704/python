from matplotlib import pyplot as plt
# 'from matplotlib import pyplot': This imports the pyplot module from matplotlib library.
# pyplot module is a file which provides a lot of functions which we can directly use in our code.
# 'as plt': This gives the pyplot module an alias (shorthand name or alternate name) called plt.
# So that we do not have to write matplotlib.pyplot everytime we use it in our code.
# This makes our code more readable.

# Output Reading

# When Base Current = 50 mA

vce_x = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5]
ic_ib_50_y = [0, 1.5, 3.5, 5.5, 7, 8, 8, 8, 8, 8]

plt.plot(vce_x, ic_ib_50_y, marker = "o", label = "Ib = 50 mA")
# Plots the data on x-y plane
# We use period (.) to access the functions that are written inside module i.e. they belong to module.

# When Base Current = 100 mA
ic_ib_100_y = [0, 1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5, 15, 16.5]

plt.plot(vce_x, ic_ib_100_y, marker = "o", label = "Ib = 100 mA")

plt.xlabel("Base-Emitter Voltage")
# To label x-axis

plt.ylabel("Base Current")
# To label y-axis

plt.title("Base-Emitter Voltage v/s Base Current")
# To add a title to the graph

plt.legend()
# To provide legend to the graph.
# Legend is a small box or label that explains what each line in the graph represents.
# It creates legends using the labels which we provide through the label argument of plt.plot()

plt.show()
# To show the plot