def tsp_simulated_annealing(init_temp=1000.0, cooling_rate=0.995, min_temp=1e-4):
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    current_len = path_length(current_path)

    best_path = current_path[:]
    best_len = current_len

    T = init_temp
    while T > min_temp:
        # 隨機挑選 2-Opt 鄰域進行擾動
        i, j = sorted(random.sample(range(num_cities), 2))
        new_path = current_path[:i] + current_path[i:j+1][::-1] + current_path[j+1:]
        new_len = path_length(new_path)

        delta = new_len - current_len

        # 若新解更短，或以機率 exp(-delta / T) 接受較差解
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_path = new_path
            current_len = new_len

            if current_len < best_len:
                best_path = current_path[:]
                best_len = current_len

        T *= cooling_rate

    return best_path, best_len
