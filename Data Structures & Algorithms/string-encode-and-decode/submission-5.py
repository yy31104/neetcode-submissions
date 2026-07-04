class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        left = 0
        right = 0
        while right < len(s):
            if s[right] == "#":
                n = int(s[left:right])
                start = right + 1
                end = right + n + 1
                decoded.append(s[start:end])
                left = end
                right = end
            else:
                right += 1
        return decoded
