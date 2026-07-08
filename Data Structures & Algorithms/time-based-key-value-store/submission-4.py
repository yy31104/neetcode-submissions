class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key in self.timemap:
            best = 0
            for n in self.timemap[key]:
                if n[0] <= timestamp:
                    if best < n[0]:
                        best = n[0]
                        ans = n[1]
        return ans

        
