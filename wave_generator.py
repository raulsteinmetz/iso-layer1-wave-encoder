from matplotlib import pyplot as plt
import numpy as np

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
    signal = 1
    encoded_array = []
    for bit in data:
        if bit == 1:
            encoded_array.append(0)
        else:
            encoded_array.append(signal)
            signal = alternate_signal(signal)
    return encoded_array

def manchester_encode(data):
    encoded_data = []
    for d in data:
        if d == 0:
            encoded_data += [1, 0]
        else:
            encoded_data += [0, 1]
    return encoded_data


def diferential_man_encode(data):
    encoded_data = []
    last_bit = 1
    for bit in data:
        if (bit == 1):
            if (last_bit == 1):
                encoded_data += [1, 0]
                last_bit = 0
            else:
                encoded_data += [0, 1]
                last_bit = 1
        else:
            if (last_bit == 1):
                encoded_data += [0, 1]
            else:
                encoded_data += [1, 0]
    return encoded_data


def mlt3_encode(binary_array):
    mlt3_array = []
    current_level = 0
    
    for i in range(len(binary_array)):
        bit = binary_array[i]
        if bit == 0:
            if i > 0 and binary_array[i-1] == 0:
                mlt3_array.append(0)
                current_level = 0
            else:
                mlt3_array.append(current_level)
        else:
            if current_level == 0:
                mlt3_array.append(1)
                current_level = 1
            elif current_level == 1:
                mlt3_array.append(-1)
                current_level = -1
            else:
                mlt3_array.append(0)
                current_level = 0
    
    return mlt3_array

def rz_encode(data):
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
        elif encode == 'MLT-3':
            data = mlt3_encode(data)
        elif encode == 'RZ':
            data = rz_encode(data)                                                                                                                                             



        data.insert(0, 0) # for ploting pourposes

        # plot data as a simple line chart with step function
        plt.step(range(1, len(data) + 1), data, where='pre', color='red')

        # set y-axis ticks and labels
        if (encode == 'AMI' or encode == 'PSEUDOTERNARIO' or encode == 'MLT-3'):
            plt.yticks([-1, 0, 1], ['-1', '0', '1'])
        else:
            plt.yticks([0, 1], ["0", "1"])

        if encode == 'MANCHESTER' or encode == 'MANCHESTER DIFERENCIAL':
            plt.xticks(np.arange(1, len(data), 2))
        else:
            plt.xticks(range(1, len(data) + 1))

        # add a grid to the plot
        # plt.grid(axis='y')
        plt.grid(axis='x')

        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches()[0], 3)  # set height to 3 inches

        fig_path = './generated_waves/plot.png'
        plt.savefig(fig_path)

        plt.clf()
