from collections import deque

def is_valid(state):
    farmer, wolf, goat, cabbage = state
    # 若農夫不在，狼跟羊同岸 -> 不合法
    if wolf == goat and farmer != wolf:
        return False
    # 若農夫不在，羊跟甘藍菜同岸 -> 不合法
    if goat == cabbage and farmer != goat:
        return False
    return True

def get_next_states(state):
    farmer, wolf, goat, cabbage = state
    next_farmer = 1 - farmer
    candidates = []
    
    # 1. 農夫自己過河
    candidates.append(((next_farmer, wolf, goat, cabbage), "農夫獨自過河"))
    
    # 2. 帶狼過河 (狼必須與農夫同側)
    if wolf == farmer:
        candidates.append(((next_farmer, 1 - wolf, goat, cabbage), "農夫帶狼過河"))
        
    # 3. 帶羊過河 (羊必須與農夫同側)
    if goat == farmer:
        candidates.append(((next_farmer, wolf, 1 - goat, cabbage), "農夫帶羊過河"))
        
    # 4. 帶甘藍菜過河 (甘藍菜必須與農夫同側)
    if cabbage == farmer:
        candidates.append(((next_farmer, wolf, goat, 1 - cabbage), "農夫帶甘藍菜過河"))
    
    # 僅保留合法狀態
    return [(s, action) for s, action in candidates if is_valid(s)]

def solve_river_crossing():
    start_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    
    # BFS 佇列結構：(目前狀態, 路徑歷史)
    # 路徑歷史記錄 (動作描述, 狀態)
    queue = deque([(start_state, [("初始狀態", start_state)])])
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        # 達到目標狀態
        if current_state == goal_state:
            return path
            
        for next_state, action in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, next_state)]))
                
    return None

def format_bank(state):
    f, w, g, c = state
    names = ["農夫", "狼", "羊", "甘藍菜"]
    left = [names[i] for i, v in enumerate(state) if v == 0]
    right = [names[i] for i, v in enumerate(state) if v == 1]
    return f"起始岸: [{', '.join(left) or '空'}] | 對岸: [{', '.join(right) or '空'}]"

# --- 執行解題 ---
if __name__ == "__main__":
    solution = solve_river_crossing()
    if solution:
        print(f"找到最短解！總步數：{len(solution) - 1} 步\n")
        for step, (action, state) in enumerate(solution):
            print(f"Step {step}: {action:<10} -> {format_bank(state)}")
    else:
        print("無解")
