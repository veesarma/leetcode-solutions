from typing import List

def solve(nums: List[int], target: int) -> List[int]:
    idx = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in idx:
            return [idx[need], i]
        idx[x] = i
    return []
