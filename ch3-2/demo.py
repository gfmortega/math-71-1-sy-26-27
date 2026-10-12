data = [
    ["id", "make", "num_wheels", "num_doors", "type"],
    [1, "Ford Focus", 4, 4, "Sedan"],
    [2, "Tesla Roadster", 4, 2, "Sports"],
    [3, "Kawasaki Ninja", 2, 0, "Motorcycle"],
    [4, "McLaren Formula 1", 4, 0, "Race"],
    [5, "Tesla S", 4, 4, "Sedan"],
]
for row in data:
    print("!")
    for x in row:
        print('Element', x)
