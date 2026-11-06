class Solution:
    def maxArea(self, heights: List[int]) -> int:
        store = 0
        i, j = 0, len(heights) - 1

        while i < j:
            height = min(heights[i], heights[j])

            out = (j - i) * height
            store = max(out, store)

            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] >= heights[j]:
                j -= 1

        return store