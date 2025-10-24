class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        balanced_numbers=set()
        base_numbers = ["1", "22", "122", "333", "1333", "4444", "14444", "22333", "55555", "122333", "155555", "224444", "666666", "1224444", "1666666", "2255555", "3334444", "7777777", "12255555"]
        for i in base_numbers:
            for x in permutations(i):
                balanced_numbers.add(int(''.join(x)))
        arr=sorted(balanced_numbers)
        idx=bisect.bisect_right(arr,n)
        return arr[idx]