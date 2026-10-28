def tsp_greedy(start_city=0):
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)

    path = [start_city]
    current = start_city

    while unvisited:
        # 貪婪挑選距離最近的下一個城市
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return path, path_length(path)
