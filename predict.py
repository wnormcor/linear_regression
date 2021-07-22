import sys

if __name__ == '__main__':

    intersept, slope = .0, .0

    try:
        with open ('coefficient.txt', 'r') as file:
            intersept, slope = file.readline().split(' ')
            intersept = float(intersept)
            slope = float(slope)

    except Exception as e:
        print("Error with file of coefficient:", e)
        sys.exit(0)

    print("Введите положительный пробег машины: ", end="")

    input_km = .0
    try:
        input_km = float(input())
        if input_km < 0:
            raise Exception('Пробег должен быть положительным числом')

    except Exception as e:
        print("Error with input:", e)
        sys.exit(0)

    print("Ожидаемая стоимость согласно модели:", intersept + slope * input_km)
