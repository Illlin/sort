import random
import time

def draw_array(array):
    print("\n"*50)
    for item in array:
        print("{0:<5}: {1}".format(item,"[]"*item),flush=True)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array = []
for i in range(20):
    array.append(random.choice(numbers))

random.shuffle(array)

def bubble(array):
    for i in range(len(array)-2):
        flag = False
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j+1] , array[j] = array[j], array[j+1]
                flag = True
                draw_array(array)
                time.sleep(0.05)
        if not flag:
            break

def insersion(array):
    for pointer in range(len(array)-1):
        current = pointer + 1
        flag = True
        while flag:
            if current == 0:
                flag = False
            elif array[current] < array[current-1]:
                array[current] , array[current-1] = array[current-1], array[current]
                current -= 1
                draw_array(array)
                time.sleep(0.05)
            else:
                flag = False



insersion(array)
bubble(array)
time.sleep(0.05)
draw_array(array)