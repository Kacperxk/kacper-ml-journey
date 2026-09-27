import random
from .engine import Value
from .nn import MLP


def verify_gradient_accumulation() -> None:
    a = Value(2.0)
    b = a * a
    b.backward()
    assert a.grad == 4.0


def verify_against_hand_derivation() -> None:
    x = [Value(1.0), Value(2.0)]
    W1 = [[Value(0.1), Value(0.2)], [Value(0.3), Value(0.4)]]
    W2 = [[Value(0.5), Value(0.6)], [Value(0.7), Value(0.8)]]
    b1 = [Value(0.0), Value(0.0)]
    b2 = [Value(0.0), Value(0.0)]

    z1 = []
    for j in range(len(W1[0])):
        val = b1[j]
        for i in range(len(x)):
            val += x[i] * W1[i][j]
        z1.append(val)

    a1 = [x.relu() for x in z1]

    z2 = []
    for j in range(len(W2[0])):
        val = b2[j]
        for i in range(len(a1)):
            val += a1[i] * W2[i][j]
        z2.append(val)

    exps = [x.exp() for x in z2]
    total = sum(exps)
    probs = [exp / total for exp in exps]

    loss = -probs[0].log()
    loss.backward()
    assert abs(W1[0][0].grad - 0.05424) < 1e-4
    assert abs(W2[1][1].grad - 0.54239) < 1e-4


def train_tiny_mlp() -> None:
    random.seed(0)
    X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
    Y = [-1.0, 1.0, 1.0, -1.0]

    model = MLP(2, [4, 4, 1])

    losses = []
    for _ in range(300):
        loss = sum((model(x) - y) ** 2 for x, y in zip(X, Y))

        for p in model.parameters():
            p.grad = 0.0

        loss.backward()

        for p in model.parameters():
            p.data -= 0.05 * p.grad

        losses.append(loss.data)

    preds = [model(x).data for x in X]
    assert losses[-1] < losses[0] * 0.01
    assert preds[0] < 0 and preds[1] > 0 and preds[2] > 0 and preds[3] < 0


def main() -> None:
    verify_gradient_accumulation()
    verify_against_hand_derivation()
    train_tiny_mlp()


if __name__ == "__main__":
    main()
