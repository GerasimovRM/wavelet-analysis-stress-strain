import sys

import numpy as np
from ssqueezepy import cwt
from ssqueezepy.visuals import plot, imshow
import os

import numpy
import numpy as np
import pywt
import pandas as pd
import csv
import matplotlib.pyplot as plt
import scaleogram as scg
from matplotlib.figure import Figure


WORK_PATH = os.path.abspath(os.getcwd())


class ExperimentalDataLoader:
    def __init__(self, file_name: str, *args, **kwargs):
        self.csv_abs_path = os.path.join(WORK_PATH, "data", file_name)
        self.csv_data = pd.read_csv(self.csv_abs_path, *args, **kwargs)

    def __str__(self):
        return self.csv_data


def dwt_plot(stress):
    c_a1, c_d1 = pywt.dwt(stress, "db2")
    c_a2, c_d2 = pywt.dwt(c_a1, "db2")
    c_a3, c_d3 = pywt.dwt(c_a2, "db2")
    c_a4, c_d4 = pywt.dwt(c_a3, "db2")
    c_a5, c_d5 = pywt.dwt(c_a4, "db2")

    titles = ["Original Stress-Strain",
              "Approximation coefficients 1", "Detail coefficients 1",
              "Approximation coefficients 2", "Detail coefficients 2",
              "Approximation coefficients 3", "Detail coefficients 3",
              "Approximation coefficients 4", "Detail coefficients 4",
              "Approximation coefficients 5", "Detail coefficients 5"
              ]
    params = {'axes.labelsize': 20,
              'axes.titlesize': 20}
    plt.rcParams.update(params)
    fig1: Figure = plt.figure(figsize=(9, 7))
    fig1.subplots_adjust(wspace=10)
    """
    ax = fig1.add_subplot(1, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=20)
    """
    ax = fig1.add_subplot(1, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[0])
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(15)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(15)
    # 1 -------------------------------------------
    fig2 = plt.figure(figsize=(9, 7))
    fig2.subplots_adjust(hspace=1)
    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)", fontsize=20)
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[0], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a1)
    ax.set_xlabel("Time (scaling) (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[1], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d1, linefmt=':')

    ax.set_title(titles[2], fontsize=10)
    # 2 -------------------------------------------
    fig2 = plt.figure(figsize=(9, 7))
    fig2.subplots_adjust(hspace=1)
    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[0], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a2)
    ax.set_xlabel("Time (scaling) (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[3], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d2, linefmt=':')

    ax.set_title(titles[4], fontsize=10)
    # 3 -------------------------------------------
    fig2 = plt.figure(figsize=(9, 7))
    fig2.subplots_adjust(hspace=1)
    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[0], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a3)
    ax.set_xlabel("Time (scaling) (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[5], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d3, linefmt=':')

    ax.set_title(titles[6], fontsize=10)
    # 4 -------------------------------------------
    fig2 = plt.figure(figsize=(9, 7))
    fig2.subplots_adjust(hspace=1)
    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[0], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a4)
    ax.set_xlabel("Time (scaling) (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[7], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d4, linefmt=':')

    ax.set_title(titles[8], fontsize=10)
    # 5 -------------------------------------------
    fig2 = plt.figure(figsize=(9, 7))
    fig2.subplots_adjust(hspace=1)
    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[9], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a5)
    ax.set_xlabel("Time (scaling) (s)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title(titles[10], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d5, linefmt=':')

    ax.set_title(titles[2], fontsize=10)



    plt.show()


def cwt_plot(stress):
    scales = np.arange(1, len(stress))
    print(scales)
    wavelet = "cmor1-3"
    scg.set_default_wavelet(wavelet)
    # and the scaleogram
    ax1 = scg.cws(stress, scales=scales, coi=False)
    plt.show()


data = ExperimentalDataLoader("StressStrainTension.csv", decimal=',', delimiter=";", encoding="cp1251")
while True:
    print("Select first column:")
    for i, col in enumerate(data.csv_data.columns):
        print(i, col)
    first_col_index = int(input())
    try:
        first_col = data.csv_data.columns[first_col_index]
    except IndexError:
        continue
    break

while True:
    print("Select second column:")
    for i, col in enumerate(data.csv_data.columns):
        print(i, col)
    second_col_index = int(input())
    try:
        second_col = data.csv_data.columns[second_col_index]
    except IndexError:
        continue
    break

time = data.csv_data[first_col].values
stress = data.csv_data[second_col].values
plot(stress, title="S(t)")
Wx, scales = cwt(stress, "hhhat")
imshow(Wx, yticks=scales, abs=1,
       title="abs(CWT)",
       ylabel="scales", xlabel="samples")
sys.exit(0)