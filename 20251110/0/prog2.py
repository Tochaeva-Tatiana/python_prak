while True:
    try:
        a = int(input())
        break
    except ValueError:
        print('введи еще')
