def saveThePrisoner(n, m, s):
    # Calcula la posición del último dulce
    result = (s + m - 2) % n + 1
    return result

if __name__ == '__main__':
    t = int(input("Enter number of test cases: ").strip())

    results = []
    for t_itr in range(t):
        n, m, s = map(int, input("Enter n (number of prisoners), m (number of sweets), s (start position): ").strip().split())
        result = saveThePrisoner(n, m, s)
        results.append(result)

    for result in results:
        print(result)
