def is_divisibility_by(number: int, div_by: int) -> bool:
    return number % div_by == 0


def is_leap(year_input: int) -> int:
    return (is_divisibility_by(year_input, 4) and
            (not is_divisibility_by(year_input, 100) or is_divisibility_by(year_input, 400)))


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
