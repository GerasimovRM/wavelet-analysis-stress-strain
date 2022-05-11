import sys
from core import cwt
from core.visuals import plot, imshow
import os

import numpy
import pandas as pd


WORK_PATH = os.path.abspath(os.getcwd())


class ExperimentalDataLoader:
    def __init__(self, file_name: str, *args, **kwargs):
        self.csv_abs_path = os.path.join(WORK_PATH, "data", file_name)
        self.csv_data = pd.read_csv(self.csv_abs_path, *args, **kwargs)

    def __str__(self):
        return self.csv_data


data = ExperimentalDataLoader("Tube-15.csv", decimal=',', delimiter=";", encoding="cp1251")
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

time = data.csv_data[first_col].values.astype(float)[290:610]
stress = data.csv_data[second_col].values.astype(float)[290:610]
data = numpy.array([time, stress])
print(data.shape, data.ndim)
print(time)
print(stress)

plot(time, stress, xlabel="Общее время, сек", ylabel="Осевое напряжение, МПа", show=1)
Wx, scales = cwt(data, scales="log-piecewise")
imshow(Wx[1], yticks=scales, abs=1,
       title="|W(a, b)|, МПа",
       ylabel="Масштаб а", xlabel="Сдвиг b, мм",
       xticks=time,
       cmap="turbo"
       )

sys.exit(0)