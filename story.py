x = 10
y = 1
def tigra(x, y):
    while True:
        print('Я вам сейчас раскажу сказку...', end='')
        y += 1
        if y < x :
            print('. Как дед насрал в коляску. ')
        elif y > x:
            print('Как чмо сосет колбаску. ')
        elif y == x:
            break
tigra(x, y)