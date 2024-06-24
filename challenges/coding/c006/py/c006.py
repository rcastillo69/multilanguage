def icecreamParlor(m,arr):
    cost_map = {}

    for i, price in enumerate(arr):
        price2 = m - price
        if price2 in cost_map:
            return [cost_map[price2]+1, i+1]
        cost_map[price] = i

if __name__ == '__main__':
    trips = int(input("Enter number of trips: ").strip())

    results = []
    for t in range(trips):
        money = int(input("Enter amount of money: ").strip())
        num_flavors = int(input("Enter number of flavors: ").strip())
        arr = list(map(int,input(f"Enter {num_flavors} space-separator:").rstrip().split()))

        result = icecreamParlor(money,arr)

        if result is not None:
            results.append(result)
        else:
            print(f"No valid pair found for a trip {t+1} with money {money} and costs {arr}")
        
    for r in results:
        print(' '.join(map(str,r)))