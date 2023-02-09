import numpy as np
import matplotlib.pyplot as plt




def main():
    print('running code')

    # open the sample file used
    file = open('qwmp1_s11.D1')

    #Have python find BEGIN and END of the file. save the real and imaginary parts of the data
    for line in file:
        if 'BEGIN' in line:
            real = []
            imag = []
        elif 'END' in line:
            break
        else:
            pass

        print(line)

if __name__ == "__main__":
     main()