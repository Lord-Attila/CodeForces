def solve():
    n, m = map(int, input().split(" "))
    def f_one(x, y):
        return x ** 2 + y
    def f_two(x, y):
        return y ** 2 + x
    solutions = 0
    for i in range(36):
        for j in range(36):
            if f_one(i, j) == n and f_two(i, j) == m:
                solutions += 1
    print(solutions)

solve()
