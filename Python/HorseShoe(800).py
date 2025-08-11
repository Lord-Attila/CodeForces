def solve():
    input_line = input()
    array = input_line.split(" ")
    collection = set()
    for element in array:
        if element not in collection and element != " ":
            collection.add(element)
    print(4-len(collection))

solve()
