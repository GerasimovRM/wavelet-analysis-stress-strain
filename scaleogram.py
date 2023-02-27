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


filename = input("Select file:")
data = ExperimentalDataLoader(filename, decimal=',', delimiter=";", encoding="cp1251")
while True:
    print("Выберите первый столбец:")
    for i, col in enumerate(data.csv_data.columns):
        print(i, col)
    first_col_index = int(input())
    try:
        first_col = data.csv_data.columns[first_col_index]
    except IndexError:
        continue
    break
column_1 = data.csv_data[first_col].values.astype(float)
print(f"Диапазон первого столбца: {min(column_1)} - {max(column_1)}")
print("Хотите взять весь диапазон? (y/n)")
answer = input().lower()

if answer in ("y", "yes", "да", "д"):
    start_index, finish_index = 0, len(column_1)
else:
    print("Выберите диапазон отображения (два числа через пробел):")
    start, end = map(float, input().split())
    data_row = list(filter(lambda x: start <= x[1] <= end, enumerate(column_1)))
    start_index, finish_index = data_row[0][0], data_row[-1][0]
column_1 = column_1[start_index: finish_index]

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
column_2 = data.csv_data[second_col].values.astype(float)[start_index: finish_index]

data = numpy.array([column_1, column_2])
print(data.shape, data.ndim)
print(column_1)
print(column_2)

plot(column_1, column_2, xlabel="Общее время, сек", ylabel="Осевое напряжение, МПа", show=1)
Wx, scales = cwt(data, scales="log-piecewise")
imshow(Wx[1], yticks=scales, abs=1,
       title="|W(a, b)|, МПа",
       ylabel="Масштаб а", xlabel=first_col,
       xticks=column_1,
       cmap="turbo"
       )

sys.exit(0)
