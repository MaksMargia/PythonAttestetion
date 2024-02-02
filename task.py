import pandas as pd
import random
#Импортируем модули
#pandas для работы с данными
#random для генерации случайных чисел

List_1 = ['robot'] * 10
#Создаем список из 10 элементов со значением 'robot'
List_1 += ['human'] * 10
# А здесь добавляем к списку еще 10 элементов со значением 'human'
random.shuffle(List_1)
#Перемешиваем элементы в списке в случайном порядке
data = pd.DataFrame({'whoAmI': List_1})
#Создаем новый DataFrame с колонкой 'whoAmI', значение которой берется из списка List_1
one_hot_data = pd.get_dummies(data['whoAmI'])
#Здесь преобразуем категориальную переменную 'whoAmI' в числовые фичи методом one-hot encoding
data = pd.concat([data, one_hot_data], axis=1)
#Объединяем исходный DataFrame с one-hot encoded фичами
data.head()                    

#Выводим первые пять строк DataFrame'a для проверки результатов