
def print_hi(name):
    print(f'Hi, {name}')

def just_func():
    arr: list = [number for number in range(100+1)]
    for value in arr:
        print(value)

if __name__ == '__main__':
    print_hi('Hi Git!')
    just_func()

