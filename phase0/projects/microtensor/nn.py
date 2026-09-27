import random
from .engine import Value


class Neuron:
    def __init__(self, n_inputs: int, nonlin: bool = True) -> None:
        self.w = [Value(random.uniform(-1, 1)) for _ in range(n_inputs)]
        self.b = Value(0.0)
        self.nonlin = nonlin

    def __call__(self, x: list[Value]) -> Value:
        val = self.b
        for i in range(len(x)):
            val += self.w[i] * x[i]
        return val.relu() if self.nonlin else val

    def parameters(self) -> list[Value]:
        return self.w + [self.b]


class Layer:
    def __init__(self, n_inputs: int, n_outputs: int, nonlin: bool = True) -> None:
        self.neurons = [Neuron(n_inputs, nonlin) for _ in range(n_outputs)]

    def __call__(self, x: list[Value]) -> "Value | list[Value]":
        outs = [neuron(x) for neuron in self.neurons]
        return outs[0] if len(outs) == 1 else outs

    def parameters(self) -> list[Value]:
        return [p for n in self.neurons for p in n.parameters()]


class MLP:
    def __init__(self, n_inputs: int, layer_sizes: list[int]) -> None:
        self.sizes = [n_inputs] + layer_sizes
        self.layers = []
        for i in range(len(layer_sizes)):
            n_in = self.sizes[i]
            n_out = self.sizes[i + 1]
            is_last = i == len(layer_sizes) - 1
            self.layers.append(Layer(n_in, n_out, nonlin=not is_last))

    def __call__(self, x: list[Value]) -> "Value | list[Value]":
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self) -> list[Value]:
        return [p for layer in self.layers for p in layer.parameters()]
