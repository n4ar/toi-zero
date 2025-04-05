def solve():
    import sys
    data = sys.stdin.read().strip().split()
    name, surname = data[0], data[1]
    first_two_name = name[:2]
    if surname.startswith(first_two_name):
        combined_surname_part = surname[2:4]
    else:
        combined_surname_part = surname[:2]
    new_word = first_two_name + combined_surname_part
    print(f"Hello {name} {surname}")
    print(new_word)

if __name__ == "__main__":
    solve()
