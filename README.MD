1) установить Python 3.10 https://www.python.org/downloads/
2) в консоле установить необходимые библиотеки: pip install -r requirements.txt
3) в scaleogram.py:22 содержится имя запускаемого файла, он должен находится в папке data в формате csv
4) в scaleogram.py:53 параметр scales задает тип масштабов ("log", "log-piecewise", "linear")
5) при запуске scaleogram.py необходимо ввести два числа: столбец абцисс и столбец ординат исходного сигнала из файла п. 3