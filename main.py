print('Asan')
print('Uson')
print('Марат')
print('Мурат')

def greet():
    print('hello')

def add(a,b):
    return a, b
print(add(1,2))

def check_number(n):
    if n < 0 or n > 100:
        return False
    else:
        return True