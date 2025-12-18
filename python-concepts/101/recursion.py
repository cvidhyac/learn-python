

def print_fifty_nums(n:int, limit:int) -> None:
    if n > limit:
        return
    print(n)
    print_fifty_nums(n+1, limit)

def demo_recursion():
    print_fifty_nums(1, 50)

if __name__ == '__main__':
    demo_recursion()