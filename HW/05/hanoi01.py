def hanoi(n, curr, dest, rest):
    if n == 1:
       print(f"move {1} from {curr} to {dest}")
       return
    hanoi(n - 1, curr, rest, dest)
    print(f"move {n} from {curr} to {dest}")
    hanoi(n - 1, rest, dest, curr)
    return
hanoi(3, 'A', 'C', 'B')
