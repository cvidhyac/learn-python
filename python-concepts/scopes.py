"""
LEGB Principle - Local -> enclosing scope -> Global -> Built-ins
Scopes Can be overridden by `nonlocal` keyword, however non-local does not have many enterprise uses.
"""

x = 100


def with_global_scope() -> int:
    global x
    x = 50
    return x


def with_local_scope() -> int:
    x = 200  # ignore shadow variable warning because this is to illustrate effects of local scope
    return x


def with_enclosing_scope() -> int:
    y = 150
    if y:
        return y
    else:
        return 0


def demo_global_scope() -> None:
    global_override = with_global_scope()
    print(f"Demo global scope {global_override}")


def demo_local_scope() -> None:
    local_override = with_local_scope()
    print(f"Demo Local scope: {local_override}")


def demo_enclosing_local_scope() -> None:
    enclosing_local_scope = with_enclosing_scope()
    print(f"Demo enclosing local scope: {enclosing_local_scope}")


if __name__ == '__main__':
    demo_global_scope()
    demo_local_scope()
    demo_enclosing_local_scope()
