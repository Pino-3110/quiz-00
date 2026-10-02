"""Test problem_03.py"""

import numpy as np

from assignment.problem_03 import (
    ChildToyNeuralNet,
    ToyNeuralNetwork,
    problem_03_part_a,
    problem_03_part_b,
)


def test_problem_03_part_a():
    """Test all four inputs in the XOR truth table."""
    x_features = np.array([[0, 0], [1, 1], [0, 1], [1, 0]], dtype=float)
    nn = ToyNeuralNetwork()
    y_predicted = problem_03_part_a(nn, x_features)
    assert np.shape(y_predicted) == (4,), "Return one output per input row."
    np.testing.assert_allclose(y_predicted, [0, 0, 1, 1])


def test_problem_03_part_b():
    """Test the new weights and every attribute initialized by the parent."""
    child_nn = ChildToyNeuralNet()
    weights_hidden = problem_03_part_b(child_nn)
    assert np.shape(weights_hidden) == (2, 2)
    np.testing.assert_allclose(weights_hidden, np.ones((2, 2)))
    parent_nn = ToyNeuralNetwork()
    np.testing.assert_array_equal(child_nn.bias_hidden, parent_nn.bias_hidden)
    np.testing.assert_array_equal(
        child_nn.weights_output, parent_nn.weights_output
    )
    assert child_nn.bias_output == parent_nn.bias_output
