import matplotlib.pyplot as plt

# sample string of zeros and ones
data_str = "1101010010110010"

# convert string to list of integers
data = [int(d) for d in data_str]

# plot data as a simple line chart with step function
plt.step(range(1, len(data) + 1), data, where='pre')

# set y-axis ticks and labels
plt.yticks([0, 1], ["0", "1"])

# set x-axis ticks and labels
plt.xticks(range(1, len(data) + 1))

# add a grid to the plot
plt.grid(axis='y')
plt.grid(axis='x')

# save plot to file
plt.savefig('./generated_waves/plot.png')

# display plot
plt.show()