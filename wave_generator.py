from matplotlib import pyplot as plt

class DataPlotter:
    def plot(self, data_str):

        if not all(c in "01" for c in data_str):
            print("Error: data_str contains non-binary characters")
            return

        # convert string to list of integers
        data = [int(d) for d in data_str]
        data.insert(0, 0)

        print(data)

        # plot data as a simple line chart with step function
        plt.step(range(1, len(data) + 1), data, where='pre')

        # set y-axis ticks and labels
        plt.yticks([0, 1], ["0", "1"])

        # set x-axis ticks and labels
        plt.xticks(range(1, len(data) + 1))

        # add a grid to the plot
        plt.grid(axis='y')
        plt.grid(axis='x')

        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()[0], 3)  # set height to 3 inches

        fig_path = './generated_waves/plot.png'
        plt.savefig(fig_path)

        plt.clf()
