# /test_example.py # g_b- 210411
#
import time
import random
import os
#выполнить pip install psutil
import psutil

car_names = ['Audi', 'Toyota', 'Renault', 'Nissan', 'Honda', 'Suzuki']
colors = ['Black', 'Blue', 'Red', 'White', 'Yellow']

def car_list(cars):
    all_cars = []
    for i in range (cars):
        car = {
            'id': i,
            'name': random.choice(car_names),
            'color': random.choice(colors)
        }
        all_cars.append(car)
    return all_cars

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory before list is created: ' + str(process.memory_info().rss/1000000))

# Вызов функции car_list и время, сколько времени это занимает
#t1 = time.clock()
t1 = time.time_ns()
print(t1)
cars = car_list(1000000)
t2 = time.time_ns()

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory after list is created: ' + str(process.memory_info().rss/1000000))

print('Took {} seconds'.format((t2-t1)/1000000000))

