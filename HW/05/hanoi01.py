def hanoi(n, source='A', target='C', auxiliary='B'):
    if n == 1:
        print(f"move 1: {source} from {target}")
        return

    hanoi(n - 1, source, auxiliary, target)
    print(f"move {n}: {source} from {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
