sequence = input('Введите последовательность чисел через пробел')
k = int(input('Введите число'))
a = sequence.split(' ')
int_sequence = []
for b in a:
    int_sequence.append(int(b))
print(a)
print(int_sequence)
int_sequence = sorted(int_sequence)
print(int_sequence)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
print(binary_search(int_sequence, k, 0, len(int_sequence)))