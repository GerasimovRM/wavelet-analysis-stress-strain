import os

import numpy as np
import pywt
import pandas as pd
import csv
import matplotlib.pyplot as plt
from multiprocessing import Process
import scaleogram as scg

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
    fig1 = plt.figure(figsize=(12, 12))

    ax = fig1.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=10)

    ax = fig1.add_subplot(3, 1, 2)
    ax.plot(c_a1)
    ax.set_title(titles[1], fontsize=10)

    ax = fig1.add_subplot(3, 1, 3)
    ax.stem(c_d1, linefmt=':')
    ax.set_title(titles[2], fontsize=10)

    fig2 = plt.figure(figsize=(12, 12))

    ax = fig2.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=10)

    ax = fig2.add_subplot(3, 1, 2)
    ax.plot(c_a2)
    ax.set_title(titles[3], fontsize=10)

    ax = fig2.add_subplot(3, 1, 3)
    ax.stem(c_d2, linefmt=':')
    ax.set_title(titles[4], fontsize=10)

    fig3 = plt.figure(figsize=(12, 12))

    ax = fig3.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=10)

    ax = fig3.add_subplot(3, 1, 2)
    ax.plot(c_a3)
    ax.set_title(titles[5], fontsize=10)

    ax = fig3.add_subplot(3, 1, 3)
    ax.stem(c_d3, linefmt=':')
    ax.set_title(titles[6], fontsize=10)

    fig4 = plt.figure(figsize=(12, 12))

    ax = fig4.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=10)

    ax = fig4.add_subplot(3, 1, 2)
    ax.plot(c_a4)
    ax.set_title(titles[7], fontsize=10)

    ax = fig4.add_subplot(3, 1, 3)
    ax.stem(c_d4, linefmt=':')
    ax.set_title(titles[8], fontsize=10)

    fig5 = plt.figure(figsize=(12, 12))

    ax = fig5.add_subplot(3, 1, 1)
    ax.plot(stress)
    ax.set_title(titles[0], fontsize=10)

    ax = fig5.add_subplot(3, 1, 2)
    ax.plot(c_a5)
    ax.set_title(titles[9], fontsize=10)

    ax = fig5.add_subplot(3, 1, 3)
    ax.stem(c_d5, linefmt=':')
    ax.set_title(titles[10], fontsize=10)

    plt.show()


def cwt_plot(stress):
    scales = scg.periods2scales(np.arange(1, 100))
    wavelet = "cmor1-1.5"
    scg.set_default_wavelet(wavelet)
    # and the scaleogram
    ax1 = scg.cws(stress, scales=scales)
    plt.show()


data = ExperimentalDataLoader("StressStrainTension.csv", decimal=',', delimiter=";", encoding="cp1251")
stress = data.csv_data["Напряжение(8800 (0,1):Нагрузка) (MPa)"].values

dwt_plot(stress)
cwt_plot(stress)


