def tsp_random_improvement(max_steps=5000):
    # 隨機產生初始路徑
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    current_len = path_length(current_path)

    for _ in range(max_steps):
        # 隨機選取兩個不同的節點交換
        i, j = random.sample(range(num_cities), 2)
        new_path = current_path[:]
        new_path[i], new_path[j] = new_path[j], new_path[i]
        new_len = path_length(new_path)

        # 嚴格變短才接受
        if new_len < current_len:
            current_path = new_path
            current_len = new_len

    return current_path, current_len
