import argparse
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--A1', type=float, default=1.0,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
A1 = """)
    parser.add_argument('--A2', type=float, default=0.6,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
A2 = """)
    parser.add_argument('--A3', type=float, default=0.4,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
A3 = """)
    parser.add_argument('--w1', type=float, default=2.0,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
w1 = """)
    parser.add_argument('--w2', type=float, default=8.0,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
w2 = """)
    parser.add_argument('--w3', type=float, default=16.0,
                        help="""A1sin(2*w1*pi*t)+A2cos(2*w2*pi*t)+A3exp(2*w3*pi*t) 
w3 = """)
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def naive_DFT(x):
    #Jumlah sampel yang diambil
    N = 400
    X = np.zeros(x.shape,dtype=np.complex128)
    start = time.time() #menghitung waktu run
    for m in range(0,N):
        for n in range(0,N):
            X[m] += x[n]*np.exp(-np.pi*2j*m*n/N)
    end = time.time()
    a = end-start 
    print("running time: ", str(a), "sec")
    return X

def calc(args):
    #interval waktu
    t = np.arange(0.0, 1.0, 0.0025)
    y = args.A1*np.sin(2*args.w1*np.pi*t)+args.A2*np.cos(2*args.w2*np.pi*t)+args.A3*np.cos(2*args.w3*np.pi*t)
    yf = naive_DFT(y)
    plt.figure(figsize=(10,15))
    #plot grafik data mentah
    plt.subplot(2, 1, 1)
    plt.plot(t, y, '-')
    #untuk memberikan judul pada grafik data mentah
    plt.title('Data Mentah')
    #untuk memberikan subjudul pada sumbu-y
    plt.ylabel('Amp')

    #plot grafik Discrete Fourier Transform
    plt.subplot(2, 1, 2)
    plt.plot(np.arange(400), abs(yf),'r')
    #untuk memberikan judul pada grafik data DFT
    plt.title('Power Spectral')
    #untuk memberikan subjudul pada masing-masing sumbu
    plt.xlabel('frek (Hz)')
    plt.ylabel('Spectral')
    plt.show()

if __name__ == '__main__':
    main()