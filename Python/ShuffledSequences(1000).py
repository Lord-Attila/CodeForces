def solve():
    number = int(input())
    list_map = list(map(int, input().split()))
    if len(list_map) != number:
        print("NO")
        return
    frequency = {}
    for element in list_map:
        frequency[element] = frequency.get(element, 0) + 1
        if frequency[element] > 2:
            print("NO")
            return
    increasing = []
    decreasing = []
    for element in sorted(frequency.keys()):
        if frequency[element] == 2:
            increasing.append(element)
            decreasing.append(element)
        elif frequency[element] == 1:
            increasing.append(element)
    used = set()
    final_increasing = []
    final_decreasing = []
    for element in sorted(increasing):
        if element not in used:
            final_increasing.append(element)
            used.add(element)
    used.clear()
    for element in sorted(decreasing, reverse=True):
        if element not in used:
            final_decreasing.append(element)
            used.add(element)
    print("YES")
    print(len(final_increasing))
    if final_increasing:
        print(" ".join(map(str, final_increasing)))
    else:
        print()
    print(len(final_decreasing))
    if final_decreasing:
        print(" ".join(map(str, final_decreasing)))
    else:
        print()
solve()
