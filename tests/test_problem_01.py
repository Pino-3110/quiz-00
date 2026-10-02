"""Test problem_01.py"""

import numpy as np
import pytest

from assignment.problem_01 import problem_01_part_a, problem_01_part_b


def test_problem_01_part_a():
    """Test problem 01 - Part A."""
    max_x = problem_01_part_a()
    assert np.ndim(max_x) == 0, "Return a single maximum value."
    assert max_x == pytest.approx(0.5)


def test_problem_01_part_b():
    """Test problem 01 - Part B."""
    dot_x = problem_01_part_b()
    assert np.ndim(dot_x) == 0, "The dot product must be a scalar."
    assert dot_x == 59
