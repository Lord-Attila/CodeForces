def solve():
    n = int(input())
    for i in range(n):
        indicies = int(input())
        string = input()
        count = 0
        answer = 0
        for char in string:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if count < 0:
                answer += 1
                count = 0
        print(answer)

solve()
