def get_military_time(parts: list[str]) -> str:
    return parts[0] + ":" + parts[1] + ":" + parts[2]


def get_meridian(s: str) -> str:
    return s[-2:]


def get_time(s: str) -> list[str]:
    return s[:len(s) - 2].split(":")


def timeConversion(s):
    meridian = get_meridian(s).upper()

    parts_time = get_time(s)

    if meridian == "PM" and int(parts_time[0]) < 12:
        parts_time[0] = str(12 + int(parts_time[0]))

    if meridian == "AM" and int(parts_time[0]) == 12:
        parts_time[0] = '00'

    return get_military_time(parts_time)


def get_args_and_kwargs(*args, **kargs):
    num = kwargs.get("num", 0)
    if not isinstance(num, int) and not isinstance(num, float):
        return False

    total_parameters = len(args) + len(kargs)

    return total_parameters >= 4 and num > 5


if __name__ == '__main__':
    # s = input("Input a datetime:")

    # print(timeConversion(s))
    args = ["a", [2], 3]
    kwargs = {"num": 4}
    result = get_args_and_kwargs(*args, **kwargs)

    print(result)
