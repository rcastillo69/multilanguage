def rotateLeft(d, arr):
    size = len(arr)
    d = d % size

    if d== 0 or d == size:
        return arr
       
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    n, d = map(int, input("Enter n and d: ").split())
    arr = list(map(int, input(f"Enter {n} space-separated integers: ").split()))
    
    result = rotateLeft(d, arr)
    
    print(' '.join(map(str, result)))
