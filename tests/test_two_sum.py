from leetcode.problems.two_sum import solve


def test_basic():
    assert solve([2, 7, 11, 15], 9) == [0, 1]


def test_none():
    assert solve([1, 2, 3], 100) == []
