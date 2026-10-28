def tsp_gradient_descent(lr=0.05, epochs=300):
    # W[t, i] 代表在第 t 步拜訪城市 i 的權重 logits
    W = [[random.uniform(-0.1, 0.1) for _ in range(num_cities)] for _ in range(num_cities)]

    def softmax_matrix(weights):
        # 對每個步驟計算通過各城市的機率分布 P[t, i]
        P = []
        for row in weights:
            max_v = max(row)
            exp_row = [math.exp(v - max_v) for v in row]
            sum_exp = sum(exp_row)
            P.append([v / sum_exp for v in exp_row])
        return P

    for _ in range(epochs):
        P = softmax_matrix(W)

        # 計算每個步驟 t 的預期坐標
        exp_coords = []
        for t in range(num_cities):
            ex = sum(P[t][i] * cities[i][0] for i in range(num_cities))
            ey = sum(P[t][i] * cities[i][1] for i in range(num_cities))
            exp_coords.append((ex, ey))

        # 數值計算數值梯度（針對每個 weight 進行小幅度數值微擾）
        grad = [[0.0] * num_cities for _ in range(num_cities)]
        eps = 1e-4

        def loss(weights):
            probs = softmax_matrix(weights)
            coords = []
            for t in range(num_cities):
                cx = sum(probs[t][k] * cities[k][0] for k in range(num_cities))
                cy = sum(probs[t][k] * cities[k][1] for k in range(num_cities))
                coords.append((cx, cy))
            
            # 連續環路歐氏距離平方和
            total_loss = 0.0
            for t in range(num_cities):
                nx, ny = coords[(t + 1) % num_cities]
                total_loss += (coords[t][0] - nx)**2 + (coords[t][1] - ny)**2
            return total_loss

        base_loss = loss(W)
        for r in range(num_cities):
            for c in range(num_cities):
                W[r][c] += eps
                grad[r][c] = (loss(W) - base_loss) / eps
                W[r][c] -= eps

        # 梯度更新：沿著負梯度方向前進
        for r in range(num_cities):
            for c in range(num_cities):
                W[r][c] -= lr * grad[r][c]

    # 解碼回離散路徑（每一步貪婪挑選未造訪且機率最高的城市）
    final_P = softmax_matrix(W)
    visited = set()
    discrete_path = []
    for t in range(num_cities):
        sorted_indices = sorted(range(num_cities), key=lambda idx: final_P[t][idx], reverse=True)
        for city_idx in sorted_indices:
            if city_idx not in visited:
                visited.add(city_idx)
                discrete_path.append(city_idx)
                break

    return discrete_path, path_length(discrete_path)
