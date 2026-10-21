import random
from loguru import logger

logger.debug('Начало работы')
logger.add('logs/log_{time}.log', level='DEBUG', rotation='100 KB')
logger.add('logs/error_log.log', level='WARNING')


def choice_sort(data: list[int]):
    logger.info(f'Сортировка {choice_sort.__name__} начала свою работу с объектом {data}')
    if len(data) < 2:
        logger.warning('Нечего сортировать')
        return data
    if type(data) != list:
        logger.error(f'Ожидается тип данных list, а передан {type(data)}')
        return None
    n = len(data)
    for a in range(n - 1):
        min_num = data[a]
        idx_min = a
        logger.debug(f'Начинается {a + 1} проход внешнего цикла, min={min_num}, idx={a}')
        for b in range(a + 1, n):
            if data[b] < min_num:
                min_num = data[b]
                idx_min = b
                logger.debug(f'На {b + 1} проходе внутреннего цикла найдено новое минимальное значение, '
                             f'min={min_num}, idx={b}')
        if idx_min != a:
            memory = data[a]
            data[a] = data[idx_min]
            data[idx_min] = memory
            logger.debug(f'Замена элементов, на индекс {a} ставим элемент {data[a]}, на {idx_min} - {data[idx_min]}')
    logger.success(f'Отсортированный список - {data}')
    return data


# a = choice_sort((1,6,0))


def bingo(data: list[int]) -> list[int]:
    # Первый проход
    max_idx = len(data) - 1
    next_value = data[max_idx]
    for i in range(max_idx - 1, -1, -1):
        if data[i] > next_value:
            next_value = data[i]

    while max_idx and data[max_idx] == next_value:
        max_idx -= 1
        # Последующие проходы
    while max_idx:
        value = next_value
        next_value = data[max_idx]
        for i in range(max_idx - 1, -1, -1):
            if data[i] == value:
                data[i], data[max_idx] = data[max_idx], data[i]
                max_idx -= 1
            elif data[i] > next_value:
                next_value = data[i]
        while max_idx and data[max_idx] == next_value:
            max_idx -= 1

    return data


def pancake(data: list[int]) -> list[int]:
    if len(data) > 1:
        for size in range(len(data), 1, -1):
            max_index = max(range(size), key=data.__getitem__)
            if max_index + 1 != size:
                if max_index != 0:
                    data[:max_index + 1] = reversed(data[:max_index + 1])
                data[:size] = reversed(data[:size])
    return data


def insertion(data: list[int]) -> list[int]:
    N = len(data)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
    return data


def binary_insert_sort(data: list[float]):
    for i in range(1, len(data)):
        key = data[i]
        low, high = 0, i - 1
        while low <= high:
            mid = (low + high) // 2
            if key < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            data[j] = data[j - 1]
        data[low] = key
    return data


def bubble_sort(data: list[float]):
    logger.info(f'Сортировка {bubble_sort.__name__} начала свою работу с объектом {data}')
    n = len(data)
    if n > 1:
        for i in range(0, n - 1):
            logger.info(f'Начинается {i + 1} проход внешнего цикла (i={i})')
            for j in range(0, n - 1 - i):
                logger.info(f'Сравнение элементов data[{j}]={data[j]} и data[{j + 1}]={data[j + 1]}')
                if data[j] > data[j + 1]:
                    logger.debug(f'{data[j]}>{data[j + 1]}, меняем элементы местами')
                    data[j], data[j + 1] = data[j + 1], data[j]
    else:
        logger.warning('Нечего сортировать')
    logger.success(f'Функция успешно отработала и вернула список - {data}')
    return data


n = choice_sort((1, 6, 0))


def merge_list(data1: list[float], data2: list[float]):
    data = []
    n = len(data1)
    m = len(data2)
    i = 0
    j = 0
    while i < n and j < m:
        if data1[i] <= data2[j]:
            data.append(data1[i])
            i += 1
        else:
            data.append(data2[j])
            j += 1
    data += data1[i:] + data2[j:]
    return data


def split_and_merge_list(data: list[float]) -> list[float]:
    n = len(data) // 2
    data1, data2 = data[:n], data[n:]
    if len(data1) > 1:
        data1 = split_and_merge_list(data1)
    if len(data2) > 1:
        data2 = split_and_merge_list(data2)
    return merge_list(data1, data2)


def quick_sort(data: list[float]):
    if len(data) > 1:
        x = data[random.randint(0, len(data) - 1)]
        low = [a for a in data if a < x]
        equal = [a for a in data if a == x]
        high = [a for a in data if a > x]
        data = quick_sort(low) + equal + quick_sort(high)
    return data


dataset = [541, 934, 661, -868, 709, -277, 142, 493, 286, 733, -229, 79]
sort1 = choice_sort(dataset.copy())
print(sort1)

sort2 = bingo(dataset.copy())
print(sort2)

sort3 = pancake(dataset.copy())
print(sort3)

sort4 = insertion(dataset.copy())
print(sort4)

sort5 = binary_insert_sort(dataset.copy())
print(sort5)

sort6 = bubble_sort(dataset.copy())
print(sort6)

sort7 = quick_sort(dataset.copy())
print(sort7)
