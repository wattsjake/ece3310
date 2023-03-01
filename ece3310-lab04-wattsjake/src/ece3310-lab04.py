import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage:")
    print("    $ python %s <data>" %
          sys.argv[0])
    sys.exit(0)
filename = sys.argv[1]

def read_data(filename):
    #reads data from file converts to numpy 
    real_str = pd.read_csv(filename, skiprows=9,skipfooter=2, sep=',', usecols=[0], engine='python')
    img_str = pd.read_csv(filename, skiprows=9,skipfooter=2, sep=',', usecols=[1], engine='python')
    real = np.array(real_str,dtype=float)
    img = np.array(img_str,dtype=float)
    #convert to 1d array
    real = real.flatten()
    img = img.flatten()
    return real, img

def s11_computation(real, img):
    s11 = np.sqrt(np.power(real,2) + np.power(img,2))
    return s11

def rl_computation(s11):
    db = 20*np.log10(s11)
    return db

def vswr_computation(s11):
    vswr = (1+s11)/(1-s11)
    return vswr

def fig1_data():
    # number of samples
    ns = 1000
    lmbda = 1
    L = 1 * lmbda
    gamma = np.array([(1/5)])
    points = np.linspace(0, L, ns)
    Z_l = 75
    Z_0 = 50
    Z_in = Z_0*((Z_l + Z_0*1j*np.tan(2*np.pi*points))/(Z_0 + Z_l*1j*np.tan(2*np.pi*points)))
    plt.grid(True)
    #title name needs to have the symbol for ohm in it
    plt.title('R = 50 ohm-Term line, Z_0 = 50 ohm')
    plt.xlabel('Lambda ( )')
    plt.ylabel('Z_in(ohm))')
    #x axis go in steps of .1
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.ylim(-10, 110)
    #y axis go in steps of 10
    plt.yticks(np.arange(0, 110, step=10))
    plt.plot(points, Z_in)
    #save figure to docs folder outside of src
    plt.savefig("fig1.png")
    plt.show()

def fig2_plt(db, gamma, vswr):
    #create title
    plt.title('')
    #turn on legend for each line
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('S11 (dB)')
    #y axis go in steps of 10
    plt.ylim(-25,0)
    plt.grid()
    plt.plot(np.linspace(2,3,200),db)
    plt.xlim(2,3)
    #y axis go in steps of .5
    plt.yticks(np.arange(-25, 0, step=2.5))
    #x axis go in steps of .1
    plt.xticks(np.arange(2, 3.1, step=0.1))
    #add a horizontal line at -10 dB dotted line
    plt.axhline(y=-10, color='black', linestyle='--', linewidth=1)
    #find the idx position where the plot crosses -10 dB
    idx = np.argwhere(np.diff(np.sign(db + 10))).flatten()
    #add a vertical line where the plot crosses -10 dB
    plt.axvline(x=2.174, color='black', linestyle='--', linewidth=1)
    plt.axvline(x=2.915, color='black', linestyle='--', linewidth=1)
    #add gamma and vswr in a box
    plt.text(2.2, -15, 'Gamma = ' + str(gamma), bbox=dict(facecolor='white', alpha=0.5))
    plt.text(2.2, -17, 'VSWR = ' + str(vswr), bbox=dict(facecolor='white', alpha=0.5))
    plt.savefig("fig2.png")
    plt.show()

def find_gamma(db):    
    return np.power(10,np.amin(db)/20)

def find_vswr(gamma):
    return (1+gamma)/(1-gamma)
    
def main():
    print('running plotting program')
    #fig1_data()
    real, img = read_data(filename)
    s11 = s11_computation(real, img)
    db = rl_computation(s11)
    gamma_value = find_gamma(db)
    vswr = find_vswr(gamma_value)
    fig2_plt(db,gamma_value,vswr)

if __name__ == "__main__":
    main()