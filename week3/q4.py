dimension = input("Enter length and breadth (separated by space): ")
dimension = list(map(int, dimension.split(" ")))
perimeter = 2 * (sum(dimension))

print("Perimeter:", perimeter)