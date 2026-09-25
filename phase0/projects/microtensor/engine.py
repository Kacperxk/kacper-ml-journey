class Value:
    def __init__(self, data: float, _children: tuple = (), _op: str = "") -> None:
        self.data = data
        self._children = _children
        self._op = _op
        self._backward = lambda: None
        self.grad = 0.0

    def __repr__(self) -> str:
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other: "Value | float") -> "Value":
        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

        out._backward = _backward
        return out

    def __mul__(self, other: "Value | float") -> "Value":
        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out


def main():
    a = Value(2.0)
    b = Value(3.0)
    c = a * b
    c.grad = 1.0
    c._backward()
    print(a)
    print(b)


if __name__ == "__main__":
    main()
