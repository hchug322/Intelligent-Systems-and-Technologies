"""
Описание домашней работы

В данной работе я реализовал простую нейронную сеть для 
классификации состояния здоровья на основе четырех входных параметров: 
веса (кг), роста (см), возраста (лет) и уровня физической активности (0 - низкий, 1 - высокий). 
Целью является предсказать, нужно ли обращаться в больницу.

Основные компоненты кода:

- библиотека numpy для работы с массивами и математическими операциями.

- Реализована функция sigmoid, которая используется для активации нейронов.

- Функция sigmoid_derivative вычисляет производную сигмоиды, 
    необходимую для обратного распространения ошибки.

- Данные представлены в виде массива, где каждая строка соответствует отдельному примеру 
    с указанными параметрами.

- Входные данные нормализуются для улучшения обучения модели.

- Определены целевые значения, указывающие, нужно ли обращаться в больницу (1 - да, 0 - нет).

- Случайные веса инициализируются для двух слоев: входного и скрытого.

- В течение 10,000 итераций выполняется процесс прямого и обратного распространения:
- Прямое распространение: вычисляются выходные значения нейронной сети.
- Обратное распространение: рассчитывается ошибка и обновляются веса для уменьшения этой ошибки.

- После обучения нейронная сеть делает прогнозы на основе обученных данных.

- Результаты выводятся на экран, показывая, нужно ли обращаться в больницу для каждого примера.


### Чугунов Иван, М23ИО
### hchug322@mail.com

### Чесноков А.Д. 
### alexandertchesnockoff@yandex.ru

"""
import numpy as np 

def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) 

def sigmoid_derivative(x): 
    return x * (1 - x) 

# Входные данные
# [вес (кг), рост (см), возраст (лет), уровень физической активности (0 - низкий, 1 - высокий)]
input_data = np.array([[70, 175, 25, 1],    # Пример 1 
                       [80, 180, 30, 0],    # Пример 2 
                       [60, 160, 22, 1],    # Пример 3 
                       [90, 190, 35, 0]])   # Пример 4 

# Нормализация
input_data = input_data / np.array([100, 200, 100, 1])

# Целевые данные (нужно ли обращаться в больницу) 
target_data = np.array([[0],   # Пример 1 - все хорошо 
                        [1],   # Пример 2 - консультация нужна 
                        [0],   # Пример 3 - все хорошо 
                        [1]])  # Пример 4 - консультация нужна 

np.random.seed(1) 
synapse_0 = 2 * np.random.random((4, 4)) - 1  # Входной слой к скрытому слою 
synapse_1 = 2 * np.random.random((4, 1)) - 1  # Скрытый слой к выходному слою 

# Обучение нейронной сети 
for j in range(10000): 
    # Прямое распространение 
    layer_1 = sigmoid(np.dot(input_data, synapse_0)) 
    layer_2 = sigmoid(np.dot(layer_1, synapse_1)) 

    # Обратное распространение 
    layer_2_error = target_data - layer_2 
    layer_2_delta = layer_2_error * sigmoid_derivative(layer_2) 

    layer_1_error = layer_2_delta.dot(synapse_1.T) 
    layer_1_delta = layer_1_error * sigmoid_derivative(layer_1) 

    # Обновление весов 
    synapse_1 += layer_1.T.dot(layer_2_delta) 
    synapse_0 += input_data.T.dot(layer_1_delta) 

# Прогнозирование состояния системы 
result = layer_2 

# Вывод результата 
print("Предсказанное состояние системы:") 
print(result) 

# Вывод самого вероятного состояния 
most_likely_state = (result > 0.5).astype(int)
for i, state in enumerate(most_likely_state): 
    print(f"Пример {i + 1}: {'Обратиться в больницу' if state else 'Все хорошо'}")