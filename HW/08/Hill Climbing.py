def tsp_hill_climbing():
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    current_len = path_length(current_path)

    improved = True
    while improved:
        improved = False
        # 遍歷所有 2-Opt 子路徑翻轉
        for i in range(num_cities - 1):
            for j in range(i + 1, num_cities):
                # 翻轉 i 到 j 之間的子路徑
                new_path = current_path[:i] + current_path[i:j+1][::-1] + current_path[j+1:]
                new_len = path_length(new_path)

                if new_len < current_len:
                    current_path = new_path
                    current_len = new_len
                    improved = True
                    break
            if improved:
                break

    return current_path, current_len
