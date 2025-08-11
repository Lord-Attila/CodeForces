def solve():
    n = int(input())
    for i in range(n):
        inputline = int(input())
        distance = (inputline-1)/2
        multiplier = 1
        moves = 0
        tiles = 8
        while distance >= 1:
            distance -= 1
            moves += multiplier * tiles
            multiplier += 1
            tiles += 8
        print(moves)

solve()
