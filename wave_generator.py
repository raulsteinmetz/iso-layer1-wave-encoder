from matplotlib import pyplot as plt

def reverse_signal(signal):
    if signal == 1:
        return 0
    if signal == 0:
        return 1

def nrzi_encode(data):
    encoded_array = []
    signal = 0
    for bit in data:
        if bit == 0:
            encoded_array.append(signal)   # no change in signal for bit 0
        else:
            signal = reverse_signal(signal)
            encoded_array.append(signal)
    return encoded_array


def nrzl_encode(data):
    return data

def alternate_signal(signal):
    if signal == 1:
        return -1
    if signal == -1:
        return 1

def ami_encode(data):
    encoded_array = []
    signal = -1
    for bit in data:
        if bit == 0:
            encoded_array.append(0)   # no change in signal for bit 0
        else:
            signal = alternate_signal(signal)
            encoded_array.append(signal)
    return encoded_array

def pseudot_encode(data):
    return data

def manchester_encode(data):
    return data

def diferential_man_encode(data):
    return data


class DataPlotter:
    def plot(self, data_str, encode):
        if not all(c in "01" for c in data_str):
            print("Error: data_str contains non-binary characters")
            return

        # convert string to list of integers
        data = [int(d) for d in data_str]

        print(f"\n\nDATA: {data}")

        if encode == 'NRZ-I':
            data = nrzi_encode(data)
        elif encode == 'NRZ-L':
            data = nrzl_encode(data)
        elif encode == 'AMI':
            data = ami_encode(data)
        elif encode == 'PSEUDOTERNARIO':
            data = pseudot_encode(data)
        elif encode == 'MANCHESTER':
            data = manchester_encode(data)
        elif encode == 'MANCHESTER DIFERENCIAL':
            data = diferential_man_encode(data)                                                                                                                                                    


        data.insert(0, 0) # for ploting pourposes

        print(data)

        # plot data as a simple line chart with step function
        plt.step(range(1, len(data) + 1), data, where='pre')

        # set y-axis ticks and labels
        if (encode == 'AMI' or encode == 'PSEUDOTERNARIO'):
            plt.yticks([-1, 0, 1], ['-1', '0', '1'])
        else:
            plt.yticks([0, 1], ["0", "1"])

        # set x-axis ticks and labels
        plt.xticks(range(1, len(data) + 1))

        # add a grid to the plot
        # plt.grid(axis='y')
        plt.grid(axis='x')

        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()[0], 3)  # set height to 3 inches

        fig_path = './generated_waves/plot.png'
        plt.savefig(fig_path)

        plt.clf()
