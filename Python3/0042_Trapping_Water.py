class Solution:
    def trap(self, height: List[int]) -> int:
        total, high, high_i = 0, 0, -1
        for i, h in enumerate(height):
            if h > high:
                high, high_i = h, i
                
        acc, high = 0, 0
        for h in height[:high_i + 1]:
            if h >= high:
                total += acc
                acc, high = 0, h
            else:
                acc += high - h
                
        acc, high = 0, 0
        for h in height[high_i:][::-1]:
            if h >= high:
                total += acc
                acc, high = 0, h
            else:
                acc += high - h
        return total
    
