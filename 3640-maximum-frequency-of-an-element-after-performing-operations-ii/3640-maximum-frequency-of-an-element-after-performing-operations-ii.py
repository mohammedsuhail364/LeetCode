from collections import Counter, defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Frequency of each number in the array
        freq = Counter(nums)

        # Stores where the number of active intervals change (+start, -end)
        interval_change = defaultdict(int)

        # Mark interval starts and ends for each unique number
        for num in freq:
            start = num - k
            end = num + k + 1  # +1 to make interval [num-k, num+k] inclusive
            interval_change[start] += freq[num]
            interval_change[end] -= freq[num]

        # All possible points we need to consider
        # (interval starts/ends + actual numbers)
        all_points = sorted(interval_change.keys() | freq.keys())

        # Sweeping variables
        max_frequency = 0       # final result
        active_intervals = 0    # how many numbers can affect this current point

        # Sweep through all relevant points
        for point in all_points:
            # Update how many intervals are currently active
            active_intervals += interval_change[point]

            # How many numbers are already equal to this point
            current_count = freq[point]

            # We can increase the frequency by converting up to numOperations
            # from other active intervals, but not more than available
            possible_extra = min(active_intervals - current_count, numOperations)

            # Total possible frequency for this value
            possible_freq = current_count + possible_extra

            # Update global maximum
            max_frequency = max(max_frequency, possible_freq)

        return max_frequency
