class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        min_heap = []  # tracks k largest nums1 values seen so far
        curr_sum = 0
        result = 0

        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            curr_sum += n1

            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                result = max(result, curr_sum * n2)

        return result