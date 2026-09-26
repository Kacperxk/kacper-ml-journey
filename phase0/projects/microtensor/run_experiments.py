from .engine import Value


def verify_gradient_accumulation() -> None:
    a = Value(2.0)
    b = a * a
    b.backward()
    assert a.grad == 4.0


def main() -> None:
    verify_gradient_accumulation()


if __name__ == "__main__":
    main()
