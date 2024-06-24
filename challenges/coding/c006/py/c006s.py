def icecreamParlor(m, arr):
    cost_map = {}
    for i, price in enumerate(arr):
        complement = m - price
        if complement in cost_map:
            return [cost_map[complement] + 1, i + 1]
        cost_map[price] = i
    return None  # Añadido para devolver algo si no se encuentra ninguna combinación, aunque según el problema esto no debería ocurrir

if __name__ == '__main__':
    t = int(input("Enter number of trips: ").strip())

    results = []
    for t_itr in range(t):
        m = int(input("Enter amount of money: ").strip())
        n = int(input("Enter number of flavors: ").strip())
        arr = list(map(int, input(f"Enter {n} space-separated costs: ").rstrip().split()))

        result = icecreamParlor(m, arr)
        if result is not None:
            results.append(result)
        else:
            print(f"No valid pair found for trip {t_itr + 1} with money {m} and costs {arr}")

    for result in results:
        print(' '.join(map(str, result)))
