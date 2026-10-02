"""Test problem_02.py"""

import numpy as np
import pytest

from assignment.problem_02 import problem_02_part_a, problem_02_part_b


def test_problem_02_part_a():
    """Test problem 02 - Part A."""
    fx = problem_02_part_a()
    assert np.ndim(fx) == 0, "The correct choice returns a scalar."
    assert fx == pytest.approx(23.2080327936)


def test_problem_02_part_b():
    """Test problem 02 - Part B."""
    fx = problem_02_part_b()
    assert np.shape(fx) == (10,), "Return one output per input element."
    np.testing.assert_allclose(fx, [0, 0, 0, 0, 0, 0, 1, 2, 3, 4])
