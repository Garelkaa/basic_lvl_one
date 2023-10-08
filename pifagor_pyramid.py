import logging

logging.basicConfig(filename='pifagor.log', level=logging.INFO)


def is_pifagor(num):
    if len(num) != 3:
        logging.error("Невірна кількість елементів!")
        raise ValueError("Невірна кількість елементів!")

    a, b, c = sorted(num)

    if a**2 + b**2 == c**2:
        return True
    else:
        return False


if __name__ == '__main__':
    test1 = [5, 3, 4]
    test2 = [6, 8, 10]
    test3 = [100, 3, 65]

    try:
        result1 = is_pifagor(test1)
        result2 = is_pifagor(test2)
        result3 = is_pifagor(test3)

        logging.info(f"Result: {result1}")
        logging.info(f"Result: {result2}")
        logging.info(f"Result: {result3}")
    except Exception as e:
        logging.error(f"Помилка: {e}")
