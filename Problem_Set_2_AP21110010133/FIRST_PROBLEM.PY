def main():
    n, m = map(int, input("Enter the number of vertices (N) and edges (M): ").split())
    degrees = [0] * n
    edge_types = [-1] * m

    if m % 2 != 0 and n % 2 != 0:
        print("The combination of odd edges and odd vertices is not allowed.")
        return

    for i in range(m):
        u, v = map(int, input(f"Enter the vertices for edge {i+1}: ").split())
        u -= 1
        v -= 1
        if degrees[u] % 2 == degrees[v] % 2:
            edge_types[i] = 0
            degrees[v] += 1
        else:
            edge_types[i] = 1
            degrees[u] += 1

    if any(degree % 2 != 0 for degree in degrees):
        print("There's a vertex with an odd degree, the graph is not valid.")
    else:
        print("Final edge types:", edge_types)

if __name__ == "__main__":
    main()
