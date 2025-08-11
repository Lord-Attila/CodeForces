from collections import deque

def solve():
    n = int(input())
    teams = 0
    for i in range(n):
        input_line = deque(input())
        sum = 0
        while len(input_line) != 0:
            char = input_line.popleft()
            if char == '1':
                sum += 1
        if sum >= 2:
            teams += 1
    print(teams)

solve()