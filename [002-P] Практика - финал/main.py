# 1
print('Алиса')

try:
    #print(2 + '3')
    print(value)
except Exception as e:
    print(f'ВЫШЕЛ ИЗ ОШИБКИ: {e.__class__.__name__}:', e)

print('Гарри')

# 2
print('-' * 30)

while True:
    try:
        while True:
            print('Hi!')
            [1, 2, 3][10]
            break
    except Exception as e:
        print('OOOOOOOOOOO', e.__class__.__name__, e)
        break

print('The End!')

# 3
print('-' * 30)


try:
    raise IndexError('la la la la')
finally:
    print('ГАРАНТИЯ 3 года')


print('THE "The End!"')















