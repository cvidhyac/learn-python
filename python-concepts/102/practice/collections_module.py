"""
Python has a collections module with many datastructures useful for iterations
"""
import random
from collections import Counter

text = f"""orem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker 
including versions of Lorem Ipsum."""

def demo_counter():
    counter = Counter(text.split())
    for word, count in sorted(counter.items()):
        print(f"{word:<12} {count:>5}")
    print(f"Number of unique keys: {len(counter.keys())}")

    random_list_of_fifty_ints = [random.randrange(1, 6) for _ in range(0, 50)]
    num_counter = Counter(random_list_of_fifty_ints)
    for number, count in sorted(num_counter.items()):
        print(f"{number:<5} {count:>5}")
    print(f"Number of unique values: {len(num_counter.keys())}")


if __name__ == '__main__':
    demo_counter()