import sys
import os
import re
from datetime import datetime
now = datetime.now()
if (sys.argv[1] == '-ping'): # Если -ping
	result=os.popen("ping -c 1 " + sys.argv[2]).read() # Делаем пинг по заданному адресу
	result=re.findall(r"time=(.*) ms", result) # Выдёргиваем из результата время
	print(result[0]) # Выводим результат в консоль
elif (sys.argv[1] == '-simple_print'): # Если simple_print
	print(sys.argv[2]) # Выводим в консоль содержимое sys.arvg[2]
elif (sys.argv[1] == '1'): # Если 1
    print(f"Dunaev Dmitriy") # Выводим в консоль имя и фамилию
elif (sys.argv[1] == '2'): # Если 2
    print(f"Date is {now}") # Выводим в консоль дату
else: # Во всех остальных случаях
	print(f"unknown input: {sys.argv[1]}") # Выводим непонятый запрос в консоль
