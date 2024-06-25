def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n, m, s = map(int, input().strip().split())
        result = saveThePrisoner(n, m, s)
        print(result)