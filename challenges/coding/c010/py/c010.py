def cavityMap(grid):
    n = len(grid)
    mgrid = [list(row) for row in grid]

    for i in range(1, n-1):
        for j in range(1, n-1):
            depth = mgrid[i][j]
            if (mgrid[i-1][j] < depth and
                mgrid[i+1][j] < depth and
                mgrid[i][j-1] < depth and
                mgrid[i][j+1] < depth):
                mgrid[i][j] = 'X'

    return [''.join(row) for row in mgrid]

if __name__ == '__main__':
    n = int(input().strip())
    grid = [input().strip() for _ in range(n)]

    result = cavityMap(grid)

    for row in result:
        print(row)
