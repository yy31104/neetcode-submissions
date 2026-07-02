class TimeMap:

    def __init__(self):
        self.stack = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stack:
            self.stack[key] = []
        self.stack[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stack:
            return ""
        n = self.stack[key]
        left = 0
        right = len(n) - 1
        while left <= right:
            mid =(left + right) // 2
            if n[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right == -1:
            return ""
        return n[right][1]
        
