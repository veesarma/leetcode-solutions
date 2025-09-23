from leetcode.problems.two_sum import solve


def test_basic():
    assert solve([2, 7, 11, 15], 9) == [0, 1]


def test_alt():
    got = solve([3, 2, 4], 6)
    assert got in ([1, 2], [2, 1], [1, 2])  # any valid pair indices ok


def test_none():
    assert solve([1, 2, 3], 100) == []
