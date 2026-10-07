def make_legal_move(pole1, pole2, name1, name2):
    if not pole1:
        pole1.append(pole2.pop())
        print(f"move {pole1[-1]}: {name2} from {name1}")
    elif not pole2:
        pole2.append(pole1.pop())
        print(f"move {pole2[-1]}: {name1} from {name2}")
    elif pole1[-1] > pole2[-1]:
        pole1.append(pole2.pop())
        print(f"move {pole1[-1]}: {name2} from {name1}")
    else:
        pole2.append(pole1.pop())
        print(f"move {pole2[-1]}: {name1} from {name2}")

def hanoi(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []
    
    src_name, aux_name, tgt_name = 'A', 'B', 'C'
    
    if n % 2 == 0:
        target, auxiliary = auxiliary, target
        tgt_name, aux_name = aux_name, tgt_name

    total_moves = 2**n - 1

    for step in range(1, total_moves + 1):
        remainder = step % 3
        if remainder == 1:
            make_legal_move(source, target, src_name, tgt_name)
        elif remainder == 2:
            make_legal_move(source, auxiliary, src_name, aux_name)
        elif remainder == 0:
            make_legal_move(auxiliary, target, aux_name, tgt_name)

hanoi_iterative(3)
