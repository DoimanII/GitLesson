def calculate_func(x, y):
    return (x*y)**0.5


def from_float_to_int(value: float) -> int:
    return int(value)


def some_func() -> None:
    print('some_func')

if __name__ == '__main__':
    result = calculate_func(5, 5)
    result = from_float_to_int(result)
    some_func()
    print(result)
