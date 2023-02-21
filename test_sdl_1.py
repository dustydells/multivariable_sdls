from sdl_1 import compute_dot_product, compute_cross_product, compute_projection
import pytest
import numpy as np

def test_compute_dot_product():
    us = [
        [1],
        [-1],
        [0],
        [-2, -8],
        [-8, 0, 1]
    ]
    vs = [
        [1],
        [-1],
        [0],
        [-2, 8],
        [2, 2, 2]
    ]

    answers = [1, 1, 0, -60, -14]

    for i in range(len(us)):
        assert compute_dot_product(u=np.array(us[i]), v=np.array(vs[i])) == answers[i]

def test_compute_cross_product():
    us = [
        [-8, 0, 1]
    ]
    vs = [
        [2, 2, 2]
    ]

    answers = [
        [-2, 18, -16]
    ]
    
    for i in range(len(us)):
        assert compute_cross_product(u=np.array(us[i]), v=np.array(vs[i])) == answers[i]

def test_compute_projection():
    pass

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])