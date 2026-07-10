
def calculate_func(x, y):
    return (x*y)**0.5


def from_float_to_int(value: float) -> int:
    return int(value)


def some_func() -> None:
    print('some_func')


def bubble_sort(array_to_sort: list) -> list:
    array_length: int = len(array_to_sort)
    for x in range(array_length):
        for y in range(0, array_length-x-1):
            if array_to_sort[y] > array_to_sort[y+1]:
                array_to_sort[y], array_to_sort[y+1] = array_to_sort[y+1], array_to_sort[y]

    return array_to_sort


if __name__ == '__main__':
    result = calculate_func(5, 5)
    result = from_float_to_int(result)
    some_func()
    print(bubble_sort([5, 10, 2, 0]))
    print(result)
