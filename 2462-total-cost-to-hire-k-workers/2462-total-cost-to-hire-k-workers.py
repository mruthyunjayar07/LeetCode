class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs) - 1
        left_heap, right_heap = [], []
        total = 0

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1

        for _ in range(k):
            left_min  = left_heap[0]  if left_heap  else float('inf')
            right_min = right_heap[0] if right_heap else float('inf')

            if left_min <= right_min:
                total += heapq.heappop(left_heap)
                if left <= right:              # refill from left
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(right_heap)
                if left <= right:              # refill from right
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total