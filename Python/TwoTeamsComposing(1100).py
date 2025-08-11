from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        students = int(input())
        input_list = list(map(int, input().split()))
        frequency_map = Counter(input_list)
        unique_numbers = len(frequency_map)
        most_frequent = max(frequency_map.values())
        if unique_numbers == most_frequent:
            print(unique_numbers - 1)
        else:
            print(min(unique_numbers, most_frequent))
solve()
