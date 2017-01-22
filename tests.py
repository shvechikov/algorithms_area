import pytest
import random
import itertools

from solutions import andrey, andrey_improved, leonid


BASIC_TESTS = (
    ([], 0),
    ([(0, 2, 2)], 4),
    ([(0, 4, 2), (4, 4, 2), (2, 3, 1), (1, 5, 2)], 10),
    ([(0, 2, 2), (0, 2, 1)], 4),
    ([(0, 5, 2), (2, 7, 4), (4, 9, 1)], 26),
    ([(0, 5, 2), (2, 7, 4), (4, 9, 1), (3, 6, 3)], 26),
    ([(0, 5, 2), (2, 6, 3), (2, 7, 4), (4, 9, 1)], 26),
    ([(0, 5, 2), (2, 7, 4), (4, 9, 1), (3, 6, 3), (11, 13, 2)], 30),
    ([(0, 5, 2), (0, 7, 2), (2, 7, 4), (4, 9, 1), (3, 6, 3), (11, 13, 2)], 30)
)

SOLUTIONS = {
    'andrey': andrey,
    'andrey_improved': andrey_improved,
    'leonid': leonid,
}

BASIC_COMBINATIONS = [
    (solution, rects, result)
    for rects, result in BASIC_TESTS
    for solution in SOLUTIONS.keys()
]
RANDOM_TESTS = itertools.product(SOLUTIONS.keys(), range(10, 15))
K = 2000


def get_rect(k):
    start = random.randint(0, k)
    end = random.randint(start, k)
    height = random.randint(0, k)
    return start, end, height


@pytest.mark.parametrize("solution, rects, result", BASIC_COMBINATIONS)
def test_basic(solution, rects, result):
    assert SOLUTIONS[solution].solve(rects) == result


@pytest.mark.skip(reason="use this one only when add new solutions")
@pytest.mark.parametrize("seed", range(100))
def test_random_correctness(seed):
    random.seed(seed)
    rects = [get_rect(K) for _ in range(K)]
    results = [solution.solve(rects) for solution in SOLUTIONS.values()]
    assert all(results[0] == r for r in results[1:])


@pytest.mark.parametrize("solution, seed", RANDOM_TESTS)
def test_random_speed(solution, seed):
    random.seed(seed)
    rects = [get_rect(K) for _ in range(K)]
    solve = SOLUTIONS[solution].solve
    solve(rects)
    assert True

