class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create buckets
        # Index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into their frequency bucket
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 4: Traverse buckets from highest frequency to lowest
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result