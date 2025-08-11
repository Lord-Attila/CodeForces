def solve():
    input_line = str(input())
    unique_characters = set()
    for char in input_line:
        if char not in unique_characters:
            unique_characters.add(char)
    if len(unique_characters) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

solve()
