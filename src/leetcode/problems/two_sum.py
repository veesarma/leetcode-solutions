def solve(nums: list[int], target: int) -> list[int]:
    idx: dict[int, int] = {}  # ✅ mypy will be happy now
    for i, x in enumerate(nums):
        need = target - x
        if need in idx:
            return [idx[need], i]
        idx[x] = i
    return []
