def multiply_by_two(a: int) -> int:
    return a * 2


def run():
    while True:
        a = int(input("Введите любое число и оно умножится на 2! "))
        result = multiply_by_two(a)
        print("Вот и число", result)


if __name__ == "__main__":
    run()
