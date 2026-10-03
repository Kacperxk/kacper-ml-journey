"""Contains Duplicate — https://neetcode.io/problems/duplicate-integer

Approach: adding new elements to the set and checking if num is already inside this set
Time: O(n) — n iterations over O(1)
Space: O(n) — worst case (no duplicates) the set stores every element
"""


def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    assert has_duplicate([1, 2, 3, 3])
    assert not has_duplicate([1, 2, 3, 4])
    assert not has_duplicate([])
    assert not has_duplicate([7])
    print("all tests passed")